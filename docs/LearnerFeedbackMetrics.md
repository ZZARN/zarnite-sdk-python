# LearnerFeedbackMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grammar_accuracy** | [**LearnerFeedbackMetric**](LearnerFeedbackMetric.md) | Heuristic grammar accuracy signal | 
**fluency** | [**LearnerFeedbackMetric**](LearnerFeedbackMetric.md) | Heuristic fluency signal | 
**vocab_range** | [**LearnerFeedbackMetric**](LearnerFeedbackMetric.md) | Vocabulary breadth signal | 
**contextual_use** | [**LearnerFeedbackMetric**](LearnerFeedbackMetric.md) | Context continuity and topical-use signal | 

## Example

```python
from zarnite.models.learner_feedback_metrics import LearnerFeedbackMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerFeedbackMetrics from a JSON string
learner_feedback_metrics_instance = LearnerFeedbackMetrics.from_json(json)
# print the JSON string representation of the object
print(LearnerFeedbackMetrics.to_json())

# convert the object into a dict
learner_feedback_metrics_dict = learner_feedback_metrics_instance.to_dict()
# create an instance of LearnerFeedbackMetrics from a dict
learner_feedback_metrics_from_dict = LearnerFeedbackMetrics.from_dict(learner_feedback_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


