# EnvelopeOrganizationAnalyticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrganizationAnalyticsResponse**](OrganizationAnalyticsResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_organization_analytics_response import EnvelopeOrganizationAnalyticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeOrganizationAnalyticsResponse from a JSON string
envelope_organization_analytics_response_instance = EnvelopeOrganizationAnalyticsResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeOrganizationAnalyticsResponse.to_json())

# convert the object into a dict
envelope_organization_analytics_response_dict = envelope_organization_analytics_response_instance.to_dict()
# create an instance of EnvelopeOrganizationAnalyticsResponse from a dict
envelope_organization_analytics_response_from_dict = EnvelopeOrganizationAnalyticsResponse.from_dict(envelope_organization_analytics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


