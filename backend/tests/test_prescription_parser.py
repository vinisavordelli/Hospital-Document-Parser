from src.document_parsers.prescription_parser import PrescriptionParser
from mocks.prescription_mocks import prescription_mock1, prescription_mock2
import pytest


@pytest.fixture()
def prescription1():
    return PrescriptionParser(prescription_mock1)


@pytest.fixture()
def prescription2():
    return PrescriptionParser(prescription_mock2)


@pytest.fixture()
def prescription3():
    return PrescriptionParser("")


def test_get_doctor_info(prescription1, prescription2, prescription3):
    assert "John Smith", "(000)-111-2222" in prescription1.get_doctor_info()
    assert "John Smith", "(900)-323- ~2222" in prescription2.get_doctor_info()
    assert prescription3.get_doctor_info() == "Not Found"


def test_get_patient_name(prescription1, prescription2, prescription3):
    assert prescription2.get_patient_name() == "Virat Kohli"
    assert prescription1.get_patient_name() == "Marta Sharapova"
    assert prescription3.get_patient_name() == "Not Found"


def test_get_address(prescription1, prescription2, prescription3):
    assert prescription1.get_address() == "9 tennis court, new Russia, DC"
    assert prescription2.get_address() == "2 cricket blvd, New Delhi"
    assert prescription3.get_address() == "Not Found"


def test_get_prescription(prescription1, prescription2, prescription3):
    assert "Taper 5 mg every 3 days", (
        "Lialda",
        "Prednisone" in prescription1.get_prescription(),
    )
    assert "Omeprazole 40" in prescription2.get_prescription()
    assert prescription3.get_prescription() == "Not Found"


def test_get_directions(prescription1, prescription2, prescription3):
    assert "Finish in 2.5 weeks" in prescription1.get_directions()
    assert (
        "Use two tablets daily for three months"
        in prescription2.get_directions()
    )
    assert prescription3.get_directions() == "Not Found"


def test_get_refill(prescription1, prescription2, prescription3):
    assert prescription1.get_refill() == "2 times"
    assert prescription2.get_refill() == "3 times"
    assert prescription3.get_refill() == "Not Found"


def test_parse(prescription1, prescription2, prescription3):
    assert prescription1.parse() == {
        "Doctor Info": "John Smith, M.D\n2 Non-Important Street,\nNew York, Phone (000)-111-2222",
        "Patient Name": "Marta Sharapova",
        "Address": "9 tennis court, new Russia, DC",
        "Prescription": "Prednisone 20 mig\nLialda 2.4 gram",
        "Directions": "Prednisone, Taper 5 mg every 3 days,\nFinish in 2.5 weeks a\nLialda - take 2 pill everyday for 1 month >",
        "Refill": "2 times",
    }

    assert prescription2.parse() == {
        "Doctor Info": "John Smith, M.D\n\n2 Non-Important Street,\nNew York, Phone (900)-323- ~2222",
        "Patient Name": "Virat Kohli",
        "Address": "2 cricket blvd, New Delhi",
        "Prescription": "| Omeprazole 40 meg",
        "Directions": "Use two tablets daily for three months",
        "Refill": "3 times",
    }

    assert prescription3.parse() == {
        "Doctor Info": "Not Found",
        "Patient Name": "Not Found",
        "Address": "Not Found",
        "Prescription": "Not Found",
        "Directions": "Not Found",
        "Refill": "Not Found",
    }
