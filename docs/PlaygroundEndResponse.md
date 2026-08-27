# PlaygroundEndResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Ended session identifier | 
**status** | **str** | New session status | 

## Example

```python
from zarnite.models.playground_end_response import PlaygroundEndResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlaygroundEndResponse from a JSON string
playground_end_response_instance = PlaygroundEndResponse.from_json(json)
# print the JSON string representation of the object
print(PlaygroundEndResponse.to_json())

# convert the object into a dict
playground_end_response_dict = playground_end_response_instance.to_dict()
# create an instance of PlaygroundEndResponse from a dict
playground_end_response_from_dict = PlaygroundEndResponse.from_dict(playground_end_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


