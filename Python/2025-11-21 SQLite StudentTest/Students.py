import itertools

class Student:
    id_iter = itertools.count(start=1, step=1)

    def __init__(self, first_name: str, last_name: str, student_number: int=None):
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = next(self.id_iter)

    @property
    def email(self):
        email_address = '{}.{}-{}@email.com'.format(self.first_name, self.last_name, self.student_number)
        return email_address
    
    @property
    def lastfirst(self):
        return '{} {}'.format(self.last_name, self.first_name)