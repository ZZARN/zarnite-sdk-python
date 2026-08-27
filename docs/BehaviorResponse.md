# BehaviorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Behavior identifier | 
**org_id** | **str** | Owning organization | 
**name** | **str** | Behavior name | 
**description** | **str** | Behavior description | [optional] 
**system_prompt** | **str** | Core instruction prompt | [optional] 
**tone** | **str** | Tone setting | [optional] 
**strictness** | **str** | Strictness setting | [optional] 
**language** | **str** | Language | [optional] 
**languages** | **List[str]** | Preferred language list | [optional] [default to []]
**guardrails** | **Dict[str, object]** | Structured guardrail rules | [optional] 
**voice** | **str** | Voice setting | [optional] 
**is_default** | **bool** | Whether this is the org default | [optional] [default to False]
**created_at** | **datetime** | Creation timestamp | 
**updated_at** | **datetime** | Last update timestamp | 

## Example

```python
from zarnite.models.behavior_response import BehaviorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BehaviorResponse from a JSON string
behavior_response_instance = BehaviorResponse.from_json(json)
# print the JSON string representation of the object
print(BehaviorResponse.to_json())

# convert the object into a dict
behavior_response_dict = behavior_response_instance.to_dict()
# create an instance of BehaviorResponse from a dict
behavior_response_from_dict = BehaviorResponse.from_dict(behavior_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


