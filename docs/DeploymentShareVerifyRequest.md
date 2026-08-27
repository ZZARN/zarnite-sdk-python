# DeploymentShareVerifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**learner_id** | **str** | Learner identifier supplied by the user (public learnerId or internal id) | 
**access_key** | **str** | Learner access key | 
**recaptcha_token** | **str** | Optional reCAPTCHA token | [optional] 

## Example

```python
from zarnite.models.deployment_share_verify_request import DeploymentShareVerifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentShareVerifyRequest from a JSON string
deployment_share_verify_request_instance = DeploymentShareVerifyRequest.from_json(json)
# print the JSON string representation of the object
print(DeploymentShareVerifyRequest.to_json())

# convert the object into a dict
deployment_share_verify_request_dict = deployment_share_verify_request_instance.to_dict()
# create an instance of DeploymentShareVerifyRequest from a dict
deployment_share_verify_request_from_dict = DeploymentShareVerifyRequest.from_dict(deployment_share_verify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


