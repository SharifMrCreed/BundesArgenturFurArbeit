import time
from deutschland import weiterbildungssuche
from pprint import pprint
from deutschland.weiterbildungssuche.api import default_api
from deutschland.weiterbildungssuche.model.response import Response

# Set the host and authentication parameters
configuration = weiterbildungssuche.Configuration(
    host="https://rest.arbeitsagentur.de/infosysbub/wbsuche"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Create an instance of the API client
with weiterbildungssuche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # Set the parameters for the search query
    page = 1
    size = 50
    sys = "C"
    sw = "Teilqualifikation"
    ssw = "Teilquali"
    orte = "Erlangen_11.005_49.595"
    uk = "Bundesweit"
    re = "BAY"
    bt = 0
    uz = 1
    dauer = 0
    uf = 101
    ban = 22210
    it = "RC"
    bg = True

    try:
        # Search for continuing education offers
        api_response = api_instance.weiterbildungssuche(page=page, size=size, sys=sys, sw=sw, ssw=ssw, orte=orte, uk=uk,
                                                        re=re, bt=bt, uz=uz, dauer=dauer, uf=uf, ban=ban, it=it, bg=bg)
        pprint(api_response)
    except weiterbildungssuche.ApiException as e:
        print("Exception when calling DefaultApi->weiterbildungssuche: %s\n" % e)
