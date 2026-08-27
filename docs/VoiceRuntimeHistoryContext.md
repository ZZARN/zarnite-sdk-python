# VoiceRuntimeHistoryContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | **str** | Compact learner summary if available | [optional] 
**recent_turns** | [**List[VoiceRuntimeHistoryTurn]**](VoiceRuntimeHistoryTurn.md) | Recent ordered turns for the active thread | [optional] [default to []]
**recent_threads** | [**List[VoiceRuntimeHistoryThread]**](VoiceRuntimeHistoryThread.md) | Compact summaries of recent threads for continuity | [optional] [default to []]
**feedback** | **Dict[str, object]** | Persisted learner feedback snapshot if available | [optional] 

## Example

```python
from zarnite.models.voice_runtime_history_context import VoiceRuntimeHistoryContext

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceRuntimeHistoryContext from a JSON string
voice_runtime_history_context_instance = VoiceRuntimeHistoryContext.from_json(json)
# print the JSON string representation of the object
print(VoiceRuntimeHistoryContext.to_json())

# convert the object into a dict
voice_runtime_history_context_dict = voice_runtime_history_context_instance.to_dict()
# create an instance of VoiceRuntimeHistoryContext from a dict
voice_runtime_history_context_from_dict = VoiceRuntimeHistoryContext.from_dict(voice_runtime_history_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


