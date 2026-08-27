# LearnerSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**learner_id** | **str** | Learner identifier | 
**learner_name** | **str** | Learner display name | 
**personalized_message** | **str** | Personalized welcome/summary message | 
**recent_topics** | **List[str]** | Recent conversation topic snippets | [optional] [default to []]
**current_score** | **int** | Current proficiency score | 
**cefr_level** | **str** | Current CEFR level | 

## Example

```python
from zarnite.models.learner_summary_response import LearnerSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerSummaryResponse from a JSON string
learner_summary_response_instance = LearnerSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(LearnerSummaryResponse.to_json())

# convert the object into a dict
learner_summary_response_dict = learner_summary_response_instance.to_dict()
# create an instance of LearnerSummaryResponse from a dict
learner_summary_response_from_dict = LearnerSummaryResponse.from_dict(learner_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


