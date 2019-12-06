# openapi_client.ToolConfigurationsApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tool_configurations_create**](ToolConfigurationsApi.md#tool_configurations_create) | **POST** /tool_configurations/ | 
[**tool_configurations_delete**](ToolConfigurationsApi.md#tool_configurations_delete) | **DELETE** /tool_configurations/{id}/ | 
[**tool_configurations_list**](ToolConfigurationsApi.md#tool_configurations_list) | **GET** /tool_configurations/ | 
[**tool_configurations_partial_update**](ToolConfigurationsApi.md#tool_configurations_partial_update) | **PATCH** /tool_configurations/{id}/ | 
[**tool_configurations_read**](ToolConfigurationsApi.md#tool_configurations_read) | **GET** /tool_configurations/{id}/ | 
[**tool_configurations_update**](ToolConfigurationsApi.md#tool_configurations_update) | **PUT** /tool_configurations/{id}/ | 


# **tool_configurations_create**
> ToolConfiguration tool_configurations_create(data)



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
api_instance = openapi_client.ToolConfigurationsApi(openapi_client.ApiClient(configuration))
data = openapi_client.ToolConfiguration() # ToolConfiguration | 

try:
    api_response = api_instance.tool_configurations_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolConfigurationsApi->tool_configurations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ToolConfiguration**](ToolConfiguration.md)|  | 

### Return type

[**ToolConfiguration**](ToolConfiguration.md)

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

# **tool_configurations_delete**
> tool_configurations_delete(id)



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
api_instance = openapi_client.ToolConfigurationsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tool_ configuration.

try:
    api_instance.tool_configurations_delete(id)
except ApiException as e:
    print("Exception when calling ToolConfigurationsApi->tool_configurations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tool_ configuration. | 

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

# **tool_configurations_list**
> InlineResponse20017 tool_configurations_list(id=id, name=name, tool_type=tool_type, url=url, authentication_type=authentication_type, limit=limit, offset=offset)



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
api_instance = openapi_client.ToolConfigurationsApi(openapi_client.ApiClient(configuration))
id = 3.4 # float |  (optional)
name = 'name_example' # str |  (optional)
tool_type = 'tool_type_example' # str |  (optional)
url = 'url_example' # str |  (optional)
authentication_type = 'authentication_type_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.tool_configurations_list(id=id, name=name, tool_type=tool_type, url=url, authentication_type=authentication_type, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolConfigurationsApi->tool_configurations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **name** | **str**|  | [optional] 
 **tool_type** | **str**|  | [optional] 
 **url** | **str**|  | [optional] 
 **authentication_type** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

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

# **tool_configurations_partial_update**
> ToolConfiguration tool_configurations_partial_update(id, data)



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
api_instance = openapi_client.ToolConfigurationsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tool_ configuration.
data = openapi_client.ToolConfiguration() # ToolConfiguration | 

try:
    api_response = api_instance.tool_configurations_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolConfigurationsApi->tool_configurations_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tool_ configuration. | 
 **data** | [**ToolConfiguration**](ToolConfiguration.md)|  | 

### Return type

[**ToolConfiguration**](ToolConfiguration.md)

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

# **tool_configurations_read**
> ToolConfiguration tool_configurations_read(id)



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
api_instance = openapi_client.ToolConfigurationsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tool_ configuration.

try:
    api_response = api_instance.tool_configurations_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolConfigurationsApi->tool_configurations_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tool_ configuration. | 

### Return type

[**ToolConfiguration**](ToolConfiguration.md)

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

# **tool_configurations_update**
> ToolConfiguration tool_configurations_update(id, data)



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
api_instance = openapi_client.ToolConfigurationsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tool_ configuration.
data = openapi_client.ToolConfiguration() # ToolConfiguration | 

try:
    api_response = api_instance.tool_configurations_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ToolConfigurationsApi->tool_configurations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tool_ configuration. | 
 **data** | [**ToolConfiguration**](ToolConfiguration.md)|  | 

### Return type

[**ToolConfiguration**](ToolConfiguration.md)

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

