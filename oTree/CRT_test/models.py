from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Hernán Villamizar'

doc = """
This app tests the Cognitive Response of participants implementing the questions by Thomson and Oppenheimer (2016)
"""


class Constants(BaseConstants):
    name_in_url = 'CRT_test'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    crt_1 = models.PositiveIntegerField()
    crt_2 = models.PositiveIntegerField()
    crt_3 = models.StringField()
    crt_4 = models.FloatField()
