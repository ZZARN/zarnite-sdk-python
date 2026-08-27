# PlaygroundRuntimeConfigDiagnostics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Runtime assistant name | [optional] 
**language** | **str** | Primary runtime language | [optional] 
**languages** | **List[str]** | Allowed/configured runtime languages | [optional] [default to []]
**voice** | **Dict[str, object]** | Runtime voice configuration | [optional] 
**tone** | **str** | Runtime tone setting | [optional] 
**strictness** | **str** | Runtime strictness setting | [optional] 

## Example

```python
from zarnite.models.playground_runtime_config_diagnostics import PlaygroundRuntimeConfigDiagnostics

# TODO update the JSON string below
json = "{}"
# create an instance of PlaygroundRuntimeConfigDiagnostics from a JSON string
playground_runtime_config_diagnostics_instance = PlaygroundRuntimeConfigDiagnostics.from_json(json)
# print the JSON string representation of the object
print(PlaygroundRuntimeConfigDiagnostics.to_json())

# convert the object into a dict
playground_runtime_config_diagnostics_dict = playground_runtime_config_diagnostics_instance.to_dict()
# create an instance of PlaygroundRuntimeConfigDiagnostics from a dict
playground_runtime_config_diagnostics_from_dict = PlaygroundRuntimeConfigDiagnostics.from_dict(playground_runtime_config_diagnostics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


