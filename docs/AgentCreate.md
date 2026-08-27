# AgentCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Optional agent identifier. If omitted the API generates one. | [optional] 
**name** | **str** | Human-readable agent name | 
**org_id** | **str** | Organization that owns this agent | 
**behavior_id** | **str** | Reference to an existing behavior record. Mutually exclusive with inline &#39;behavior&#39;. | [optional] 
**behavior** | [**BehaviorCreate**](BehaviorCreate.md) | Inline behavior config — auto-creates a behavior record and links it to this agent. Mutually exclusive with behaviorId. | [optional] 
**description** | **str** | Optional agent description | [optional] 
**api_key_id** | **str** | API key binding selected for this agent | [optional] 
**assigned_learners** | **int** | Count of learners assigned to this agent | [optional] [default to 0]
**status** | **str** | Operational status for the agent | [optional] [default to 'active']
**language** | **str** | Language for the agent (e.g. English, Spanish) | [optional] 
**languages** | **List[str]** | Preferred language list | [optional] 
**system_prompt** | **str** | System prompt | [optional] 
**tone** | **str** | Agent tone | [optional] 
**strictness** | **str** | Agent strictness setting (e.g. high, low) | [optional] 
**guardrails** | [**GuardrailsConfig**](GuardrailsConfig.md) | Structured guardrail rules | [optional] 
**enable_live_playground** | **bool** | Enable live playground toggle | [optional] [default to False]
**voice** | **str** | Voice setting | [optional] 
**enable_knowledge_base** | **bool** | Whether knowledge base is enabled | [optional] [default to True]

## Example

```python
from zarnite.models.agent_create import AgentCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCreate from a JSON string
agent_create_instance = AgentCreate.from_json(json)
# print the JSON string representation of the object
print(AgentCreate.to_json())

# convert the object into a dict
agent_create_dict = agent_create_instance.to_dict()
# create an instance of AgentCreate from a dict
agent_create_from_dict = AgentCreate.from_dict(agent_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


