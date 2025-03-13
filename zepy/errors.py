class ZepyError(Exception):
    ...


class ProjectError(ZepyError):
    ...


class ProjectSettingsError(ProjectError):
    ...


class ProjectTemplateError(ProjectError):
    ...