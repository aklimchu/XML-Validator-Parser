import pytest
from xml_validator import validate_and_parse

VALID_XML = "tests/valid_example.xml"
INVALID_XML = "tests/invalid_example.xml"
XSD = "schemas/pain.001.001.09.xsd"

def test_valid_xml_passes_validation(capsys):
    validate_and_parse(VALID_XML, XSD)
    captured = capsys.readouterr()
    assert "✅ XML is valid" in captured.out

def test_invalid_xml_fails_validation(capsys):
    validate_and_parse(INVALID_XML, XSD)
    captured = capsys.readouterr()
    assert "❌ XML is INVALID" in captured.out

def test_parses_key_fields():
    # Can be added later
    pass