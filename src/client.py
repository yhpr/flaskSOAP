from suds.client import Client
from ..app import flag_name



client = Client(url)

result = client.service.(flag_name)

r = client.service.FullCountryInfo(result)

print(r)
