# VoiceRuntimeFeedbackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted** | **bool** | Whether the worker feedback was accepted | [optional] [default to True]
**stored** | **bool** | Whether the feedback event was stored locally | [optional] [default to False]
**duplicate** | **bool** | Whether the feedback event had already been processed | [optional] [default to False]

## Example

```python
from zarnite.models.voice_runtime_feedback_response import VoiceRuntimeFeedbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceRuntimeFeedbackResponse from a JSON string
voice_runtime_feedback_response_instance = VoiceRuntimeFeedbackResponse.from_json(json)
# print the JSON string representation of the object
print(VoiceRuntimeFeedbackResponse.to_json())

# convert the object into a dict
voice_runtime_feedback_response_dict = voice_runtime_feedback_response_instance.to_dict()
# create an instance of VoiceRuntimeFeedbackResponse from a dict
voice_runtime_feedback_response_from_dict = VoiceRuntimeFeedbackResponse.from_dict(voice_runtime_feedback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


