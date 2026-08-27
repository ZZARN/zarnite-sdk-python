# PlaygroundSessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Created session identifier | 
**session_kind** | **str** | Session classification | 
**is_billable** | **bool** | Whether this session counts toward billing | 
**room_name** | **str** | LiveKit room name | 
**participant_identity** | **str** | Participant identity string | 
**participant_name** | **str** | Participant display name | 
**user_id** | **str** | Resolved user for the session | 
**thread_id** | **str** | Resolved conversation thread | 
**resumed_from_session_id** | **str** | Previous session id when resuming | [optional] 
**resume_supported** | **bool** | Whether the client can resume the same thread in a fresh session | [optional] [default to True]
**max_duration_s** | **int** | Max duration for the current session in seconds | 
**recommended_resume_after_s** | **int** | Recommended client-side reconnect time for seamless continuation | 
**voice** | [**PlaygroundVoiceConfigOutput**](PlaygroundVoiceConfigOutput.md) | Resolved voice config | [optional] 
**voice_quota** | **Dict[str, object]** | Billable voice quota snapshot for this session | [optional] 
**routing_category** | **str** | Resolved routing category used for this session | [optional] 
**livekit_stack** | **str** | Resolved LiveKit stack used for token minting | [optional] 
**tts_provider** | **str** | Resolved TTS provider label | [optional] 
**voice_access** | **str** | Resolved voice entitlement tier (free|paid) | [optional] 
**livekit** | [**LiveKitDetails**](LiveKitDetails.md) | LiveKit connection details | 
**expires_at** | **str** | Token expiry ISO timestamp | 

## Example

```python
from zarnite.models.playground_session_response import PlaygroundSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlaygroundSessionResponse from a JSON string
playground_session_response_instance = PlaygroundSessionResponse.from_json(json)
# print the JSON string representation of the object
print(PlaygroundSessionResponse.to_json())

# convert the object into a dict
playground_session_response_dict = playground_session_response_instance.to_dict()
# create an instance of PlaygroundSessionResponse from a dict
playground_session_response_from_dict = PlaygroundSessionResponse.from_dict(playground_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


