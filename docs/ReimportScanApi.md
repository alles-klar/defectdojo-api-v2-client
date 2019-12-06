# openapi_client.ReimportScanApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reimport_scan_create**](ReimportScanApi.md#reimport_scan_create) | **POST** /reimport-scan/ | 


# **reimport_scan_create**
> ReImportScan reimport_scan_create(scan_date, scan_type, test, minimum_severity=minimum_severity, active=active, verified=verified, tags=tags, file=file)



### Example

* Api Key Authentication (api_key):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
configuration = openapi_client.Configuration()
# Configure API key authorization: api_key
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost:8080/api/v2
configuration.host = "http://localhost:8080/api/v2"
# Create an instance of the API class
api_instance = openapi_client.ReimportScanApi(openapi_client.ApiClient(configuration))
scan_date = '2013-10-20' # date | 
scan_type = 'scan_type_example' # str | 
test = 56 # int | 
minimum_severity = 'Info' # str |  (optional) (default to 'Info')
active = True # bool |  (optional) (default to True)
verified = True # bool |  (optional) (default to True)
tags = 'tags_example' # list[str] |  (optional)
file = '/path/to/file' # file |  (optional)

try:
    api_response = api_instance.reimport_scan_create(scan_date, scan_type, test, minimum_severity=minimum_severity, active=active, verified=verified, tags=tags, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReimportScanApi->reimport_scan_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_date** | **date**|  | 
 **scan_type** | **str**|  | 
 **test** | **int**|  | 
 **minimum_severity** | **str**|  | [optional] [default to &#39;Info&#39;]
 **active** | **bool**|  | [optional] [default to True]
 **verified** | **bool**|  | [optional] [default to True]
 **tags** | [**list[str]**](str.md)|  | [optional] 
 **file** | **file**|  | [optional] 

### Return type

[**ReImportScan**](ReImportScan.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

