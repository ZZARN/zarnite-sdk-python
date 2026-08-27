# AgentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Agent identifier | 
**org_id** | **str** | Owning organization | 
**name** | **str** | Agent name | 
**behavior_id** | **str** | Linked behavior identifier | [optional] 
**behavior** | [**BehaviorResponse**](BehaviorResponse.md) | Resolved behavior config (populated on GET) | [optional] 
**description** | **str** | Agent description | [optional] 
**api_key_id** | **str** | API key binding | [optional] 
**assigned_learners** | **int** | Assigned learner count | [optional] [default to 0]
**status** | **str** | Agent status | 
**created_at** | **datetime** | Creation timestamp | 
**updated_at** | **datetime** | Last update timestamp | 
**language** | **str** | Agent language | [optional] 
**languages** | **List[str]** | Preferred language list | [optional] [default to []]
**system_prompt** | **str** | Agent system prompt | [optional] 
**tone** | **str** | Agent tone | [optional] 
**strictness** | **str** | Agent strictness string | [optional] 
**guardrails** | **Dict[str, object]** | Structured guardrail rules | [optional] 
**enable_live_playground** | **bool** | Enable live playground | [optional] [default to False]
**voice** | **str** | Agent voice | [optional] 
**enable_knowledge_base** | **bool** | Knowledge base enabled toggle | [optional] [default to True]

## Example

```python
from zarnite.models.agent_response import AgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentResponse from a JSON string
agent_response_instance = AgentResponse.from_json(json)
# print the JSON string representation of the object
print(AgentResponse.to_json())

# convert the object into a dict
agent_response_dict = agent_response_instance.to_dict()
# create an instance of AgentResponse from a dict
agent_response_from_dict = AgentResponse.from_dict(agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


