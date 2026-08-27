# AgentUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Updated agent name | [optional] 
**behavior_id** | **str** | Updated behavior/profile identifier | [optional] 
**description** | **str** | Updated agent description | [optional] 
**api_key_id** | **str** | Updated API key binding | [optional] 
**assigned_learners** | **int** | Updated assigned learner count | [optional] 
**status** | **str** | Updated operational status | [optional] 
**language** | **str** | Updated language | [optional] 
**languages** | **List[str]** | Updated language list | [optional] 
**system_prompt** | **str** | Updated system prompt | [optional] 
**tone** | **str** | Updated tone | [optional] 
**strictness** | **str** | Updated strictness | [optional] 
**guardrails** | [**GuardrailsConfig**](GuardrailsConfig.md) | Updated structured guardrail rules | [optional] 
**enable_live_playground** | **bool** | Updated playground toggle | [optional] 
**voice** | **str** | Updated voice | [optional] 
**enable_knowledge_base** | **bool** | Updated knowledge base toggle | [optional] 

## Example

```python
from zarnite.models.agent_update import AgentUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AgentUpdate from a JSON string
agent_update_instance = AgentUpdate.from_json(json)
# print the JSON string representation of the object
print(AgentUpdate.to_json())

# convert the object into a dict
agent_update_dict = agent_update_instance.to_dict()
# create an instance of AgentUpdate from a dict
agent_update_from_dict = AgentUpdate.from_dict(agent_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


