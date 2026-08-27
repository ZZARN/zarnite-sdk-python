# LearnerCreateResponse

Returned only on creation — contains the one-time raw access key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Learner identifier | 
**org_id** | **str** | Organization scope | 
**name** | **str** | Learner name | 
**email** | **str** | Learner email | [optional] 
**learner_id** | **str** | External learner identifier | [optional] 
**status** | **str** | Learner status | 
**access_key** | **str** | One-time raw access key — shown only on creation, never retrievable again | 
**access_key_prefix** | **str** | Key prefix for identification (e.g. &#39;zrn_lrn_&#39;) | 
**created_at** | **datetime** | Creation timestamp | 
**updated_at** | **datetime** | Last update timestamp | 

## Example

```python
from zarnite.models.learner_create_response import LearnerCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerCreateResponse from a JSON string
learner_create_response_instance = LearnerCreateResponse.from_json(json)
# print the JSON string representation of the object
print(LearnerCreateResponse.to_json())

# convert the object into a dict
learner_create_response_dict = learner_create_response_instance.to_dict()
# create an instance of LearnerCreateResponse from a dict
learner_create_response_from_dict = LearnerCreateResponse.from_dict(learner_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


