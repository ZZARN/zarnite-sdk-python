# EnvelopeActivityFeedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ActivityFeedResponse**](ActivityFeedResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_activity_feed_response import EnvelopeActivityFeedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeActivityFeedResponse from a JSON string
envelope_activity_feed_response_instance = EnvelopeActivityFeedResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeActivityFeedResponse.to_json())

# convert the object into a dict
envelope_activity_feed_response_dict = envelope_activity_feed_response_instance.to_dict()
# create an instance of EnvelopeActivityFeedResponse from a dict
envelope_activity_feed_response_from_dict = EnvelopeActivityFeedResponse.from_dict(envelope_activity_feed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


