# PlaygroundSessionTranscriptResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** | Voice session identifier | 
**thread_id** | **str** | Conversation thread identifier | 
**session_kind** | **str** | Session classification | 
**status** | **str** | Current session status | 
**started_at** | **str** | Session start time | [optional] 
**ended_at** | **str** | Session end time | [optional] 
**last_activity_at** | **str** | Most recent activity time | [optional] 
**livekit_room_name** | **str** | LiveKit room backing the session | [optional] 
**messages** | [**List[PlaygroundTranscriptMessage]**](PlaygroundTranscriptMessage.md) | Ordered transcript messages for the session | [optional] [default to []]

## Example

```python
from zarnite.models.playground_session_transcript_response import PlaygroundSessionTranscriptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlaygroundSessionTranscriptResponse from a JSON string
playground_session_transcript_response_instance = PlaygroundSessionTranscriptResponse.from_json(json)
# print the JSON string representation of the object
print(PlaygroundSessionTranscriptResponse.to_json())

# convert the object into a dict
playground_session_transcript_response_dict = playground_session_transcript_response_instance.to_dict()
# create an instance of PlaygroundSessionTranscriptResponse from a dict
playground_session_transcript_response_from_dict = PlaygroundSessionTranscriptResponse.from_dict(playground_session_transcript_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


