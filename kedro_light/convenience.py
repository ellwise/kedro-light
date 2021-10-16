import logging.config as lc
from typing import List

from kedro.config import ConfigLoader
from kedro.io import DataCatalog
from kedro.runner import SequentialRunner
from kedro.pipeline import Pipeline
from kedro.pipeline.node import Node


def io(
    conf_paths=["conf/base", "conf/local"],
    catalog="catalog.yml",
    credentials=None,
    parameters=None,
    logging=None,
) -> DataCatalog:

    conf_loader = ConfigLoader(conf_paths)
    conf_catalog = conf_loader.get(catalog)
    conf_credentials = conf_loader.get(credentials) if credentials else None
    io = DataCatalog.from_config(conf_catalog, credentials=conf_credentials)

    if parameters:
        conf_params = conf_loader.get(parameters)
        io.add_feed_dict({f"params:{k}": v for k, v in conf_params.items()})

    if logging:
        conf_logging = conf_loader.get(logging)
        lc.dictConfig(conf_logging)

    return io


def run(dag: List[Node], io: DataCatalog):
    pipeline = Pipeline(dag)
    runner = SequentialRunner()
    runner.run(pipeline, io)
