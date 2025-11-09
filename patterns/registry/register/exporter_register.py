from abc import ABC
from typing import Dict, Type
from .base_exporter import BaseExport

class ExporterRegistry(ABC):
    _exporters: Dict[str, Type[BaseExport]] = {}

    @classmethod
    def register(cls, format_name: str):
        def decorator(exporter_cls: Type[BaseExport]) -> Type[BaseExport]:
            cls._exporters[format_name] = exporter_cls
            return exporter_cls
        return decorator

    @classmethod
    def get_exporter(cls, format: str) -> Type[BaseExport]:
        if format not in cls._exporters:
            raise ValueError(f"No exporter registered for format: {format}")
        return cls._exporters[format]

    @classmethod
    def available_formats(cls) -> list[str]:
        return list(cls._exporters.keys())