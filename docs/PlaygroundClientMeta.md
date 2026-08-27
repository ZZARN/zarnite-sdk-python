# PlaygroundClientMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Client source identifier | [optional] [default to 'web_playground']
**user_agent** | **str** | Browser user-agent | [optional] 
**debug_panel** | **bool** | Whether the debug panel is active | [optional] [default to False]

## Example

```python
from zarnite.models.playground_client_meta import PlaygroundClientMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PlaygroundClientMeta from a JSON string
playground_client_meta_instance = PlaygroundClientMeta.from_json(json)
# print the JSON string representation of the object
print(PlaygroundClientMeta.to_json())

# convert the object into a dict
playground_client_meta_dict = playground_client_meta_instance.to_dict()
# create an instance of PlaygroundClientMeta from a dict
playground_client_meta_from_dict = PlaygroundClientMeta.from_dict(playground_client_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


