# VoiceRuntimeUsagePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_tokens** | **int** | Input tokens consumed | [optional] [default to 0]
**output_tokens** | **int** | Output tokens consumed | [optional] [default to 0]
**total_tokens** | **int** | Total tokens consumed | [optional] [default to 0]
**voice_seconds** | **float** | Voice/audio duration in seconds | [optional] [default to 0]

## Example

```python
from zarnite.models.voice_runtime_usage_payload import VoiceRuntimeUsagePayload

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceRuntimeUsagePayload from a JSON string
voice_runtime_usage_payload_instance = VoiceRuntimeUsagePayload.from_json(json)
# print the JSON string representation of the object
print(VoiceRuntimeUsagePayload.to_json())

# convert the object into a dict
voice_runtime_usage_payload_dict = voice_runtime_usage_payload_instance.to_dict()
# create an instance of VoiceRuntimeUsagePayload from a dict
voice_runtime_usage_payload_from_dict = VoiceRuntimeUsagePayload.from_dict(voice_runtime_usage_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


