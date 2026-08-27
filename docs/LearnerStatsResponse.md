# LearnerStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_sessions** | **int** | Total voice sessions for this learner | 
**avg_duration_minutes** | **float** | Average session duration in minutes | 
**avg_latency_ms** | **float** | Average STT/TTS latency in milliseconds | 
**est_inference_cost_per_session** | **float** | Estimated inference cost per session (USD) | 
**total_tokens_used** | **int** | Total tokens consumed across all sessions | 
**last_session_at** | **str** | ISO timestamp of the most recent session | [optional] 

## Example

```python
from zarnite.models.learner_stats_response import LearnerStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerStatsResponse from a JSON string
learner_stats_response_instance = LearnerStatsResponse.from_json(json)
# print the JSON string representation of the object
print(LearnerStatsResponse.to_json())

# convert the object into a dict
learner_stats_response_dict = learner_stats_response_instance.to_dict()
# create an instance of LearnerStatsResponse from a dict
learner_stats_response_from_dict = LearnerStatsResponse.from_dict(learner_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


