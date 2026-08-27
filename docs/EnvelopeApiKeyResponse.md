# EnvelopeApiKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApiKeyResponse**](ApiKeyResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_api_key_response import EnvelopeApiKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeApiKeyResponse from a JSON string
envelope_api_key_response_instance = EnvelopeApiKeyResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeApiKeyResponse.to_json())

# convert the object into a dict
envelope_api_key_response_dict = envelope_api_key_response_instance.to_dict()
# create an instance of EnvelopeApiKeyResponse from a dict
envelope_api_key_response_from_dict = EnvelopeApiKeyResponse.from_dict(envelope_api_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


