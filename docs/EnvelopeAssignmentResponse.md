# EnvelopeAssignmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AssignmentResponse**](AssignmentResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_assignment_response import EnvelopeAssignmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeAssignmentResponse from a JSON string
envelope_assignment_response_instance = EnvelopeAssignmentResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeAssignmentResponse.to_json())

# convert the object into a dict
envelope_assignment_response_dict = envelope_assignment_response_instance.to_dict()
# create an instance of EnvelopeAssignmentResponse from a dict
envelope_assignment_response_from_dict = EnvelopeAssignmentResponse.from_dict(envelope_assignment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


