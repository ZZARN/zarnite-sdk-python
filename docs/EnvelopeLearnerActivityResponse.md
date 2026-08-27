# EnvelopeLearnerActivityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LearnerActivityResponse**](LearnerActivityResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_learner_activity_response import EnvelopeLearnerActivityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeLearnerActivityResponse from a JSON string
envelope_learner_activity_response_instance = EnvelopeLearnerActivityResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeLearnerActivityResponse.to_json())

# convert the object into a dict
envelope_learner_activity_response_dict = envelope_learner_activity_response_instance.to_dict()
# create an instance of EnvelopeLearnerActivityResponse from a dict
envelope_learner_activity_response_from_dict = EnvelopeLearnerActivityResponse.from_dict(envelope_learner_activity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


