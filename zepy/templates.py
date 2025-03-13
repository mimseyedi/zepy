from pathlib import Path
from string import Template

from .errors import ProjectTemplateError


class ProjectTemplate:
    def __init__(self, template: str, **tags) -> None:
        self._template = self._get_template(template)
        self._tags = tags

    @property
    def template(self) -> Path:
        return self._template

    @property
    def tags(self) -> dict:
        return self._tags

    @property
    def name(self) -> str:
        return self._template.name

    def build(self, dest: Path) -> None:
        dest.mkdir(parents=True, exist_ok=True)

        for item in self.template.rglob('*'):
            if self._is_hidden_item(item):
                continue

            relative = self.render(
                item.relative_to(
                    self.template
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

    def _get_template(self, template: str) -> Path:
        if (
            t_path := Path(
                Path(__file__).parent,
                "templates",
                template,
            )
        ).is_dir():
            return self._template_validation(t_path)
        else:
            if (
                t_path := Path(template)
            ).is_dir():
                return self._template_validation(t_path)
            raise ProjectTemplateError(
                "Error: No template was found in this path."
            )

    @staticmethod
    def _template_validation(template_path: Path) -> Path:
        if not Path(
            template_path,
            "settings.yaml",
        ).is_file():
            raise ProjectTemplateError(
                "Error: Template is corrupted.\n"
                "\t- The 'settings.yaml' file was not found."
            )
        return template_path

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
            f"{self.template},"
            f"{self.tags})"
        )

    def __str__(self) -> str:
        return f"ProjectTemplate({self.template})"