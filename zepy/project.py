from __future__ import annotations

from typing import (
    Any,
    Dict,
    Optional,
)
from ruamel.yaml import (
    YAML,
    YAMLError,
)
from pathlib import Path

from .errors import ProjectSettingsError


class ProjectSettings:
    def __init__(self, settings_file: Path) -> None:
        self._settings_file = settings_file

    @property
    def settings_file(self) -> Path:
        return self._settings_file

    def get(self, name: str) -> Any:
        settings = self.load()
        return settings.get(name, None)

    def load(self) -> Dict:
        try:
            settings = YAML().load(
                self._settings_file.read_text()
            )
        except YAMLError:
            raise ProjectSettingsError(
                "The settings file is corrupt and unreadable"
            )
        else:
            return settings

    def __repr__(self) -> str:
        return f"ProjectSettings({self.settings_file})"


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
        python_interpreter: Optional[str] = None,
        license_: Optional[str] = None,
        user: Optional[str] = None,
    ) -> Project:
        ...

    @classmethod
    def open(cls, root: Path) -> Project:
        ...