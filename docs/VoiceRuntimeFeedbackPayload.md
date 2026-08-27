# VoiceRuntimeFeedbackPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Feedback/event kind emitted by the worker | 
**narrative** | **str** | Human-readable summary or note | [optional] 
**recommendation** | **str** | Recommended learner next step | [optional] 
**confidence_score** | **float** | Confidence score if computed by the worker | [optional] 
**cefr_level** | **str** | CEFR level if inferred by the worker | [optional] 
**strengths** | **List[str]** | Optional learner strengths | [optional] [default to []]
**weaknesses** | **List[str]** | Optional learner weaknesses | [optional] [default to []]
**details** | **Dict[str, object]** | Additional structured feedback details | [optional] 

## Example

```python
from zarnite.models.voice_runtime_feedback_payload import VoiceRuntimeFeedbackPayload

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceRuntimeFeedbackPayload from a JSON string
voice_runtime_feedback_payload_instance = VoiceRuntimeFeedbackPayload.from_json(json)
# print the JSON string representation of the object
print(VoiceRuntimeFeedbackPayload.to_json())

# convert the object into a dict
voice_runtime_feedback_payload_dict = voice_runtime_feedback_payload_instance.to_dict()
# create an instance of VoiceRuntimeFeedbackPayload from a dict
voice_runtime_feedback_payload_from_dict = VoiceRuntimeFeedbackPayload.from_dict(voice_runtime_feedback_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


