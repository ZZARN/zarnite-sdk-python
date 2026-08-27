# AssignmentCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**learner_id** | **str** | Learner to assign | 
**org_id** | **str** | Organization scope | 

## Example

```python
from zarnite.models.assignment_create import AssignmentCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AssignmentCreate from a JSON string
assignment_create_instance = AssignmentCreate.from_json(json)
# print the JSON string representation of the object
print(AssignmentCreate.to_json())

# convert the object into a dict
assignment_create_dict = assignment_create_instance.to_dict()
# create an instance of AssignmentCreate from a dict
assignment_create_from_dict = AssignmentCreate.from_dict(assignment_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


