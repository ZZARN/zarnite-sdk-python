# AgentPerformanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** |  | 
**agent_id** | **str** |  | 
**sessions** | **Dict[str, object]** | Session stats | 
**messages** | **Dict[str, object]** | Message volume | 
**errors** | **int** | Total error events | 
**error_rate** | **float** | Error rate (errors / sessions) | 

## Example

```python
from zarnite.models.agent_performance_response import AgentPerformanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentPerformanceResponse from a JSON string
agent_performance_response_instance = AgentPerformanceResponse.from_json(json)
# print the JSON string representation of the object
print(AgentPerformanceResponse.to_json())

# convert the object into a dict
agent_performance_response_dict = agent_performance_response_instance.to_dict()
# create an instance of AgentPerformanceResponse from a dict
agent_performance_response_from_dict = AgentPerformanceResponse.from_dict(agent_performance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


