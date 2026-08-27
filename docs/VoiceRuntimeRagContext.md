# VoiceRuntimeRagContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents_available** | **bool** | Whether any scoped knowledge documents exist | [optional] [default to False]
**knowledge_scope** | **List[str]** | Human-readable scope labels for the available knowledge | [optional] [default to []]
**agent_document_count** | **int** | Count of agent-scoped knowledge documents | [optional] [default to 0]
**org_document_count** | **int** | Count of org-scoped knowledge documents | [optional] [default to 0]

## Example

```python
from zarnite.models.voice_runtime_rag_context import VoiceRuntimeRagContext

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceRuntimeRagContext from a JSON string
voice_runtime_rag_context_instance = VoiceRuntimeRagContext.from_json(json)
# print the JSON string representation of the object
print(VoiceRuntimeRagContext.to_json())

# convert the object into a dict
voice_runtime_rag_context_dict = voice_runtime_rag_context_instance.to_dict()
# create an instance of VoiceRuntimeRagContext from a dict
voice_runtime_rag_context_from_dict = VoiceRuntimeRagContext.from_dict(voice_runtime_rag_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


