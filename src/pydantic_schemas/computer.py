from pydantic import BaseModel, EmailStr, validator
from pydantic.types import PastDate, FutureDate, List, PaymentCardNumber
from pydantic.networks import IPv4Address, IPv6Address

from src.pydantic_schemas.physical import Physical

from src.enums.user_enums import Statuses


class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr


class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]


class Computer(BaseModel):
    id: int
    status: Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo


class Human(BaseModel):
    name: str
    last_name: str
    surname: str = None
    is_hide: bool

    @validator('is_hide')
    def validate_surname_showing(cls, hide_value, values):
        """
        Пример валидатора, который используется для проверки значения в поле
        is_hide.
        """
        if hide_value is False and values.get('surname') is None:
            raise ValueError('Surname should be presented')
        return hide_value


human = Human.parse_obj({
    "name": "Andrii",
    "last_name": "Shevchenko",
    "is_hide": True
})


class Inventory(BaseModel):
    sold: int
    string: int
    unavailable: int
    pending: int
    available: int
    not_available: int
    status01: int
    status: int

# computer = {
#     "id": 21,
#     "status": "ACTIVE",
#     "activated_at": "2013-06-01",
#     "expiration_at": "2040-06-01",
#     "host_v4": "91.192.222.17",
#     "host_v6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
#     "detailed_info": {
#         "physical": {
#             "color": 'green',
#             "photo": 'https://images.unsplash.com/photo-1587831990711-23ca6441447b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8ZGVza3RvcCUyMGNvbXB1dGVyfGVufDB8fDB8fA%3D%3D&w=1000&q=80',
#             "uuid": "73860f46-5606-4912-95d3-4abaa6e1fd2c"
#         },
#         "owners": [{
#             "name": "Stephan Nollan",
#             "card_number": "4000000000000002",
#             "email": "shtephan.nollan@gmail.com",
#         }]
#     }
# }