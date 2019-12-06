# openapi_client.JiraProductConfigurationsApi

All URIs are relative to *http://localhost:8080/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jira_product_configurations_create**](JiraProductConfigurationsApi.md#jira_product_configurations_create) | **POST** /jira_product_configurations/ | 
[**jira_product_configurations_delete**](JiraProductConfigurationsApi.md#jira_product_configurations_delete) | **DELETE** /jira_product_configurations/{id}/ | 
[**jira_product_configurations_list**](JiraProductConfigurationsApi.md#jira_product_configurations_list) | **GET** /jira_product_configurations/ | 
[**jira_product_configurations_partial_update**](JiraProductConfigurationsApi.md#jira_product_configurations_partial_update) | **PATCH** /jira_product_configurations/{id}/ | 
[**jira_product_configurations_read**](JiraProductConfigurationsApi.md#jira_product_configurations_read) | **GET** /jira_product_configurations/{id}/ | 
[**jira_product_configurations_update**](JiraProductConfigurationsApi.md#jira_product_configurations_update) | **PUT** /jira_product_configurations/{id}/ | 


# **jira_product_configurations_create**
> JIRA jira_product_configurations_create(data)



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
api_instance = openapi_client.JiraProductConfigurationsApi(openapi_client.ApiClient(configuration))
data = openapi_client.JIRA() # JIRA | 

try:
    api_response = api_instance.jira_product_configurations_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JiraProductConfigurationsApi->jira_product_configurations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**JIRA**](JIRA.md)|  | 

### Return type

[**JIRA**](JIRA.md)

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

# **jira_product_configurations_delete**
> jira_product_configurations_delete(id)



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
api_instance = openapi_client.JiraProductConfigurationsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this jir a_p key.

try:
    api_instance.jira_product_configurations_delete(id)
except ApiException as e:
    print("Exception when calling JiraProductConfigurationsApi->jira_product_configurations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_p key. | 

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

# **jira_product_configurations_list**
> InlineResponse2007 jira_product_configurations_list(id=id, conf=conf, product=product, component=component, project_key=project_key, push_all_issues=push_all_issues, enable_engagement_epic_mapping=enable_engagement_epic_mapping, push_notes=push_notes, limit=limit, offset=offset)



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
api_instance = openapi_client.JiraProductConfigurationsApi(openapi_client.ApiClient(configuration))
id = 3.4 # float |  (optional)
conf = 'conf_example' # str |  (optional)
product = 'product_example' # str |  (optional)
component = 'component_example' # str |  (optional)
project_key = 'project_key_example' # str |  (optional)
push_all_issues = 'push_all_issues_example' # str |  (optional)
enable_engagement_epic_mapping = 'enable_engagement_epic_mapping_example' # str |  (optional)
push_notes = 'push_notes_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.jira_product_configurations_list(id=id, conf=conf, product=product, component=component, project_key=project_key, push_all_issues=push_all_issues, enable_engagement_epic_mapping=enable_engagement_epic_mapping, push_notes=push_notes, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JiraProductConfigurationsApi->jira_product_configurations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **float**|  | [optional] 
 **conf** | **str**|  | [optional] 
 **product** | **str**|  | [optional] 
 **component** | **str**|  | [optional] 
 **project_key** | **str**|  | [optional] 
 **push_all_issues** | **str**|  | [optional] 
 **enable_engagement_epic_mapping** | **str**|  | [optional] 
 **push_notes** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

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

# **jira_product_configurations_partial_update**
> JIRA jira_product_configurations_partial_update(id, data)



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
api_instance = openapi_client.JiraProductConfigurationsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this jir a_p key.
data = openapi_client.JIRA() # JIRA | 

try:
    api_response = api_instance.jira_product_configurations_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JiraProductConfigurationsApi->jira_product_configurations_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_p key. | 
 **data** | [**JIRA**](JIRA.md)|  | 

### Return type

[**JIRA**](JIRA.md)

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

# **jira_product_configurations_read**
> JIRA jira_product_configurations_read(id)



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
api_instance = openapi_client.JiraProductConfigurationsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this jir a_p key.

try:
    api_response = api_instance.jira_product_configurations_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JiraProductConfigurationsApi->jira_product_configurations_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_p key. | 

### Return type

[**JIRA**](JIRA.md)

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

# **jira_product_configurations_update**
> JIRA jira_product_configurations_update(id, data)



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
api_instance = openapi_client.JiraProductConfigurationsApi(openapi_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this jir a_p key.
data = openapi_client.JIRA() # JIRA | 

try:
    api_response = api_instance.jira_product_configurations_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JiraProductConfigurationsApi->jira_product_configurations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this jir a_p key. | 
 **data** | [**JIRA**](JIRA.md)|  | 

### Return type

[**JIRA**](JIRA.md)

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

