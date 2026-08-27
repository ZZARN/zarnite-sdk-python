# VoiceRuntimeBootstrapRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Voice session identifier | 
**org_id** | **str** | Organization scope | 
**agent_id** | **str** | Agent scope | 
**user_id** | **str** | Learner/user identifier | 
**thread_id** | **str** | Conversation thread identifier | 
**room_name** | **str** | LiveKit room name | [optional] 
**channel** | **str** | Channel label for the worker | [optional] [default to 'voice']
**is_preview** | **bool** | Whether the session is a preview/playground session | [optional] [default to False]
**started_at** | **datetime** | Worker-observed session start time | [optional] 

## Example

```python
from zarnite.models.voice_runtime_bootstrap_request import VoiceRuntimeBootstrapRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceRuntimeBootstrapRequest from a JSON string
voice_runtime_bootstrap_request_instance = VoiceRuntimeBootstrapRequest.from_json(json)
# print the JSON string representation of the object
print(VoiceRuntimeBootstrapRequest.to_json())

# convert the object into a dict
voice_runtime_bootstrap_request_dict = voice_runtime_bootstrap_request_instance.to_dict()
# create an instance of VoiceRuntimeBootstrapRequest from a dict
voice_runtime_bootstrap_request_from_dict = VoiceRuntimeBootstrapRequest.from_dict(voice_runtime_bootstrap_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


