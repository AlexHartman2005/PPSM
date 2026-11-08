import csv
import unittest
from pathlib import Path

from ppsm.export import CSV_HEADERS, export_to_csv


class ExportToCsvTests(unittest.TestCase):
    def setUp(self):
        self.output_path = Path(__file__).with_name("_test_export.csv")
        self.addCleanup(self.output_path.unlink, missing_ok=True)

    def read_rows(self):
        with self.output_path.open(encoding="utf-8", newline="") as csv_file:
            return list(csv.reader(csv_file))

    def test_exports_headers_and_records_in_ppsm_order(self):
        records = [
            {
                "ports": 443,
                "protocol": "tcp",
                "service": "https",
                "source_ip": "10.0.0.5",
                "source_name": "workstation",
                "destination_ip": "10.0.0.10",
                "destination_name": "web-server",
            }
        ]

        result = export_to_csv(records, self.output_path)

        self.assertEqual(result, self.output_path)
        self.assertEqual(
            self.read_rows(),
            [
                list(CSV_HEADERS),
                [
                    "443",
                    "tcp",
                    "https",
                    "10.0.0.5",
                    "workstation",
                    "10.0.0.10",
                    "web-server",
                ],
            ],
        )

    def test_accepts_singular_port_and_escapes_csv_values(self):
        record = {
            "port": "80, 443",
            "protocol": "tcp",
            "service": 'web "frontend"',
            "source_ip": "10.0.0.5",
            "source_name": "user workstation",
            "destination_ip": "10.0.0.10",
            "destination_name": "web-server\nproduction",
        }

        export_to_csv([record], self.output_path)

        self.assertEqual(self.read_rows()[1], list(record.values()))

    def test_empty_export_still_contains_headers(self):
        export_to_csv([], self.output_path)

        self.assertEqual(self.read_rows(), [list(CSV_HEADERS)])

    def test_rejects_a_record_with_missing_fields(self):
        with self.assertRaisesRegex(ValueError, "source_name"):
            export_to_csv(
                [
                    {
                        "ports": 22,
                        "protocol": "tcp",
                        "service": "ssh",
                        "source_ip": "10.0.0.5",
                        "destination_ip": "10.0.0.10",
                        "destination_name": "server",
                    }
                ],
                self.output_path,
            )

    def test_rejects_non_mapping_records(self):
        with self.assertRaisesRegex(TypeError, "record 1 must be a mapping"):
            export_to_csv([[22, "tcp", "ssh"]], self.output_path)


if __name__ == "__main__":
    unittest.main()
