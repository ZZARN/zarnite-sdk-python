# OrgOverviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** |  | 
**active_users30d** | **int** | Users active in last 30 days | 
**total_sessions** | **int** |  | 
**active_sessions** | **int** |  | 
**total_messages** | **int** |  | 
**popular_agents** | **List[Dict[str, object]]** | Top agents by session count | 

## Example

```python
from zarnite.models.org_overview_response import OrgOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrgOverviewResponse from a JSON string
org_overview_response_instance = OrgOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(OrgOverviewResponse.to_json())

# convert the object into a dict
org_overview_response_dict = org_overview_response_instance.to_dict()
# create an instance of OrgOverviewResponse from a dict
org_overview_response_from_dict = OrgOverviewResponse.from_dict(org_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


