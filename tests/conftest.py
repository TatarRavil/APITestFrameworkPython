import pytest
import requests
import configuration


# scope='session' - можно использовать для коннекта к базе. Выполняется единожды за ссесию и кешируется.
# autouse= True - фикстура будет выполняется автоматически для всех тестов. Можно не указывать фикстуру.

@pytest.fixture(scope='function', autouse=False)
def authorization():
    print('Авторизация')
