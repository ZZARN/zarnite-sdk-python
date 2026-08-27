# EnvelopePlaygroundMetricsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PlaygroundMetricsResponse**](PlaygroundMetricsResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_playground_metrics_response import EnvelopePlaygroundMetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopePlaygroundMetricsResponse from a JSON string
envelope_playground_metrics_response_instance = EnvelopePlaygroundMetricsResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopePlaygroundMetricsResponse.to_json())

# convert the object into a dict
envelope_playground_metrics_response_dict = envelope_playground_metrics_response_instance.to_dict()
# create an instance of EnvelopePlaygroundMetricsResponse from a dict
envelope_playground_metrics_response_from_dict = EnvelopePlaygroundMetricsResponse.from_dict(envelope_playground_metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


