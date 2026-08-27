# EnvelopeLearnerCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LearnerCreateResponse**](LearnerCreateResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_learner_create_response import EnvelopeLearnerCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeLearnerCreateResponse from a JSON string
envelope_learner_create_response_instance = EnvelopeLearnerCreateResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeLearnerCreateResponse.to_json())

# convert the object into a dict
envelope_learner_create_response_dict = envelope_learner_create_response_instance.to_dict()
# create an instance of EnvelopeLearnerCreateResponse from a dict
envelope_learner_create_response_from_dict = EnvelopeLearnerCreateResponse.from_dict(envelope_learner_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


