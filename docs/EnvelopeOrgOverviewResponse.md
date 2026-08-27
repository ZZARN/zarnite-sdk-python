# EnvelopeOrgOverviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrgOverviewResponse**](OrgOverviewResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_org_overview_response import EnvelopeOrgOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeOrgOverviewResponse from a JSON string
envelope_org_overview_response_instance = EnvelopeOrgOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeOrgOverviewResponse.to_json())

# convert the object into a dict
envelope_org_overview_response_dict = envelope_org_overview_response_instance.to_dict()
# create an instance of EnvelopeOrgOverviewResponse from a dict
envelope_org_overview_response_from_dict = EnvelopeOrgOverviewResponse.from_dict(envelope_org_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


