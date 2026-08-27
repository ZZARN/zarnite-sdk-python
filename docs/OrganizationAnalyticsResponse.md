# OrganizationAnalyticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | **str** | Selected range label | 
**view** | **str** | Selected analytics lens | 
**classes** | **List[Optional[str]]** | Available class filters | [optional] [default to []]
**date_ranges** | **List[Optional[str]]** | Available date ranges | [optional] [default to []]
**institution** | **Dict[str, object]** | Institution overview payload | 
**agents** | **List[Optional[Dict[str, object]]]** | Agent performance payload | [optional] [default to []]
**students** | **List[Optional[Dict[str, object]]]** | Student list payload | [optional] [default to []]
**student_detail** | **Dict[str, object]** | Selected student detail payload | [optional] 

## Example

```python
from zarnite.models.organization_analytics_response import OrganizationAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationAnalyticsResponse from a JSON string
organization_analytics_response_instance = OrganizationAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print(OrganizationAnalyticsResponse.to_json())

# convert the object into a dict
organization_analytics_response_dict = organization_analytics_response_instance.to_dict()
# create an instance of OrganizationAnalyticsResponse from a dict
organization_analytics_response_from_dict = OrganizationAnalyticsResponse.from_dict(organization_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


