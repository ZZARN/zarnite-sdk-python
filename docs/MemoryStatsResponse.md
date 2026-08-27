# MemoryStatsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Organization scope | 
**agent_id** | **str** | Agent scope | 
**kb_doc_count** | **int** | Total KB documents reachable by this org/agent, including org-wide KB | 
**memory_doc_count** | **int** | Total memory documents for this org/agent | 

## Example

```python
from zarnite.models.memory_stats_response import MemoryStatsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryStatsResponse from a JSON string
memory_stats_response_instance = MemoryStatsResponse.from_json(json)
# print the JSON string representation of the object
print(MemoryStatsResponse.to_json())

# convert the object into a dict
memory_stats_response_dict = memory_stats_response_instance.to_dict()
# create an instance of MemoryStatsResponse from a dict
memory_stats_response_from_dict = MemoryStatsResponse.from_dict(memory_stats_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


