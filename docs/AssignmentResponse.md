# AssignmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Assignment identifier | 
**learner_id** | **str** | Assigned learner | 
**agent_id** | **str** | Assigned agent | 
**org_id** | **str** | Organization scope | 
**assigned_at** | **datetime** | Assignment timestamp | 

## Example

```python
from zarnite.models.assignment_response import AssignmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentResponse from a JSON string
assignment_response_instance = AssignmentResponse.from_json(json)
# print the JSON string representation of the object
print(AssignmentResponse.to_json())

# convert the object into a dict
assignment_response_dict = assignment_response_instance.to_dict()
# create an instance of AssignmentResponse from a dict
assignment_response_from_dict = AssignmentResponse.from_dict(assignment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


