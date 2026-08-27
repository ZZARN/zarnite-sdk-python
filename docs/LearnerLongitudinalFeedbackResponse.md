# LearnerLongitudinalFeedbackResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**learner_id** | **str** | Learner identifier | 
**learner_name** | **str** | Learner display name | 
**sessions_analyzed** | **int** | Number of recent sessions included | 
**conversation_window** | **str** | Conversation window label | 
**narrative** | **str** | Concise longitudinal feedback paragraph | 
**metrics** | [**LearnerFeedbackMetrics**](LearnerFeedbackMetrics.md) | Current and previous learning signals | 
**strengths** | **List[Optional[str]]** | Top positive learner signals | [optional] [default to []]
**improvement_areas** | **List[Optional[str]]** | Top improvement areas | [optional] [default to []]
**recommended_next_step** | **str** | Suggested action for the next session | 
**recent_topics** | **List[Optional[str]]** | Recent topic keywords | [optional] [default to []]
**generated_at** | **str** | ISO timestamp when feedback was generated | 
**evaluation_mode** | **str** | Feedback generation mode, e.g. heuristic or llm_hybrid | [optional] 
**rubric_type** | **str** | Evaluation rubric used for the feedback | [optional] 
**rubric_reasoning** | **str** | Short explanation of why the rubric was selected | [optional] 
**evaluation_criteria** | **List[Dict[str, str]]** | Frontend-ready rubric criteria used for the evaluation | [optional] 
**progression_comparison** | **Dict[str, object]** | Comparison of the latest part of the window against the older part | [optional] 

## Example

```python
from zarnite.models.learner_longitudinal_feedback_response import LearnerLongitudinalFeedbackResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerLongitudinalFeedbackResponse from a JSON string
learner_longitudinal_feedback_response_instance = LearnerLongitudinalFeedbackResponse.from_json(json)
# print the JSON string representation of the object
print(LearnerLongitudinalFeedbackResponse.to_json())

# convert the object into a dict
learner_longitudinal_feedback_response_dict = learner_longitudinal_feedback_response_instance.to_dict()
# create an instance of LearnerLongitudinalFeedbackResponse from a dict
learner_longitudinal_feedback_response_from_dict = LearnerLongitudinalFeedbackResponse.from_dict(learner_longitudinal_feedback_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


