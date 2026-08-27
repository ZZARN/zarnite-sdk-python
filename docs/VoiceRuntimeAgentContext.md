# VoiceRuntimeAgentContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** | Agent identifier | 
**behavior_id** | **str** | Resolved behavior/profile identifier | [optional] 
**system_prompt** | **str** | Resolved system prompt. This is the primary runtime behavior source. | [optional] 
**response_language** | **str** | Resolved response locale/language | [optional] 
**allowed_languages** | **List[Optional[str]]** | Configured allowed languages after normalization | [optional] [default to []]
**voice** | **Dict[str, object]** | Resolved voice configuration | [optional] 
**guardrails** | **Dict[str, object]** | Resolved guardrail payload | [optional] 
**knowledge_base_enabled** | **bool** | Whether knowledge base is enabled for this agent | [optional] [default to True]

## Example

```python
from zarnite.models.voice_runtime_agent_context import VoiceRuntimeAgentContext

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceRuntimeAgentContext from a JSON string
voice_runtime_agent_context_instance = VoiceRuntimeAgentContext.from_json(json)
# print the JSON string representation of the object
print(VoiceRuntimeAgentContext.to_json())

# convert the object into a dict
voice_runtime_agent_context_dict = voice_runtime_agent_context_instance.to_dict()
# create an instance of VoiceRuntimeAgentContext from a dict
voice_runtime_agent_context_from_dict = VoiceRuntimeAgentContext.from_dict(voice_runtime_agent_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


