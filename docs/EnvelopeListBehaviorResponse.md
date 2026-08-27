# EnvelopeListBehaviorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BehaviorResponse]**](BehaviorResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_list_behavior_response import EnvelopeListBehaviorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeListBehaviorResponse from a JSON string
envelope_list_behavior_response_instance = EnvelopeListBehaviorResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeListBehaviorResponse.to_json())

# convert the object into a dict
envelope_list_behavior_response_dict = envelope_list_behavior_response_instance.to_dict()
# create an instance of EnvelopeListBehaviorResponse from a dict
envelope_list_behavior_response_from_dict = EnvelopeListBehaviorResponse.from_dict(envelope_list_behavior_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


