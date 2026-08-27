# LearnerReinitiateResponse

Returned on reinitiation — contains the new one-time raw access key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Learner identifier | 
**org_id** | **str** | Organization scope | 
**name** | **str** | Learner name | 
**email** | **str** | Learner email | [optional] 
**learner_id** | **str** | External learner identifier | [optional] 
**status** | **str** | Learner status (always &#39;active&#39; after reinitiation) | 
**access_key** | **str** | New one-time raw access key — old key is immediately revoked | 
**access_key_prefix** | **str** | Key prefix for identification | 
**updated_at** | **datetime** | Last update timestamp | 

## Example

```python
from zarnite.models.learner_reinitiate_response import LearnerReinitiateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerReinitiateResponse from a JSON string
learner_reinitiate_response_instance = LearnerReinitiateResponse.from_json(json)
# print the JSON string representation of the object
print(LearnerReinitiateResponse.to_json())

# convert the object into a dict
learner_reinitiate_response_dict = learner_reinitiate_response_instance.to_dict()
# create an instance of LearnerReinitiateResponse from a dict
learner_reinitiate_response_from_dict = LearnerReinitiateResponse.from_dict(learner_reinitiate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


