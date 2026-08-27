# VoiceRuntimeTranscriptPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[VoiceRuntimeTranscriptMessage]**](VoiceRuntimeTranscriptMessage.md) | Ordered transcript messages | [optional] [default to []]

## Example

```python
from zarnite.models.voice_runtime_transcript_payload import VoiceRuntimeTranscriptPayload

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceRuntimeTranscriptPayload from a JSON string
voice_runtime_transcript_payload_instance = VoiceRuntimeTranscriptPayload.from_json(json)
# print the JSON string representation of the object
print(VoiceRuntimeTranscriptPayload.to_json())

# convert the object into a dict
voice_runtime_transcript_payload_dict = voice_runtime_transcript_payload_instance.to_dict()
# create an instance of VoiceRuntimeTranscriptPayload from a dict
voice_runtime_transcript_payload_from_dict = VoiceRuntimeTranscriptPayload.from_dict(voice_runtime_transcript_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


