Kedro Light provides a minimal interface to [Kedro](https://github.com/kedro-org/kedro) and [Kedro-Viz](https://github.com/kedro-org/kedro-viz).
It is intended for when you want to use Kedro's data catalog system and pipeline objects (to separate data from logic), as well as its visualisation capabilities, but don't want to embrace the full Kedro project structure and workflow.
Kedro Light defines/re-exports the following functions:

* `data_catalog` creates a `DataCatalog` (for loading/saving named datasets)
* `node` creates a `Node` (for transforming named datasets)
* `pipeline` creates a `Pipeline` using Kedro's modular pipeline constructor (this defines a DAG of data transformations)
* `run` and `run_node` run a pipeline or node respectively
* `show` serves a web app that displays a collection of pipelines

A condensed usage example is given below.
Further details can be found [here](usage.md).

```py linenums="1"
import kedro_light as kl

catalog = kl.data_catalog(project_path=..., conf_source=...)

node = kl.node(func=..., inputs=..., outputs=...)
dag = [node, ...]

pipeline = kl.pipeline(dag)
kl.run(pipeline, catalog)

pipelines = {"__default__": pipeline, ...}
kl.show(pipelines, catalog)
```
