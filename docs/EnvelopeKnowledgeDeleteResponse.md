# EnvelopeKnowledgeDeleteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**KnowledgeDeleteResponse**](KnowledgeDeleteResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_knowledge_delete_response import EnvelopeKnowledgeDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeKnowledgeDeleteResponse from a JSON string
envelope_knowledge_delete_response_instance = EnvelopeKnowledgeDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeKnowledgeDeleteResponse.to_json())

# convert the object into a dict
envelope_knowledge_delete_response_dict = envelope_knowledge_delete_response_instance.to_dict()
# create an instance of EnvelopeKnowledgeDeleteResponse from a dict
envelope_knowledge_delete_response_from_dict = EnvelopeKnowledgeDeleteResponse.from_dict(envelope_knowledge_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


