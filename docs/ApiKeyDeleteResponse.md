# ApiKeyDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Revoked key identifier | 
**deleted** | **bool** | Deletion result | [optional] [default to True]

## Example

```python
from zarnite.models.api_key_delete_response import ApiKeyDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyDeleteResponse from a JSON string
api_key_delete_response_instance = ApiKeyDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(ApiKeyDeleteResponse.to_json())

# convert the object into a dict
api_key_delete_response_dict = api_key_delete_response_instance.to_dict()
# create an instance of ApiKeyDeleteResponse from a dict
api_key_delete_response_from_dict = ApiKeyDeleteResponse.from_dict(api_key_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


