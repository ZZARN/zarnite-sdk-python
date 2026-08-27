# EnvelopePlaygroundSessionDiagnosticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaygroundSessionDiagnosticsResponse**](PlaygroundSessionDiagnosticsResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_playground_session_diagnostics_response import EnvelopePlaygroundSessionDiagnosticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopePlaygroundSessionDiagnosticsResponse from a JSON string
envelope_playground_session_diagnostics_response_instance = EnvelopePlaygroundSessionDiagnosticsResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopePlaygroundSessionDiagnosticsResponse.to_json())

# convert the object into a dict
envelope_playground_session_diagnostics_response_dict = envelope_playground_session_diagnostics_response_instance.to_dict()
# create an instance of EnvelopePlaygroundSessionDiagnosticsResponse from a dict
envelope_playground_session_diagnostics_response_from_dict = EnvelopePlaygroundSessionDiagnosticsResponse.from_dict(envelope_playground_session_diagnostics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


