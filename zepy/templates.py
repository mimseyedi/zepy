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
        dest.mkdir(parents=True, exist_ok=True)

        for item in self.source.rglob('*'):
            if self._is_hidden_item(item):
                continue

            relative = self.render(
                item.relative_to(
                    self.source
                ).__str__()
            )
            dest_item = Path(
                dest, relative,
            )

            if item.is_dir():
                dest_item.mkdir(
                    parents=True,
                    exist_ok=True,
                )
            elif item.is_file():
                rendered_data = self.render(
                    item.read_text('utf-8')
                )
                dest_item.write_text(
                    rendered_data,
                    'utf-8',
                )

    def render(self, string: str) -> str:
        return Template(
            template=string,
        ).safe_substitute(self.tags)

    @staticmethod
    def _is_hidden_item(item: Path) -> bool:
        if item.name.startswith('.'):
            return True
        for parent in item.parents:
            if parent.name.startswith('.'):
                return True
        return False

    def __repr__(self) -> str:
        return (
            f"ProjectTemplate("
            f"{self.source},"
            f"{self.tags})"
        )

    def __str__(self) -> str:
        return f"ProjectTemplate({self.source})"