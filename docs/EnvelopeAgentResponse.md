# EnvelopeAgentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AgentResponse**](AgentResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_agent_response import EnvelopeAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeAgentResponse from a JSON string
envelope_agent_response_instance = EnvelopeAgentResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeAgentResponse.to_json())

# convert the object into a dict
envelope_agent_response_dict = envelope_agent_response_instance.to_dict()
# create an instance of EnvelopeAgentResponse from a dict
envelope_agent_response_from_dict = EnvelopeAgentResponse.from_dict(envelope_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


