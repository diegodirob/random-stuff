import csv
from typing import Callable, List, Literal

from django.conf import settings

# document_import( document=tsv_parser('news/fixtures/hashtags'), model='Hashtag )

def tsv_parser(path: str):
    with open(f'{path}.tsv') as f:
        return [line for line in csv.reader(f, delimiter="\t")]


def document_import(document: List[list], model: Literal['FirstTranslatableModel', 'SecondTranslatableModel']):
    # Based on tsv document that have:
    # First row to handle different languages
    # Other to handle static work/text and his translations
    # With this script we can handle import all text and translations, and handle it subsequently in admin panel

    model = {'FirstTranslatableModel': FirstTranslatableModel, 'SecondTranslatableModel': SecondTranslatableModel}[model]
    supported_languages = [el[0] for el in settings.LANGUAGES]

    # Convert and find en value
    document[0] = list(map(lambda key: key.lower(), document[0]))
    en_idx = document[0].index('en')

    for line in document[1:]:
        qs = model.objects.translated('en', label=line[en_idx])
        instance = model.objects.create(label=line[en_idx]) if not qs.exists() else qs.first()
        print(f'Processing word {line[en_idx]}')

        for idx, word in enumerate(line):
            language_code = document[0][idx]

            if idx == en_idx or model.objects.translated(language_code, label=word).exists() or language_code not in supported_languages:
                continue

            # Cannot use update_or_create -> Not supported
            instance.set_current_language(language_code)
            instance.label = word
            instance.save()
            print(f' - Added translation in {language_code}: {word}')