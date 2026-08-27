# PlaygroundActivityResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Updated session identifier | 
**status** | **str** | Current session status | 
**last_activity_at** | **str** | Last activity timestamp | 

## Example

```python
from zarnite.models.playground_activity_response import PlaygroundActivityResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlaygroundActivityResponse from a JSON string
playground_activity_response_instance = PlaygroundActivityResponse.from_json(json)
# print the JSON string representation of the object
print(PlaygroundActivityResponse.to_json())

# convert the object into a dict
playground_activity_response_dict = playground_activity_response_instance.to_dict()
# create an instance of PlaygroundActivityResponse from a dict
playground_activity_response_from_dict = PlaygroundActivityResponse.from_dict(playground_activity_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


