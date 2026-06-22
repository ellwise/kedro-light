from pathlib import Path

from kedro.config import OmegaConfigLoader
from kedro.io import DataCatalog
from kedro.pipeline import Pipeline
from kedro.runner import ParallelRunner, SequentialRunner, ThreadRunner


def data_catalog(project_path: str, conf_source: str) -> DataCatalog:
    """
    Create a data catalog for reading and writing datasets given a project path and a relative
    configuration path
    """
    config_loader = OmegaConfigLoader(str(Path(project_path) / conf_source))
    return DataCatalog.from_config(
        catalog=config_loader.get("catalog"),
        credentials=config_loader.get("credentials"),
    )


def run(
    pipeline: Pipeline,
    catalog: DataCatalog,
    parallel=False,
    threaded=False,
    only_missing=False,
):
    """Run a pipeline using the datasets within a given data catalog"""
    if parallel and threaded:
        raise ValueError("Can only choose one of `parallel` and `threaded`")
    runner = ParallelRunner() if parallel else ThreadRunner() if threaded else SequentialRunner()
    runner.run(pipeline, catalog, only_missing_outputs=only_missing)
