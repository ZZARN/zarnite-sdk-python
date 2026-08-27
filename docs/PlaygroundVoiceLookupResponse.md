# PlaygroundVoiceLookupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Organization scope | 
**user_id** | **str** | Optional user scope | [optional] 
**category** | **str** | Resolved routing category | 
**source** | **str** | Category source (user_override|org_default) | 
**livekit_stack** | **str** | Resolved LiveKit stack label | 
**tts_provider** | **str** | Resolved TTS provider label | 
**voice_access** | **str** | Resolved voice entitlement tier (free|paid) | 
**voices** | **List[str]** | Allowed voices for the resolved tier | 

## Example

```python
from zarnite.models.playground_voice_lookup_response import PlaygroundVoiceLookupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlaygroundVoiceLookupResponse from a JSON string
playground_voice_lookup_response_instance = PlaygroundVoiceLookupResponse.from_json(json)
# print the JSON string representation of the object
print(PlaygroundVoiceLookupResponse.to_json())

# convert the object into a dict
playground_voice_lookup_response_dict = playground_voice_lookup_response_instance.to_dict()
# create an instance of PlaygroundVoiceLookupResponse from a dict
playground_voice_lookup_response_from_dict = PlaygroundVoiceLookupResponse.from_dict(playground_voice_lookup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


