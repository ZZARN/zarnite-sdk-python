# EnvelopeLearnerScoreResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LearnerScoreResponse**](LearnerScoreResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_learner_score_response import EnvelopeLearnerScoreResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeLearnerScoreResponse from a JSON string
envelope_learner_score_response_instance = EnvelopeLearnerScoreResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeLearnerScoreResponse.to_json())

# convert the object into a dict
envelope_learner_score_response_dict = envelope_learner_score_response_instance.to_dict()
# create an instance of EnvelopeLearnerScoreResponse from a dict
envelope_learner_score_response_from_dict = EnvelopeLearnerScoreResponse.from_dict(envelope_learner_score_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


