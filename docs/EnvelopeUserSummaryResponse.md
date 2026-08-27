# EnvelopeUserSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserSummaryResponse**](UserSummaryResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_user_summary_response import EnvelopeUserSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeUserSummaryResponse from a JSON string
envelope_user_summary_response_instance = EnvelopeUserSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeUserSummaryResponse.to_json())

# convert the object into a dict
envelope_user_summary_response_dict = envelope_user_summary_response_instance.to_dict()
# create an instance of EnvelopeUserSummaryResponse from a dict
envelope_user_summary_response_from_dict = EnvelopeUserSummaryResponse.from_dict(envelope_user_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


