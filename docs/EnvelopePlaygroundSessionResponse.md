# EnvelopePlaygroundSessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaygroundSessionResponse**](PlaygroundSessionResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_playground_session_response import EnvelopePlaygroundSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopePlaygroundSessionResponse from a JSON string
envelope_playground_session_response_instance = EnvelopePlaygroundSessionResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopePlaygroundSessionResponse.to_json())

# convert the object into a dict
envelope_playground_session_response_dict = envelope_playground_session_response_instance.to_dict()
# create an instance of EnvelopePlaygroundSessionResponse from a dict
envelope_playground_session_response_from_dict = EnvelopePlaygroundSessionResponse.from_dict(envelope_playground_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


