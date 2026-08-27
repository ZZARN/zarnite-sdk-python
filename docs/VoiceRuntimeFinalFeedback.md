# VoiceRuntimeFinalFeedback


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence_score** | **float** | Final confidence score if computed by the worker | [optional] 
**cefr_level** | **str** | Final CEFR level if applicable | [optional] 
**recommendation** | **str** | Short learner recommendation | [optional] 
**strengths** | **List[str]** | Optional learner strengths | [optional] [default to []]
**weaknesses** | **List[str]** | Optional learner weaknesses | [optional] [default to []]

## Example

```python
from zarnite.models.voice_runtime_final_feedback import VoiceRuntimeFinalFeedback

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceRuntimeFinalFeedback from a JSON string
voice_runtime_final_feedback_instance = VoiceRuntimeFinalFeedback.from_json(json)
# print the JSON string representation of the object
print(VoiceRuntimeFinalFeedback.to_json())

# convert the object into a dict
voice_runtime_final_feedback_dict = voice_runtime_final_feedback_instance.to_dict()
# create an instance of VoiceRuntimeFinalFeedback from a dict
voice_runtime_final_feedback_from_dict = VoiceRuntimeFinalFeedback.from_dict(voice_runtime_final_feedback_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


