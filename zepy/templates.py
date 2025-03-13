from pathlib import Path
from string import Template


class ProjectTemplate:
    def __init__(self, source: Path, **tags) -> None:
        self._source = source
        self._tags = tags

    @property
    def source(self) -> Path:
        return self._source

    @property
    def tags(self) -> dict:
        return self._tags

    @property
    def name(self) -> str:
        return self._source.name

    def build(self, dest: Path) -> None:
        ...

    def render(self, string: str) -> str:
        ...

    @staticmethod
    def _is_hidden_item(item: Path) -> bool:
        ...

    def __repr__(self) -> str:
        ...

    def __str__(self) -> str:
        ...