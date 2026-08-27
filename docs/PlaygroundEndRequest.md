# PlaygroundEndRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Reason for ending the session | [optional] [default to 'user_left']

## Example

```python
from zarnite.models.playground_end_request import PlaygroundEndRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlaygroundEndRequest from a JSON string
playground_end_request_instance = PlaygroundEndRequest.from_json(json)
# print the JSON string representation of the object
print(PlaygroundEndRequest.to_json())

# convert the object into a dict
playground_end_request_dict = playground_end_request_instance.to_dict()
# create an instance of PlaygroundEndRequest from a dict
playground_end_request_from_dict = PlaygroundEndRequest.from_dict(playground_end_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


