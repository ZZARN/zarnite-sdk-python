# EnvelopeMemorySearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**MemorySearchResponse**](MemorySearchResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_memory_search_response import EnvelopeMemorySearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeMemorySearchResponse from a JSON string
envelope_memory_search_response_instance = EnvelopeMemorySearchResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeMemorySearchResponse.to_json())

# convert the object into a dict
envelope_memory_search_response_dict = envelope_memory_search_response_instance.to_dict()
# create an instance of EnvelopeMemorySearchResponse from a dict
envelope_memory_search_response_from_dict = EnvelopeMemorySearchResponse.from_dict(envelope_memory_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


