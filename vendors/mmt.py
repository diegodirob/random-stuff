from typing import List, Tuple

import requests
import os


# Settings

MMT_MAX_CHARACTERS, MMT_MAX_ROWS = 6000, 100
MAX_SUPPORTED_CAPACITY = 8 * 1024
MMT_ENDPOINT = 'https://api.modernmt.eu/translate'
MMT_APIKEY = os.environ.get('MMT_APIKEY', 'dev_key')
MMT_HEADERS = {'MMT-ApiKey': MMT_APIKEY, 'Content-Type': 'application/json', 'X-HTTP-Method-Override': 'GET'}


# Object

class Sentence:
    original: str
    translated: str
    back_translated: str

    def __init__(self, original, translated, back_translated):
        self.original = original
        self.translated = translated
        self.back_translated = back_translated


# Classes

class MMT:
    def data_parser(self, data: List[str]) -> List[List]:
        # Validate characters and sentences limits
        container: List[List] = []
        sub: List = []
        sub_chars_count: int = 0
        sub_sentences_count: int = 0

        for sentence in data:
            # Fill sub or container and reset sub
            if (sub_chars_count + len(sentence)) <= MMT_MAX_CHARACTERS and (sub_sentences_count + 1) <= MMT_MAX_ROWS:
                sub.append(sentence)
            else:
                container.append(sub)
                sub = []

            # Updated params
            sub_chars_count, sub_sentences_count = sum(map(lambda row: len(row), sub)), len(sub)

        # Append last sub
        if sub:
            container.append(sub)

        return container

    def translate(self, source: str, target: str, q: list, only_translation: bool = True) -> List:
        response = requests.post(url=MMT_ENDPOINT, headers=MMT_HEADERS, params={'source': source, 'target': target, 'q': q})

        if response.status_code != 200:
            # error_handler(message='Error during MMT translation')
            pass

        response = response.json()['data']
        response = [response] if isinstance(response, dict) else response
        return [el['translation'] for el in response] if only_translation else response

    def bulk_translate(self, container: list, source: str, target: str) -> Tuple[List[Sentence], list]:
        response, container_translated = [], []
        for data in container:
            first_translation = self.translate(source, target, data)
            second_translation = self.translate(target, source, first_translation)

            # Fill response with Sentence objects
            data_translated = []
            for original, translated, back_translated in zip(data, first_translation, second_translation):
                data_translated.append(Sentence(original=original, translated=translated, back_translated=back_translated))
                container_translated.append(back_translated)
            response.extend(data_translated)

        return response, container_translated
