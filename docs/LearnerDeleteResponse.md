# LearnerDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Deleted learner identifier | 
**deleted** | **bool** | Deletion result | [optional] [default to True]

## Example

```python
from zarnite.models.learner_delete_response import LearnerDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerDeleteResponse from a JSON string
learner_delete_response_instance = LearnerDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(LearnerDeleteResponse.to_json())

# convert the object into a dict
learner_delete_response_dict = learner_delete_response_instance.to_dict()
# create an instance of LearnerDeleteResponse from a dict
learner_delete_response_from_dict = LearnerDeleteResponse.from_dict(learner_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


