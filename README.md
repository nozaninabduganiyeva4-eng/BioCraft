# 🌿 BioCraft — Telegram Ta'lim va Viktorina Boti (@takeabiobot)

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![aiogram Version](https://img.shields.io/badge/aiogram-3.x-green.svg)
![Database](https://img.shields.io/badge/database-SQLite-lightgrey.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**BioCraft** — maktab o'quvchilari, abituriyentlar hamda biologiya ixlosmandlari uchun mo'ljallangan interaktiv ta'lim, viktorina va qidiruv Telegram boti.

Telegramda bot manzili: [@takeabiobot](https://t.me/takeabiobot)

---

## ✨ Asosiy Imkoniyatlar

1. 🧬 **Biologiya Bo'limlari (Nazariy Bilimlar):**
   - 🌿 **Botanika:** O'simlik to'qimalari, fotosintez jarayoni va organlar tuzilishi.
   - 🦁 **Zoologiya:** Umurtqasizlar va umurtqalilar (baliq, amfibiya, reptiliya, qush va sutemizuvchilar).
   - 🫀 **Odam Anatomiyasi:** Yurak-qon tomir tizimi, qon guruhlari, asab tizimi va bosh miya bo'limlari.
   - 🧬 **Sitologiya & Genetika:** Hujayra organoidlari, ATF sintezi, Mendel qonunlari va DNK/RNK.
   - 🌍 **Ekologiya & Evolutsiya:** Oziq zanjiri, ekologik omillar va Darvin ta'limoti.

2. 🧪 **Interaktiv Viktorina (Quiz Game):**
   - Biologiyaning turli yo'nalishlaridan 4 variantli test savollari.
   - Har bir to'g'ri javob uchun **+10 ball**.
   - Har bir savoldan keyin javobning ilmiy izohi va tushuntirishi.

3. 📖 **Biologik Terminlar Lug'ati (Smart Search):**
   - 25+ dan ortiq fundamental biologik terminlar bazasi (Mitoz, Meyoz, Fotosintez, ATF, Gomologik organlar va h.k.).
   - Foydalanuvchi qidirmoqchi bo'lgan so'zni yozishi bilan tezkor ta'rifni topib beradi.

4. 💡 **Qiziqarli Faktlar:**
   - Tirik tabiat va organizmlar haqida qiziqarli va hayratlanarli ilmiy faktlar.

5. 🏆 **Reyting va Shaxsiy Profil:**
   - Foydalanuvchining to'plagan ballari, yechgan testlari soni va aniqlik foizi.
   - Top-10 yetakchilar reyting jadvali (Leaderboard).

---

## 📁 Loyiha Tuzilishi

```text
BioCraft/
├── data/
│   ├── __init__.py
│   ├── biology_topics.py   # Bo'limlar va darsliklar
│   ├── quiz_questions.py   # Test savollari va javoblar izohi
│   ├── glossary.py         # Terminlar lug'ati va qidiruv
│   └── facts.py            # Qiziqarli biologik faktlar
├── handlers/
│   ├── __init__.py
│   ├── start.py            # /start, /help va xush kelibsiz
│   ├── topics.py           # Darsliklar va bo'limlar navigatsiyasi
│   ├── quiz.py             # Viktorina va test jarayoni
│   ├── glossary.py         # Lug'at va qidiruv handleri
│   ├── facts.py            # Tasodifiy faktlar
│   └── profile.py          # Profil va reyting (top-10)
├── keyboards/
│   ├── __init__.py
│   ├── main_menu.py        # Asosiy menyu (Reply Keyboard)
│   └── inline_keyboards.py # Inline navigatsiya va test tugmalari
├── .env.example            # Muhit o'zgaruvchilari namunasi
├── .gitignore              # Xavfsizlik va keraksiz fayllar filtri
├── bot.py                  # Asosiy ishga tushiruvchi fayl
├── config.py               # Sozlamalar va .env o'quvchi modul
├── database.py             # SQLite ma'lumotlar bazasi boshqaruvi
├── requirements.txt        # Kerakli Python kutubxonalari
└── README.md               # Qo'llanma va hujjatlar
```

---

## 🚀 Ishga Tushirish Yo'riqnomasi

### 1. Loyihani yuklab olish va o'tish:
```bash
git clone https://github.com/nozaninabduganiyeva4-eng/BioCraft.git
cd BioCraft
```

### 2. Virtual muhit yaratish va faollashtirish (ixtiyoriy):
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

### 3. Kutubxonalarni o'rnatish:
```bash
pip install -r requirements.txt
```

### 4. `.env` faylini sozlash:
`.env.example` faylidan nusxa olib `.env` yarating va BotFather bergan tokenni kiriting:
```ini
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN_HERE
```

### 5. Botni ishga tushirish:
```bash
python bot.py
```

---

## 🔒 Xavfsizlik Eslatmasi
Bot tokeni maxfiy ma'lumot hisoblanadi. Hech qachon haqiqiy tokenni GitHub ommaviy repozitoriyalariga commit qilmang. Shu sababli `.env` fayli `.gitignore` ga qo'shilgan.

---

## 👩‍💻 Muallif
**Nozanin Abduganiyeva**  
GitHub: [@nozaninabduganiyeva4-eng](https://github.com/nozaninabduganiyeva4-eng)
