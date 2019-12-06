# openapi_client.ScanSettingsApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scan_settings_create**](ScanSettingsApi.md#scan_settings_create) | **POST** /scan_settings/ | 
[**scan_settings_delete**](ScanSettingsApi.md#scan_settings_delete) | **DELETE** /scan_settings/{id}/ | 
[**scan_settings_list**](ScanSettingsApi.md#scan_settings_list) | **GET** /scan_settings/ | 
[**scan_settings_partial_update**](ScanSettingsApi.md#scan_settings_partial_update) | **PATCH** /scan_settings/{id}/ | 
[**scan_settings_read**](ScanSettingsApi.md#scan_settings_read) | **GET** /scan_settings/{id}/ | 
[**scan_settings_update**](ScanSettingsApi.md#scan_settings_update) | **PUT** /scan_settings/{id}/ | 


# **scan_settings_create**
> ScanSettingsCreate scan_settings_create(data)



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
api_instance = openapi_client.ScanSettingsApi(openapi_client.ApiClient(configuration))
data = openapi_client.ScanSettingsCreate() # ScanSettingsCreate | 

try:
    api_response = api_instance.scan_settings_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanSettingsApi->scan_settings_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ScanSettingsCreate**](ScanSettingsCreate.md)|  | 

### Return type

[**ScanSettingsCreate**](ScanSettingsCreate.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_settings_delete**
> scan_settings_delete(id)



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
api_instance = openapi_client.ScanSettingsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this scan settings.

try:
    api_instance.scan_settings_delete(id)
except ApiException as e:
    print("Exception when calling ScanSettingsApi->scan_settings_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this scan settings. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_settings_list**
> InlineResponse20012 scan_settings_list(limit=limit, offset=offset)



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
api_instance = openapi_client.ScanSettingsApi(openapi_client.ApiClient(configuration))
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.scan_settings_list(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanSettingsApi->scan_settings_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_settings_partial_update**
> ScanSettings scan_settings_partial_update(id, data)



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
api_instance = openapi_client.ScanSettingsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this scan settings.
data = openapi_client.ScanSettings() # ScanSettings | 

try:
    api_response = api_instance.scan_settings_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanSettingsApi->scan_settings_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this scan settings. | 
 **data** | [**ScanSettings**](ScanSettings.md)|  | 

### Return type

[**ScanSettings**](ScanSettings.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_settings_read**
> ScanSettings scan_settings_read(id)



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
api_instance = openapi_client.ScanSettingsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this scan settings.

try:
    api_response = api_instance.scan_settings_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanSettingsApi->scan_settings_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this scan settings. | 

### Return type

[**ScanSettings**](ScanSettings.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scan_settings_update**
> ScanSettings scan_settings_update(id, data)



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
api_instance = openapi_client.ScanSettingsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this scan settings.
data = openapi_client.ScanSettings() # ScanSettings | 

try:
    api_response = api_instance.scan_settings_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScanSettingsApi->scan_settings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this scan settings. | 
 **data** | [**ScanSettings**](ScanSettings.md)|  | 

### Return type

[**ScanSettings**](ScanSettings.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

