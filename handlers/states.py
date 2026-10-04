from aiogram.fsm.state import State, StatesGroup


class GenerationStates(StatesGroup):
    waiting_for_bio_input = State()
    waiting_for_username_input = State()
    waiting_for_caption_input = State()
    waiting_for_hashtag_input = State()
    waiting_for_status_input = State()
