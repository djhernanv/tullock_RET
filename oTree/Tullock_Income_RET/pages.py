from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

import numpy as np
import string

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class CompetitionInstructions1(Page):
    def is_displayed(self):
        return self.round_number == 1


class CompetitionInstructions2Example(Page):
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        if Constants.treatment:
            return {'income_1': self.participant.vars['net_income_1'],
                    'income_2': self.participant.vars['net_income_2'],
                    'income_3': self.participant.vars['net_income_3'],
                    'income_4': self.participant.vars['net_income_4'],
                    'valuation': self.participant.vars['net_income_3'] - self.participant.vars['net_income_1'],
                    'abs_valuation': abs(self.participant.vars['net_income_3'] - self.participant.vars['net_income_1']),
                    'taxed_valuation': self.participant.vars['net_income_4'] - self.participant.vars['net_income_2'],
                    'taxed_abs_valuation': abs(self.participant.vars['net_income_4'] - self.participant.vars['net_income_2']),
                    }
        else:
            return {'income_1': self.participant.vars['net_income_1'],
                    'income_2': self.participant.vars['net_income_2'],
                    'valuation': self.participant.vars['net_income_2'] - self.participant.vars['net_income_1'],
                    'abs_valuation': abs(self.participant.vars['net_income_2'] - self.participant.vars['net_income_1']),
                    }


class CompetitionInstructions3(Page):
    def is_displayed(self):
        return self.round_number == 1


class FairnessFirst(Page):
    form_model = 'player'
    form_fields = ['fairness_first',
                   ]

    def is_displayed(self):
        return self.round_number == 1


class Waiting(WaitPage):
    def after_all_players_arrive(self):
        # Make Sure the generating seed depends on the round or session
        string_list = []  # this will be the list of strings to be used
        for n in range(10, 200,
                       Constants.increase_per_string):  # where "a" is the smallest and "b-1" the largest possible string.
            # For now with an increment of "c"
            character_list = string.ascii_lowercase  # where the random sample for the strings will be drawn
            np.random.seed(
                Constants.random_seed_ret + n + self.round_number)  # on every turn of the loop a new character list will be created
            character_list += "a" * np.random.randint(15, 30)  # this gives, in average one "a" for each letter
            np.random.seed(Constants.random_seed_ret + 1 + n + self.round_number)  # to ensure reproducibility
            #  of the alphabet s.t. the relationship is 2:1 but still allows for enough variability
            string_list.append("".join(np.random.choice(list(character_list), size=n)))
        self.session.vars['string_list'] = string_list
        # count solutions
        a_count = []
        for i in range(len(string_list)):
            a_count.append(string_list[i].count("a"))
        self.session.vars['a_count'] = a_count


class RoundStart(Page):

    def vars_for_template(self):
        if self.round_number > 1:
            return {'winner_last': self.player.in_round(self.round_number - 1).is_winner,
                    'winner_last_0': self.player.get_others_in_group()[0].in_round(self.round_number - 1).is_winner,
                    'winner_last_1': self.player.get_others_in_group()[1].in_round(self.round_number - 1).is_winner,
                    }


class BeliefsProduction(Page):
    form_model = 'player'
    form_fields = [
        'production_belief_0',
        'production_belief_1',

    ]

    def vars_for_template(self):
        if self.round_number > 1:
            return {'winner_last': self.player.in_round(self.round_number - 1).is_winner,
                    'winner_last_0': self.player.get_others_in_group()[0].in_round(self.round_number - 1).is_winner,
                    'winner_last_1': self.player.get_others_in_group()[1].in_round(self.round_number - 1).is_winner,
                    }

class StartSubmit(Page):
    pass


class RET(Page):
    timeout_seconds = Constants.t
    form_model = 'player'
    form_fields = ['t101',
                   't102',
                   't103',
                   't104',
                   't105',
                   't106',
                   't107',
                   't108',
                   't109',
                   't110',
                   't111',
                   't112',
                   't113',
                   't114',
                   't115',
                   't116',
                   't117',
                   't118',
                   't119',
                   't120',
                   't121',
                   't122',
                   't123',
                   't124',
                   't125',
                   't126',
                   't127',
                   't128',
                   't129',
                   't130',
                   't131',
                   't132',
                   't133',
                   't134',
                   't135',
                   't136',
                   't137',
                   't138',
                   't139',
                   't140',
                   't141',
                   't142',
                   't143',
                   't144',
                   't145',
                   'production_strings',
                   'switch1',
                   'additional_time'
                   ]

    def before_next_page(self):
        self.player.set_switch()

    def vars_for_template(self):
        if self.round_number > 1:
            return {'winner_last': self.player.in_round(self.round_number - 1).is_winner}


class Waiting2(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_incomes()
        self.group.set_fiscal()


class BeliefsInvestment(Page):

    def is_displayed(self):
        return self.round_number < Constants.num_rounds

    form_model = 'player'
    form_fields = [
        'investment_belief_0',
        'investment_belief_1',

    ]

    def vars_for_template(self):
        if self.round_number > 1:
            return {'winner_last': self.player.in_round(self.round_number - 1).is_winner,
                    'winner_last_0': self.player.get_others_in_group()[0].in_round(self.round_number - 1).is_winner,
                    'winner_last_1': self.player.get_others_in_group()[1].in_round(self.round_number - 1).is_winner,
                    }


class Investment(Page):
    form_model = 'player'
    form_fields = ['investment_amount']

    def vars_for_template(self):
        return {'income': safe_json(round(self.player.available_income, 2))}

    def is_displayed(self):
        return self.round_number < Constants.num_rounds


class Waiting3(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_probabilities()
        self.group.set_winner()
        self.group.set_payoffs()


class Feedback(Page):
    pass


class Results(Page):

    def is_displayed(self):
        return self.round_number < Constants.num_rounds

    def vars_for_template(self):
        if self.round_number > 1:
            return {'winner_last': self.player.in_round(self.round_number - 1).is_winner,
                    'winner_last_0': self.player.get_others_in_group()[0].in_round(self.round_number - 1).is_winner,
                    'winner_last_1': self.player.get_others_in_group()[1].in_round(self.round_number - 1).is_winner,
                    }


class EndCompetition(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class FairnessEnd(Page):
    form_model = 'player'
    form_fields = ['fairness_end',
                   ]

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class AllGroupsWaitPage(WaitPage):
    wait_for_all_groups = True

page_sequence = [
    AllGroupsWaitPage,
    CompetitionInstructions1,
    CompetitionInstructions2Example,
    CompetitionInstructions3,
    FairnessFirst,
    RoundStart,  # informs about the present round.
    BeliefsProduction,
    Waiting,  # creates string list
    StartSubmit,
    RET,
    Waiting2,  # sets income for winner/loser of last round
    Feedback,  # information about production
    BeliefsInvestment,
    Investment,  # Participant can invest some of her earnings to win prize
    Waiting3,  # sets probabilities and determines winner
    Results,  # what the investments were and who won
    FairnessEnd,
    EndCompetition,
]
