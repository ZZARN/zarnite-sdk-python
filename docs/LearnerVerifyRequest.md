# LearnerVerifyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**learner_id** | **str** | Learner identifier to verify (public learnerId or internal id) | 
**access_key** | **str** | Raw access key to verify against stored hash | 
**org_id** | **str** | Organization scope | 

## Example

```python
from zarnite.models.learner_verify_request import LearnerVerifyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerVerifyRequest from a JSON string
learner_verify_request_instance = LearnerVerifyRequest.from_json(json)
# print the JSON string representation of the object
print(LearnerVerifyRequest.to_json())

# convert the object into a dict
learner_verify_request_dict = learner_verify_request_instance.to_dict()
# create an instance of LearnerVerifyRequest from a dict
learner_verify_request_from_dict = LearnerVerifyRequest.from_dict(learner_verify_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


