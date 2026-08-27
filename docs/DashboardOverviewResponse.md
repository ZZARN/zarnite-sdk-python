# DashboardOverviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kpis** | **Dict[str, object]** | Overview KPI payload | 
**system_status** | **Dict[str, object]** | System health summary | 
**usage_trends** | **Dict[str, object]** | Daily, weekly, and monthly chart series | 
**progress_distribution** | **List[Optional[Dict[str, object]]]** | Learner proficiency distribution | [optional] [default to []]
**progression_delta_pct** | **float** | Optional progression delta percentage | [optional] 
**progression_summary** | **str** | Optional progression summary text | [optional] 
**agent_activity** | **List[Optional[Dict[str, object]]]** | Top agent activity entries | [optional] [default to []]
**top_error** | **Dict[str, object]** | Top error category summary | [optional] 

## Example

```python
from zarnite.models.dashboard_overview_response import DashboardOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardOverviewResponse from a JSON string
dashboard_overview_response_instance = DashboardOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(DashboardOverviewResponse.to_json())

# convert the object into a dict
dashboard_overview_response_dict = dashboard_overview_response_instance.to_dict()
# create an instance of DashboardOverviewResponse from a dict
dashboard_overview_response_from_dict = DashboardOverviewResponse.from_dict(dashboard_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


