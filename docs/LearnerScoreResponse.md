# LearnerScoreResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**learner_id** | **str** | Learner identifier | 
**score** | **int** | Overall proficiency score (0-100) | 
**cefr_level** | **str** | CEFR level (A1-C2) | 
**breakdown** | [**ScoreBreakdown**](ScoreBreakdown.md) | Per-dimension score breakdown | 
**recommendation** | **str** | AI-generated recommendation text | 
**assessed_at** | **str** | ISO timestamp of assessment | 
**rubric_type** | **str** | Evaluation rubric used for scoring | [optional] 
**rubric_reasoning** | **str** | Short explanation of why the rubric was selected | [optional] 
**evaluation_mode** | **str** | Scoring mode, e.g. heuristic or llm_hybrid | [optional] 

## Example

```python
from zarnite.models.learner_score_response import LearnerScoreResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerScoreResponse from a JSON string
learner_score_response_instance = LearnerScoreResponse.from_json(json)
# print the JSON string representation of the object
print(LearnerScoreResponse.to_json())

# convert the object into a dict
learner_score_response_dict = learner_score_response_instance.to_dict()
# create an instance of LearnerScoreResponse from a dict
learner_score_response_from_dict = LearnerScoreResponse.from_dict(learner_score_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


