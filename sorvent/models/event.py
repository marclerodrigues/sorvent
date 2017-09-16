# How to use:
#
# event_attributes = {
#     'name': 'Rails Girls',
#     'tutors': [],
#     'participants': [],
#     'date': '09/25/2017',
#     'address': 'Av. Ininga, 777',
#     'organizers': []
# }
# event = Event(event_attributes)
#
# print(event)
# print(event.total_attendees())

class Event:
    def __init__(self, attributes = {}):
        self.participants = attributes['participants']
        self.tutors = attributes['tutors']
        self.max_participants = attributes['participants']
        self.organizers = attributes['organizers']
        self.name = attributes['name']
        self.date = attributes['date']
        self.address = attributes['address']

    def total_attendees(self):
        return len(self.organizers) + len(self.tutors) + len(self.participants)

    def __str__(self):
        return self.name

