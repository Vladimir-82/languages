from gtts import gTTS
from io import BytesIO

from lang.exceptions import LangException


def record_track(text_to_record: str, language: str) -> BytesIO:
    """Record text to speak."""
    file_to_record = BytesIO()
    tts = gTTS(text_to_record, lang=language)
    tts.write_to_fp(file_to_record)
    return file_to_record
