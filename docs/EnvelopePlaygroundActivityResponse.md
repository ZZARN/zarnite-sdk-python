# EnvelopePlaygroundActivityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaygroundActivityResponse**](PlaygroundActivityResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_playground_activity_response import EnvelopePlaygroundActivityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopePlaygroundActivityResponse from a JSON string
envelope_playground_activity_response_instance = EnvelopePlaygroundActivityResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopePlaygroundActivityResponse.to_json())

# convert the object into a dict
envelope_playground_activity_response_dict = envelope_playground_activity_response_instance.to_dict()
# create an instance of EnvelopePlaygroundActivityResponse from a dict
envelope_playground_activity_response_from_dict = EnvelopePlaygroundActivityResponse.from_dict(envelope_playground_activity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


