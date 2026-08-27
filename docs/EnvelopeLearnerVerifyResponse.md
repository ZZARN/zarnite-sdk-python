# EnvelopeLearnerVerifyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LearnerVerifyResponse**](LearnerVerifyResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_learner_verify_response import EnvelopeLearnerVerifyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeLearnerVerifyResponse from a JSON string
envelope_learner_verify_response_instance = EnvelopeLearnerVerifyResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeLearnerVerifyResponse.to_json())

# convert the object into a dict
envelope_learner_verify_response_dict = envelope_learner_verify_response_instance.to_dict()
# create an instance of EnvelopeLearnerVerifyResponse from a dict
envelope_learner_verify_response_from_dict = EnvelopeLearnerVerifyResponse.from_dict(envelope_learner_verify_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


