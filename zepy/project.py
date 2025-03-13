from __future__ import annotations

from typing import (
    Any,
    Dict,
)
from pathlib import Path


class ProjectSettings:
    def __init__(self, settings_file: Path) -> None:
        self._settings_file = settings_file

    def get(self, name: str) -> Any:
        ...

    def load(self) -> Dict:
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...