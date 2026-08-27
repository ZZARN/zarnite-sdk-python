# EnvelopePlaygroundEndResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaygroundEndResponse**](PlaygroundEndResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_playground_end_response import EnvelopePlaygroundEndResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopePlaygroundEndResponse from a JSON string
envelope_playground_end_response_instance = EnvelopePlaygroundEndResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopePlaygroundEndResponse.to_json())

# convert the object into a dict
envelope_playground_end_response_dict = envelope_playground_end_response_instance.to_dict()
# create an instance of EnvelopePlaygroundEndResponse from a dict
envelope_playground_end_response_from_dict = EnvelopePlaygroundEndResponse.from_dict(envelope_playground_end_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


