# EnvelopeAssignmentDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AssignmentDeleteResponse**](AssignmentDeleteResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_assignment_delete_response import EnvelopeAssignmentDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeAssignmentDeleteResponse from a JSON string
envelope_assignment_delete_response_instance = EnvelopeAssignmentDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeAssignmentDeleteResponse.to_json())

# convert the object into a dict
envelope_assignment_delete_response_dict = envelope_assignment_delete_response_instance.to_dict()
# create an instance of EnvelopeAssignmentDeleteResponse from a dict
envelope_assignment_delete_response_from_dict = EnvelopeAssignmentDeleteResponse.from_dict(envelope_assignment_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


