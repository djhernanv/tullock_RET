from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Hernán Villamizar'

doc = """
This app displays a final page to inform participants the session is over
"""


class Constants(BaseConstants):
    name_in_url = 'D_Final_Results'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
