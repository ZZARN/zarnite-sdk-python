# PlaygroundTranscriptMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Transcript speaker role | 
**content** | **str** | Transcript message content | 
**created_at** | **str** | Message timestamp | 

## Example

```python
from zarnite.models.playground_transcript_message import PlaygroundTranscriptMessage

# TODO update the JSON string below
json = "{}"
# create an instance of PlaygroundTranscriptMessage from a JSON string
playground_transcript_message_instance = PlaygroundTranscriptMessage.from_json(json)
# print the JSON string representation of the object
print(PlaygroundTranscriptMessage.to_json())

# convert the object into a dict
playground_transcript_message_dict = playground_transcript_message_instance.to_dict()
# create an instance of PlaygroundTranscriptMessage from a dict
playground_transcript_message_from_dict = PlaygroundTranscriptMessage.from_dict(playground_transcript_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


