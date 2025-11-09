from .base_exporter import BaseExport
from .data_type import Data
from json import dumps
from .exporter_register import register_exporter 

@register_exporter
class JSONExporter(BaseExport):
    format = "json"

    def export(self, data: Data) -> None:
        print(f"Exporting data to JSON:\n{dumps(data, indent=2)}")