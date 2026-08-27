# PlaygroundPublicSessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Filter by status | [optional] 
**name** | **str** | Draft tutor display name | [optional] 
**description** | **str** | Draft tutor description | [optional] 
**system_prompt** | **str** | Unsaved draft system prompt to test | [optional] 
**tone** | **str** | Draft tone setting | [optional] 
**strictness** | **str** | Draft strictness setting | [optional] 
**language** | **str** | Draft strictness setting | [optional] 
**languages** | **List[str]** | Draft allowed language list | [optional] 
**voice** | [**PlaygroundVoiceConfigInput**](PlaygroundVoiceConfigInput.md) | Draft voice config | [optional] 
**guardrails** | [**GuardrailsConfig**](GuardrailsConfig.md) | Draft guardrail config | [optional] 
**behavior** | **Dict[str, object]** | Optional raw behavior object from the create-agent form | [optional] 
**preview_agent_id** | **str** | Filter by status | [optional] 
**enable_knowledge_base** | **bool** | Whether the preview session should use knowledge retrieval. | [optional] 
**knowledge_base_agent_ids** | **List[str]** | Optional KB agent ids to search during preview sessions. | [optional] 
**learner_id** | **str** | Filter by status | [optional] 
**thread_id** | **str** | Filter by status | [optional] 
**max_duration_s** | **int** | Preview session duration cap in seconds. Must be 180-300 seconds. | [optional] [default to 300]
**client** | [**PlaygroundClientMeta**](PlaygroundClientMeta.md) | Client metadata | [optional] 

## Example

```python
from zarnite.models.playground_public_session_request import PlaygroundPublicSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlaygroundPublicSessionRequest from a JSON string
playground_public_session_request_instance = PlaygroundPublicSessionRequest.from_json(json)
# print the JSON string representation of the object
print(PlaygroundPublicSessionRequest.to_json())

# convert the object into a dict
playground_public_session_request_dict = playground_public_session_request_instance.to_dict()
# create an instance of PlaygroundPublicSessionRequest from a dict
playground_public_session_request_from_dict = PlaygroundPublicSessionRequest.from_dict(playground_public_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


