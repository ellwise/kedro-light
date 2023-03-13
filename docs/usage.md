# Usage

## An example project

=== "File system"

    ```
    iris_analysis
    ├── data
    │   ├── base/catalog.yaml
    │   └── local/.gitkeep
    └── eda/01_analysis.py
    ```

=== "catalog.yaml"

    ```yaml
    iris:
        type: pandas.CSVDataSet
        filepath: data/iris.csv

    pca:
        type: yaml.YAMLDataSet
        filepath: data/pca.yaml
    ```

=== "01_analysis.py"

    ```py title="01_analysis.py" linenums="1"
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
    ```

Kedro Light is intended to be useful regardless of how you want to lay out your project.
As a simple example, consider the project depicted on the tabs above.
Note that Kedro expects you to have both a base and overriding set of configuration files, with the former in a folder named "base" and the latter in a folder that, by default, is expected to be named "local".

## Creating a data catalog

```py linenums="13"
my_project = Path(__file__).parents[1]
catalog = kl.data_catalog(
    project_path=my_project,
    conf_source="data",
)
```

To create a Kedro `DataCatalog` object, you just need to provide a path to your project folder, along with an indication of where your Kedro configuration files will be kept.
You might find it convenient to identify your project folder using the `__file__` property of a file within your project.

## Transforming data

```py linenums="20"
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
```

Kedro `Node` objects are created using the standard Kedro `node` function, which has been re-exported by Kedro Light for convenience.
For example, let's assume you want to load the famous [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris) into your data folder, undertake principal component analysis on it, and plot the results.
To do so, you should define or identify functions representing these transformations, and apply them to named datasets, as shown above.
Dataset names beginning with an underscore above are ones which will remain in memory, rather than being written to disk, hence they do not appear in your data catalog.
The inputs and outputs of your nodes should collectively form a directed, acyclic graph (DAG).

## Creating/running a pipeline

```py linenums="50"
pipeline = kl.pipeline(dag)
kl.run(
    pipeline,
    catalog,
    parallel=False,
    threaded=False,
    only_missing=False,
)
```

Kedro `Pipeline` objects can be created by passing your DAG of nodes into Kedro's `pipeline` function, which has also been re-exported by Kedro Light for convenience.
To actually use that pipeline, Kedro Light includes a `run` function.
This takes some optional keyword arguments that specify the Kedro runner that is used (`SequentialRunner` by default, otherwise `ParallelRunner` or `ThreadRunner`), and the run method that is called (either `run` or `run_only_missing`).

## Visualising a pipeline

```py linenums="59"
pipelines = {"__default__": pipeline}
kl.show(pipelines, catalog)
```

Kedro Light also provides a function for serving a local web-app via Kedro-Viz.
This function side-steps Kedro-Viz's usual approach of identifying pipelines based on a typical Kedro project structure, and instead lets you pass in pipelines in as Python objects explicitly.
The web-app will be served from `http://localhost:4141/`.
