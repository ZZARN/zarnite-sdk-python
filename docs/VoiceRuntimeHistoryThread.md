# VoiceRuntimeHistoryThread


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **str** | Thread identifier | 
**learner_name** | **str** | Learner name carried in stored snapshots | [optional] 
**latest_question** | **str** | Latest learner question in that thread | [optional] 
**latest_answer** | **str** | Latest assistant answer in that thread | [optional] 
**last_message_at** | **str** | Last message timestamp for the thread | [optional] 

## Example

```python
from zarnite.models.voice_runtime_history_thread import VoiceRuntimeHistoryThread

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceRuntimeHistoryThread from a JSON string
voice_runtime_history_thread_instance = VoiceRuntimeHistoryThread.from_json(json)
# print the JSON string representation of the object
print(VoiceRuntimeHistoryThread.to_json())

# convert the object into a dict
voice_runtime_history_thread_dict = voice_runtime_history_thread_instance.to_dict()
# create an instance of VoiceRuntimeHistoryThread from a dict
voice_runtime_history_thread_from_dict = VoiceRuntimeHistoryThread.from_dict(voice_runtime_history_thread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


