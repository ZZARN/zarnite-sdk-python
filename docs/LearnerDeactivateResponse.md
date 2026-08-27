# LearnerDeactivateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Deactivated learner identifier | 
**status** | **str** | New status | [optional] [default to 'inactive']
**deactivated_at** | **datetime** | Timestamp of deactivation | 

## Example

```python
from zarnite.models.learner_deactivate_response import LearnerDeactivateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerDeactivateResponse from a JSON string
learner_deactivate_response_instance = LearnerDeactivateResponse.from_json(json)
# print the JSON string representation of the object
print(LearnerDeactivateResponse.to_json())

# convert the object into a dict
learner_deactivate_response_dict = learner_deactivate_response_instance.to_dict()
# create an instance of LearnerDeactivateResponse from a dict
learner_deactivate_response_from_dict = LearnerDeactivateResponse.from_dict(learner_deactivate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


