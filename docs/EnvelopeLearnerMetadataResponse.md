# EnvelopeLearnerMetadataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LearnerMetadataResponse**](LearnerMetadataResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_learner_metadata_response import EnvelopeLearnerMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeLearnerMetadataResponse from a JSON string
envelope_learner_metadata_response_instance = EnvelopeLearnerMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeLearnerMetadataResponse.to_json())

# convert the object into a dict
envelope_learner_metadata_response_dict = envelope_learner_metadata_response_instance.to_dict()
# create an instance of EnvelopeLearnerMetadataResponse from a dict
envelope_learner_metadata_response_from_dict = EnvelopeLearnerMetadataResponse.from_dict(envelope_learner_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


