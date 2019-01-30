from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

# The app will be shown only after ALL participants have finished to avoid them leaving early etc.


class AllGroupsWaitPage(WaitPage):
    wait_for_all_groups = True


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    def vars_for_template(self):
        return {'net_income_1': self.participant.vars['net_income_1'],
                'net_income_2': self.participant.vars['net_income_2'],
                'payoff': self.participant.payoff,
                }


page_sequence = [
    AllGroupsWaitPage,
    ResultsWaitPage,
    Results
]
