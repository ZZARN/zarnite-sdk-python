# EnvelopeListApiKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiKeyResponse]**](ApiKeyResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_list_api_key_response import EnvelopeListApiKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeListApiKeyResponse from a JSON string
envelope_list_api_key_response_instance = EnvelopeListApiKeyResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeListApiKeyResponse.to_json())

# convert the object into a dict
envelope_list_api_key_response_dict = envelope_list_api_key_response_instance.to_dict()
# create an instance of EnvelopeListApiKeyResponse from a dict
envelope_list_api_key_response_from_dict = EnvelopeListApiKeyResponse.from_dict(envelope_list_api_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


