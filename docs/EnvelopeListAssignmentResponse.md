# EnvelopeListAssignmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AssignmentResponse]**](AssignmentResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_list_assignment_response import EnvelopeListAssignmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeListAssignmentResponse from a JSON string
envelope_list_assignment_response_instance = EnvelopeListAssignmentResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeListAssignmentResponse.to_json())

# convert the object into a dict
envelope_list_assignment_response_dict = envelope_list_assignment_response_instance.to_dict()
# create an instance of EnvelopeListAssignmentResponse from a dict
envelope_list_assignment_response_from_dict = EnvelopeListAssignmentResponse.from_dict(envelope_list_assignment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


