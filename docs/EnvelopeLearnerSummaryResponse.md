# EnvelopeLearnerSummaryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LearnerSummaryResponse**](LearnerSummaryResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_learner_summary_response import EnvelopeLearnerSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeLearnerSummaryResponse from a JSON string
envelope_learner_summary_response_instance = EnvelopeLearnerSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeLearnerSummaryResponse.to_json())

# convert the object into a dict
envelope_learner_summary_response_dict = envelope_learner_summary_response_instance.to_dict()
# create an instance of EnvelopeLearnerSummaryResponse from a dict
envelope_learner_summary_response_from_dict = EnvelopeLearnerSummaryResponse.from_dict(envelope_learner_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


