# EnvelopeDashboardOverviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DashboardOverviewResponse**](DashboardOverviewResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_dashboard_overview_response import EnvelopeDashboardOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeDashboardOverviewResponse from a JSON string
envelope_dashboard_overview_response_instance = EnvelopeDashboardOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeDashboardOverviewResponse.to_json())

# convert the object into a dict
envelope_dashboard_overview_response_dict = envelope_dashboard_overview_response_instance.to_dict()
# create an instance of EnvelopeDashboardOverviewResponse from a dict
envelope_dashboard_overview_response_from_dict = EnvelopeDashboardOverviewResponse.from_dict(envelope_dashboard_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


