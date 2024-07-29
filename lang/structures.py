from dataclasses import dataclass


@dataclass
class Languages:
    """Auxiliary structures."""

    Languages: dict
    translate: dict


languages = Languages(
    {
        'en': 'English',
        'de': 'Deutsch',
        'fr': 'Français',
        'ru': 'Русский',
        'uk': 'Українська',
        'pl': 'Polski',
    },
    {
        'English': 'en',
        'Deutsch': 'de',
        'Français': 'fr',
        'Русский': 'ru',
        'Українська': 'uk',
        'Polski': 'pl',
    },
)
