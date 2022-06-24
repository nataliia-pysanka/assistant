import pytest
from contact_book.contactbook import ContactBook
from unittest.mock import Mock, MagicMock, PropertyMock


@pytest.fixture(name="contact_book")
def fixture_contact_book():
    return ContactBook()


@pytest.fixture(name="record")
def fixture_record():
    record = MagicMock()
    type(record).name = PropertyMock(return_value='name')
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


def test_contact_book_str(contact_book, record):
    contact_book.add(record)
    msg = f'My contacts: \n name'
    assert contact_book.__str__() == msg

