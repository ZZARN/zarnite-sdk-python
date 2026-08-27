# PlaygroundSessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Organization scope | 
**agent_id** | **str** | Agent to test | 
**mode** | **str** | Session mode: debug | eval | learner_live | [optional] [default to 'debug']
**playground** | **bool** | Whether this is a playground session | [optional] [default to True]
**learner_id** | **str** | Optional learner/user being simulated | [optional] 
**thread_id** | **str** | Optional conversation thread | [optional] 
**resume_session_id** | **str** | Optional prior session id to resume on the same thread | [optional] 
**language** | **str** | Session-level language override (e.g. English, French) | [optional] 
**voice** | [**PlaygroundVoiceConfigInput**](PlaygroundVoiceConfigInput.md) | Voice config | [optional] 
**client** | [**PlaygroundClientMeta**](PlaygroundClientMeta.md) | Client metadata | [optional] 

## Example

```python
from zarnite.models.playground_session_request import PlaygroundSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlaygroundSessionRequest from a JSON string
playground_session_request_instance = PlaygroundSessionRequest.from_json(json)
# print the JSON string representation of the object
print(PlaygroundSessionRequest.to_json())

# convert the object into a dict
playground_session_request_dict = playground_session_request_instance.to_dict()
# create an instance of PlaygroundSessionRequest from a dict
playground_session_request_from_dict = PlaygroundSessionRequest.from_dict(playground_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


