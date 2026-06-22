import json
from pathlib import Path
from typing import Dict

from pandas import DataFrame
from plotly.express import scatter
from plotly.express.data import iris
from plotly.graph_objects import Figure
from sklearn.decomposition import PCA

import kedro_light as kl

my_project = Path(__file__).parents[1]
catalog = kl.data_catalog(
    project_path=my_project,
    conf_source="data",
)


def transform(iris: DataFrame) -> DataFrame:
    features = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    target = "species"
    data = PCA(n_components=2).fit_transform(iris[features])
    pca = DataFrame(data=data, columns=["pc1", "pc2"])
    pca[target] = iris[target]
    return pca


def plot(pca: DataFrame) -> Figure:
    return scatter(
        data_frame=pca,
        x="pc1",
        y="pc2",
        color="species",
    )


def serialize(figure: Figure) -> Dict:
    return json.loads(figure.to_json())


dag = [
    kl.node(func=iris, inputs=None, outputs="iris"),
    kl.node(func=transform, inputs="iris", outputs="_transformed"),
    kl.node(func=plot, inputs="_transformed", outputs="_figure"),
    kl.node(func=serialize, inputs="_figure", outputs="pca"),
    kl.node(func=Figure.show, inputs="_figure", outputs=None),
]

pipeline = kl.pipeline(dag)
kl.run(
    pipeline,
    catalog,
    parallel=False,
    threaded=False,
    only_missing=False,
)

pipelines = {"__default__": pipeline}
kl.show(pipelines, catalog)
