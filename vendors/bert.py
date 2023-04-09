from typing import List

import os

from torch import Tensor
from bert_score import score


class Bert:
    def __init__(self):
        self.model_type = os.environ.get('BERT_MODEL_TYPE', 't5-small')

    def score_getter(self, first: List, second: List) -> Tensor:
        from app.views import SOURCE_LANG
        p, r, f = score(first, second, lang=SOURCE_LANG, model_type=self.model_type)
        return f
