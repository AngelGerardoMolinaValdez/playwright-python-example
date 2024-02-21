import os
from dataclasses import dataclass, make_dataclass
from utils.abstract_data_reader import AbstractDataReader

class DataTableCreator:
    @staticmethod
    def create_table(reader: AbstractDataReader, source: str) -> list[dataclass]:
        """Create a DataTable from the CSV file."""
        cd = os.path.dirname(__file__)
        data_dir = os.path.join(cd, "..", "data")
        data_source = os.path.abspath(os.path.join(data_dir, source))

        datatables: list[dataclass] = []
        testdata_rows = reader.read(data_source)

        for testdata_row in testdata_rows:
            DataTable: dataclass = make_dataclass("DataTable", testdata_row.keys())
            datatables.append(DataTable(**testdata_row))

        return datatables
