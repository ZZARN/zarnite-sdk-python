# VoiceRuntimeTranscriptMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Transcript speaker role | 
**text** | **str** | Transcript content | 
**created_at** | **datetime** | Optional original message timestamp | [optional] 

## Example

```python
from zarnite.models.voice_runtime_transcript_message import VoiceRuntimeTranscriptMessage

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceRuntimeTranscriptMessage from a JSON string
voice_runtime_transcript_message_instance = VoiceRuntimeTranscriptMessage.from_json(json)
# print the JSON string representation of the object
print(VoiceRuntimeTranscriptMessage.to_json())

# convert the object into a dict
voice_runtime_transcript_message_dict = voice_runtime_transcript_message_instance.to_dict()
# create an instance of VoiceRuntimeTranscriptMessage from a dict
voice_runtime_transcript_message_from_dict = VoiceRuntimeTranscriptMessage.from_dict(voice_runtime_transcript_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


