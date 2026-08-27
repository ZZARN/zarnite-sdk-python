# VoiceRuntimeFeedbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Idempotency-safe worker feedback event identifier | 
**session_id** | **str** | Voice session identifier | 
**org_id** | **str** | Organization scope | 
**agent_id** | **str** | Agent scope | 
**user_id** | **str** | Learner/user identifier | 
**thread_id** | **str** | Conversation thread identifier | 
**feedback** | [**VoiceRuntimeFeedbackPayload**](VoiceRuntimeFeedbackPayload.md) | Structured feedback payload | 
**source** | **str** | Worker source label | [optional] [default to 'livekit-mig-worker']
**created_at** | **datetime** | Worker-observed feedback timestamp | [optional] 

## Example

```python
from zarnite.models.voice_runtime_feedback_request import VoiceRuntimeFeedbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceRuntimeFeedbackRequest from a JSON string
voice_runtime_feedback_request_instance = VoiceRuntimeFeedbackRequest.from_json(json)
# print the JSON string representation of the object
print(VoiceRuntimeFeedbackRequest.to_json())

# convert the object into a dict
voice_runtime_feedback_request_dict = voice_runtime_feedback_request_instance.to_dict()
# create an instance of VoiceRuntimeFeedbackRequest from a dict
voice_runtime_feedback_request_from_dict = VoiceRuntimeFeedbackRequest.from_dict(voice_runtime_feedback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


