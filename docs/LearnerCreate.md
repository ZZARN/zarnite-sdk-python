# LearnerCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Learner full name | 
**email** | **str** | Learner email address | [optional] 
**learner_id** | **str** | External learner identifier | [optional] 
**org_id** | **str** | Organization scope | 
**status** | **str** | Learner status | [optional] [default to 'active']

## Example

```python
from zarnite.models.learner_create import LearnerCreate

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerCreate from a JSON string
learner_create_instance = LearnerCreate.from_json(json)
# print the JSON string representation of the object
print(LearnerCreate.to_json())

# convert the object into a dict
learner_create_dict = learner_create_instance.to_dict()
# create an instance of LearnerCreate from a dict
learner_create_from_dict = LearnerCreate.from_dict(learner_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


