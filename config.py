from os import environ


class Config:
	APPINSIGHTS_KEY = environ.get('APPINSIGHTS_INSTRUMENTATIONKEY')
	MONGODB_URI = environ.get('MONGODB_URI')
	KUSTO_CLUSTER = 'https://datatubestgeastus2.eastus2.kusto.windows.net/'
	AZURE_TENANT_ID = environ.get('AZURE_TENANT_ID')
	AZURE_CLIENT_ID = environ.get('AZURE_CLIENT_ID')
	AZURE_SECRET_KEY = environ.get('AZURE_SECRET_KEY')
