# EnvelopeListPlaygroundSessionTranscriptResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PlaygroundSessionTranscriptResponse]**](PlaygroundSessionTranscriptResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_list_playground_session_transcript_response import EnvelopeListPlaygroundSessionTranscriptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeListPlaygroundSessionTranscriptResponse from a JSON string
envelope_list_playground_session_transcript_response_instance = EnvelopeListPlaygroundSessionTranscriptResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeListPlaygroundSessionTranscriptResponse.to_json())

# convert the object into a dict
envelope_list_playground_session_transcript_response_dict = envelope_list_playground_session_transcript_response_instance.to_dict()
# create an instance of EnvelopeListPlaygroundSessionTranscriptResponse from a dict
envelope_list_playground_session_transcript_response_from_dict = EnvelopeListPlaygroundSessionTranscriptResponse.from_dict(envelope_list_playground_session_transcript_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


