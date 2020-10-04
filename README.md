# data-engineering
Some challenge exercises

## Requirements

* Python = 3.7
* Postgres >= 10.0
* everything in Conda environment.yml file

## Installation 

Install Miniconda, then:
~~~
conda env update
conda activate data_eng_env
~~~

## DB Preparation

### Running existing migrations

* Create postgres database called `data_eng_dev` for development or `data_eng_live` for production.
* With an activated conda environment run:
~~~
export CONFIG_TYPE=dev
FLASK_APP=run.py flask db upgrade
~~~
Use "dev" for development server and "live" for production server.

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

## Running the flask app
~~~
export FLASK_APP=run.py
flask run
~~~

## Using API
Open api/document.py the doc strings will be very helpful.

## Using the REST service with cURL utility
### Storing a document
~~~
curl http://localhost:5000/documents -X POST -H "Content-Type: application/json" -d '{"text":<contents of the document>}
~~~


### Retrieving a document
~~~
curl http://localhost:5000/documents/<document_id>
~~~

### Retrieving a summary
~~~
curl http://localhost:5000/summary/<document_id>
~~~

### Deleting a document
~~~
curl http://localhost:5000/documents/<document_id> -X DELETE
~~~

### Code standards

Use Python Black formatting:
~~~
black --check --line-length 120 .
~~~

## Unit testing

* With an activated conda environment run:
~~~
export CONFIG_TYPE=dev
python -m pytest unit_tests/ -vs
~~~
