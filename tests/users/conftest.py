import pytest
import requests
import configuration
from src.data_generators.create_User_Generator import CreateUserGenerator


# scope='session' - можно использовать для коннекта к базе. Выполняется единожды за ссесию и кешируется.
# autouse= True - фикстура будет выполняется автоматически для всех тестов. Можно не указывать фикстуру.

@pytest.fixture()
def create_player_generator():
    return CreateUserGenerator('en_US')


@pytest.fixture(scope='function', autouse=False)
def get_response():
    response = requests.get(configuration.GOREST_URL)
    return response


def _sum_numbers(x, y):
    return x + y


@pytest.fixture
def sum_numbers():
    return _sum_numbers


@pytest.fixture
def connection_to_db():
    print('Connection to DB')
    yield
    print('Disconnect to DB')
