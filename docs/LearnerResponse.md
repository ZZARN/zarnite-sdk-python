# LearnerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Learner identifier | 
**org_id** | **str** | Organization scope | 
**name** | **str** | Learner name | 
**email** | **str** | Learner email | [optional] 
**learner_id** | **str** | External learner identifier | [optional] 
**status** | **str** | Learner status | 
**created_at** | **datetime** | Creation timestamp | 
**updated_at** | **datetime** | Last update timestamp | 

## Example

```python
from zarnite.models.learner_response import LearnerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerResponse from a JSON string
learner_response_instance = LearnerResponse.from_json(json)
# print the JSON string representation of the object
print(LearnerResponse.to_json())

# convert the object into a dict
learner_response_dict = learner_response_instance.to_dict()
# create an instance of LearnerResponse from a dict
learner_response_from_dict = LearnerResponse.from_dict(learner_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


