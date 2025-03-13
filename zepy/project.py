from __future__ import annotations

from typing import (
    Any,
    Dict,
    Optional,
)
from pathlib import Path


class ProjectSettings:
    def __init__(self, settings_file: Path) -> None:
        self._settings_file = settings_file

    @property
    def settings_file(self) -> Path:
        return self._settings_file

    def get(self, name: str) -> Any:
        ...

    def load(self) -> Dict:
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...


class Project:
    def __init__(self, settings: ProjectSettings) -> None:
        self._settings = settings

    @property
    def settings(self) -> ProjectSettings:
        return self._settings

    @classmethod
    def new(
        cls,
        root: Path,
        template: Path,
        *,
        description: Optional[str] = None,
        python_version: Optional[str] = None,
        license_: Optional[str] = None,
        user: Optional[str] = None,
    ) -> Project:
        ...

    @classmethod
    def open(cls, root: Path) -> Project:
        ...