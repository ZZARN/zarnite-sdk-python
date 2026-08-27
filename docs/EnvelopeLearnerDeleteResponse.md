# EnvelopeLearnerDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LearnerDeleteResponse**](LearnerDeleteResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_learner_delete_response import EnvelopeLearnerDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeLearnerDeleteResponse from a JSON string
envelope_learner_delete_response_instance = EnvelopeLearnerDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeLearnerDeleteResponse.to_json())

# convert the object into a dict
envelope_learner_delete_response_dict = envelope_learner_delete_response_instance.to_dict()
# create an instance of EnvelopeLearnerDeleteResponse from a dict
envelope_learner_delete_response_from_dict = EnvelopeLearnerDeleteResponse.from_dict(envelope_learner_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


