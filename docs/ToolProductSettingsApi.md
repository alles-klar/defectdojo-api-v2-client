# openapi_client.ToolProductSettingsApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tool_product_settings_create**](ToolProductSettingsApi.md#tool_product_settings_create) | **POST** /tool_product_settings/ | 
[**tool_product_settings_delete**](ToolProductSettingsApi.md#tool_product_settings_delete) | **DELETE** /tool_product_settings/{id}/ | 
[**tool_product_settings_list**](ToolProductSettingsApi.md#tool_product_settings_list) | **GET** /tool_product_settings/ | 
[**tool_product_settings_partial_update**](ToolProductSettingsApi.md#tool_product_settings_partial_update) | **PATCH** /tool_product_settings/{id}/ | 
[**tool_product_settings_read**](ToolProductSettingsApi.md#tool_product_settings_read) | **GET** /tool_product_settings/{id}/ | 
[**tool_product_settings_update**](ToolProductSettingsApi.md#tool_product_settings_update) | **PUT** /tool_product_settings/{id}/ | 


# **tool_product_settings_create**
> ToolProductSettings tool_product_settings_create(data)



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
api_instance = openapi_client.ToolProductSettingsApi(openapi_client.ApiClient(configuration))
data = openapi_client.ToolProductSettings() # ToolProductSettings | 

try:
    api_response = api_instance.tool_product_settings_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolProductSettingsApi->tool_product_settings_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ToolProductSettings**](ToolProductSettings.md)|  | 

### Return type

[**ToolProductSettings**](ToolProductSettings.md)

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

# **tool_product_settings_delete**
> tool_product_settings_delete(id)



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
api_instance = openapi_client.ToolProductSettingsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tool_ product_ settings.

try:
    api_instance.tool_product_settings_delete(id)
except ApiException as e:
    print("Exception when calling ToolProductSettingsApi->tool_product_settings_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tool_ product_ settings. | 

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

# **tool_product_settings_list**
> InlineResponse20018 tool_product_settings_list(id=id, name=name, product=product, tool_configuration=tool_configuration, tool_project_id=tool_project_id, url=url, limit=limit, offset=offset)



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
api_instance = openapi_client.ToolProductSettingsApi(openapi_client.ApiClient(configuration))
id = 3.4 # float |  (optional)
name = 'name_example' # str |  (optional)
product = 'product_example' # str |  (optional)
tool_configuration = 'tool_configuration_example' # str |  (optional)
tool_project_id = 'tool_project_id_example' # str |  (optional)
url = 'url_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.tool_product_settings_list(id=id, name=name, product=product, tool_configuration=tool_configuration, tool_project_id=tool_project_id, url=url, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolProductSettingsApi->tool_product_settings_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **name** | **str**|  | [optional] 
 **product** | **str**|  | [optional] 
 **tool_configuration** | **str**|  | [optional] 
 **tool_project_id** | **str**|  | [optional] 
 **url** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20018**](InlineResponse20018.md)

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

# **tool_product_settings_partial_update**
> ToolProductSettings tool_product_settings_partial_update(id, data)



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
api_instance = openapi_client.ToolProductSettingsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tool_ product_ settings.
data = openapi_client.ToolProductSettings() # ToolProductSettings | 

try:
    api_response = api_instance.tool_product_settings_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolProductSettingsApi->tool_product_settings_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tool_ product_ settings. | 
 **data** | [**ToolProductSettings**](ToolProductSettings.md)|  | 

### Return type

[**ToolProductSettings**](ToolProductSettings.md)

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

# **tool_product_settings_read**
> ToolProductSettings tool_product_settings_read(id)



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
api_instance = openapi_client.ToolProductSettingsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tool_ product_ settings.

try:
    api_response = api_instance.tool_product_settings_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolProductSettingsApi->tool_product_settings_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tool_ product_ settings. | 

### Return type

[**ToolProductSettings**](ToolProductSettings.md)

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

# **tool_product_settings_update**
> ToolProductSettings tool_product_settings_update(id, data)



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
api_instance = openapi_client.ToolProductSettingsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tool_ product_ settings.
data = openapi_client.ToolProductSettings() # ToolProductSettings | 

try:
    api_response = api_instance.tool_product_settings_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolProductSettingsApi->tool_product_settings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tool_ product_ settings. | 
 **data** | [**ToolProductSettings**](ToolProductSettings.md)|  | 

### Return type

[**ToolProductSettings**](ToolProductSettings.md)

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

