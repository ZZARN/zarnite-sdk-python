# LearnerDeletionScheduleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**learner_id** | **str** | Learner identifier | 
**scheduled** | **bool** | Whether learner deletion is currently scheduled | 
**requested_at** | **datetime** | When deletion was requested | [optional] 
**scheduled_for** | **datetime** | When learner deletion will execute | [optional] 
**requested_by** | **str** | Identifier for the admin who scheduled deletion | [optional] 
**days_remaining** | **int** | Whole days remaining until deletion executes | [optional] 
**cancellable** | **bool** | Whether deletion can still be cancelled | [optional] [default to False]

## Example

```python
from zarnite.models.learner_deletion_schedule_response import LearnerDeletionScheduleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerDeletionScheduleResponse from a JSON string
learner_deletion_schedule_response_instance = LearnerDeletionScheduleResponse.from_json(json)
# print the JSON string representation of the object
print(LearnerDeletionScheduleResponse.to_json())

# convert the object into a dict
learner_deletion_schedule_response_dict = learner_deletion_schedule_response_instance.to_dict()
# create an instance of LearnerDeletionScheduleResponse from a dict
learner_deletion_schedule_response_from_dict = LearnerDeletionScheduleResponse.from_dict(learner_deletion_schedule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


