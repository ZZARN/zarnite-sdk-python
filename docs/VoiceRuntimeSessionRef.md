# VoiceRuntimeSessionRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Voice session identifier | 
**thread_id** | **str** | Conversation thread identifier | 
**room_name** | **str** | LiveKit room name for the session | [optional] 

## Example

```python
from zarnite.models.voice_runtime_session_ref import VoiceRuntimeSessionRef

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceRuntimeSessionRef from a JSON string
voice_runtime_session_ref_instance = VoiceRuntimeSessionRef.from_json(json)
# print the JSON string representation of the object
print(VoiceRuntimeSessionRef.to_json())

# convert the object into a dict
voice_runtime_session_ref_dict = voice_runtime_session_ref_instance.to_dict()
# create an instance of VoiceRuntimeSessionRef from a dict
voice_runtime_session_ref_from_dict = VoiceRuntimeSessionRef.from_dict(voice_runtime_session_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


