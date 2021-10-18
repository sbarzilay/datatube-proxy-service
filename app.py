import json
import logging
import os
import sys
import time

from flask import Flask, request
from opencensus.ext.azure.log_exporter import AzureLogHandler

from kusto import Kusto
print('init python')
app = Flask(__name__)

client = Kusto()

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

application_insights_key = os.getenv('APPINSIGHTS_INSTRUMENTATIONKEY')
logger.addHandler(AzureLogHandler(
	connection_string=f'InstrumentationKey={application_insights_key}')
)
logger.info('init logger')

@app.route('/', methods=['GET'])
def hello():
	return f'Hello World!'


@app.route('/query', methods=['POST'])
def query():
	body = request.json
	database = body.get("database")
	query = body.get("query")
	query_start_time = time.perf_counter()
	results = client.query(
		database=database,
		query=query
	)
	logger.info(f'query finished in {time.perf_counter() - query_start_time}')
	before_dumps_time = time.perf_counter()
	result = json.dumps(results)
	logger.info(f'dumps finished in {time.perf_counter() - before_dumps_time}')
	return result, 200, {'Content-Type': 'application/json'}


if __name__ == '__main__':
	app.run(host='localhost', port=8086, threaded=True)
