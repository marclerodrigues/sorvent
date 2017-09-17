from random import shuffle
from sorvent.models import Team

class SortTeamsService:
    def __init__(self, attributes = {}):
        self.tutors = attributes['tutors']
        self.participants = attributes['participants']
        self.teams_size = attributes['teams_size']
        self.teams = []

    def sort(self):
        shuffle(self.participants)

        for index, tutor in enumerate(self.tutors):
            team_participants = []

            for number in range(self.teams_size):
                team_participants.append(self.participants.pop(number))

            team = self.__create_team(index, tutor, team_participants)

            self.teams.append(team)

        return self.teams

    def teamless_participants(self):
        return self.participants

    @staticmethod
    def __create_team(index, tutor, participants):
        team_attributes = {
            'name': 'Team %(index)s' % { 'index': index },
            'tutor': tutor,
            'participants': participants
        }

        return Team(team_attributes)

