"""
BioCraft Bot - Biologiya Fan Bo'limlari va Mavzulari
"""

TOPICS = {
    "botany": {
        "title": "🌿 Botanika (O'simliklar Dunyosi)",
        "description": "O'simliklarning tuzilishi, fiziologiyasi, to'qimalari va ko'payishi haqida ilmiy ma'lumotlar.",
        "sections": [
            {
                "id": "bot_tissues",
                "name": "O'simlik To'qimalari",
                "content": (
                    "🌿 <b>O'simlik To'qimalari</b>\n\n"
                    "O'simliklarda 5 ta asosiy to'qima guruhi mavjud:\n\n"
                    "1️⃣ <b>Hosil qiluvchi (Meristema):</b> Hujayralari doimiy bo'linish xususiyatiga ega. "
                    "O'simlikning bo'yiga (uchki) va eniga (yonbosh - kambiy) o'sishini ta'minlaydi.\n"
                    "2️⃣ <b>Asosiy (Parenxima):</b> Assimilyatsiya (fotosintez), jamg'aruvchi, havo va suv saqlovchi turlarga bo'linadi.\n"
                    "3️⃣ <b>Qoplovchi:</b> Epidermis (birlamchi) va periderma/po'kak (ikkilamchi). O'simlikni qurib qolish va zararlanishdan asraydi.\n"
                    "4️⃣ <b>O'tkazuvchi:</b> Ksiléma (naylar - suv va mineral moddalarni pastdan yuqoriga tashiydi) va "
                    "Floéma (elaksimon naylar - organik moddalarni bargdan ildizga tashiydi).\n"
                    "5️⃣ <b>Mexanik:</b> Kollenxima va sklerenxima. O'simlikka pishiqlik va elastiklik beradi."
                ),
            },
            {
                "id": "bot_photosynthesis",
                "name": "Fotosintez Jarayoni",
                "content": (
                    "☀️ <b>Fotosintez Jarayoni</b>\n\n"
                    "Yashil o'simliklar xloroplastlarida quyosh nuri energiyasi hisobiga noorganik moddalardan "
                    "(CO₂ va H₂O) organik moddalar (glyukoza) sintezlanishi va kislorod ajralishi jarayoni.\n\n"
                    "<b>Tenglamasi:</b>\n"
                    "<code>6CO₂ + 6H₂O + Quyosh nuri ➔ C₆H₁₂O₆ + 6O₂</code>\n\n"
                    "<b>Fazalari:</b>\n"
                    "• <b>Yorug'lik fazasi:</b> Tilakoid membranasida kechadi. Xlorofill nurni yutadi, suv fotolizga uchraydi, "
                    "O₂ ajraladi, ATF va NADF·H hosil bo'ladi.\n"
                    "• <b>Qorong'ilik fazasi (Kalvin sikli):</b> Xloroplast stromasida kechadi. ATF energiyasi yordamida "
                    "CO₂ dan glyukoza sintezlanadi."
                ),
            },
            {
                "id": "bot_organs",
                "name": "O'simlik Organlari (Vegetativ va Generativ)",
                "content": (
                    "🌱 <b>O'simlik Organlari</b>\n\n"
                    "• <b>Vegetativ organlar:</b> O'simlikning oziqlanishi, o'sishi va hayot kechirishini ta'minlaydi.\n"
                    "  — <i>Ildiz:</i> O'q ildiz va popuk ildiz tizimlari. Suv va oziqni shimadi.\n"
                    "  — <i>Poya va Barg:</i> Moddalar harakati, fotosintez, transpiratsiya (suv bug'latish) va gaz almashinuvi.\n\n"
                    "• <b>Generativ organlar:</b> Jinsiy ko'payish organlari.\n"
                    "  — <i>Gul:</i> Changchi (erkaklik) va urug'chi (urg'ochilik) qismlaridan iborat.\n"
                    "  — <i>Meva va Urug':</i> Yangi avlod nishonasi, o'simlikning tarqalishini ta'minlaydi."
                ),
            },
        ],
    },
    "zoology": {
        "title": "🦁 Zoologiya (Hayvonot Olami)",
        "description": "Hayvonlarning xilma-xilligi, sistematikasi, anatomiyasi va moslashuvlari.",
        "sections": [
            {
                "id": "zoo_invertebrates",
                "name": "Umurtqasiz Hayvonlar",
                "content": (
                    "🪱 <b>Umurtqasiz Hayvonlar Dunyosi</b>\n\n"
                    "Yer yuzidagi barcha hayvon turlarining qariyb 95% ini tashkil qiladi:\n\n"
                    "• <b>Sodda hayvonlar (Bir hujayralilar):</b> Amyoba, Yashil evglena, Infuzoriya-tufelka.\n"
                    "• <b>Bo'shliqichlilar:</b> Gidra, meduzalar, marjon riflari.\n"
                    "• <b>Chuvalchanglar:</b> Yassi (jigar qurti, tasmasimon chuvalchang), To'garak (askarida), Halqali (yomg'ir chuvalchangi).\n"
                    "• <b>Molyuskalar:</b> Qorinoyoqlilar (shilliqurt), Ikki pallalilar (baqachanoq), Boshoyoqlilar (sakkizoyoq, kalmar).\n"
                    "• <b>Bo'g'imoyoqlilar:</b> Qisqichbaqasimonlar, O'rgimchaksimonlar, Hasharotlar (eng ko'p sonli guruh)."
                ),
            },
            {
                "id": "zoo_vertebrates",
                "name": "Umurtqali Hayvonlar (Xordalilar)",
                "content": (
                    "🦅 <b>Umurtqali Hayvonlar Sinf va Xususiyatlari</b>\n\n"
                    "1️⃣ <b>Baliqlar:</b> Jabralar orqali nafas oladi, 2 kamerali yurak (1 ta bo'lmacha, 1 ta qorincha), sovuqqonli.\n"
                    "2️⃣ <b>Suvda ham quruqlikda yashovchilar (Amfibiyalar):</b> Baqalar, salamandralar. 3 kamerali yurak, o'pka va teri orqali nafas oladi.\n"
                    "3️⃣ <b>Sudralib yuruvchilar (Reptiliyalar):</b> Kaltakesaklar, ilonlar, toshbaqalar, timsohlar (timsohda 4 kamerali yurak!). Sovuqqonli.\n"
                    "4️⃣ <b>Qushlar:</b> Issiqqonli, 4 kamerali yurak, pat qoplami, havo xaltachalari (qo'shaloq nafas olish).\n"
                    "5️⃣ <b>Sutemizuvchilar:</b> Bolasini sut bilan boqadi, tirik tug'adi (yo'ldoshlilar), 4 kamerali yurak, mukammal bosh miya po'stlog'i."
                ),
            },
        ],
    },
    "human": {
        "title": "🫀 Odam Anatomiyasi va Fiziologiyasi",
        "description": "Inson tanasi tizimlari: qon aylanish, asab, nafas, ovqat hazm qilish va immunitet.",
        "sections": [
            {
                "id": "hum_blood",
                "name": "Qon va Qon Aylanish Tizimi",
                "content": (
                    "❤️ <b>Qon va Yurak Tizimi</b>\n\n"
                    "• <b>Yurak:</b> 4 kamerali (2 ta bo'lmacha, 2 ta qorincha). Avtomatizm xususiyatiga ega.\n"
                    "• <b>Qon shaklli elementlari:</b>\n"
                    "  — <i>Eritrotsitlar:</i> Gemoglobin orqali O₂ va CO₂ tashiydi (yadroga ega emas).\n"
                    "  — <i>Leykotsitlar:</i> Himoya (fagotsitoz va antitanachalar ishlab chiqarish).\n"
                    "  — <i>Trombotsitlar:</i> Qon ivishini ta'minlovchi qon plastinkalari.\n\n"
                    "• <b>Qon guruhlari (AB0 tizimi):</b>\n"
                    "  — I (0) — universal donor\n"
                    "  — II (A), III (B)\n"
                    "  — IV (AB) — universal retsipiyent\n"
                    "  — Rezus omil (Rh+ va Rh-)."
                ),
            },
            {
                "id": "hum_nervous",
                "name": "Asab Tizimi va Miya",
                "content": (
                    "🧠 <b>Asab Tizimi</b>\n\n"
                    "• <b>Markaziy asab tizimi (MAT):</b> Bosh miya va orqa miya.\n"
                    "• <b>Periferik asab tizimi:</b> Asab tolalari va tugunlari.\n"
                    "• <b>Bosh miya bo'limlari:</b>\n"
                    "  — <i>Uzunchoq miya:</i> Hayotiy markazlar (nafas olish, yurak urishi, yutish, aksirish, yo'tal).\n"
                    "  — <i>Miyacha:</i> Harakatlarni muvofiqlashtirish va muvozanat.\n"
                    "  — <i>O'rta miya:</i> Ko'rish va eshitish yo'naltiruvchi reflekslari, mushaklar tonusi.\n"
                    "  — <i>Oraliq miya:</i> Talamus va gipotalamus (gomeostaz, termoregulyatsiya, his-tuyg'ular).\n"
                    "  — <i>Katta yarimsharlar po'stlog'i:</i> Oliy asab faoliyati, tafakkur, xotira, nutq."
                ),
            },
        ],
    },
    "genetics": {
        "title": "🧬 Sitologiya va Genetika",
        "description": "Hujayra biologiyasi, organoidlar, DNK/RNK, Mendel qonunlari va mutatsiyalar.",
        "sections": [
            {
                "id": "gen_cell",
                "name": "Hujayra Organoidlari",
                "content": (
                    "🔬 <b>Hujayra Organoidlari va Funksiyalari</b>\n\n"
                    "• <b>Yadro:</b> Irsiy axborot (xromatin/DNK) saqlanadi va boshqaruv markazi.\n"
                    "• <b>Mitoxondriya:</b> Hujayraning 'elektr stansiyasi' — ATF sintezlaydi (hujayraviy nafas olish).\n"
                    "• <b>Ribosoma:</b> Membranasiz organoid, oqsil biosintezini amalga oshiradi.\n"
                    "• <b>Endoplazmatik to'r (EPT):</b> Silliq (lipid va uglevod) hamda donador (oqsil tashiydi).\n"
                    "• <b>Goldji majmuasi:</b> Moddalarni saralash, qadoqlash va lizosomalarni hosil qilish.\n"
                    "• <b>Lizosoma:</b> Hazm qiluvchi fermentlar saqlaydi (avtoliz va parchalanish)."
                ),
            },
            {
                "id": "gen_mendel",
                "name": "Genetika va Mendel Qonunlari",
                "content": (
                    "🧪 <b>Gregor Mendel Qonunlari</b>\n\n"
                    "1️⃣ <b>1-qonun (Bir xillik qonuni):</b> Dominant va retsessiv gomozigotalar chatishtirilganda "
                    "(AA x aa), birinchi bo'g'inda (F₁) barcha duragaylar bir xil fenotip va geterozigota (Aa) genotipga ega bo'ladi.\n\n"
                    "2️⃣ <b>2-qonun (Ajralish qonuni):</b> F₁ geterozigotalar (Aa x Aa) o'zaro chatishtirilganda, "
                    "F₂ da fenotip bo'yicha <b>3:1</b>, genotip bo'yicha <b>1:2:1</b> (1 AA : 2 Aa : 1 aa) nisbatda ajralish yuz beradi.\n\n"
                    "3️⃣ <b>3-qonun (Erkin kombinirlanish qonuni):</b> Digeterozigotalar chatishtirilganda "
                    "(AaBb x AaBb), belgilar bir-biriga bog'liq bo'lmagan holda <b>9:3:3:1</b> nisbatda ajraladi."
                ),
            },
        ],
    },
    "ecology": {
        "title": "🌍 Ekologiya va Evolutsiya",
        "description": "Tirik organizmlarning muhit bilan aloqasi, biosfera, oziq zanjiri va turlarning paydo bo'lishi.",
        "sections": [
            {
                "id": "eco_factors",
                "name": "Ekologik Omillar va Oziq Zanjiri",
                "content": (
                    "🌲 <b>Ekologik Omillar</b>\n\n"
                    "• <b>Abiotik:</b> O'lik tabiat omillari (yorug'lik, harorat, namlik, bosim, tuproq tarkibi).\n"
                    "• <b>Biotik:</b> Tirik organizmlarning bir-biriga ta'siri (simbioz, parazitizm, yirtqichlik, raqobat).\n"
                    "• <b>Antropogen:</b> Inson faoliyatining tabiatga ta'siri.\n\n"
                    "🔗 <b>Oziq Zanjiri Bosqichlari:</b>\n"
                    "1. <b>Produtsentlar:</b> Avtotroflar (yashil o'simliklar, sianobakteriyalar).\n"
                    "2. <b>Konsumentlar:</b> Getertroflar (1-tartib: o'txo'rlar, 2-tartib: yirtqichlar).\n"
                    "3. <b>Redutsentlar:</b> Organik moddalarni noorganik moddalarga parchalovchi zamburug' va bakteriyalar."
                ),
            },
            {
                "id": "eco_evolution",
                "name": "Evolutsiya Nazariyasi",
                "content": (
                    "🦕 <b>Charlz Darvin Evolutsiya Ta'limoti</b>\n\n"
                    "Evolutsiyaning harakatlantiruvchi kuchlari:\n"
                    "• <b>Irsiy o'zgaruvchanlik:</b> Mutatsiya va kombinativ o'zgaruvchanlik yangi belgilarni yuzaga keltiradi.\n"
                    "• <b>Yashash uchun kurash:</b> Tur ichidagi, turlararo va noqulay muhit sharoitlariga qarshi kurash.\n"
                    "• <b>Tabiiy tanlanish:</b> Muhitga eng yaxshi moslashgan organizmlarning tirik qolishi va nasl qoldirishi.\n\n"
                    "🔍 <b>Muvofiqlashuv turlari:</b>\n"
                    "• <i>Aromorfoz:</i> Tuzilish darajasining umuman yuksalishi (masalan, 4 kamerali yurak).\n"
                    "• <i>Idioadaptatsiya:</i> Xususiy moslanishlar (qushlar tumshug'ining har xil shakli).\n"
                    "• <i>Degeneratsiya:</i> Ayrim organlarning soddalashishi yoki yo'qolishi (parazit chuvalchanglar)."
                ),
            },
        ],
    },
}
