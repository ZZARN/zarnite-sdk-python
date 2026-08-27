# EnvelopeVoiceRuntimeFeedbackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**VoiceRuntimeFeedbackResponse**](VoiceRuntimeFeedbackResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_voice_runtime_feedback_response import EnvelopeVoiceRuntimeFeedbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeVoiceRuntimeFeedbackResponse from a JSON string
envelope_voice_runtime_feedback_response_instance = EnvelopeVoiceRuntimeFeedbackResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeVoiceRuntimeFeedbackResponse.to_json())

# convert the object into a dict
envelope_voice_runtime_feedback_response_dict = envelope_voice_runtime_feedback_response_instance.to_dict()
# create an instance of EnvelopeVoiceRuntimeFeedbackResponse from a dict
envelope_voice_runtime_feedback_response_from_dict = EnvelopeVoiceRuntimeFeedbackResponse.from_dict(envelope_voice_runtime_feedback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


