# OrgCreditWalletResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_id** | **str** | Organization scope | 
**month** | **str** | UTC month in YYYY-MM format | 
**included_credits** | **int** | Included monthly credits | 
**used_credits** | **int** | Used credits in the month | 
**remaining_credits** | **int** | Remaining credits in the month | 

## Example

```python
from zarnite.models.org_credit_wallet_response import OrgCreditWalletResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrgCreditWalletResponse from a JSON string
org_credit_wallet_response_instance = OrgCreditWalletResponse.from_json(json)
# print the JSON string representation of the object
print(OrgCreditWalletResponse.to_json())

# convert the object into a dict
org_credit_wallet_response_dict = org_credit_wallet_response_instance.to_dict()
# create an instance of OrgCreditWalletResponse from a dict
org_credit_wallet_response_from_dict = OrgCreditWalletResponse.from_dict(org_credit_wallet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


