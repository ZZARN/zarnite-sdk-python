# OrgRagSessionLimitUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether org-level monthly RAG session limits are enforced | 
**monthly_session_limit** | **int** | Maximum distinct RAG sessions (thread_id) allowed per month when enabled | [optional] 
**monthly_user_session_limit** | **int** | Maximum distinct RAG sessions per user per month when enabled | [optional] 
**monthly_user_time_limit_minutes** | **int** | Maximum cumulative RAG active time per user per month, in minutes, when enabled | [optional] 

## Example

```python
from zarnite.models.org_rag_session_limit_update_request import OrgRagSessionLimitUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrgRagSessionLimitUpdateRequest from a JSON string
org_rag_session_limit_update_request_instance = OrgRagSessionLimitUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(OrgRagSessionLimitUpdateRequest.to_json())

# convert the object into a dict
org_rag_session_limit_update_request_dict = org_rag_session_limit_update_request_instance.to_dict()
# create an instance of OrgRagSessionLimitUpdateRequest from a dict
org_rag_session_limit_update_request_from_dict = OrgRagSessionLimitUpdateRequest.from_dict(org_rag_session_limit_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


