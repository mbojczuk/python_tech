from .base_exporter import BaseExport
from .data_type import Data
from .exporter_register import ExporterRegistry

@ExporterRegistry.register
class ExportPDF(BaseExport):
    _format = "pdf"
    
    def export_data(self, data: Data) -> None:
       print(f"Exporting PDF: {data}")