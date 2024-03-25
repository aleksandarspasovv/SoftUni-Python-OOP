class Profile:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__username

    @password.setter
    def password(self, value):
        len_is_valid = len(value) >= 8
        is_upper = len([c for c in value if c.isupper()]) > 0
        is_digit = len([c for c in value if c.isdigit()]) > 0

        if not len_is_valid and not is_digit and not is_upper:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__username = value

    def __str__(self):

        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'




correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)