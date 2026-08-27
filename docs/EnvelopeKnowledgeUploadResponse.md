# EnvelopeKnowledgeUploadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**KnowledgeUploadResponse**](KnowledgeUploadResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_knowledge_upload_response import EnvelopeKnowledgeUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeKnowledgeUploadResponse from a JSON string
envelope_knowledge_upload_response_instance = EnvelopeKnowledgeUploadResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeKnowledgeUploadResponse.to_json())

# convert the object into a dict
envelope_knowledge_upload_response_dict = envelope_knowledge_upload_response_instance.to_dict()
# create an instance of EnvelopeKnowledgeUploadResponse from a dict
envelope_knowledge_upload_response_from_dict = EnvelopeKnowledgeUploadResponse.from_dict(envelope_knowledge_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


