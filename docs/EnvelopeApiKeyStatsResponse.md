# EnvelopeApiKeyStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApiKeyStatsResponse**](ApiKeyStatsResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_api_key_stats_response import EnvelopeApiKeyStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeApiKeyStatsResponse from a JSON string
envelope_api_key_stats_response_instance = EnvelopeApiKeyStatsResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeApiKeyStatsResponse.to_json())

# convert the object into a dict
envelope_api_key_stats_response_dict = envelope_api_key_stats_response_instance.to_dict()
# create an instance of EnvelopeApiKeyStatsResponse from a dict
envelope_api_key_stats_response_from_dict = EnvelopeApiKeyStatsResponse.from_dict(envelope_api_key_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


