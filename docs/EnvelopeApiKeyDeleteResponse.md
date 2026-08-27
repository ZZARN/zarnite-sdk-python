# EnvelopeApiKeyDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ApiKeyDeleteResponse**](ApiKeyDeleteResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_api_key_delete_response import EnvelopeApiKeyDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeApiKeyDeleteResponse from a JSON string
envelope_api_key_delete_response_instance = EnvelopeApiKeyDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeApiKeyDeleteResponse.to_json())

# convert the object into a dict
envelope_api_key_delete_response_dict = envelope_api_key_delete_response_instance.to_dict()
# create an instance of EnvelopeApiKeyDeleteResponse from a dict
envelope_api_key_delete_response_from_dict = EnvelopeApiKeyDeleteResponse.from_dict(envelope_api_key_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


