# LearnerVerifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid** | **bool** | Whether the learner-id + access key pair is valid | 
**id** | **str** | Internal learner system ID when verification succeeds | [optional] 
**learner_id** | **str** | The public learner identifier that was verified | 
**org_id** | **str** | Organization scope | 
**status** | **str** | Learner status when valid, null when invalid | [optional] 

## Example

```python
from zarnite.models.learner_verify_response import LearnerVerifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerVerifyResponse from a JSON string
learner_verify_response_instance = LearnerVerifyResponse.from_json(json)
# print the JSON string representation of the object
print(LearnerVerifyResponse.to_json())

# convert the object into a dict
learner_verify_response_dict = learner_verify_response_instance.to_dict()
# create an instance of LearnerVerifyResponse from a dict
learner_verify_response_from_dict = LearnerVerifyResponse.from_dict(learner_verify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


