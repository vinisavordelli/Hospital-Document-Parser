from src.document_parsers.prescription_parser import PrescriptionParser
import mocks.prescription_mocks as pm
import pytest


@pytest.fixture()
def prescription1():
    return PrescriptionParser(pm.prescription_mock1)


@pytest.fixture()
def prescription2():
    return PrescriptionParser(pm.prescription_mock2)


@pytest.fixture()
def prescription3():
    return PrescriptionParser("")


def test_parse(prescription1, prescription2, prescription3):

    assert prescription3.parse() == pm.expected3
