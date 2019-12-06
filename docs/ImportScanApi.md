# openapi_client.ImportScanApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_scan_create**](ImportScanApi.md#import_scan_create) | **POST** /import-scan/ | 


# **import_scan_create**
> ImportScan import_scan_create(scan_type, engagement, scan_date=scan_date, minimum_severity=minimum_severity, active=active, verified=verified, test_type=test_type, file=file, lead=lead, tags=tags, close_old_findings=close_old_findings)



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
api_instance = openapi_client.ImportScanApi(openapi_client.ApiClient(configuration))
scan_type = 'scan_type_example' # str | 
engagement = 56 # int | 
scan_date = '2013-10-20' # date |  (optional)
minimum_severity = 'Info' # str |  (optional) (default to 'Info')
active = True # bool |  (optional) (default to True)
verified = True # bool |  (optional) (default to True)
test_type = 'test_type_example' # str |  (optional)
file = '/path/to/file' # file |  (optional)
lead = 56 # int |  (optional)
tags = 'tags_example' # list[str] |  (optional)
close_old_findings = False # bool |  (optional) (default to False)

try:
    api_response = api_instance.import_scan_create(scan_type, engagement, scan_date=scan_date, minimum_severity=minimum_severity, active=active, verified=verified, test_type=test_type, file=file, lead=lead, tags=tags, close_old_findings=close_old_findings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImportScanApi->import_scan_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scan_type** | **str**|  | 
 **engagement** | **int**|  | 
 **scan_date** | **date**|  | [optional] 
 **minimum_severity** | **str**|  | [optional] [default to &#39;Info&#39;]
 **active** | **bool**|  | [optional] [default to True]
 **verified** | **bool**|  | [optional] [default to True]
 **test_type** | **str**|  | [optional] 
 **file** | **file**|  | [optional] 
 **lead** | **int**|  | [optional] 
 **tags** | [**list[str]**](str.md)|  | [optional] 
 **close_old_findings** | **bool**|  | [optional] [default to False]

### Return type

[**ImportScan**](ImportScan.md)

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

