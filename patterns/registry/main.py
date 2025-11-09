from .register.exporter_register import ExporterRegistry
from .register.data_type import Data
# Import the exporters to ensure they register
from .register import export_csv, export_json, export_pdf

def export_data(data: Data, format: str):
    exporter_cls = ExporterRegistry.get_exporter(format)
    exporter = exporter_cls()
    exporter.export_data(data)

if __name__ == "__main__":
    same_data = Data({"name": "Dingo", "age": 30})

    print("Available formats:", ExporterRegistry.available_formats())

    export_data(same_data, "csv")
    export_data(same_data, "json")
    export_data(same_data, "pdf")