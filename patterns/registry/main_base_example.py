import json
from typing import Any, Callable  # For type hints: Any = any type, Callable = function type
from functools import wraps       # To preserve function metadata when wrapping functions

class Data: data_dict: dict[str, Any]
ExportFn = Callable[[Data], None]

# --- Registry dictionary ---
# This dictionary will hold all registered exporters, keyed by format name
# e.g., { "pdf": export_pdf_function, "json": export_json_function, ... }
exporters: dict[str, ExportFn] = {}

# --- Decorator factory ---
def register_exporter(format: str) -> Callable[[ExportFn], ExportFn]:
    """
    A decorator factory that registers a function as an exporter for a given format.
    Example:
        @register_exporter("pdf")
        def export_pdf(...): ...
    """
    def decorator(fn: ExportFn) -> ExportFn:
        # wraps() preserves the original function’s name, docstring, etc.
        @wraps(fn)
        def wrapper(data: Data) -> None:
            # The wrapper just calls the original function
            return fn(data)

        # Register the wrapped function in the global exporters dictionary
        exporters[format] = wrapper

        # Return the wrapped function so it can still be called normally
        return wrapper

    # Return the actual decorator
    return decorator

@register_exporter('pdf')
def export_pdf(data: Data) -> None:
    print(f"Exporting data to PDF: {data}")

@register_exporter('json')
def export_json(data: Data) -> None:
    print(f"Exporting data to JSON: {json.dumps(data, indent=2)}")

@register_exporter('csv')
def export_csv(data: Data) -> None:
    print(f"Exporting data to CSV: {data}")

# --- Function that calls the correct exporter ---
def export_data(data: Data, format: str) -> None:
    """
    Looks up the exporter for the requested format and calls it.
    """
    exporter = exporters.get(format)
    if not exporter:
        raise ValueError(f"No exporter registered for format: {format}")
    exporter(data)



if __name__ == '__main__':
    same_data = {"name": "Dingo", "age": 30}

    # Call each registered exporter
    export_data(same_data, "pdf")
    export_data(same_data, "json")
    export_data(same_data, "csv")