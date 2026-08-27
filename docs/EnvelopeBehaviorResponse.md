# EnvelopeBehaviorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BehaviorResponse**](BehaviorResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_behavior_response import EnvelopeBehaviorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeBehaviorResponse from a JSON string
envelope_behavior_response_instance = EnvelopeBehaviorResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeBehaviorResponse.to_json())

# convert the object into a dict
envelope_behavior_response_dict = envelope_behavior_response_instance.to_dict()
# create an instance of EnvelopeBehaviorResponse from a dict
envelope_behavior_response_from_dict = EnvelopeBehaviorResponse.from_dict(envelope_behavior_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


