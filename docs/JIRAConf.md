# JIRAConf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**configuration_name** | **str** | Enter a name to give to this configuration | [optional] 
**url** | **str** | For configuring Jira, view: https://defectdojo.readthedocs.io/en/latest/features.html#jira-integration | 
**username** | **str** |  | 
**password** | **str** |  | 
**default_issue_type** | **str** |  | [optional] 
**epic_name_id** | **int** | To obtain the &#39;Epic name id&#39; visit https://&lt;YOUR JIRA URL&gt;/rest/api/2/field and search for Epic Name. Copy the number out of cf[number] and paste it here. | 
**open_status_key** | **int** | To obtain the &#39;open status key&#39; visit https://&lt;YOUR JIRA URL&gt;/rest/api/latest/issue/&lt;ANY VALID ISSUE KEY&gt;/transitions?expand&#x3D;transitions.fields | 
**close_status_key** | **int** | To obtain the &#39;open status key&#39; visit https://&lt;YOUR JIRA URL&gt;/rest/api/latest/issue/&lt;ANY VALID ISSUE KEY&gt;/transitions?expand&#x3D;transitions.fields | 
**info_mapping_severity** | **str** | Maps to the &#39;Priority&#39; field in Jira. For example: Info | 
**low_mapping_severity** | **str** | Maps to the &#39;Priority&#39; field in Jira. For example: Low | 
**medium_mapping_severity** | **str** | Maps to the &#39;Priority&#39; field in Jira. For example: Medium | 
**high_mapping_severity** | **str** | Maps to the &#39;Priority&#39; field in Jira. For example: High | 
**critical_mapping_severity** | **str** | Maps to the &#39;Priority&#39; field in Jira. For example: Critical | 
**finding_text** | **str** | Additional text that will be added to the finding in Jira. For example including how the finding was created or who to contact for more information. | [optional] 
**accepted_mapping_resolution** | **str** | JIRA resolution names (comma-separated values) that maps to an Accepted Finding | [optional] 
**false_positive_mapping_resolution** | **str** | JIRA resolution names (comma-separated values) that maps to a False Positive Finding | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


