# EnvelopeLearnerStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LearnerStatsResponse**](LearnerStatsResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_learner_stats_response import EnvelopeLearnerStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeLearnerStatsResponse from a JSON string
envelope_learner_stats_response_instance = EnvelopeLearnerStatsResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeLearnerStatsResponse.to_json())

# convert the object into a dict
envelope_learner_stats_response_dict = envelope_learner_stats_response_instance.to_dict()
# create an instance of EnvelopeLearnerStatsResponse from a dict
envelope_learner_stats_response_from_dict = EnvelopeLearnerStatsResponse.from_dict(envelope_learner_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


