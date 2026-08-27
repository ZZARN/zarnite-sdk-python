# OrgRoutingConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Organization scope | 
**category** | **str** | Effective org routing category | 
**voice_stack** | **str** | Configured voice stack selector | 
**pricing_plan** | **str** | Configured org pricing plan | [optional] 
**tts_provider** | **str** | Configured TTS provider | [optional] 
**metadata** | **Dict[str, object]** | Custom org routing metadata | [optional] 

## Example

```python
from zarnite.models.org_routing_config_response import OrgRoutingConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrgRoutingConfigResponse from a JSON string
org_routing_config_response_instance = OrgRoutingConfigResponse.from_json(json)
# print the JSON string representation of the object
print(OrgRoutingConfigResponse.to_json())

# convert the object into a dict
org_routing_config_response_dict = org_routing_config_response_instance.to_dict()
# create an instance of OrgRoutingConfigResponse from a dict
org_routing_config_response_from_dict = OrgRoutingConfigResponse.from_dict(org_routing_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


