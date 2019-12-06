# openapi_client.ProductTypesApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_types_create**](ProductTypesApi.md#product_types_create) | **POST** /product_types/ | 
[**product_types_generate_report**](ProductTypesApi.md#product_types_generate_report) | **POST** /product_types/{id}/generate_report/ | 
[**product_types_list**](ProductTypesApi.md#product_types_list) | **GET** /product_types/ | 
[**product_types_partial_update**](ProductTypesApi.md#product_types_partial_update) | **PATCH** /product_types/{id}/ | 
[**product_types_read**](ProductTypesApi.md#product_types_read) | **GET** /product_types/{id}/ | 
[**product_types_update**](ProductTypesApi.md#product_types_update) | **PUT** /product_types/{id}/ | 


# **product_types_create**
> ProductType product_types_create(data)



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
api_instance = openapi_client.ProductTypesApi(openapi_client.ApiClient(configuration))
data = openapi_client.ProductType() # ProductType | 

try:
    api_response = api_instance.product_types_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypesApi->product_types_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ProductType**](ProductType.md)|  | 

### Return type

[**ProductType**](ProductType.md)

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

# **product_types_generate_report**
> ProductType product_types_generate_report(id, data)



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
api_instance = openapi_client.ProductTypesApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this product_ type.
data = openapi_client.ProductType() # ProductType | 

try:
    api_response = api_instance.product_types_generate_report(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypesApi->product_types_generate_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product_ type. | 
 **data** | [**ProductType**](ProductType.md)|  | 

### Return type

[**ProductType**](ProductType.md)

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

# **product_types_list**
> InlineResponse20010 product_types_list(limit=limit, offset=offset)



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
api_instance = openapi_client.ProductTypesApi(openapi_client.ApiClient(configuration))
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.product_types_list(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypesApi->product_types_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

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

# **product_types_partial_update**
> ProductType product_types_partial_update(id, data)



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
api_instance = openapi_client.ProductTypesApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this product_ type.
data = openapi_client.ProductType() # ProductType | 

try:
    api_response = api_instance.product_types_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypesApi->product_types_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product_ type. | 
 **data** | [**ProductType**](ProductType.md)|  | 

### Return type

[**ProductType**](ProductType.md)

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

# **product_types_read**
> ProductType product_types_read(id)



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
api_instance = openapi_client.ProductTypesApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this product_ type.

try:
    api_response = api_instance.product_types_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypesApi->product_types_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product_ type. | 

### Return type

[**ProductType**](ProductType.md)

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

# **product_types_update**
> ProductType product_types_update(id, data)



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
api_instance = openapi_client.ProductTypesApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this product_ type.
data = openapi_client.ProductType() # ProductType | 

try:
    api_response = api_instance.product_types_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductTypesApi->product_types_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this product_ type. | 
 **data** | [**ProductType**](ProductType.md)|  | 

### Return type

[**ProductType**](ProductType.md)

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

