# EnvelopeLearnerInsightsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LearnerInsightsResponse**](LearnerInsightsResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_learner_insights_response import EnvelopeLearnerInsightsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeLearnerInsightsResponse from a JSON string
envelope_learner_insights_response_instance = EnvelopeLearnerInsightsResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeLearnerInsightsResponse.to_json())

# convert the object into a dict
envelope_learner_insights_response_dict = envelope_learner_insights_response_instance.to_dict()
# create an instance of EnvelopeLearnerInsightsResponse from a dict
envelope_learner_insights_response_from_dict = EnvelopeLearnerInsightsResponse.from_dict(envelope_learner_insights_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


