# PlaygroundMetricsEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Event row ID | 
**event_type** | **str** | Event type (stt_complete, tts_complete, etc.) | 
**payload** | **Dict[str, object]** | Event payload | [optional] 
**created_at** | **str** | Event timestamp | 

## Example

```python
from zarnite.models.playground_metrics_event import PlaygroundMetricsEvent

# TODO update the JSON string below
json = "{}"
# create an instance of PlaygroundMetricsEvent from a JSON string
playground_metrics_event_instance = PlaygroundMetricsEvent.from_json(json)
# print the JSON string representation of the object
print(PlaygroundMetricsEvent.to_json())

# convert the object into a dict
playground_metrics_event_dict = playground_metrics_event_instance.to_dict()
# create an instance of PlaygroundMetricsEvent from a dict
playground_metrics_event_from_dict = PlaygroundMetricsEvent.from_dict(playground_metrics_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


