# VoiceRuntimeBootstrapResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session** | [**VoiceRuntimeSessionRef**](VoiceRuntimeSessionRef.md) | Session identifiers | 
**learner** | [**VoiceRuntimeLearnerContext**](VoiceRuntimeLearnerContext.md) | Learner context | 
**agent_runtime** | [**VoiceRuntimeAgentContext**](VoiceRuntimeAgentContext.md) | Resolved runtime behavior and language configuration | 
**history** | [**VoiceRuntimeHistoryContext**](VoiceRuntimeHistoryContext.md) | Compact history context | 
**rag** | [**VoiceRuntimeRagContext**](VoiceRuntimeRagContext.md) | Knowledge availability summary | 

## Example

```python
from zarnite.models.voice_runtime_bootstrap_response import VoiceRuntimeBootstrapResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceRuntimeBootstrapResponse from a JSON string
voice_runtime_bootstrap_response_instance = VoiceRuntimeBootstrapResponse.from_json(json)
# print the JSON string representation of the object
print(VoiceRuntimeBootstrapResponse.to_json())

# convert the object into a dict
voice_runtime_bootstrap_response_dict = voice_runtime_bootstrap_response_instance.to_dict()
# create an instance of VoiceRuntimeBootstrapResponse from a dict
voice_runtime_bootstrap_response_from_dict = VoiceRuntimeBootstrapResponse.from_dict(voice_runtime_bootstrap_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


