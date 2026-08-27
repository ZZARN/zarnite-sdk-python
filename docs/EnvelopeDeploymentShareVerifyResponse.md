# EnvelopeDeploymentShareVerifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DeploymentShareVerifyResponse**](DeploymentShareVerifyResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_deployment_share_verify_response import EnvelopeDeploymentShareVerifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeDeploymentShareVerifyResponse from a JSON string
envelope_deployment_share_verify_response_instance = EnvelopeDeploymentShareVerifyResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeDeploymentShareVerifyResponse.to_json())

# convert the object into a dict
envelope_deployment_share_verify_response_dict = envelope_deployment_share_verify_response_instance.to_dict()
# create an instance of EnvelopeDeploymentShareVerifyResponse from a dict
envelope_deployment_share_verify_response_from_dict = EnvelopeDeploymentShareVerifyResponse.from_dict(envelope_deployment_share_verify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


