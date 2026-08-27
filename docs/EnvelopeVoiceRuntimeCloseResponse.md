# EnvelopeVoiceRuntimeCloseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**VoiceRuntimeCloseResponse**](VoiceRuntimeCloseResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_voice_runtime_close_response import EnvelopeVoiceRuntimeCloseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeVoiceRuntimeCloseResponse from a JSON string
envelope_voice_runtime_close_response_instance = EnvelopeVoiceRuntimeCloseResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeVoiceRuntimeCloseResponse.to_json())

# convert the object into a dict
envelope_voice_runtime_close_response_dict = envelope_voice_runtime_close_response_instance.to_dict()
# create an instance of EnvelopeVoiceRuntimeCloseResponse from a dict
envelope_voice_runtime_close_response_from_dict = EnvelopeVoiceRuntimeCloseResponse.from_dict(envelope_voice_runtime_close_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


