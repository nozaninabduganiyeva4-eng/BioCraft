import logging
import aiohttp
from config import GEMINI_API_KEY, AVAILABLE_STYLES
from database import make_cache_key, get_cached_response, save_cached_response

logger = logging.getLogger(__name__)

# Google Gemini rasmiy tavsiya qilgan eng so'nggi va tezkor modellari
PRIMARY_MODEL = "gemini-3.5-flash-lite"
FALLBACK_MODELS = ["gemini-3.5-flash", "gemma-4-26b-a4b-it", "gemini-flash-latest"]


async def call_gemini_api(prompt: str) -> str:
    """Google Gemini API ga asinxron so'rov yuborish"""
    models = [PRIMARY_MODEL] + FALLBACK_MODELS
    timeout = aiohttp.ClientTimeout(total=20)

    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.8,
            "maxOutputTokens": 1200,
        },
    }

    async with aiohttp.ClientSession(timeout=timeout) as session:
        last_error = None
        for model in models:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={GEMINI_API_KEY}"
            try:
                async with session.post(url, json=payload, headers=headers) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        candidates = data.get("candidates", [])
                        if candidates and "content" in candidates[0]:
                            parts = candidates[0]["content"].get("parts", [])
                            if parts and "text" in parts[0]:
                                text = parts[0]["text"].strip()
                                if text:
                                    return text
                    elif resp.status == 429:
                        logger.warning(f"Model {model} limit (429) berdi. Keyingi modelga o'tilmoqda...")
                        last_error = "LIMIT_EXCEEDED"
                        continue
                    else:
                        err_text = await resp.text()
                        logger.warning(f"Model {model} xatosi ({resp.status}): {err_text[:100]}")
                        last_error = f"HTTP_{resp.status}"
            except Exception as e:
                logger.warning(f"Model {model} ulanish xatosi: {e}")
                last_error = str(e)

        if last_error == "LIMIT_EXCEEDED":
            raise RuntimeError("API_LIMIT")
        raise RuntimeError(f"API_ERROR: {last_error}")


async def generate_content_with_cache(task_type: str, user_input: str, style_key: str, system_prompt: str) -> tuple[str, bool]:
    """
    Kesh va Gemini API orqali javob olish.
    Qaytaradi: (matn, keshdan_olindimi: bool)
    """
    style_info = AVAILABLE_STYLES.get(style_key, AVAILABLE_STYLES["aesthetic"])
    cache_key = make_cache_key(task_type, user_input, style_key)

    # 1. Keshni tekshirish (Tezkor va API so'rovlarni tejaydi)
    cached = get_cached_response(cache_key)
    if cached:
        logger.info(f"Keshdan qaytarildi: {task_type} [{style_key}]")
        return cached, True

    # 2. Gemini API ga so'rov jo'natish
    full_prompt = (
        f"{system_prompt}\n\n"
        f"Talab qilingan uslub: {style_info['instruction']}\n"
        f"Foydalanuvchi ma'lumoti: \"{user_input}\"\n\n"
        "MUHIM TALAB: Faqat natijani chiroyli emojilar va format bilan taqdim et. "
        "Ortiqcha kirish so'zlar yoki tushuntirishlarsiz, to'g'ridan-to'g'ri nusxalab Instagramga qo'yishga tayyor bo'lsin."
    )

    try:
        generated_text = await call_gemini_api(full_prompt)
        # Keshga saqlash
        save_cached_response(cache_key, generated_text)
        return generated_text, False
    except RuntimeError as e:
        if "API_LIMIT" in str(e):
            # API limiti to'lsa zaxira shablon
            fallback_text = get_fallback_result(task_type, user_input, style_key)
            return (
                "⚠️ <i>(Eslatma: AI so'rovlar limiti vaqtincha to'lganligi sababli, aqlli zaxira shablon taqdim etildi)</i>\n\n"
                + fallback_text,
                False,
            )
        raise e


# --- Promptlar ---

async def ai_generate_bio(user_input: str, style_key: str) -> tuple[str, bool]:
    system_prompt = (
        "Sen professional Instagram BIO mutaxassisisan. "
        "Foydalanuvchi ma'lumotlari asosida Instagram uchun 4 ta turli xil, "
        "ko'rkam va estetik BIO variantini yarat. "
        "Har bir variantda chiroyli emojilar, qator ajratishlar va Call-to-Action bo'lsin. "
        "Variantlarni 1️⃣, 2️⃣, 3️⃣, 4️⃣ deb raqamlab ko'rsat."
    )
    return await generate_content_with_cache("bio", user_input, style_key, system_prompt)


async def ai_generate_usernames(user_input: str, style_key: str) -> tuple[str, bool]:
    system_prompt = (
        "Sen ijtimoiy tarmoqlar uchun esda qolarli, estetik va o'ziga xos username (nikneym) mutaxassisisan. "
        "Foydalanuvchi kiritgan so'z yoki ism asosida Instagram/Telegram uchun 10-12 ta zamonaviy, "
        "ixcham, nuqta yoki tagchiziq bilan boyitilgan jozibador username variantlarini taklif qil."
    )
    return await generate_content_with_cache("username", user_input, style_key, system_prompt)


async def ai_generate_caption(user_input: str, style_key: str) -> tuple[str, bool]:
    system_prompt = (
        "Sen professional Instagram post va story kopirayterisan. "
        "Foydalanuvchi mavzusi bo'yicha to'liq post matnini yoz:\n"
        "• Kuchli diqqat jalb qiluvchi birinchi qator (Hook)\n"
        "• Asosiy qiziqarli mazmun va o'ylar\n"
        "• Fikr bildirishga undovchi savol yoki Call to Action\n"
        "• 5 ta mos hashtag."
    )
    return await generate_content_with_cache("caption", user_input, style_key, system_prompt)


async def ai_generate_hashtags(user_input: str, style_key: str) -> tuple[str, bool]:
    system_prompt = (
        "Sen Instagram hashtag algoritmlari bo'yicha mutaxassisisan. "
        "Foydalanuvchi mavzusiga mos eng samarali 25-30 ta hashtag to'plamini tuz:\n"
        "1. Katta qamrovli (Ommabop)\n"
        "2. O'rta qamrovli (Target auditoriya)\n"
        "3. Tor nisha (Aynan soha bo'yicha)\n"
        "Ularni chiroyli guruhlab ko'rsat."
    )
    return await generate_content_with_cache("hashtag", user_input, style_key, system_prompt)


async def ai_generate_status(user_input: str, style_key: str) -> tuple[str, bool]:
    system_prompt = (
        "Sen chuqur ma'noli va aesthetic statuslar, sitatalar va iqtiboslar ustasisan. "
        "Foydalanuvchi mavzusi yoki kayfiyatiga mos 5 ta go'zal, ta'sirli va esda qolarli status yozib ber."
    )
    return await generate_content_with_cache("status", user_input, style_key, system_prompt)


# --- Favqulodda zaxira shablonlar (Offline Fallback) ---
def get_fallback_result(task_type: str, user_input: str, style_key: str) -> str:
    cleaned = user_input.replace("\n", " ").strip()
    if task_type == "bio":
        return (
            f"1️⃣ ✨ <b>{cleaned}</b>\n"
            f"🌿 Har bir lahzada go'zallik izlab\n"
            f"📍 Tashkent | Creator\n"
            f"👇 Loyihalarim va aloqa:\n\n"
            f"2️⃣ 💼 <b>{cleaned}</b> | Professional\n"
            f"🚀 G'oyalarni haqiqatga aylantiramiz\n"
            f"📩 Hamkorlik uchun DM\n\n"
            f"3️⃣ ☕ {cleaned} vibes\n"
            f"💭 Hayot — katta bir hikoya\n"
            f"🕊️ Just be yourself\n\n"
            f"4️⃣ 🎯 Focus. Passion. Growth.\n"
            f"🔗 {cleaned}\n"
            f"✨ Yangi postlar har hafta!"
        )
    elif task_type == "username":
        clean_word = "".join(e for e in cleaned.lower() if e.isalnum())[:12]
        return (
            f"✨ @the.{clean_word}\n"
            f"🌿 @{clean_word}.aesthetic\n"
            f"💼 @{clean_word}_official\n"
            f"🚀 @real.{clean_word}\n"
            f"🎨 @its_{clean_word}\n"
            f"🌙 @{clean_word}.diary\n"
            f"☕ @vibes.with.{clean_word}\n"
            f"🎯 @{clean_word}.hub"
        )
    elif task_type == "caption":
        return (
            f"✨ <b>{cleaned.capitalize()}</b> haqida hech o'ylab ko'rganmisiz?\n\n"
            f"Ba'zida kichik bir qadam katta o'zgarishlarga sabab bo'ladi. "
            f"Har bir yangi kun — yangi imkoniyat va yangi ilhom degani.\n\n"
            f"Siz bu haqda qanday fikrdasiz? Fikrlaringizni izohlarda yozib qoldiring! 👇💬\n\n"
            f"#aesthetic #inspire #growth #life #tashkent #uzbekistan"
        )
    elif task_type == "hashtag":
        return (
            f"#️⃣ <b>Katta qamrovli:</b>\n#instagram #uzbekistan #tashkent #explore #reels #trend\n\n"
            f"#️⃣ <b>O'rta qamrovli:</b>\n#{cleaned.replace(' ', '_')} #lifevibes #aestheticedits #dailypost\n\n"
            f"#️⃣ <b>Nisha hashtaglar:</b>\n#{cleaned.replace(' ', '')}uz #uzbstyle #instatashkent"
        )
    else:
        return (
            f"1. «Eng go'zal hikoyalar jimlikda boshlanadi.» ✨\n"
            f"2. «O'zing bo'lish — eng jasoratli san'at.» 🌿\n"
            f"3. «{cleaned.capitalize()} — qalbdan boshlanadi.» 🤍\n"
            f"4. «Katta orzular tinimsiz mehnatni talab qiladi.» 🚀\n"
            f"5. «Peace over drama, always.» ☕"
        )
