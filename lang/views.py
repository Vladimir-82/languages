from googletrans import Translator
from django.shortcuts import render
from django.core.files.base import ContentFile

from .models import Translate
from .utils import record_track



LANGUAGES = {
    'en': 'English',
    'de': 'Deutsch',
    'fr': 'Français',
    'ru': 'Русский',
    'uk': 'Українська',
    'pl': 'Polski',
}
TRANSLATE = {
    'English': 'en',
    'Deutsch': 'de',
    'Français': 'fr',
    'Русский': 'ru',
    'Українська': 'uk',
    'Polski': 'pl',
}

def index(request):
    """Translate text."""
    if request.method == 'POST':
        request_data = request.POST

        text_for_translate = request_data['text_for_translate']
        language_to = request_data['languages']

        translate_to = TRANSLATE.get(language_to, 'en')

        translator = Translator()

        answer = translator.detect(text_for_translate).lang

        translate = translator.translate(text_for_translate, dest=translate_to)

        translated_text = translate.text

        translate_object = Translate.objects.create()
        name = ''.join(('track', '-', str(translate_object.pk)))
        translate_object.title = name

        mp3_file_1 = record_track(text_to_record=text_for_translate, language=answer)
        translate_object.file_one.save(
            name=name + '_1',
            content=ContentFile(mp3_file_1.getvalue()),
            save=False,
        )
        mp3_file_2 = record_track(text_to_record=translated_text, language=translate_to)
        translate_object.file_two.save(
            name=name + '_2',
            content=ContentFile(mp3_file_2.getvalue()),
            save=False,
        )
        translate_object.save()

        language_input = LANGUAGES.get(answer)
        language_output = LANGUAGES.get(translate_to)
        translate_data_to_render = {
            "language_input": language_input,
            "text_for_translate": text_for_translate,
            "translate_object": translate_object,
            "translated_text": translated_text,
            "language_output": language_output,
        }
    else:
        translate_data_to_render = {"answer": ""}
    return render(request, 'app/index.html', context=translate_data_to_render)
