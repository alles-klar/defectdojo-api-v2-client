# openapi_client.DevelopmentEnvironmentsApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**development_environments_create**](DevelopmentEnvironmentsApi.md#development_environments_create) | **POST** /development_environments/ | 
[**development_environments_list**](DevelopmentEnvironmentsApi.md#development_environments_list) | **GET** /development_environments/ | 
[**development_environments_partial_update**](DevelopmentEnvironmentsApi.md#development_environments_partial_update) | **PATCH** /development_environments/{id}/ | 
[**development_environments_read**](DevelopmentEnvironmentsApi.md#development_environments_read) | **GET** /development_environments/{id}/ | 
[**development_environments_update**](DevelopmentEnvironmentsApi.md#development_environments_update) | **PUT** /development_environments/{id}/ | 


# **development_environments_create**
> DevelopmentEnvironment development_environments_create(data)



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
api_instance = openapi_client.DevelopmentEnvironmentsApi(openapi_client.ApiClient(configuration))
data = openapi_client.DevelopmentEnvironment() # DevelopmentEnvironment | 

try:
    api_response = api_instance.development_environments_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopmentEnvironmentsApi->development_environments_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**DevelopmentEnvironment**](DevelopmentEnvironment.md)|  | 

### Return type

[**DevelopmentEnvironment**](DevelopmentEnvironment.md)

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

# **development_environments_list**
> InlineResponse200 development_environments_list(limit=limit, offset=offset)



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
api_instance = openapi_client.DevelopmentEnvironmentsApi(openapi_client.ApiClient(configuration))
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.development_environments_list(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopmentEnvironmentsApi->development_environments_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

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

# **development_environments_partial_update**
> DevelopmentEnvironment development_environments_partial_update(id, data)



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
api_instance = openapi_client.DevelopmentEnvironmentsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this development_ environment.
data = openapi_client.DevelopmentEnvironment() # DevelopmentEnvironment | 

try:
    api_response = api_instance.development_environments_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopmentEnvironmentsApi->development_environments_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this development_ environment. | 
 **data** | [**DevelopmentEnvironment**](DevelopmentEnvironment.md)|  | 

### Return type

[**DevelopmentEnvironment**](DevelopmentEnvironment.md)

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

# **development_environments_read**
> DevelopmentEnvironment development_environments_read(id)



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
api_instance = openapi_client.DevelopmentEnvironmentsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this development_ environment.

try:
    api_response = api_instance.development_environments_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopmentEnvironmentsApi->development_environments_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this development_ environment. | 

### Return type

[**DevelopmentEnvironment**](DevelopmentEnvironment.md)

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

# **development_environments_update**
> DevelopmentEnvironment development_environments_update(id, data)



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
api_instance = openapi_client.DevelopmentEnvironmentsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this development_ environment.
data = openapi_client.DevelopmentEnvironment() # DevelopmentEnvironment | 

try:
    api_response = api_instance.development_environments_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevelopmentEnvironmentsApi->development_environments_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this development_ environment. | 
 **data** | [**DevelopmentEnvironment**](DevelopmentEnvironment.md)|  | 

### Return type

[**DevelopmentEnvironment**](DevelopmentEnvironment.md)

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

