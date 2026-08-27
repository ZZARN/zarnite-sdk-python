# LearnerInsightsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**learner** | **Dict[str, object]** | Learner identity summary | 
**stats** | **Dict[str, object]** | Learner stats payload | 
**score** | **Dict[str, object]** | Learner score payload | 
**feedback** | **Dict[str, object]** | Persisted rolling learner feedback payload | 
**overview** | **Dict[str, object]** | Overview tab payload | 
**learning_insights** | **Dict[str, object]** | Learning insights tab payload | 
**system_health** | **Dict[str, object]** | System health tab payload | 

## Example

```python
from zarnite.models.learner_insights_response import LearnerInsightsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerInsightsResponse from a JSON string
learner_insights_response_instance = LearnerInsightsResponse.from_json(json)
# print the JSON string representation of the object
print(LearnerInsightsResponse.to_json())

# convert the object into a dict
learner_insights_response_dict = learner_insights_response_instance.to_dict()
# create an instance of LearnerInsightsResponse from a dict
learner_insights_response_from_dict = LearnerInsightsResponse.from_dict(learner_insights_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


