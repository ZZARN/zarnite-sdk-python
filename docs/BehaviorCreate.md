# BehaviorCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Organization scope | 
**name** | **str** | Human-readable behavior name | 
**description** | **str** | Behavior description | [optional] 
**system_prompt** | **str** | Core instruction prompt | [optional] 
**tone** | **str** | e.g. friendly, professional | [optional] 
**strictness** | **str** | e.g. high, medium, low | [optional] 
**language** | **str** | e.g. English, Spanish | [optional] 
**languages** | **List[str]** | Preferred language list | [optional] 
**guardrails** | [**GuardrailsConfig**](GuardrailsConfig.md) | Structured guardrail rules | [optional] 
**voice** | **str** | Voice setting for TTS | [optional] 
**is_default** | **bool** | Whether this is the org default behavior | [optional] [default to False]

## Example

```python
from zarnite.models.behavior_create import BehaviorCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BehaviorCreate from a JSON string
behavior_create_instance = BehaviorCreate.from_json(json)
# print the JSON string representation of the object
print(BehaviorCreate.to_json())

# convert the object into a dict
behavior_create_dict = behavior_create_instance.to_dict()
# create an instance of BehaviorCreate from a dict
behavior_create_from_dict = BehaviorCreate.from_dict(behavior_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


