# sandbox

Simple Sample Proeject for [dagster-dbt](https://docs.dagster.io/integrations/libraries/dbt/transform-dbt).


This is a [Dagster](https://dagster.io/) project scaffolded with [`dagster project scaffold`](https://docs.dagster.io/guides/build/projects/creating-a-new-project).

## Getting started

Install subumodules ([dbt_sample_project_with_duckdb](https://github.com/toukoudo/dbt_sample_project_with_duckdb)).

```bash
git submodule update --init
```

Install packages.
```bash
pip install -e ".[dev]"
```

Then, start the Dagster UI web server:

```bash
dagster dev
```
