# EnvelopeListKnowledgeDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[KnowledgeDocument]**](KnowledgeDocument.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_list_knowledge_document import EnvelopeListKnowledgeDocument

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeListKnowledgeDocument from a JSON string
envelope_list_knowledge_document_instance = EnvelopeListKnowledgeDocument.from_json(json)
# print the JSON string representation of the object
print(EnvelopeListKnowledgeDocument.to_json())

# convert the object into a dict
envelope_list_knowledge_document_dict = envelope_list_knowledge_document_instance.to_dict()
# create an instance of EnvelopeListKnowledgeDocument from a dict
envelope_list_knowledge_document_from_dict = EnvelopeListKnowledgeDocument.from_dict(envelope_list_knowledge_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


