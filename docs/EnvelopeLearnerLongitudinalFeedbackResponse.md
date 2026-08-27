# EnvelopeLearnerLongitudinalFeedbackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LearnerLongitudinalFeedbackResponse**](LearnerLongitudinalFeedbackResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_learner_longitudinal_feedback_response import EnvelopeLearnerLongitudinalFeedbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeLearnerLongitudinalFeedbackResponse from a JSON string
envelope_learner_longitudinal_feedback_response_instance = EnvelopeLearnerLongitudinalFeedbackResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeLearnerLongitudinalFeedbackResponse.to_json())

# convert the object into a dict
envelope_learner_longitudinal_feedback_response_dict = envelope_learner_longitudinal_feedback_response_instance.to_dict()
# create an instance of EnvelopeLearnerLongitudinalFeedbackResponse from a dict
envelope_learner_longitudinal_feedback_response_from_dict = EnvelopeLearnerLongitudinalFeedbackResponse.from_dict(envelope_learner_longitudinal_feedback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


