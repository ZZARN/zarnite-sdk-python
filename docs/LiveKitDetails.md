# LiveKitDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | LiveKit WSS URL | 
**token** | **str** | Short-lived LiveKit access token | 

## Example

```python
from zarnite.models.live_kit_details import LiveKitDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LiveKitDetails from a JSON string
live_kit_details_instance = LiveKitDetails.from_json(json)
# print the JSON string representation of the object
print(LiveKitDetails.to_json())

# convert the object into a dict
live_kit_details_dict = live_kit_details_instance.to_dict()
# create an instance of LiveKitDetails from a dict
live_kit_details_from_dict = LiveKitDetails.from_dict(live_kit_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


