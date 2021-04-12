

class AccountObj:
    def __init__(self, first_name, last_name, email, password, birth_month, birth_day, birth_year, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.birth_month = birth_month.value
        self.birth_day = birth_day
        self.birth_year = birth_year
        self.gender = gender.value

