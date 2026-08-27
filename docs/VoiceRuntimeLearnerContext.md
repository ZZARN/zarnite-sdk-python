# VoiceRuntimeLearnerContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | Learner/user identifier | 
**display_name** | **str** | Display name the worker can use for neutral personalization | 
**email** | **str** | Learner email if available | [optional] 
**learner_id** | **str** | External learner identifier if available | [optional] 
**status** | **str** | Learner status | 
**cefr_level** | **str** | Latest learner CEFR level if known | [optional] 
**preferred_language** | **str** | Preferred learner language/locale if known | [optional] 

## Example

```python
from zarnite.models.voice_runtime_learner_context import VoiceRuntimeLearnerContext

# TODO update the JSON string below
json = "{}"
# create an instance of VoiceRuntimeLearnerContext from a JSON string
voice_runtime_learner_context_instance = VoiceRuntimeLearnerContext.from_json(json)
# print the JSON string representation of the object
print(VoiceRuntimeLearnerContext.to_json())

# convert the object into a dict
voice_runtime_learner_context_dict = voice_runtime_learner_context_instance.to_dict()
# create an instance of VoiceRuntimeLearnerContext from a dict
voice_runtime_learner_context_from_dict = VoiceRuntimeLearnerContext.from_dict(voice_runtime_learner_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


