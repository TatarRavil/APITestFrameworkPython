import pytest
import requests
import configuration
from src.baseClasses.response import Response
from src.pydantic_schemas import computer
from src.pydantic_schemas.computer import Computer
from src.pydantic_schemas.user import User, User1


from src.pydantic_schemas.post import Post


def test_getting_posts():
    r = requests.get(configuration.SERVICE_URL)
    response = Response(r)

    response.assert_status_code(200).validate_json(Post)

@pytest.mark.prod
# @pytest.mark.skip('wrong api')
def test_getting_users(authorization, get_response, sum_numbers, connection_to_db):
    """
    In that test we try to get users from GOREST_URL
    """
    test_data = Response(get_response, 'data')
    test_data.assert_status_code(200).validate_json(User)


@pytest.mark.dev
@pytest.mark.parametrize('page', ['1', '2', '3'])
def test_get_users(page):
    """
        In that test we try to get users from REQRES_URL
    """
    response = requests.get(configuration.REQRES_URL + '/api/users?page=' + page)
    test_data = Response(response, 'data')
    test_data.assert_status_code(200).validate_json(User1)


def test_register_user(create_player_generator):
    response = requests.post(
        url=configuration.REQRES_URL + '/api/register',
        data=create_player_generator.build())

    test_data = Response(response)
    test_data.assert_status_code(200)
    print(test_data.response_json)


def test_create_file_to_send(create_player_generator):
    data = create_player_generator.update_inner_value(['temp', 'ru', 'example'], 'ex@gmail.com').build()

    print(data)

def test_pydantic_object():
    """
    Пример того, как после инициализации pydantic объекта, можно получить
    доступ к любому из его параметров.
    """
    comp = Computer.parse_obj(computer)
    print(comp.detailed_info.physical.color)