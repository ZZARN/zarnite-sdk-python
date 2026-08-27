# UserTopicsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topics** | **List[Dict[str, object]]** | List of recent conversation topics | 

## Example

```python
from zarnite.models.user_topics_response import UserTopicsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserTopicsResponse from a JSON string
user_topics_response_instance = UserTopicsResponse.from_json(json)
# print the JSON string representation of the object
print(UserTopicsResponse.to_json())

# convert the object into a dict
user_topics_response_dict = user_topics_response_instance.to_dict()
# create an instance of UserTopicsResponse from a dict
user_topics_response_from_dict = UserTopicsResponse.from_dict(user_topics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


