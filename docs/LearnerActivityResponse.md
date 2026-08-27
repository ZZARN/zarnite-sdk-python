# LearnerActivityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**learner_id** | **str** | Learner identifier | 
**events** | [**List[LearnerActivityEvent]**](LearnerActivityEvent.md) | Recent session activity events | [optional] [default to []]

## Example

```python
from zarnite.models.learner_activity_response import LearnerActivityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerActivityResponse from a JSON string
learner_activity_response_instance = LearnerActivityResponse.from_json(json)
# print the JSON string representation of the object
print(LearnerActivityResponse.to_json())

# convert the object into a dict
learner_activity_response_dict = learner_activity_response_instance.to_dict()
# create an instance of LearnerActivityResponse from a dict
learner_activity_response_from_dict = LearnerActivityResponse.from_dict(learner_activity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


