# kedro-light

This package provides a minimal interface to [Kedro](https://github.com/quantumblacklabs/kedro). It is intended for when you want to use Kedro's data catalog and pipelines (to help separate data and logic), but don't want to embrace the full Kedro project structure and workflow. It defines/re-exports the following functions:
* `io` - Creates a `DataCatalog` (for loading/saving named datasets) and configures logging
* `node` - Creates a `Node` (these collectively define a DAG of data transformations on named datasets)
* `run` - Creates a `Pipeline` based on a given DAG, then runs it using a `SequentialRunner`

You can use kedro-light as follows:
```
import kedro_light as kl

io = kl.io(conf_paths=..., catalog=...)
dag = [
    kl.node(func=..., inputs=..., outputs=...),
    ...
]
kl.run(dag, io)
```
