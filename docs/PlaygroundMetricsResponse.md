# PlaygroundMetricsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Session identifier | 
**session_kind** | **str** | Session classification | 
**status** | **str** | Current session status | 
**duration_s** | **float** | Session duration in seconds | [optional] 
**total_events** | **int** | Total events recorded | 
**events** | [**List[PlaygroundMetricsEvent]**](PlaygroundMetricsEvent.md) | Session events (latency, STT/TTS, etc.) | [optional] [default to []]

## Example

```python
from zarnite.models.playground_metrics_response import PlaygroundMetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlaygroundMetricsResponse from a JSON string
playground_metrics_response_instance = PlaygroundMetricsResponse.from_json(json)
# print the JSON string representation of the object
print(PlaygroundMetricsResponse.to_json())

# convert the object into a dict
playground_metrics_response_dict = playground_metrics_response_instance.to_dict()
# create an instance of PlaygroundMetricsResponse from a dict
playground_metrics_response_from_dict = PlaygroundMetricsResponse.from_dict(playground_metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


