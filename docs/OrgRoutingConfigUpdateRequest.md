# OrgRoutingConfigUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Org routing category (enterprise|standard|ngo|paid|free) | [optional] 
**voice_stack** | **str** | Voice stack selector (default|enterprise) | [optional] 
**pricing_plan** | **str** | Optional pricing plan label used by backend policy | [optional] 
**tts_provider** | **str** | Optional TTS provider label for diagnostics/routing | [optional] 
**metadata** | **Dict[str, object]** | Optional custom org routing metadata | [optional] 

## Example

```python
from zarnite.models.org_routing_config_update_request import OrgRoutingConfigUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrgRoutingConfigUpdateRequest from a JSON string
org_routing_config_update_request_instance = OrgRoutingConfigUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(OrgRoutingConfigUpdateRequest.to_json())

# convert the object into a dict
org_routing_config_update_request_dict = org_routing_config_update_request_instance.to_dict()
# create an instance of OrgRoutingConfigUpdateRequest from a dict
org_routing_config_update_request_from_dict = OrgRoutingConfigUpdateRequest.from_dict(org_routing_config_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


