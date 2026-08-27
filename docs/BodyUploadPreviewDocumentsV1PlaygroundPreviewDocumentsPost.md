# BodyUploadPreviewDocumentsV1PlaygroundPreviewDocumentsPost


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** |  | 
**preview_agent_id** | **str** |  | 
**files** | **List[bytes]** |  | 
**user_id** | **str** |  | [optional] 

## Example

```python
from zarnite.models.body_upload_preview_documents_v1_playground_preview_documents_post import BodyUploadPreviewDocumentsV1PlaygroundPreviewDocumentsPost

# TODO update the JSON string below
json = "{}"
# create an instance of BodyUploadPreviewDocumentsV1PlaygroundPreviewDocumentsPost from a JSON string
body_upload_preview_documents_v1_playground_preview_documents_post_instance = BodyUploadPreviewDocumentsV1PlaygroundPreviewDocumentsPost.from_json(json)
# print the JSON string representation of the object
print(BodyUploadPreviewDocumentsV1PlaygroundPreviewDocumentsPost.to_json())

# convert the object into a dict
body_upload_preview_documents_v1_playground_preview_documents_post_dict = body_upload_preview_documents_v1_playground_preview_documents_post_instance.to_dict()
# create an instance of BodyUploadPreviewDocumentsV1PlaygroundPreviewDocumentsPost from a dict
body_upload_preview_documents_v1_playground_preview_documents_post_from_dict = BodyUploadPreviewDocumentsV1PlaygroundPreviewDocumentsPost.from_dict(body_upload_preview_documents_v1_playground_preview_documents_post_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


