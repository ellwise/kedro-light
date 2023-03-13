from kedro.framework.session import KedroSession
from kedro.io import DataCatalog
from kedro.pipeline import Pipeline
from kedro.pipeline.node import Node
from kedro.runner import ParallelRunner, SequentialRunner, ThreadRunner


def data_catalog(project_path: str, conf_source: str) -> DataCatalog:
    """
    Create a data catalog for reading and writing datasets given a project path and a relative
    configuration path
    """
    with KedroSession(
        session_id=None, project_path=project_path, conf_source=conf_source
    ) as session:
        context = session.load_context()
    return context.catalog


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
    func = runner.run_only_missing if only_missing else runner.run
    func(pipeline, catalog)


def run_node(
    node: Node,
    catalog: DataCatalog,
    is_async=False,
):
    """Run a node using the datasets within a given data catalog"""
    runner = SequentialRunner()
    runner.run_node(node, catalog, is_async=is_async)
