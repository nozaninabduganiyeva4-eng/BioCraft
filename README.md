# ✨ BioCraft AI — Instagram Bio & SMM Sun'iy Intellekt Boti (@takeabiobot)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![aiogram](https://img.shields.io/badge/aiogram-3.x-green.svg)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-AI%20API-orange.svg)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

**BioCraft AI** — Instagram va boshqa ijtimoiy tarmoqlar (Telegram, TikTok) uchun professional, estetik va diqqatni tortuvchi BIO (biografiya), noyob username, post va story captionlari, mos hashtaglar hamda statuslar yaratib beruvchi Telegram bot.

Bot manzili: [@takeabiobot](https://t.me/takeabiobot)

---

## 🌟 Asosiy Imkoniyatlar

1. 🌟 **Instagram BIO Generator:**
   - Foydalanuvchi faoliyati, qiziqishlari yoki shioriga mos 4 xil estetik va tayyor BIO varianti.
   - Chiroyli emojilar, qator ajratishlar va Call-to-Action (havolaga yo'naltiruvchi) elementlari.
2. 🏷 **Noyob Username Generator:**
   - Ism, brend yoki kalit so'z bo'yicha 10-12 ta zamonaviy, esda qolarli nikneym g'oyalari.
3. ✍️ **Post & Story Caption:**
   - Diqqatni jalb qiluvchi kuchli Hook, qiziqarli asosiy qism va munosabat bildirishga chorlovchi xulosalar.
4. #️⃣ **Mos Hashtaglar To'plami:**
   - Katta qamrovli, o'rta qamrovli va tor nisha bo'yicha saralangan 25-30 ta samarali hashtaglar.
5. 💬 **Aesthetic Status va Iqtiboslar:**
   - Instagram Notes, Telegram Bio va Stories uchun chuqur ma'noli, chiroyli sitatalar.
6. 🎨 **5 Xil Uslub (Tone & Style):**
   - ✨ **Aesthetic:** Nafis, shinam, chiroyli shrift va simvollar bilan.
   - 🌿 **Minimal:** Qisqa, lo'nda, sodda va ortiqcha bezaklarsiz.
   - 💼 **Professional:** Biznes, rasmiy, ekspert va ishonchli ohangda.
   - 😂 **Funny:** Do'stona, kulgili va samimiy hazilomuz kayfiyatda.
   - 🚀 **Creative:** Noodatiy, yangicha va diqqatni darhol tortuvchi.

---

## 🧠 Sun'iy Intellekt va Optimallashtirish

- **Google Gemini API Integratsiyasi:** `gemini-3.5-flash-lite`, `gemini-3.5-flash` va `gemma-4-26b-a4b-it` modellar zanjiri orqali uzluksiz generatsiya.
- **Tezkor SQLite Keshlash:** Takroriy so'rovlar avval keshdan tekshiriladi, natija bir zumda beriladi va API kvotasi tejaladi.
- **Spam Himoyasi (Cooldown):** Har bir foydalanuvchi so'rovlari orasida 5 soniyalik kutish vaqti.
- **Kunlik Limitlar Boshqaruvi:** Bepul tier uchun kunlik limitlar nazorati va qoldiq ko'rsatgichi.
- **Aqlli Zaxira Shablonlar (Offline Fallback):** Agar API limiti tugasa yoki internetda uzilish bo'lsa ham, bot foydalanuvchini javobsiz qoldirmaydi.

---

## 📁 Loyiha Strukturasi

```text
BioCraft/
├── assets/
│   └── banner.png            # Start buyrug'idagi taqdimot rasmi
├── handlers/
│   ├── __init__.py
│   ├── start.py              # /start, rasm bilan xush kelibsiz va /help
│   ├── bio.py                # Instagram BIO generatsiya oqimi
│   ├── username.py           # Username g'oyalari generatsiyasi
│   ├── caption.py            # Post & Story caption yaratish
│   ├── hashtag.py            # Hashtag to'plamlari
│   ├── status.py             # Status va iqtiboslar
│   ├── settings.py           # 5 xil uslubni tanlash va saqlash
│   ├── profile.py            # Profil, statistika va limitlar
│   └── states.py             # aiogram 3 FSM holatlari
├── keyboards/
│   ├── __init__.py
│   ├── main_menu.py          # Asosiy ReplyKeyboardMarkup menyusi
│   └── inline_keyboards.py   # Inline uslub va harakatlar tugmalari
├── services/
│   ├── __init__.py
│   └── gemini_service.py     # Asinxron Google Gemini mijozi, kesh va fallback
├── .env.example              # Muhit o'zgaruvchilari namunasi
├── .gitignore                # Maxfiy kalitlar va keshlarni yashirish
├── bot.py                    # Asosiy ishga tushiruvchi dastur
├── config.py                 # Bot va API sozlamalari
├── database.py               # SQLite foydalanuvchilar va kesh bazasi
├── requirements.txt          # Kerakli Python kutubxonalari
└── README.md                 # Hujjatlar va qo'llanma
```

---

## 🚀 Ishga Tushirish Yo'riqnomasi

### 1. Loyihani yuklab olish:
```bash
git clone https://github.com/nozaninabduganiyeva4-eng/BioCraft.git
cd BioCraft
```

### 2. Kutubxonalarni o'rnatish:
```bash
pip install -r requirements.txt
```

### 3. `.env` faylini sozlash:
Loyiha ildizida `.env` faylini yarating va quyidagi kalitlarni kiriting:
```ini
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN_HERE
GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE
```

### 4. Botni ishga tushirish:
```bash
python bot.py
```

Ishga tushirgach, Telegramda **[@takeabiobot](https://t.me/takeabiobot)** botingizga `/start` yuboring!

---

## 🔒 Xavfsizlik
`.env` faylidagi barcha maxfiy kalitlar (Bot Token va Gemini API Key) [`.gitignore`](.gitignore) orqali himoyalangan va GitHub'ga yuklanmaydi.

---

## 👩‍💻 Muallif
**Nozanin Abduganiyeva**  
GitHub: [@nozaninabduganiyeva4-eng](https://github.com/nozaninabduganiyeva4-eng)
