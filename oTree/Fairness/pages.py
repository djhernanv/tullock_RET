from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Fairness(Page):
    form_model = 'player'
    form_fields = ['fairness',
                   ]


page_sequence = [
    Fairness,
]
