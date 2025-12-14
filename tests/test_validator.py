import pytest
from xml_validator import validate_and_parse

def test_valid_xml_passes_validation():
    validate_and_parse()
    return