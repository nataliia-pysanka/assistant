import pytest
from contact_book.contactbook import ContactBook
from unittest.mock import MagicMock, PropertyMock
from datetime import date


@pytest.fixture(name="contact_book")
def fixture_contact_book():
    return ContactBook()


@pytest.fixture(name="record")
def fixture_record():
    record = MagicMock()
    type(record).name = PropertyMock(return_value='name')
    type(record).birthday = PropertyMock(return_value=date(year=2022, month=6, day=24))

    return record


def test_contact_book_add(contact_book, record):
    contact_book.add(record)
    assert len(contact_book.names) == 1
    assert contact_book.names[0] == 'name'


def test_contact_book_delete(contact_book, record):
    contact_book.add(record)
    res = contact_book.delete('name')
    assert len(contact_book.names) == 0
    assert res is True


def test_contact_book_delete_if_no_data(contact_book):
    res = contact_book.delete('name')
    assert len(contact_book.names) == 0
    assert res is False


def test_contact_book_str(contact_book, record):
    contact_book.add(record)
    msg = f'My contacts: \nname\n'
    assert contact_book.__str__() == msg


def test_contact_book_str_if_no_data(contact_book):
    assert contact_book.__str__() is None


def test_search(contact_book, record):
    contact_book.add(record)
    rec = contact_book.search('name')
    assert rec == record
    assert len(contact_book.names) == 1


def test_search_if_no_data(contact_book):
    rec = contact_book.search('name')
    assert rec is None
    assert len(contact_book.names) == 0
