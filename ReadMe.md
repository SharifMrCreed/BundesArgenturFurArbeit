# Continuing Education Search

Search one of the largest continuing education databases in Germany.

Authentication is done via OAuth 2 Client Credentials with JWTs. The following client credentials can be used:

**ClientID:** 38053956-6618-4953-b670-b4ae7a2360b1

**ClientSecret:** c385073c-3b97-42a9-b916-08fd8a5d1795.

**Attention**: the generated token must be included in the header as 'OAuthAccessToken' for the following GET requests.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 0.1.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/AndreasFischer1985/weiterbildungssuche-api](https://github.com/AndreasFischer1985/weiterbildungssuche-api)

## Requirements

Python >= 3.6

## Installation & Usage

### pip install

```sh
pip install deutschland[weiterbildungssuche]
```

### poetry install

```sh
poetry add deutschland -E weiterbildungssuche
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

## Usage

Import the package:

```python

from deutschland import weiterbildungssuche
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import time
from deutschland import weiterbildungssuche
from pprint import pprint
from deutschland.weiterbildungssuche.api import default_api
from deutschland.weiterbildungssuche.model.response import Response
# Defining the host is optional and defaults to https://rest.arbeitsagentur.de/infosysbub/wbsuche
# See configuration.py for a list of all supported configuration parameters.
configuration = weiterbildungssuche.Configuration(
    host = "https://rest.arbeitsagentur.de/infosysbub/wbsuche"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: clientCredAuth
configuration = weiterbildungssuche.Configuration(
    host = "https://rest.arbeitsagentur.de/infosysbub/wbsuche"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


# Enter a context with an instance of the API client
with weiterbildungssuche.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    page = 1 # int | Results page (optional)
    size = 50 # int | Number of results per page (maximum 2000). A total of 10,000 results are displayed across all pages. (optional)
    sys = "C" # str | Systematic - C=Professional Qualification, D=Advanced Training, CD=Systematic search. (optional)
    sw = "Partial qualification" # str | Search word (optional)
    ssw = "Partial quali" # str | selectedStarSearchWords (incomplete search words, e.g., Partial quali; potentially multiple, separated by commas). (optional)
    orte = "Erlangen_11.005_49.595" # str | Location and coordinates (longitude and latitude) separated by underscores. (optional)
    uk = "Nationwide" # str | Radius - Nationwide=Nationwide, 25=25 km, 50=50 km, 100=100 km, 150=150 km, 200=200 km. (optional)
    re = "BAY" # str | BAW=Baden-Württemberg, BAY=Bavaria, BER=Berlin, BRA=Brandenburg, BRE=Bremen, HAM=Hamburg, HES=Hessen, MBV=Mecklenburg-Western Pomerania, NDS=Lower Saxony, NRW=North Rhine-Westphalia, RPF=Rhineland-Palatinate, SAA=Saarland, SAC=Saxony, SAN=Saxony-Anhalt, SLH=Schleswig-Holstein, TH%C3%9C=Thuringia, -=overregional, iGB=Great Britain, iP=Portugal, iCH=Switzerland, iA=Austria, iE=Spain. Multiple comma-separated values possible (e.g., re=TH%C3%9C,BAW). (optional)
    bt = 0 # int | Start date - 0=regular start, 1=this month, 2=next month, 3=in two months, 4=in three months, 5=in more than three months (optional)
    uz = 1 # int | Lesson time - 1=Full-time, 2=Part-time. Multiple comma-separated values possible. (optional)
    dauer = 0 # int | Duration - 0=On request, 1,2=up to
```

## Documentation for API Endpoints

All URIs are relative to *https://rest.arbeitsagentur.de/infosysbub/wbsuche*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**weiterbildungssuche**](docs/DefaultApi.md#weiterbildungssuche) | **GET** /pc/v1/bildungsangebot | Weiterbildungssuche

## Documentation For Models

- [Response](docs/Response.md)
- [ResponseAggregations](docs/ResponseAggregations.md)
- [ResponseAggregationsANZAHLAUSGEFILTERT](docs/ResponseAggregationsANZAHLAUSGEFILTERT.md)
- [ResponseAggregationsANZAHLGESAMT](docs/ResponseAggregationsANZAHLGESAMT.md)
- [ResponseAggregationsLERNFORMEN](docs/ResponseAggregationsLERNFORMEN.md)
- [ResponseAggregationsREGIONEN](docs/ResponseAggregationsREGIONEN.md)
- [ResponseAggregationsUNTERRICHSTZEIT](docs/ResponseAggregationsUNTERRICHSTZEIT.md)
- [ResponseEmbedded](docs/ResponseEmbedded.md)
- [ResponseEmbeddedTermineInner](docs/ResponseEmbeddedTermineInner.md)
- [ResponseEmbeddedTermineInnerAdresse](docs/ResponseEmbeddedTermineInnerAdresse.md)
- [ResponseEmbeddedTermineInnerAdresseKoordinaten](docs/ResponseEmbeddedTermineInnerAdresseKoordinaten.md)
- [ResponseEmbeddedTermineInnerAdresseOrtStraE](docs/ResponseEmbeddedTermineInnerAdresseOrtStraE.md)
- [ResponseEmbeddedTermineInnerAdresseOrtStraELand](docs/ResponseEmbeddedTermineInnerAdresseOrtStraELand.md)
- [ResponseEmbeddedTermineInnerAngebot](docs/ResponseEmbeddedTermineInnerAngebot.md)
- [ResponseEmbeddedTermineInnerAnsprechpartnerInner](docs/ResponseEmbeddedTermineInnerAnsprechpartnerInner.md)
- [ResponseEmbeddedTermineInnerAnsprechpartnerInnerRollen](docs/ResponseEmbeddedTermineInnerAnsprechpartnerInnerRollen.md)
- [ResponseEmbeddedTermineInnerDauer](docs/ResponseEmbeddedTermineInnerDauer.md)
- [ResponseEmbeddedTermineInnerUnterrichtsform](docs/ResponseEmbeddedTermineInnerUnterrichtsform.md)
- [ResponseEmbeddedTermineInnerUnterrichtszeit](docs/ResponseEmbeddedTermineInnerUnterrichtszeit.md)
- [ResponseLinks](docs/ResponseLinks.md)
- [ResponseLinksFirst](docs/ResponseLinksFirst.md)
- [ResponseLinksLast](docs/ResponseLinksLast.md)
- [ResponseLinksNext](docs/ResponseLinksNext.md)
- [ResponsePage](docs/ResponsePage.md)

## Documentation For Authorization

## clientCredAuth

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**:
- **Scopes**: N/A

## Author

andreasfischer1985@web.de

## Notes for Large OpenAPI documents

If the OpenAPI document is large, imports in weiterbildungssuche.apis and weiterbildungssuche.models may fail with a RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:

- `from deutschland.weiterbildungssuche.api.default_api import DefaultApi`
- `from deutschland.weiterbildungssuche.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:

```python

import sys
sys.setrecursionlimit(1500)
from deutschland import weiterbildungssuche
from deutschland.weiterbildungssuche.apis import *
from deutschland.weiterbildungssuche.models import *
```