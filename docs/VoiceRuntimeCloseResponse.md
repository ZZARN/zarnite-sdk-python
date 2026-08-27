# VoiceRuntimeCloseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted** | **bool** | Whether the worker event was accepted | [optional] [default to True]
**session_persisted** | **bool** | Whether the session close was persisted locally | [optional] [default to False]
**analytics_enqueued** | **bool** | Whether learner analytics refresh was triggered | [optional] [default to False]
**billing_enqueued** | **bool** | Whether usage/billing payload was persisted for downstream processing | [optional] [default to False]
**credit_wallet** | **Dict[str, object]** | Optional month credit wallet snapshot after debit | [optional] 

## Example

```python
from zarnite.models.voice_runtime_close_response import VoiceRuntimeCloseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceRuntimeCloseResponse from a JSON string
voice_runtime_close_response_instance = VoiceRuntimeCloseResponse.from_json(json)
# print the JSON string representation of the object
print(VoiceRuntimeCloseResponse.to_json())

# convert the object into a dict
voice_runtime_close_response_dict = voice_runtime_close_response_instance.to_dict()
# create an instance of VoiceRuntimeCloseResponse from a dict
voice_runtime_close_response_from_dict = VoiceRuntimeCloseResponse.from_dict(voice_runtime_close_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


