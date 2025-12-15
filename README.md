# XML-Validator-Parser
A tool to validate an XML file against the official pain.001 (Customer Credit Transfer Initiation) XSD schema and extracts key payment details

## Features

- Validates XML files against the official pain.001.001.09 XSD schema (using xmlschema)
- Safely extracts and displays key payment information:
  - Number of transactions
  - Debtor name
  - Total amount of transactions
- Command-line friendly (via argparse)
- Includes automated tests (pytest) and linting (pylint)
- Continuous Integration with GitHub Actions (lint + test on every push)

## Requirements

- Python 3.9+
- lxml
- xmlschema

## Installation & Usage

#### 1. Clone the repository:
```bash
git clone https://github.com/aklimchu/XML-Validator-Parser.git
cd XML-Validator-Parser
```

#### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Run the validator on an example file:
```bash
python xml_validator.py tests/valid_example.xml
```
Example output:
```bash
✅ XML is valid against the schema!

Summary:
   Number of transactions: 2
   Debtor: Acme Corp
   First creditor: Global Tech
   Control sum: 1100.00 EUR
```

#### 5. Try an invalid example (included in tests/):
```bash
python xml_validator.py tests/invalid_example.xml
```
→ Shows schema validation errors

#### 6. Get help:
```bash
python xml_validator.py --help
```

## Project Structure
```bash
├── xml_validator.py          # Main script
├── schemas/
│   └── pain.001.001.09.xsd   # Official schema
├── tests/
│   ├── valid_example.xml
│   ├── invalid_example.xml
│   └── test_validator.py     # Pytest suite
├── .github/workflows/ci.yml  # GitHub Actions CI
├── requirements.txt
├── LICENSE
└── README.md
```
