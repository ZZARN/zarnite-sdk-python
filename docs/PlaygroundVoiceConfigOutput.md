# PlaygroundVoiceConfigOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voice_id** | **str** | Gemini Realtime voice preset. Supported values: Zephyr, Puck, Charon, Kore, Fenrir, Leda, Orus, Aoede, Callirrhoe, Autonoe, Enceladus, Iapetus, Umbriel, Algieba, Despina, Erinome, Algenib, Rasalgethi, Laomedeia, Achernar, Alnilam, Schedar, Gacrux, Pulcherrima, Achird, Zubenelgenubi, Vindemiatrix, Sadachbia, Sadaltager, Sulafat | [optional] 
**locale** | **str** | Locale for TTS/STT | [optional] 
**pitch** | **float** | Pitch hint for TTS voice | [optional] 
**speaking_rate** | **float** | Speaking rate hint for TTS voice | [optional] 

## Example

```python
from zarnite.models.playground_voice_config_output import PlaygroundVoiceConfigOutput

# TODO update the JSON string below
json = "{}"
# create an instance of PlaygroundVoiceConfigOutput from a JSON string
playground_voice_config_output_instance = PlaygroundVoiceConfigOutput.from_json(json)
# print the JSON string representation of the object
print(PlaygroundVoiceConfigOutput.to_json())

# convert the object into a dict
playground_voice_config_output_dict = playground_voice_config_output_instance.to_dict()
# create an instance of PlaygroundVoiceConfigOutput from a dict
playground_voice_config_output_from_dict = PlaygroundVoiceConfigOutput.from_dict(playground_voice_config_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


