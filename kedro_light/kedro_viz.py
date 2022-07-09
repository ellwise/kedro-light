from typing import Dict

import uvicorn
from kedro.io import DataCatalog
from kedro.pipeline import Pipeline
from kedro_viz.api import apps
from kedro_viz.data_access import data_access_manager
from kedro_viz.server import populate_data


def show(pipelines: Dict[str, Pipeline], io: DataCatalog):

    populate_data(data_access_manager, io, pipelines, None)
    app = apps.create_api_app_from_project(None)
    host, port = "localhost", 4141
    print(f"Kedro-Viz is running on http://{host}:{port}/")
    uvicorn.run(app, host=host, port=port, log_config=None)
