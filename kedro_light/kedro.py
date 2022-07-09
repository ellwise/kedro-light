from kedro.framework.project import settings
from kedro.framework.session import KedroSession
from kedro.io import DataCatalog
from kedro.pipeline import Pipeline
from kedro.runner import SequentialRunner


def io(project_path: str, conf_source: str) -> DataCatalog:
    settings.CONF_SOURCE = conf_source  # this must be before Kedro.load_context
    with KedroSession(session_id=None, project_path=project_path) as session:
        context = session.load_context()
    return context.catalog


def run(pipeline: Pipeline, io: DataCatalog):
    runner = SequentialRunner()
    runner.run(pipeline, io)
