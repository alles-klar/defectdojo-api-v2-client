# openapi_client.TestTypesApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**test_types_create**](TestTypesApi.md#test_types_create) | **POST** /test_types/ | 
[**test_types_list**](TestTypesApi.md#test_types_list) | **GET** /test_types/ | 
[**test_types_partial_update**](TestTypesApi.md#test_types_partial_update) | **PATCH** /test_types/{id}/ | 
[**test_types_read**](TestTypesApi.md#test_types_read) | **GET** /test_types/{id}/ | 
[**test_types_update**](TestTypesApi.md#test_types_update) | **PUT** /test_types/{id}/ | 


# **test_types_create**
> TestType test_types_create(data)



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
api_instance = openapi_client.TestTypesApi(openapi_client.ApiClient(configuration))
data = openapi_client.TestType() # TestType | 

try:
    api_response = api_instance.test_types_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestTypesApi->test_types_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TestType**](TestType.md)|  | 

### Return type

[**TestType**](TestType.md)

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

# **test_types_list**
> InlineResponse20015 test_types_list(limit=limit, offset=offset)



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
api_instance = openapi_client.TestTypesApi(openapi_client.ApiClient(configuration))
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.test_types_list(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestTypesApi->test_types_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

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

# **test_types_partial_update**
> TestType test_types_partial_update(id, data)



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
api_instance = openapi_client.TestTypesApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this test_ type.
data = openapi_client.TestType() # TestType | 

try:
    api_response = api_instance.test_types_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestTypesApi->test_types_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test_ type. | 
 **data** | [**TestType**](TestType.md)|  | 

### Return type

[**TestType**](TestType.md)

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

# **test_types_read**
> TestType test_types_read(id)



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
api_instance = openapi_client.TestTypesApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this test_ type.

try:
    api_response = api_instance.test_types_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestTypesApi->test_types_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test_ type. | 

### Return type

[**TestType**](TestType.md)

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

# **test_types_update**
> TestType test_types_update(id, data)



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
api_instance = openapi_client.TestTypesApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this test_ type.
data = openapi_client.TestType() # TestType | 

try:
    api_response = api_instance.test_types_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestTypesApi->test_types_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this test_ type. | 
 **data** | [**TestType**](TestType.md)|  | 

### Return type

[**TestType**](TestType.md)

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

