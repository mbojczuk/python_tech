from .base_exporter import BaseExport
from .data_type import Data
from .exporter_register import ExporterRegistry

@ExporterRegistry.register
class ExportCSV(BaseExport):
    _format = "csv"
    
    def export_data(self, data: Data) -> None:
        # Simulated CSV output
        headers = ",".join(data.keys())
        values = ",".join(str(v) for v in data.values())
        print(f"Exporting data to CSV:\n{headers}\n{values}")