# AggregatedUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Organization scope | 
**total_tokens** | **int** | Total tokens consumed in period | 
**total_sessions** | **int** | Total voice sessions in period | 
**start_date** | **date** | Filter start date | [optional] 
**end_date** | **date** | Filter end date | [optional] 

## Example

```python
from zarnite.models.aggregated_usage import AggregatedUsage

# TODO update the JSON string below
json = "{}"
# create an instance of AggregatedUsage from a JSON string
aggregated_usage_instance = AggregatedUsage.from_json(json)
# print the JSON string representation of the object
print(AggregatedUsage.to_json())

# convert the object into a dict
aggregated_usage_dict = aggregated_usage_instance.to_dict()
# create an instance of AggregatedUsage from a dict
aggregated_usage_from_dict = AggregatedUsage.from_dict(aggregated_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


