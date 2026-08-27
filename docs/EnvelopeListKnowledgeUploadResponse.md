# EnvelopeListKnowledgeUploadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[KnowledgeUploadResponse]**](KnowledgeUploadResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_list_knowledge_upload_response import EnvelopeListKnowledgeUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeListKnowledgeUploadResponse from a JSON string
envelope_list_knowledge_upload_response_instance = EnvelopeListKnowledgeUploadResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeListKnowledgeUploadResponse.to_json())

# convert the object into a dict
envelope_list_knowledge_upload_response_dict = envelope_list_knowledge_upload_response_instance.to_dict()
# create an instance of EnvelopeListKnowledgeUploadResponse from a dict
envelope_list_knowledge_upload_response_from_dict = EnvelopeListKnowledgeUploadResponse.from_dict(envelope_list_knowledge_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


