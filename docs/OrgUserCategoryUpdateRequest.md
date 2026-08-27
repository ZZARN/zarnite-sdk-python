# OrgUserCategoryUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Per-user routing category override | 

## Example

```python
from zarnite.models.org_user_category_update_request import OrgUserCategoryUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrgUserCategoryUpdateRequest from a JSON string
org_user_category_update_request_instance = OrgUserCategoryUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(OrgUserCategoryUpdateRequest.to_json())

# convert the object into a dict
org_user_category_update_request_dict = org_user_category_update_request_instance.to_dict()
# create an instance of OrgUserCategoryUpdateRequest from a dict
org_user_category_update_request_from_dict = OrgUserCategoryUpdateRequest.from_dict(org_user_category_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


