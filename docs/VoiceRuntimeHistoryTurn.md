# VoiceRuntimeHistoryTurn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Speaker role | 
**text** | **str** | Turn text | 
**created_at** | **str** | Turn timestamp | [optional] 

## Example

```python
from zarnite.models.voice_runtime_history_turn import VoiceRuntimeHistoryTurn

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceRuntimeHistoryTurn from a JSON string
voice_runtime_history_turn_instance = VoiceRuntimeHistoryTurn.from_json(json)
# print the JSON string representation of the object
print(VoiceRuntimeHistoryTurn.to_json())

# convert the object into a dict
voice_runtime_history_turn_dict = voice_runtime_history_turn_instance.to_dict()
# create an instance of VoiceRuntimeHistoryTurn from a dict
voice_runtime_history_turn_from_dict = VoiceRuntimeHistoryTurn.from_dict(voice_runtime_history_turn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


