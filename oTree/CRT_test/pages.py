from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class CRT(Page):
    form_model = 'player'
    form_fields = ['crt_1',
                   'crt_2',
                   'crt_3',
                   'crt_4',
                   ]


class AllGroupsWaitPage(WaitPage):
    wait_for_all_groups = True

page_sequence = [
    CRT,
    AllGroupsWaitPage,  # for reading of instructions in mpl
]
