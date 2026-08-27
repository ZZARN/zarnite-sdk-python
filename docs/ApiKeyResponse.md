# ApiKeyResponse

Standard key response — never includes the raw key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | API key identifier | 
**org_id** | **str** | Organization scope | 
**name** | **str** | Key name | 
**prefix** | **str** | Key prefix for identification | 
**scopes** | **List[str]** | Permission scopes | 
**rate_limit** | **int** | Rate limit (req/min) | 
**is_active** | **bool** | Whether key is active | 
**last_used_at** | **datetime** | Last usage timestamp | [optional] 
**total_requests** | **int** | Lifetime request count | [optional] [default to 0]
**created_at** | **datetime** | Creation timestamp | 
**updated_at** | **datetime** | Last update | 

## Example

```python
from zarnite.models.api_key_response import ApiKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyResponse from a JSON string
api_key_response_instance = ApiKeyResponse.from_json(json)
# print the JSON string representation of the object
print(ApiKeyResponse.to_json())

# convert the object into a dict
api_key_response_dict = api_key_response_instance.to_dict()
# create an instance of ApiKeyResponse from a dict
api_key_response_from_dict = ApiKeyResponse.from_dict(api_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


