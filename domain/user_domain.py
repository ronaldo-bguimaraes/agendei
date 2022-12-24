class UserDomain:
    def __init__(self, id_user: int, first_name: str, last_name: str, birth_date: str, email: str, password: str):
        self.id_user = id_user
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.email = email
        self.password = password

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
