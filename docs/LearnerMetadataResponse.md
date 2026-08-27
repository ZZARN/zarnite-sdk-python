# LearnerMetadataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**learner** | [**LearnerResponse**](LearnerResponse.md) | Safe learner profile metadata | 
**stats** | [**LearnerStatsResponse**](LearnerStatsResponse.md) | Aggregated usage and session stats | 
**score** | [**LearnerScoreResponse**](LearnerScoreResponse.md) | Current CEFR/progression score | 
**summary** | [**LearnerSummaryResponse**](LearnerSummaryResponse.md) | Personalized learner summary | 
**recent_activity** | [**List[LearnerActivityEvent]**](LearnerActivityEvent.md) | Recent voice session activity | [optional] [default to []]

## Example

```python
from zarnite.models.learner_metadata_response import LearnerMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerMetadataResponse from a JSON string
learner_metadata_response_instance = LearnerMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(LearnerMetadataResponse.to_json())

# convert the object into a dict
learner_metadata_response_dict = learner_metadata_response_instance.to_dict()
# create an instance of LearnerMetadataResponse from a dict
learner_metadata_response_from_dict = LearnerMetadataResponse.from_dict(learner_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


