# KnowledgeUploadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Upload outcome | 
**scope** | **str** | Knowledge base scope that received the file | 
**org_id** | **str** | Organization scope | 
**agent_id** | **str** | Agent scope when uploading to an agent KB | [optional] 
**kb_target_agent_id** | **str** | Agent identifier actually stored in KB metadata | 
**user_id** | **str** | Optional user attribution stored on uploaded chunks | [optional] 
**file** | **str** | Uploaded filename | 
**chunks_indexed** | **int** | Number of chunks inserted into the vector store | 
**chunk_limit_applied** | **bool** | Whether upload chunk cap truncated the document | 

## Example

```python
from zarnite.models.knowledge_upload_response import KnowledgeUploadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeUploadResponse from a JSON string
knowledge_upload_response_instance = KnowledgeUploadResponse.from_json(json)
# print the JSON string representation of the object
print(KnowledgeUploadResponse.to_json())

# convert the object into a dict
knowledge_upload_response_dict = knowledge_upload_response_instance.to_dict()
# create an instance of KnowledgeUploadResponse from a dict
knowledge_upload_response_from_dict = KnowledgeUploadResponse.from_dict(knowledge_upload_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


