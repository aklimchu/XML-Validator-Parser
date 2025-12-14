import argparse
import xmlschema
from lxml import etree

def validate_and_parse(xml_file: str, xsd_file: str):
    # Load and validate against schema
    schema = xmlschema.XMLSchema(xsd_file)
    if schema.is_valid(xml_file):
        print("✅ XML is valid against the schema!")
    else:
        print("❌ XML is INVALID:")
        try:
            schema.validate(xml_file)
        except xmlschema.XMLSchemaValidationError as e:
            print(e)
        return

    # Parse and extract key info
    tree = etree.parse(xml_file)
    root = tree.getroot()

    ns = {'doc': 'urn:iso:std:iso:20022:tech:xsd:pain.001.001.09'}

    print("\nSummary:")

    # Find and print number of transactions
    nb_of_txs_elem = root.find('.//doc:GrpHdr/doc:NbOfTxs', namespaces=ns)
    if nb_of_txs_elem is not None:
        print(f"   Number of transactions: {nb_of_txs_elem.text}")
    else:
        print("   Number of transactions: Not found")

    # Find and print control sum
    ctrl_sum_elem = root.find('.//doc:GrpHdr/doc:CtrlSum', namespaces=ns)
    if ctrl_sum_elem is not None:
        print(f"   Control sum: {ctrl_sum_elem.text} EUR")
    else:
        print("   Control sum: Not found")

    # Find and print debtor name
    debtor_name_elem = root.find('.//doc:PmtInf/doc:Dbtr/doc:Nm', namespaces=ns)
    if debtor_name_elem is not None:
        print(f"   Debtor: {debtor_name_elem.text}")
    else:
        print("   Debtor name: Not found")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate and parse ISO 20022 pain.001 XML")
    parser.add_argument("xml_file", help="Path to the XML file")
    parser.add_argument("--xsd", default="schemas/pain.001.001.09.xsd", help="Path to XSD schema")
    args = parser.parse_args()

    validate_and_parse(args.xml_file, args.xsd)