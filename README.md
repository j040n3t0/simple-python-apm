# simple-python-apm
Example of Python Script to test APM with Elastic using Flask.

### Create a virtual env
```python -m venv .venv```

### Activate de virtual env
```source .venv/bin/activate```

### Instal dependecies
```pip install "elastic-apm[flask]"```

### Configure the variables 
```sh
app.config['ELASTIC_APM'] = {
  'SERVICE_NAME': 'my-service-name', #Service Name - The name will be show in the Kibana APM
  'SECRET_TOKEN': 'XPTO', # You can see this token in the APM Integration
  'SERVER_URL': 'http://endpoint.elastic.co:8200', # Elasticsearch Enpoint
  'ENVIRONMENT': 'development' # Development / Homologation / Production
}
```

### Run the application
```python app.py```

### Access you browser
```http://localhost:5000```

### Check de APM section in you Kibana