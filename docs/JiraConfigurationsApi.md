# openapi_client.JiraConfigurationsApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jira_configurations_create**](JiraConfigurationsApi.md#jira_configurations_create) | **POST** /jira_configurations/ | 
[**jira_configurations_delete**](JiraConfigurationsApi.md#jira_configurations_delete) | **DELETE** /jira_configurations/{id}/ | 
[**jira_configurations_list**](JiraConfigurationsApi.md#jira_configurations_list) | **GET** /jira_configurations/ | 
[**jira_configurations_partial_update**](JiraConfigurationsApi.md#jira_configurations_partial_update) | **PATCH** /jira_configurations/{id}/ | 
[**jira_configurations_read**](JiraConfigurationsApi.md#jira_configurations_read) | **GET** /jira_configurations/{id}/ | 
[**jira_configurations_update**](JiraConfigurationsApi.md#jira_configurations_update) | **PUT** /jira_configurations/{id}/ | 


# **jira_configurations_create**
> JIRAConf jira_configurations_create(data)



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
api_instance = openapi_client.JiraConfigurationsApi(openapi_client.ApiClient(configuration))
data = openapi_client.JIRAConf() # JIRAConf | 

try:
    api_response = api_instance.jira_configurations_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JiraConfigurationsApi->jira_configurations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**JIRAConf**](JIRAConf.md)|  | 

### Return type

[**JIRAConf**](JIRAConf.md)

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

# **jira_configurations_delete**
> jira_configurations_delete(id)



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
api_instance = openapi_client.JiraConfigurationsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this jir a_ conf.

try:
    api_instance.jira_configurations_delete(id)
except ApiException as e:
    print("Exception when calling JiraConfigurationsApi->jira_configurations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ conf. | 

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

# **jira_configurations_list**
> InlineResponse2005 jira_configurations_list(id=id, url=url, limit=limit, offset=offset)



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
api_instance = openapi_client.JiraConfigurationsApi(openapi_client.ApiClient(configuration))
id = 3.4 # float |  (optional)
url = 'url_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.jira_configurations_list(id=id, url=url, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JiraConfigurationsApi->jira_configurations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **url** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

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

# **jira_configurations_partial_update**
> JIRAConf jira_configurations_partial_update(id, data)



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
api_instance = openapi_client.JiraConfigurationsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this jir a_ conf.
data = openapi_client.JIRAConf() # JIRAConf | 

try:
    api_response = api_instance.jira_configurations_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JiraConfigurationsApi->jira_configurations_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ conf. | 
 **data** | [**JIRAConf**](JIRAConf.md)|  | 

### Return type

[**JIRAConf**](JIRAConf.md)

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

# **jira_configurations_read**
> JIRAConf jira_configurations_read(id)



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
api_instance = openapi_client.JiraConfigurationsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this jir a_ conf.

try:
    api_response = api_instance.jira_configurations_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JiraConfigurationsApi->jira_configurations_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ conf. | 

### Return type

[**JIRAConf**](JIRAConf.md)

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

# **jira_configurations_update**
> JIRAConf jira_configurations_update(id, data)



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
api_instance = openapi_client.JiraConfigurationsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this jir a_ conf.
data = openapi_client.JIRAConf() # JIRAConf | 

try:
    api_response = api_instance.jira_configurations_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JiraConfigurationsApi->jira_configurations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ conf. | 
 **data** | [**JIRAConf**](JIRAConf.md)|  | 

### Return type

[**JIRAConf**](JIRAConf.md)

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

