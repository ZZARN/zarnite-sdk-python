# PlaygroundLatencyDiagnostics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_turn_latency_ms** | **float** | Average completed voice turn latency in milliseconds | [optional] 
**avg_rag_latency_ms** | **float** | Average RAG/tool lookup latency in milliseconds | [optional] 
**completed_turns** | **int** | Completed voice turn count included in the averages | [optional] [default to 0]
**rag_calls** | **int** | RAG/tool call count included in the averages | [optional] [default to 0]

## Example

```python
from zarnite.models.playground_latency_diagnostics import PlaygroundLatencyDiagnostics

# TODO update the JSON string below
json = "{}"
# create an instance of PlaygroundLatencyDiagnostics from a JSON string
playground_latency_diagnostics_instance = PlaygroundLatencyDiagnostics.from_json(json)
# print the JSON string representation of the object
print(PlaygroundLatencyDiagnostics.to_json())

# convert the object into a dict
playground_latency_diagnostics_dict = playground_latency_diagnostics_instance.to_dict()
# create an instance of PlaygroundLatencyDiagnostics from a dict
playground_latency_diagnostics_from_dict = PlaygroundLatencyDiagnostics.from_dict(playground_latency_diagnostics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


