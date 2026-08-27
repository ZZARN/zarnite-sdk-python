# UserSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** |  | 
**agent_id** | **str** |  | 
**user_id** | **str** |  | 
**messages** | **Dict[str, object]** | Message counts (total, user, assistant) | 
**first_activity** | **str** | ISO timestamp of first activity | [optional] 
**last_activity** | **str** | ISO timestamp of last activity | [optional] 
**sessions** | **Dict[str, object]** | Session stats (total, active, avg_duration_s, last_session) | 
**most_active_hours** | **List[object]** | Top 5 most active hours | 

## Example

```python
from zarnite.models.user_summary_response import UserSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserSummaryResponse from a JSON string
user_summary_response_instance = UserSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(UserSummaryResponse.to_json())

# convert the object into a dict
user_summary_response_dict = user_summary_response_instance.to_dict()
# create an instance of UserSummaryResponse from a dict
user_summary_response_from_dict = UserSummaryResponse.from_dict(user_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


