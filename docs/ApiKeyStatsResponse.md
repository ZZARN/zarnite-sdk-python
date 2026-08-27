# ApiKeyStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Organization scope | 
**total_keys** | **int** | Total API keys | 
**active_keys** | **int** | Active API keys | 
**total_requests** | **int** | All-time request count | 

## Example

```python
from zarnite.models.api_key_stats_response import ApiKeyStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeyStatsResponse from a JSON string
api_key_stats_response_instance = ApiKeyStatsResponse.from_json(json)
# print the JSON string representation of the object
print(ApiKeyStatsResponse.to_json())

# convert the object into a dict
api_key_stats_response_dict = api_key_stats_response_instance.to_dict()
# create an instance of ApiKeyStatsResponse from a dict
api_key_stats_response_from_dict = ApiKeyStatsResponse.from_dict(api_key_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


