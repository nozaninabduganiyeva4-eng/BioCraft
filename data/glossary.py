"""
BioCraft Bot - Biologik Terminlar Lug'ati (Glossary)
"""

GLOSSARY = {
    "fotosintez": "Yashil o'simliklar va ayrim bakteriyalarning yorug'lik energiyasi yordamida noorganik moddalardan organik moddalar sintezlash jarayoni.",
    "mitoz": "Eukariotik hujayralarning bo'linish usuli. Natijada boshlang'ich hujayraga aynan o'xshash xromosomalar to'plamiga ega ikkita yangi hujayra hosil bo'ladi.",
    "meyoz": "Jinsiy hujayralar (gametalar) hosil bo'lishidagi reduksion bo'linish. Xromosoma to'plami 2 barobar kamayadi (diploiddan gaploidga).",
    "atf": "Adenozintrifosfat kislota — hujayraning universal energiya manbai bo'lgan makroergik birikma.",
    "dnk": "Dezoksiribonuklein kislota — tirik organizmlarning irsiy axborotini saqlovchi va avloddan-avlodga uzatuvchi qo'sh spiral molekula.",
    "rnk": "Ribonuklein kislota — oqsil biosintezida va irsiy axborotni amalga oshirishda ishtirok etuvchi bir zanjirli nuklein kislota.",
    "xromosoma": "Hujayra yadrosida joylashgan, DNK va oqsillardan tashkil topgan irsiyat tashuvchi tuzilma.",
    "genotip": "Organizmning barcha genlari yig'indisi.",
    "fenotip": "Genotipning tashqi muhit bilan o'zaro ta'sirida namoyon bo'ladigan tashqi va ichki belgilar majmui.",
    "gomologik": "Kelib chiqishi va tuzilishi bir xil bo'lgan, lekin turli funksiyalarni bajarishi mumkin bo'lgan organlar (masalan: odam qo'li va qush qanoti).",
    "analogik": "Bajaradigan funksiyasi o'xshash, lekin kelib chiqishi har xil bo'lgan organlar (masalan: kapalak qanoti va qush qanoti).",
    "gomeostaz": "Tirik organizm ichki muhiti (harorat, qon bosimi, kimyoviy tarkib)ning nisbiy barqarorligi.",
    "fagotsitoz": "Hujayraning yirik qattiq zarrachalarni qamrab olib hazm qilishi (I.I. Mechnikov kashf etgan).",
    "pinositoz": "Hujayraning suyuq tomchilarni yutish jarayoni.",
    "ferment": "Biologik katalizatorlar — organizmdagi kimyoviy reaksiyalarni millionlab marta tezlashtiruvchi oqsillar.",
    "simbioz": "Ikki turli organizmning bir-biri uchun foydali bo'lgan birga yashashi (masalan: lishayniklar).",
    "parazitizm": "Bir organizm boshqa organizm hisobiga yashab, unga zarar yetkazishi.",
    "abiotik": "Tirik organizmlarga ta'sir ko'rsatuvchi jonsiz tabiat omillari (quyosh, harorat, suv, havo).",
    "biotik": "Tirik organizmlarning bir-biriga ko'rsatadigan ta'sirlari majmui.",
    "antropogen": "Inson faoliyati natijasida yuzaga keladigan va tabiatga ta'sir etuvchi omillar.",
    "aromorfoz": "Evolutsiyada organizmlar tuzilishining umumiy yuksalishi va hayot faoliyatining murakkablashishi.",
    "mutatsiya": "Organizm irsiy materiali (DNK yoki xromosomalar)ning to'satdan va sakrashsimon o'zgarishi.",
    "ribosoma": "Oqsil biosintezini amalga oshiruvchi membranasiz hujayra organoidi.",
    "mitoxondriya": "Hujayraning ATF sintezlaydigan, ikki qavat membranali nafas olish organoidi.",
    "kambiy": "O'simlik poyasi va ildizining eniga o'sishini ta'minlovchi hosil qiluvchi (meristema) to'qima.",
}


def search_term(query: str):
    query = query.lower().strip()
    results = {}
    for term, definition in GLOSSARY.items():
        if query in term or term in query:
            results[term] = definition
    return results
