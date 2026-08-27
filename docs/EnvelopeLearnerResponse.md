# EnvelopeLearnerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LearnerResponse**](LearnerResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_learner_response import EnvelopeLearnerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeLearnerResponse from a JSON string
envelope_learner_response_instance = EnvelopeLearnerResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeLearnerResponse.to_json())

# convert the object into a dict
envelope_learner_response_dict = envelope_learner_response_instance.to_dict()
# create an instance of EnvelopeLearnerResponse from a dict
envelope_learner_response_from_dict = EnvelopeLearnerResponse.from_dict(envelope_learner_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


