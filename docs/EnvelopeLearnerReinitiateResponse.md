# EnvelopeLearnerReinitiateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LearnerReinitiateResponse**](LearnerReinitiateResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_learner_reinitiate_response import EnvelopeLearnerReinitiateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeLearnerReinitiateResponse from a JSON string
envelope_learner_reinitiate_response_instance = EnvelopeLearnerReinitiateResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeLearnerReinitiateResponse.to_json())

# convert the object into a dict
envelope_learner_reinitiate_response_dict = envelope_learner_reinitiate_response_instance.to_dict()
# create an instance of EnvelopeLearnerReinitiateResponse from a dict
envelope_learner_reinitiate_response_from_dict = EnvelopeLearnerReinitiateResponse.from_dict(envelope_learner_reinitiate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


