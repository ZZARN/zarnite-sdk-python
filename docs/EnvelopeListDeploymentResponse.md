# EnvelopeListDeploymentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DeploymentResponse]**](DeploymentResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_list_deployment_response import EnvelopeListDeploymentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeListDeploymentResponse from a JSON string
envelope_list_deployment_response_instance = EnvelopeListDeploymentResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeListDeploymentResponse.to_json())

# convert the object into a dict
envelope_list_deployment_response_dict = envelope_list_deployment_response_instance.to_dict()
# create an instance of EnvelopeListDeploymentResponse from a dict
envelope_list_deployment_response_from_dict = EnvelopeListDeploymentResponse.from_dict(envelope_list_deployment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


