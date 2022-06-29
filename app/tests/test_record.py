import pytest
from contact_book.record import Record, Name, Phone, Email, Birthday
from unittest.mock import MagicMock, PropertyMock
from datetime import date, datetime

PHONE = '0000000000'
NAME = 'Nataly'
EMAIL = 'first@go.com'
BIRTH = '01.01.2000'

@pytest.fixture(name='name')
def name_fixture():
    return Name(NAME)


@pytest.fixture(name='phone')
def phone_fixture():
    return Phone(PHONE)


@pytest.fixture(name='email')
def email_fixture():
    return Email(EMAIL)


@pytest.fixture(name='birthday')
def birthday_fixture():
    return Birthday(BIRTH)


def test_init_no_args(name):
    rec = Record(name=name)
    assert rec.name.value == NAME
    assert rec.nums == []
    assert rec.emails == []
    assert rec.birthday is None


def test_init_args(name, phone, birthday, email):
    rec = Record(name=name, num=phone, birthday=birthday, email=email)
    assert rec.name.value == NAME
    assert len(rec.nums) == 1
    assert rec.numbers[0] == phone
    assert len(rec.emails) == 1
    assert rec.e_mails[0] == email
    assert rec.birthday.value_as_str == BIRTH
    assert rec.birthday.value == datetime.strptime(BIRTH,
                                                   '%d.%m.%Y').date()


def test_add_email_to_empty(name, email):
    rec = Record(name=name)
    rec.add_email(email)
    assert len(rec.e_mails) == 1


def test_add_phone_to_empty(name, phone):
    rec = Record(name=name)
    rec.add_phone(phone)
    assert len(rec.numbers) == 1


def test_add_email_to_not_empty(name, email):
    rec = Record(name=name, email=email)
    rec.add_email(email)
    assert len(rec.e_mails) == 1


def test_add_phone_to_not_empty(name, phone):
    rec = Record(name=name, num=phone)
    rec.add_phone(phone)
    assert len(rec.numbers) == 1


def test_remove_phone_from_empty(name, phone):
    rec = Record(name=name)
    with pytest.raises(ValueError):
        rec.remove_phone(phone)


def test_remove_phone(name, phone):
    rec = Record(name=name, num=phone)
    num = rec.remove_phone(phone)
    assert num == phone
    assert len(rec.nums) == 0
    assert rec.numbers is None


def test_edit_phone_in_empty(name, phone):
    rec = Record(name=name)
    with pytest.raises(ValueError):
        rec.edit_phone(phone, phone)


def test_number_in_list_positive(name, phone):
    rec = Record(name=name, num=phone)
    some_num = Phone(phone.value)
    exist = rec.number_in_list(some_num)
    assert exist == phone


def test_number_in_list_negative(name, phone):
    rec = Record(name=name)
    exist = rec.number_in_list(phone)
    assert exist is None


def test_email_in_list_positive(name, email):
    rec = Record(name=name, email=email)
    some_email = Email(email.value)
    exist = rec.email_in_list(some_email)
    assert exist == email


def test_email_in_list_negative(name, email):
    rec = Record(name=name)
    exist = rec.email_in_list(email)
    assert exist is None


def test_get_email_positive(name, email):
    rec = Record(name=name, email=email)
    obj = rec.get_email(EMAIL)
    assert obj == email


def test_get_email_negative(name, email):
    rec = Record(name=name)
    obj = rec.get_email(EMAIL)
    assert obj is None


def test_get_phone_positive(name, phone):
    rec = Record(name=name, num=phone)
    obj = rec.get_phone(PHONE)
    assert obj == phone


def test_get_phone_negative(name, phone):
    rec = Record(name=name)
    obj = rec.get_phone(PHONE)
    assert obj is None