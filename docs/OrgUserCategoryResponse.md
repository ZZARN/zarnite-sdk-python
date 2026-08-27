# OrgUserCategoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Organization scope | 
**user_id** | **str** | User scope | 
**category** | **str** | Effective user category | 
**source** | **str** | Category source (user_override|org_default) | 

## Example

```python
from zarnite.models.org_user_category_response import OrgUserCategoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrgUserCategoryResponse from a JSON string
org_user_category_response_instance = OrgUserCategoryResponse.from_json(json)
# print the JSON string representation of the object
print(OrgUserCategoryResponse.to_json())

# convert the object into a dict
org_user_category_response_dict = org_user_category_response_instance.to_dict()
# create an instance of OrgUserCategoryResponse from a dict
org_user_category_response_from_dict = OrgUserCategoryResponse.from_dict(org_user_category_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


