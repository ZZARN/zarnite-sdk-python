# EnvelopeOrgUserCategoryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrgUserCategoryResponse**](OrgUserCategoryResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_org_user_category_response import EnvelopeOrgUserCategoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeOrgUserCategoryResponse from a JSON string
envelope_org_user_category_response_instance = EnvelopeOrgUserCategoryResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeOrgUserCategoryResponse.to_json())

# convert the object into a dict
envelope_org_user_category_response_dict = envelope_org_user_category_response_instance.to_dict()
# create an instance of EnvelopeOrgUserCategoryResponse from a dict
envelope_org_user_category_response_from_dict = EnvelopeOrgUserCategoryResponse.from_dict(envelope_org_user_category_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


