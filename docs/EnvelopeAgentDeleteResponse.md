# EnvelopeAgentDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AgentDeleteResponse**](AgentDeleteResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_agent_delete_response import EnvelopeAgentDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeAgentDeleteResponse from a JSON string
envelope_agent_delete_response_instance = EnvelopeAgentDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeAgentDeleteResponse.to_json())

# convert the object into a dict
envelope_agent_delete_response_dict = envelope_agent_delete_response_instance.to_dict()
# create an instance of EnvelopeAgentDeleteResponse from a dict
envelope_agent_delete_response_from_dict = EnvelopeAgentDeleteResponse.from_dict(envelope_agent_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


