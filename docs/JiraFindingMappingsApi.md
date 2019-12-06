# openapi_client.JiraFindingMappingsApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jira_finding_mappings_create**](JiraFindingMappingsApi.md#jira_finding_mappings_create) | **POST** /jira_finding_mappings/ | 
[**jira_finding_mappings_delete**](JiraFindingMappingsApi.md#jira_finding_mappings_delete) | **DELETE** /jira_finding_mappings/{id}/ | 
[**jira_finding_mappings_list**](JiraFindingMappingsApi.md#jira_finding_mappings_list) | **GET** /jira_finding_mappings/ | 
[**jira_finding_mappings_partial_update**](JiraFindingMappingsApi.md#jira_finding_mappings_partial_update) | **PATCH** /jira_finding_mappings/{id}/ | 
[**jira_finding_mappings_read**](JiraFindingMappingsApi.md#jira_finding_mappings_read) | **GET** /jira_finding_mappings/{id}/ | 
[**jira_finding_mappings_update**](JiraFindingMappingsApi.md#jira_finding_mappings_update) | **PUT** /jira_finding_mappings/{id}/ | 


# **jira_finding_mappings_create**
> JIRAIssue jira_finding_mappings_create(data)



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
api_instance = openapi_client.JiraFindingMappingsApi(openapi_client.ApiClient(configuration))
data = openapi_client.JIRAIssue() # JIRAIssue | 

try:
    api_response = api_instance.jira_finding_mappings_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JiraFindingMappingsApi->jira_finding_mappings_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**JIRAIssue**](JIRAIssue.md)|  | 

### Return type

[**JIRAIssue**](JIRAIssue.md)

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

# **jira_finding_mappings_delete**
> jira_finding_mappings_delete(id)



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
api_instance = openapi_client.JiraFindingMappingsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this jir a_ issue.

try:
    api_instance.jira_finding_mappings_delete(id)
except ApiException as e:
    print("Exception when calling JiraFindingMappingsApi->jira_finding_mappings_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ issue. | 

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

# **jira_finding_mappings_list**
> InlineResponse2006 jira_finding_mappings_list(id=id, jira_id=jira_id, jira_key=jira_key, limit=limit, offset=offset)



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
api_instance = openapi_client.JiraFindingMappingsApi(openapi_client.ApiClient(configuration))
id = 3.4 # float |  (optional)
jira_id = 'jira_id_example' # str |  (optional)
jira_key = 'jira_key_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.jira_finding_mappings_list(id=id, jira_id=jira_id, jira_key=jira_key, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JiraFindingMappingsApi->jira_finding_mappings_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **jira_id** | **str**|  | [optional] 
 **jira_key** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

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

# **jira_finding_mappings_partial_update**
> JIRAIssue jira_finding_mappings_partial_update(id, data)



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
api_instance = openapi_client.JiraFindingMappingsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this jir a_ issue.
data = openapi_client.JIRAIssue() # JIRAIssue | 

try:
    api_response = api_instance.jira_finding_mappings_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JiraFindingMappingsApi->jira_finding_mappings_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ issue. | 
 **data** | [**JIRAIssue**](JIRAIssue.md)|  | 

### Return type

[**JIRAIssue**](JIRAIssue.md)

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

# **jira_finding_mappings_read**
> JIRAIssue jira_finding_mappings_read(id)



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
api_instance = openapi_client.JiraFindingMappingsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this jir a_ issue.

try:
    api_response = api_instance.jira_finding_mappings_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JiraFindingMappingsApi->jira_finding_mappings_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ issue. | 

### Return type

[**JIRAIssue**](JIRAIssue.md)

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

# **jira_finding_mappings_update**
> JIRAIssue jira_finding_mappings_update(id, data)



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
api_instance = openapi_client.JiraFindingMappingsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this jir a_ issue.
data = openapi_client.JIRAIssue() # JIRAIssue | 

try:
    api_response = api_instance.jira_finding_mappings_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JiraFindingMappingsApi->jira_finding_mappings_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_ issue. | 
 **data** | [**JIRAIssue**](JIRAIssue.md)|  | 

### Return type

[**JIRAIssue**](JIRAIssue.md)

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

