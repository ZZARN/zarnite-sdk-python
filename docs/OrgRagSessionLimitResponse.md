# OrgRagSessionLimitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Organization scope | 
**enabled** | **bool** | Whether monthly session limit is enabled | 
**monthly_session_limit** | **int** | Configured monthly session cap | [optional] 
**monthly_user_session_limit** | **int** | Configured monthly per-user session cap | [optional] 
**monthly_user_time_limit_minutes** | **int** | Configured monthly per-user RAG time cap in minutes | [optional] 
**month** | **str** | UTC month window in YYYY-MM format | 
**used_sessions** | **int** | Distinct sessions already used this month | 
**remaining_sessions** | **int** | Remaining sessions for this month (null when disabled/unbounded) | [optional] 
**user_id** | **str** | Queried user scope when provided | [optional] 
**used_user_sessions** | **int** | Distinct sessions used by queried user this month | [optional] 
**remaining_user_sessions** | **int** | Remaining sessions for queried user this month | [optional] 
**used_user_time_minutes** | **float** | Used RAG time by queried user this month in minutes | [optional] 
**remaining_user_time_minutes** | **float** | Remaining RAG time by queried user this month in minutes | [optional] 

## Example

```python
from zarnite.models.org_rag_session_limit_response import OrgRagSessionLimitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrgRagSessionLimitResponse from a JSON string
org_rag_session_limit_response_instance = OrgRagSessionLimitResponse.from_json(json)
# print the JSON string representation of the object
print(OrgRagSessionLimitResponse.to_json())

# convert the object into a dict
org_rag_session_limit_response_dict = org_rag_session_limit_response_instance.to_dict()
# create an instance of OrgRagSessionLimitResponse from a dict
org_rag_session_limit_response_from_dict = OrgRagSessionLimitResponse.from_dict(org_rag_session_limit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


