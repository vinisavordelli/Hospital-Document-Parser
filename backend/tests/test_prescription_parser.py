from src.document_parsers.prescription_parser import PrescriptionParser
from mocks.prescription_mocks import prescription_mock1, prescription_mock2
import pytest


@pytest.fixture()
def prescription1():
    return PrescriptionParser(prescription_mock1)


@pytest.fixture()
def prescription2():
    return PrescriptionParser(prescription_mock2)


def test_get_doctor_info(prescription1, prescription2):
    assert "John Smith", "(000)-111-2222" in prescription1.get_doctor_info()
    assert "John Smith", "(900)-323- ~2222" in prescription2.get_doctor_info()


def test_get_patient_name(prescription1, prescription2):
    assert prescription2.get_patient_name() == "Virat Kohli"
    assert prescription1.get_patient_name() == "Marta Sharapova"


def test_get_address(prescription1, prescription2):
    assert prescription1.get_address() == "9 tennis court, new Russia, DC"
    assert prescription2.get_address() == "2 cricket blvd, New Delhi"


def test_get_prescription(prescription1, prescription2):
    assert "Taper 5 mg every 3 days", (
        "Lialda",
        "Prednisone" in prescription1.get_prescription(),
    )
    assert "Omeprazole 40" in prescription2.get_prescription()


def test_get_directions(prescription1, prescription2):
    assert (
        "Use two tablets daily for three months"
        in prescription2.get_directions()
    )


def test_get_refill(prescription1, prescription2):
    assert prescription1.get_refill() == "2 times"
    assert prescription2.get_refill() == "3 times"
