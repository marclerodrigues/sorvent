# Responsible for holding team information
# How to use:
#
# team_attributes = {
#     'name': 'Beta',
#     'tutor': 'Jame',
#     'participants': []
# }
#
# team = Team(team_attributes)
#
# print(team)

class Team:
    def __init__(self, attributes = {}):
        self.tutor = attributes['tutor']
        self.name = attributes['name'] or 'No Name'
        self.participants = attributes['participants']

    def size(self):
        return len(self.participants)

    def __str__(self):
        return 'Team %(name)s' % { 'name': self.name }

