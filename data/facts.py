"""
BioCraft Bot - Hayratlanarli Biologik Faktlar
"""

import random

FACTS = [
    "🧬 <b>DNK uzunligi:</b> Odam tanasidagi barcha hujayralarning DNK spiralini yozib, bir-biriga ulasak, uning uzunligi Quyosh tizimining narigi chekkasigacha yetishi mumkin (taxminan 10 milliard mil)!",
    "🫀 <b>Yurak qudrati:</b> Inson yuragi bir kunda o'rtacha 100 000 marta uradi va umr davomida taxminan 200 million litr qon haydaydi.",
    "🐙 <b>Sakkizoyoq siri:</b> Sakkizoyoqlarning (osminog) 3 ta yuragi va ko'k rangli qoni bor! Ularning qonida temir o'rniga mis (gemotsianin) kislorod tashiydi.",
    "🌿 <b>Kislorod manbai:</b> Yer yuzidagi kislorodning yarmidan ko'pini tropik o'rmonlar emas, balki okeandagi mikroskopik fitoplanktonlar ishlab chiqaradi!",
    "🦴 <b>Suyaklar mustahkamligi:</b> Odam suyagi (ayniqsa boldir suyagi) og'irlik ko'tarish bo'yicha betondan 4 barobar mustahkamroq hisoblanadi.",
    "🐝 <b>Asalari raqsi:</b> Asalarilar bir-biriga yangi gulzor qayerdaligini ko'rsatish uchun murakkab 'figurali raqs'dan foydalanishadi.",
    "🦥 <b>Eng sekin hazm:</b> Yalqovlar (sloth) bitta bargni to'liq hazm qilish uchun deyarli 1 oy vaqt sarflaydi!",
    "👁️ <b>Ko'z qobiliyati:</b> Inson ko'zi 10 milliondan ortiq turli xil rang va tuslarni ajrata olish qobiliyatiga ega.",
    "🦠 <b>Bakteriyalar soni:</b> Odam tanasidagi bakteriya hujayralari soni odamning o'z tana hujayralari soni bilan deyarli teng (taxminan 38 trillionta).",
    "🐬 <b>Delfinlar uyqusi:</b> Delfinlar uxlaganda miyasining faqat bitta yarimshari uxlaydi, ikkinchi yarmi esa nafas olish va cho'kib ketmaslik uchun hushyor turadi.",
    "🌳 <b>Daraxtlarning aloqasi:</b> O'rmondagi daraxtlar yer ostidagi zamburug' iplari (mikoriza) orqali bir-biriga oziq va xavf haqida signal yubora oladi ('Wood Wide Web').",
    "🦈 <b>Akulalar immuniteti:</b> Akulalar saraton kasalligiga deyarli chalinmaydi, chunki ularning skeleti suyakdan emas, tog'aydan iborat va maxsus birikmalarga boy.",
]


def get_random_fact() -> str:
    return random.choice(FACTS)
