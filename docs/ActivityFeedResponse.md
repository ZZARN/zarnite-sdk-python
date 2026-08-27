# ActivityFeedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | **List[Dict[str, object]]** | Recent organization activity items | [optional] [default to []]

## Example

```python
from zarnite.models.activity_feed_response import ActivityFeedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityFeedResponse from a JSON string
activity_feed_response_instance = ActivityFeedResponse.from_json(json)
# print the JSON string representation of the object
print(ActivityFeedResponse.to_json())

# convert the object into a dict
activity_feed_response_dict = activity_feed_response_instance.to_dict()
# create an instance of ActivityFeedResponse from a dict
activity_feed_response_from_dict = ActivityFeedResponse.from_dict(activity_feed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


