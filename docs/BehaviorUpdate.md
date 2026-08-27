# BehaviorUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Updated name | [optional] 
**description** | **str** | Updated description | [optional] 
**system_prompt** | **str** | Updated system prompt | [optional] 
**tone** | **str** | Updated tone | [optional] 
**strictness** | **str** | Updated strictness | [optional] 
**language** | **str** | Updated language | [optional] 
**languages** | **List[str]** | Updated language list | [optional] 
**guardrails** | [**GuardrailsConfig**](GuardrailsConfig.md) | Updated guardrails | [optional] 
**voice** | **str** | Updated voice | [optional] 
**is_default** | **bool** | Updated default flag | [optional] 

## Example

```python
from zarnite.models.behavior_update import BehaviorUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of BehaviorUpdate from a JSON string
behavior_update_instance = BehaviorUpdate.from_json(json)
# print the JSON string representation of the object
print(BehaviorUpdate.to_json())

# convert the object into a dict
behavior_update_dict = behavior_update_instance.to_dict()
# create an instance of BehaviorUpdate from a dict
behavior_update_from_dict = BehaviorUpdate.from_dict(behavior_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


