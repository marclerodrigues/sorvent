# Responsible for holding person information
# How to use:
#
# person_attributes = {
#     'name': 'James Bond',
#     'age': 19,
#     'gender': 'male',
#     'kind': 'tutor'
# }
# person = Person(person_attributes)
#
# print(person.is_tutor())
# print(person.is_organizer())
# print(person)

class Person:
    def __init__(self, attributes = {}):
        self.name   = attributes['name']
        self.age    = attributes['age']
        self.gender = attributes['gender']
        self.kind   = attributes['kind']

    def is_tutor(self):
        return self.kind == 'tutor'

    def is_participant(self):
        return self.kind == 'participant'

    def is_organizer(self):
        return self.kind == 'organizer'

    def __str__(self):
        return self.name

