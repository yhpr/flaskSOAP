from suds.client import Client


url = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'

client = Client(url)


# r = client.service.FullCountryInfo("US")
r = client.service.FullCountryInfoAllCountries()

print(r)
