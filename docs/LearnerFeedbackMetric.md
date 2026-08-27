# LearnerFeedbackMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **int** | Current metric value (0-100) | 
**previous** | **int** | Previous baseline metric value (0-100) | 
**delta** | **int** | Current minus previous value | 
**direction** | **str** | Trend direction compared with previous sessions | 

## Example

```python
from zarnite.models.learner_feedback_metric import LearnerFeedbackMetric

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerFeedbackMetric from a JSON string
learner_feedback_metric_instance = LearnerFeedbackMetric.from_json(json)
# print the JSON string representation of the object
print(LearnerFeedbackMetric.to_json())

# convert the object into a dict
learner_feedback_metric_dict = learner_feedback_metric_instance.to_dict()
# create an instance of LearnerFeedbackMetric from a dict
learner_feedback_metric_from_dict = LearnerFeedbackMetric.from_dict(learner_feedback_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


