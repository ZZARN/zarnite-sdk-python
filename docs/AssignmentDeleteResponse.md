# AssignmentDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**learner_id** | **str** | Unassigned learner | 
**agent_id** | **str** | Agent removed from | 
**deleted** | **bool** | Deletion result | [optional] [default to True]

## Example

```python
from zarnite.models.assignment_delete_response import AssignmentDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentDeleteResponse from a JSON string
assignment_delete_response_instance = AssignmentDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(AssignmentDeleteResponse.to_json())

# convert the object into a dict
assignment_delete_response_dict = assignment_delete_response_instance.to_dict()
# create an instance of AssignmentDeleteResponse from a dict
assignment_delete_response_from_dict = AssignmentDeleteResponse.from_dict(assignment_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


