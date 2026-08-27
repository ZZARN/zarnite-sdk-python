# EnvelopeLearnerDeletionScheduleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LearnerDeletionScheduleResponse**](LearnerDeletionScheduleResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_learner_deletion_schedule_response import EnvelopeLearnerDeletionScheduleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeLearnerDeletionScheduleResponse from a JSON string
envelope_learner_deletion_schedule_response_instance = EnvelopeLearnerDeletionScheduleResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeLearnerDeletionScheduleResponse.to_json())

# convert the object into a dict
envelope_learner_deletion_schedule_response_dict = envelope_learner_deletion_schedule_response_instance.to_dict()
# create an instance of EnvelopeLearnerDeletionScheduleResponse from a dict
envelope_learner_deletion_schedule_response_from_dict = EnvelopeLearnerDeletionScheduleResponse.from_dict(envelope_learner_deletion_schedule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


