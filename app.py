from flask import Flask
import logging

# Or use ELASTIC_APM in your application's settings
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)

app.config['ELASTIC_APM'] = {
  'SERVICE_NAME': 'my-service-name',
  'SECRET_TOKEN': 'XPTO',
  'SERVER_URL': 'http://endpoint.elastic.co:8200',
  'ENVIRONMENT': 'development'
}

apm = ElasticAPM(app, logging=logging.ERROR)

@app.route('/')
def index():
    return "Hello World!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)