# MemorySearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** | Query to search against KB and memory | 
**org_id** | **str** | Organization scope | 
**agent_id** | **str** | Agent scope | 
**user_id** | **str** | User scope (enforced by RBAC for user role) | 
**thread_id** | **str** | Optional conversation/session identifier. When present, the API first searches memory summaries from that thread before falling back to user-level memory. | [optional] 
**step_size** | **int** | Retrieval step size override | [optional] 

## Example

```python
from zarnite.models.memory_search_request import MemorySearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MemorySearchRequest from a JSON string
memory_search_request_instance = MemorySearchRequest.from_json(json)
# print the JSON string representation of the object
print(MemorySearchRequest.to_json())

# convert the object into a dict
memory_search_request_dict = memory_search_request_instance.to_dict()
# create an instance of MemorySearchRequest from a dict
memory_search_request_from_dict = MemorySearchRequest.from_dict(memory_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


