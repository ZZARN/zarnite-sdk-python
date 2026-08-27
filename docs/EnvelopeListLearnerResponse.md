# EnvelopeListLearnerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[LearnerResponse]**](LearnerResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_list_learner_response import EnvelopeListLearnerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeListLearnerResponse from a JSON string
envelope_list_learner_response_instance = EnvelopeListLearnerResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeListLearnerResponse.to_json())

# convert the object into a dict
envelope_list_learner_response_dict = envelope_list_learner_response_instance.to_dict()
# create an instance of EnvelopeListLearnerResponse from a dict
envelope_list_learner_response_from_dict = EnvelopeListLearnerResponse.from_dict(envelope_list_learner_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


