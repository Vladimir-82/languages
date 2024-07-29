from googletrans import Translator
from gtts import gTTS
from io import BytesIO

from lang.structures import languages


def get_translate_text(language_to: str, text_for_translate: str) -> tuple[str, str, str]:
    """Get translated_text and language."""
    translate_to = languages.translate.get(language_to, 'en')
    translator = Translator()

    translate_from = translator.detect(text_for_translate).lang
    translated = translator.translate(text_for_translate, dest=translate_to)

    return translated.text, translate_from, translate_to


def record_track(text_to_record: str, language: str) -> BytesIO:
    """Record text to speak."""
    file_to_record = BytesIO()
    tts = gTTS(text_to_record, lang=language)
    tts.write_to_fp(file_to_record)
    return file_to_record
