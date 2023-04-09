PARLER_DEFAULT_LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', 'English'), ('nl', 'Dutch'), ('it', 'Italian'), ('fr', 'French'), ('es', 'Spanish'),
    ('zh', 'Chinese'), ('ko', 'Korean'), ('fa', 'Persian'), ('pt', 'Portuguese'), ('hy', 'Armenian'),
    ('de', 'German'), ('az', 'Azerbaijani'), ('bn', 'Bengali'), ('ru', 'Russian'), ('ar', 'Arabic'),
    ('bg', 'Bulgarian'), ('km', 'Khmer'), ('hr', 'Croatian'), ('da', 'Danish'), ('et', 'Estonian'),
    ('fi', 'Finnish'), ('lv', 'Latvian'), ('el', 'Greek'), ('nb', 'Norwegian Bokmål'), ('is', 'Icelandic'),
    ('ur', 'Urdu'), ('pl', 'Polish'), ('mk', 'Macedonian'), ('ro', 'Romanian'), ('sr', 'Serbian'),
    ('sk', 'Slovak'), ('sl', 'Slovenian'), ('sv', 'Swedish'), ('hu', 'Hungarian'), ('uk', 'Ukrainian'),
    ('iw', 'Hebrew'), ('ja', 'Japanese'), ('tr', 'Turkish'),
)

PARLER_LANGUAGES = {
    None: (
        {'code': 'en'}, {'code': 'nl'}, {'code': 'it'}, {'code': 'fr'}, {'code': 'es'},
        {'code': 'zh'}, {'code': 'ko'}, {'code': 'fa'}, {'code': 'pt'}, {'code': 'hy'},
        {'code': 'de'}, {'code': 'az'}, {'code': 'bn'}, {'code': 'ru'}, {'code': 'ar'},
        {'code': 'bg'}, {'code': 'km'}, {'code': 'hr'}, {'code': 'da'}, {'code': 'et'},
        {'code': 'fi'}, {'code': 'lv'}, {'code': 'el'}, {'code': 'nb'}, {'code': 'is'},
        {'code': 'ur'}, {'code': 'pl'}, {'code': 'mk'}, {'code': 'ro'}, {'code': 'sr'},
        {'code': 'sk'}, {'code': 'sl'}, {'code': 'sv'}, {'code': 'hu'}, {'code': 'uk'},
        {'code': 'iw'}, {'code': 'ja'}, {'code': 'tr'},
    ),
    'default': {
        'fallbacks': ['en'],
        'hide_untranslated': False,
    }
}
