# EnvelopeUsageTrendsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UsageTrendsResponse**](UsageTrendsResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_usage_trends_response import EnvelopeUsageTrendsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeUsageTrendsResponse from a JSON string
envelope_usage_trends_response_instance = EnvelopeUsageTrendsResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeUsageTrendsResponse.to_json())

# convert the object into a dict
envelope_usage_trends_response_dict = envelope_usage_trends_response_instance.to_dict()
# create an instance of EnvelopeUsageTrendsResponse from a dict
envelope_usage_trends_response_from_dict = EnvelopeUsageTrendsResponse.from_dict(envelope_usage_trends_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


