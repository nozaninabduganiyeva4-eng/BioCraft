from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.biology_topics import TOPICS


def get_topics_keyboard() -> InlineKeyboardMarkup:
    buttons = []
    for key, topic in TOPICS.items():
        buttons.append([InlineKeyboardButton(text=topic["title"], callback_data=f"topic_{key}")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_sections_keyboard(topic_key: str) -> InlineKeyboardMarkup:
    topic = TOPICS.get(topic_key)
    buttons = []
    if topic:
        for sec in topic["sections"]:
            buttons.append([InlineKeyboardButton(text=f"📌 {sec['name']}", callback_data=f"sec_{sec['id']}")])
    buttons.append([InlineKeyboardButton(text="⬅️ Bo'limlar ro'yxatiga", callback_data="back_topics")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_section_detail_keyboard(topic_key: str) -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="⬅️ Mavzularga qaytish", callback_data=f"topic_{topic_key}")],
        [InlineKeyboardButton(text="🧪 Shu mavzudan test ishlash", callback_data="start_quiz")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_quiz_keyboard(question_id: int, options: list) -> InlineKeyboardMarkup:
    buttons = []
    for idx, opt in enumerate(options):
        buttons.append([
            InlineKeyboardButton(
                text=opt,
                callback_data=f"ans_{question_id}_{idx}"
            )
        ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_next_quiz_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="➡️ Keyingi Savol", callback_data="next_quiz")],
        [InlineKeyboardButton(text="🏆 Reytingni ko'rish", callback_data="view_ranking")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_fact_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="🔄 Boshqa qiziqarli fakt", callback_data="next_fact")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
