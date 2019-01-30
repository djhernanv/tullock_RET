from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Hernán Villamizar'

doc = """
This is a questionnaire of general demographics questions such as gender and age
"""


class Constants(BaseConstants):
    name_in_url = 'Fairness'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    fairness = models.PositiveIntegerField(default=0)
