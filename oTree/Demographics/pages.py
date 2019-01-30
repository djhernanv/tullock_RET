from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Demographics(Page):
    form_model = 'player'
    form_fields = ['gender',
                   'year_of_birth',
                   ]


class AllGroupsWaitPage(WaitPage):
    wait_for_all_groups = True


page_sequence = [
    Demographics,
    AllGroupsWaitPage,
]
