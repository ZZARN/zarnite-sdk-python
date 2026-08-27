# VoiceRuntimeCloseRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Idempotency-safe worker event identifier | 
**session_id** | **str** | Voice session identifier | 
**org_id** | **str** | Organization scope | 
**agent_id** | **str** | Agent scope | 
**user_id** | **str** | Learner/user identifier | 
**thread_id** | **str** | Conversation thread identifier | 
**room_name** | **str** | LiveKit room name | [optional] 
**started_at** | **datetime** | Worker-observed start time | [optional] 
**ended_at** | **datetime** | Worker-observed end time | [optional] 
**duration_seconds** | **float** | Final session duration in seconds | [optional] 
**status** | **str** | Worker-reported final session status | [optional] [default to 'completed']
**usage** | [**VoiceRuntimeUsagePayload**](VoiceRuntimeUsagePayload.md) | Usage payload | [optional] 
**transcript** | [**VoiceRuntimeTranscriptPayload**](VoiceRuntimeTranscriptPayload.md) | Transcript payload | [optional] 
**final_feedback** | [**VoiceRuntimeFinalFeedback**](VoiceRuntimeFinalFeedback.md) | Optional final feedback summary | [optional] 

## Example

```python
from zarnite.models.voice_runtime_close_request import VoiceRuntimeCloseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceRuntimeCloseRequest from a JSON string
voice_runtime_close_request_instance = VoiceRuntimeCloseRequest.from_json(json)
# print the JSON string representation of the object
print(VoiceRuntimeCloseRequest.to_json())

# convert the object into a dict
voice_runtime_close_request_dict = voice_runtime_close_request_instance.to_dict()
# create an instance of VoiceRuntimeCloseRequest from a dict
voice_runtime_close_request_from_dict = VoiceRuntimeCloseRequest.from_dict(voice_runtime_close_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


