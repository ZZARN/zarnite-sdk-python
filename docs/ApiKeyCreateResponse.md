# ApiKeyCreateResponse

Returned only on creation — contains the one-time raw key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | API key identifier | 
**org_id** | **str** | Organization scope | 
**name** | **str** | Key name | 
**prefix** | **str** | Key prefix for identification (e.g. &#39;zrn_abc123&#39;) | 
**raw_key** | **str** | Full API key — shown only once on creation | 
**scopes** | **List[str]** | Permission scopes | 
**rate_limit** | **int** | Rate limit (req/min) | 
**is_active** | **bool** | Whether key is active | [optional] [default to True]
**created_at** | **datetime** | Creation timestamp | 

## Example

```python
from zarnite.models.api_key_create_response import ApiKeyCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyCreateResponse from a JSON string
api_key_create_response_instance = ApiKeyCreateResponse.from_json(json)
# print the JSON string representation of the object
print(ApiKeyCreateResponse.to_json())

# convert the object into a dict
api_key_create_response_dict = api_key_create_response_instance.to_dict()
# create an instance of ApiKeyCreateResponse from a dict
api_key_create_response_from_dict = ApiKeyCreateResponse.from_dict(api_key_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


