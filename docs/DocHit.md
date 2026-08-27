# DocHit

A single document chunk retrieved during memory/KB search.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_file** | **str** | Source file name | [optional] 
**scope** | **str** | kb scope: agent or organization | [optional] 
**relevance_score** | **float** | Cosine similarity score (0-1, higher is better) | 
**preview** | **str** | Truncated document content | 
**metadata** | **Dict[str, object]** | Full chunk metadata | [optional] 

## Example

```python
from zarnite.models.doc_hit import DocHit

# TODO update the JSON string below
json = "{}"
# create an instance of DocHit from a JSON string
doc_hit_instance = DocHit.from_json(json)
# print the JSON string representation of the object
print(DocHit.to_json())

# convert the object into a dict
doc_hit_dict = doc_hit_instance.to_dict()
# create an instance of DocHit from a dict
doc_hit_from_dict = DocHit.from_dict(doc_hit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


