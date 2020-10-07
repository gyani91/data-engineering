# data-engineering

## Setup
### Requirements

* Python = 3.7
* Postgres >= 10.0
* everything in Conda environment.yml file

### Installation 

Install Miniconda, then:
~~~
conda env update
conda activate data_eng_env
~~~

### DB Preparation

Running existing migrations

* Create postgres database called `data_eng_dev` for development or `data_eng_live` for production.
* With an activated conda environment run:
~~~
export CONFIG_TYPE=dev
FLASK_APP=run.py flask db upgrade
~~~
Use "dev" for development server and "live" for production server.

## Using the repo
### Store data into db and run queries

~~~
python driver_scripts/main_load_transaction_table_run_sqls.py
~~~

### Query results as CSVs

~~~
data/query_results/
~~~

## Further Details

### Creating a new migration
~~~
FLASK_APP=run.py flask db migrate -m "Description of migration"
~~~
Replace the "Description of migration" with an appropriate description.

To view the history and current version
~~~
FLASK_APP=run.py flask db history
FLASK_APP=run.py flask db current
~~~

### Code standards

Use Python Black formatting:
~~~
black --check --line-length 120 .
~~~
