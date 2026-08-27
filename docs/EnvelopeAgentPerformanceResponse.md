# EnvelopeAgentPerformanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AgentPerformanceResponse**](AgentPerformanceResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_agent_performance_response import EnvelopeAgentPerformanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeAgentPerformanceResponse from a JSON string
envelope_agent_performance_response_instance = EnvelopeAgentPerformanceResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeAgentPerformanceResponse.to_json())

# convert the object into a dict
envelope_agent_performance_response_dict = envelope_agent_performance_response_instance.to_dict()
# create an instance of EnvelopeAgentPerformanceResponse from a dict
envelope_agent_performance_response_from_dict = EnvelopeAgentPerformanceResponse.from_dict(envelope_agent_performance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


