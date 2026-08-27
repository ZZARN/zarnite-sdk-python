# EnvelopeOrgRoutingConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrgRoutingConfigResponse**](OrgRoutingConfigResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_org_routing_config_response import EnvelopeOrgRoutingConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeOrgRoutingConfigResponse from a JSON string
envelope_org_routing_config_response_instance = EnvelopeOrgRoutingConfigResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeOrgRoutingConfigResponse.to_json())

# convert the object into a dict
envelope_org_routing_config_response_dict = envelope_org_routing_config_response_instance.to_dict()
# create an instance of EnvelopeOrgRoutingConfigResponse from a dict
envelope_org_routing_config_response_from_dict = EnvelopeOrgRoutingConfigResponse.from_dict(envelope_org_routing_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


