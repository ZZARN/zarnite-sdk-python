# EnvelopeUserTopicsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UserTopicsResponse**](UserTopicsResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_user_topics_response import EnvelopeUserTopicsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeUserTopicsResponse from a JSON string
envelope_user_topics_response_instance = EnvelopeUserTopicsResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeUserTopicsResponse.to_json())

# convert the object into a dict
envelope_user_topics_response_dict = envelope_user_topics_response_instance.to_dict()
# create an instance of EnvelopeUserTopicsResponse from a dict
envelope_user_topics_response_from_dict = EnvelopeUserTopicsResponse.from_dict(envelope_user_topics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


