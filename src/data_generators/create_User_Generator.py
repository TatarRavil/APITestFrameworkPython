from faker import Faker
from src.baseClasses.builder import BuilderBaseClass


class CreateUserGenerator(BuilderBaseClass):

    def __init__(self, lang):
        super().__init__()
        self.faker = Faker(lang)
        self.result = {}
        self.reset()

    def update_email(self, email=None):
        self.result['email'] = email or self.faker.ascii_free_email()
        return self

    def update_password(self, password=None):
        self.result['password'] = password or self.faker.first_name()
        return self

    def reset(self):
        self.update_email()
        self.update_password()
        return self
