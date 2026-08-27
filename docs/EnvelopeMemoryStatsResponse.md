# EnvelopeMemoryStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MemoryStatsResponse**](MemoryStatsResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_memory_stats_response import EnvelopeMemoryStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeMemoryStatsResponse from a JSON string
envelope_memory_stats_response_instance = EnvelopeMemoryStatsResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeMemoryStatsResponse.to_json())

# convert the object into a dict
envelope_memory_stats_response_dict = envelope_memory_stats_response_instance.to_dict()
# create an instance of EnvelopeMemoryStatsResponse from a dict
envelope_memory_stats_response_from_dict = EnvelopeMemoryStatsResponse.from_dict(envelope_memory_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


