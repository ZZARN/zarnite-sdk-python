# MemorySearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kb_docs_retrieved** | **int** | Number of KB documents retrieved | 
**memory_docs_retrieved** | **int** | Number of memory documents retrieved | 
**context_tokens_used** | **int** | Estimated tokens used across KB and memory previews | 
**context_token_budget** | **int** | Maximum token budget for this tier | 
**pricing_tier** | **str** | Resolved pricing tier for the org | 
**effective_step_size** | **int** | Effective step size after tier resolution | 
**thread_scope_applied** | **bool** | Whether memory search was narrowed to the supplied thread_id | 
**resolved_thread_id** | **str** | thread_id that was actually applied to memory search, or null when user-level fallback was used | [optional] 
**kb_context_preview** | **str** | Preview of retrieved KB context (truncated) | 
**memory_context_preview** | **str** | Preview of retrieved memory context (truncated) | 
**kb_hits** | [**List[DocHit]**](DocHit.md) | Individual KB document hits with metadata | [optional] [default to []]
**memory_hits** | [**List[DocHit]**](DocHit.md) | Individual memory hits with metadata | [optional] [default to []]

## Example

```python
from zarnite.models.memory_search_response import MemorySearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MemorySearchResponse from a JSON string
memory_search_response_instance = MemorySearchResponse.from_json(json)
# print the JSON string representation of the object
print(MemorySearchResponse.to_json())

# convert the object into a dict
memory_search_response_dict = memory_search_response_instance.to_dict()
# create an instance of MemorySearchResponse from a dict
memory_search_response_from_dict = MemorySearchResponse.from_dict(memory_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


