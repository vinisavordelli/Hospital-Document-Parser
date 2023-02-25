from backend.src.document_parsers.patient_details_parser import (
    PatientDetailsParser,
)
import mocks.patient_details_mocks as pdm
import pytest


@pytest.fixture()
def patient_details1():
    return PatientDetailsParser(pdm.pd_mock1).parse()


@pytest.fixture()
def patient_details2():
    return PatientDetailsParser(pdm.pd_mock2).parse()


@pytest.fixture()
def patient_details3():
    return PatientDetailsParser(pdm.pd_mock3).parse()


def test_get_patient_name(
    patient_details1, patient_details2, patient_details3
):
    assert patient_details1["patient_name"] == pdm.expected1["patient_name"]
    assert patient_details2["patient_name"] == pdm.expected2["patient_name"]
    assert patient_details3["patient_name"] == pdm.expected3["patient_name"]
