## class_static_methods.py

## TODO `@classmethod`

class User:

    all_users = []

    def __init__(self, first_name, last_name, email) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        User.all_users.append(self)

    @classmethod
    def clear_users(cls):
        cls.all_users.clear()


## TODO `@staticmethod`

    @staticmethod
    def validate_user(user):
        print(user.first_name)
        if len(user.first_name) < 2:
            print("first name must be at least two chars")

john = User("john", "doe", "jd@email.com")
mary = User("mary", "jane", "mj@aol.com")
d = User("d", "Smith", "ddog@dogpound.com")