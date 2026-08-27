# KnowledgeDocument

A single knowledge base document (represents a group of chunks from one file).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Stable identifier for this document (derived from source_file + scope) | 
**source_file** | **str** | Original uploaded filename | 
**scope** | **str** | Whether this document belongs to an agent KB or org-wide KB | 
**org_id** | **str** | Organization scope | 
**agent_id** | **str** | Agent scope (null for org-wide documents) | [optional] 
**chunk_count** | **int** | Number of vector chunks stored for this document | 
**uploaded_by** | **str** | User who uploaded this document | [optional] 
**created_at** | **str** | Earliest chunk creation time (approximate upload time) | [optional] 

## Example

```python
from zarnite.models.knowledge_document import KnowledgeDocument

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeDocument from a JSON string
knowledge_document_instance = KnowledgeDocument.from_json(json)
# print the JSON string representation of the object
print(KnowledgeDocument.to_json())

# convert the object into a dict
knowledge_document_dict = knowledge_document_instance.to_dict()
# create an instance of KnowledgeDocument from a dict
knowledge_document_from_dict = KnowledgeDocument.from_dict(knowledge_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


