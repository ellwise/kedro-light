# kedro-light

This package provides a minimal interface to [Kedro](https://github.com/kedro-org/kedro) and [Kedro-Viz](https://github.com/kedro-org/kedro-viz). It is intended for when you want to use Kedro's data catalog and pipelines (to separate data from logic), as well as its visualisation capabilities, but don't want to embrace the full Kedro project structure and workflow. It defines/re-exports the following functions:
* `io` - Creates a `DataCatalog` (for loading/saving named datasets)
* `node` - Creates a `Node` (for transforming named datasets)
* `pipeline` - Creates a `Pipeline` using Kedro's `modular_pipeline` constructor (this defines a DAG of data transformations)
* `run` - Runs a pipeline using a `SequentialRunner`
* `show` - Serves a web app that displays a collection of pipelines

You can use kedro-light as follows:
```
import kedro_light as kl

io = kl.io(project_path=..., conf_source=...)

node = kl.node(func=..., inputs=..., outputs=...)
...
dag = [node, ...]
pipeline = kl.pipeline(dag)
kl.run(pipeline, io)

pipelines = {"__default__": pipeline, ...}
kl.show(pipelines, io)
```
