#from azure.kusto.data import KustoConnectionStringBuilder, ClientRequestProperties
from azure.kusto.data.response import KustoResponseDataSet

from config import Config
from skusto import KustoClient, KustoConnectionStringBuilder, ClientRequestProperties

class Kusto:

	def __init__(self):
		print(Config.AZURE_CLIENT_ID)
		print(Config.AZURE_SECRET_KEY)
		print(Config.AZURE_TENANT_ID)
		kcsb = KustoConnectionStringBuilder.with_aad_application_key_authentication(
			connection_string=Config.KUSTO_CLUSTER,
			aad_app_id=Config.AZURE_CLIENT_ID,
			app_key=Config.AZURE_SECRET_KEY,
			authority_id=Config.AZURE_TENANT_ID
		)
		self._client = KustoClient(kcsb)
		self._properties = ClientRequestProperties()
		self._properties.set_option('results_progressive_enabled', True)
		self._properties.set_option('request_description', 'telegram42069blazeitfagit')

	def query(self, database: str, query: str):
		return self._client.execute(
			database=database,
			query=query,
			properties=self._properties,
		)
