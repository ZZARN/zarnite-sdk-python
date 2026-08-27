# PlaygroundSessionDiagnosticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Session identifier | 
**session_kind** | **str** | Session classification | 
**status** | **str** | Current session status | 
**latency** | [**PlaygroundLatencyDiagnostics**](PlaygroundLatencyDiagnostics.md) | Latency rollup | 
**events** | [**List[PlaygroundMetricsEvent]**](PlaygroundMetricsEvent.md) | Recent session events | [optional] [default to []]
**voice_quota** | **Dict[str, object]** | Voice quota snapshot attached to the session | [optional] 
**runtime_config** | [**PlaygroundRuntimeConfigDiagnostics**](PlaygroundRuntimeConfigDiagnostics.md) | Runtime configuration visible to frontend diagnostics | 

## Example

```python
from zarnite.models.playground_session_diagnostics_response import PlaygroundSessionDiagnosticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlaygroundSessionDiagnosticsResponse from a JSON string
playground_session_diagnostics_response_instance = PlaygroundSessionDiagnosticsResponse.from_json(json)
# print the JSON string representation of the object
print(PlaygroundSessionDiagnosticsResponse.to_json())

# convert the object into a dict
playground_session_diagnostics_response_dict = playground_session_diagnostics_response_instance.to_dict()
# create an instance of PlaygroundSessionDiagnosticsResponse from a dict
playground_session_diagnostics_response_from_dict = PlaygroundSessionDiagnosticsResponse.from_dict(playground_session_diagnostics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


