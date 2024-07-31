"""Views language identifier."""

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from .structures import language
from .utils import create_translate_object, get_translate_text


def index(request: WSGIRequest) -> HttpResponse:  # noqa: WPS210
    """Language identifier."""
    if request.method == 'POST':
        request_data = request.POST

        text_for_translate = request_data['text_for_translate']
        language_to = request_data['languages']

        translated_text, translate_from, translate_to = get_translate_text(language_to, text_for_translate)

        translate_object = create_translate_object(text_for_translate, translate_from, translated_text, translate_to)

        language_input = language.language.get(translate_from)
        language_output = language.language.get(translate_to)
        translate_data_to_render = {
            'language_input': language_input,
            'text_for_translate': text_for_translate,
            'translate_object': translate_object,
            'translated_text': translated_text,
            'language_output': language_output,
        }
    else:
        translate_data_to_render = {}
    return render(request, 'app/index.html', context=translate_data_to_render)
