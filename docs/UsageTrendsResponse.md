# UsageTrendsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trends** | **List[Dict[str, object]]** | Daily usage trends over the requested period | 

## Example

```python
from zarnite.models.usage_trends_response import UsageTrendsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsageTrendsResponse from a JSON string
usage_trends_response_instance = UsageTrendsResponse.from_json(json)
# print the JSON string representation of the object
print(UsageTrendsResponse.to_json())

# convert the object into a dict
usage_trends_response_dict = usage_trends_response_instance.to_dict()
# create an instance of UsageTrendsResponse from a dict
usage_trends_response_from_dict = UsageTrendsResponse.from_dict(usage_trends_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


