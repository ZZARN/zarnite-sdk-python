# BehaviorDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Deleted behavior identifier | 
**org_id** | **str** | Organization | 
**deleted** | **bool** | Deletion result | [optional] [default to True]

## Example

```python
from zarnite.models.behavior_delete_response import BehaviorDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BehaviorDeleteResponse from a JSON string
behavior_delete_response_instance = BehaviorDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(BehaviorDeleteResponse.to_json())

# convert the object into a dict
behavior_delete_response_dict = behavior_delete_response_instance.to_dict()
# create an instance of BehaviorDeleteResponse from a dict
behavior_delete_response_from_dict = BehaviorDeleteResponse.from_dict(behavior_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


