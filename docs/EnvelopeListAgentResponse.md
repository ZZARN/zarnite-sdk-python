# EnvelopeListAgentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AgentResponse]**](AgentResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_list_agent_response import EnvelopeListAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeListAgentResponse from a JSON string
envelope_list_agent_response_instance = EnvelopeListAgentResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeListAgentResponse.to_json())

# convert the object into a dict
envelope_list_agent_response_dict = envelope_list_agent_response_instance.to_dict()
# create an instance of EnvelopeListAgentResponse from a dict
envelope_list_agent_response_from_dict = EnvelopeListAgentResponse.from_dict(envelope_list_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


