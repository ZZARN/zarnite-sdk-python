# EnvelopeLearnerDeactivateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LearnerDeactivateResponse**](LearnerDeactivateResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_learner_deactivate_response import EnvelopeLearnerDeactivateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeLearnerDeactivateResponse from a JSON string
envelope_learner_deactivate_response_instance = EnvelopeLearnerDeactivateResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeLearnerDeactivateResponse.to_json())

# convert the object into a dict
envelope_learner_deactivate_response_dict = envelope_learner_deactivate_response_instance.to_dict()
# create an instance of EnvelopeLearnerDeactivateResponse from a dict
envelope_learner_deactivate_response_from_dict = EnvelopeLearnerDeactivateResponse.from_dict(envelope_learner_deactivate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


