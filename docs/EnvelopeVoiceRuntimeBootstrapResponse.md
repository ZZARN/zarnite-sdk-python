# EnvelopeVoiceRuntimeBootstrapResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**VoiceRuntimeBootstrapResponse**](VoiceRuntimeBootstrapResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_voice_runtime_bootstrap_response import EnvelopeVoiceRuntimeBootstrapResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeVoiceRuntimeBootstrapResponse from a JSON string
envelope_voice_runtime_bootstrap_response_instance = EnvelopeVoiceRuntimeBootstrapResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeVoiceRuntimeBootstrapResponse.to_json())

# convert the object into a dict
envelope_voice_runtime_bootstrap_response_dict = envelope_voice_runtime_bootstrap_response_instance.to_dict()
# create an instance of EnvelopeVoiceRuntimeBootstrapResponse from a dict
envelope_voice_runtime_bootstrap_response_from_dict = EnvelopeVoiceRuntimeBootstrapResponse.from_dict(envelope_voice_runtime_bootstrap_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


