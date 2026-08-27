# ApiKeyCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Human-readable name for this API key | 
**org_id** | **str** | Organization scope | 
**scopes** | **List[str]** | Permission scopes (e.g. [&#39;rag:read&#39;, &#39;agents:write&#39;]) | [optional] [default to []]
**rate_limit** | **int** | Requests per minute rate limit | [optional] [default to 1000]

## Example

```python
from zarnite.models.api_key_create import ApiKeyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyCreate from a JSON string
api_key_create_instance = ApiKeyCreate.from_json(json)
# print the JSON string representation of the object
print(ApiKeyCreate.to_json())

# convert the object into a dict
api_key_create_dict = api_key_create_instance.to_dict()
# create an instance of ApiKeyCreate from a dict
api_key_create_from_dict = ApiKeyCreate.from_dict(api_key_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


