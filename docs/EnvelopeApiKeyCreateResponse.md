# EnvelopeApiKeyCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApiKeyCreateResponse**](ApiKeyCreateResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_api_key_create_response import EnvelopeApiKeyCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeApiKeyCreateResponse from a JSON string
envelope_api_key_create_response_instance = EnvelopeApiKeyCreateResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeApiKeyCreateResponse.to_json())

# convert the object into a dict
envelope_api_key_create_response_dict = envelope_api_key_create_response_instance.to_dict()
# create an instance of EnvelopeApiKeyCreateResponse from a dict
envelope_api_key_create_response_from_dict = EnvelopeApiKeyCreateResponse.from_dict(envelope_api_key_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


