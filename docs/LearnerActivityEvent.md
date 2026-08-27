# LearnerActivityEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Session identifier | 
**agent_id** | **str** | Agent used in this session | 
**session_kind** | **str** | Session type (playground_debug, learner_live, etc.) | 
**status** | **str** | Session status (active, ended, timed_out) | 
**started_at** | **str** | Session start time | [optional] 
**ended_at** | **str** | Session end time | [optional] 
**duration_s** | **float** | Session duration in seconds | [optional] [default to 0]
**event_count** | **int** | Number of events recorded in this session | [optional] [default to 0]

## Example

```python
from zarnite.models.learner_activity_event import LearnerActivityEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerActivityEvent from a JSON string
learner_activity_event_instance = LearnerActivityEvent.from_json(json)
# print the JSON string representation of the object
print(LearnerActivityEvent.to_json())

# convert the object into a dict
learner_activity_event_dict = learner_activity_event_instance.to_dict()
# create an instance of LearnerActivityEvent from a dict
learner_activity_event_from_dict = LearnerActivityEvent.from_dict(learner_activity_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


