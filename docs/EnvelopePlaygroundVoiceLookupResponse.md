# EnvelopePlaygroundVoiceLookupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaygroundVoiceLookupResponse**](PlaygroundVoiceLookupResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_playground_voice_lookup_response import EnvelopePlaygroundVoiceLookupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopePlaygroundVoiceLookupResponse from a JSON string
envelope_playground_voice_lookup_response_instance = EnvelopePlaygroundVoiceLookupResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopePlaygroundVoiceLookupResponse.to_json())

# convert the object into a dict
envelope_playground_voice_lookup_response_dict = envelope_playground_voice_lookup_response_instance.to_dict()
# create an instance of EnvelopePlaygroundVoiceLookupResponse from a dict
envelope_playground_voice_lookup_response_from_dict = EnvelopePlaygroundVoiceLookupResponse.from_dict(envelope_playground_voice_lookup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


