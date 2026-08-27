# EnvelopeBehaviorDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BehaviorDeleteResponse**](BehaviorDeleteResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_behavior_delete_response import EnvelopeBehaviorDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeBehaviorDeleteResponse from a JSON string
envelope_behavior_delete_response_instance = EnvelopeBehaviorDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeBehaviorDeleteResponse.to_json())

# convert the object into a dict
envelope_behavior_delete_response_dict = envelope_behavior_delete_response_instance.to_dict()
# create an instance of EnvelopeBehaviorDeleteResponse from a dict
envelope_behavior_delete_response_from_dict = EnvelopeBehaviorDeleteResponse.from_dict(envelope_behavior_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


