# KnowledgeDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | Deleted document identifier | 
**chunks_deleted** | **int** | Number of vector chunks removed | 
**deleted** | **bool** | Deletion result | [optional] [default to True]

## Example

```python
from zarnite.models.knowledge_delete_response import KnowledgeDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeDeleteResponse from a JSON string
knowledge_delete_response_instance = KnowledgeDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(KnowledgeDeleteResponse.to_json())

# convert the object into a dict
knowledge_delete_response_dict = knowledge_delete_response_instance.to_dict()
# create an instance of KnowledgeDeleteResponse from a dict
knowledge_delete_response_from_dict = KnowledgeDeleteResponse.from_dict(knowledge_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


