# OrgCreditWalletUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grant_credits** | **int** | Monthly included credits for the active month | 

## Example

```python
from zarnite.models.org_credit_wallet_update_request import OrgCreditWalletUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrgCreditWalletUpdateRequest from a JSON string
org_credit_wallet_update_request_instance = OrgCreditWalletUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(OrgCreditWalletUpdateRequest.to_json())

# convert the object into a dict
org_credit_wallet_update_request_dict = org_credit_wallet_update_request_instance.to_dict()
# create an instance of OrgCreditWalletUpdateRequest from a dict
org_credit_wallet_update_request_from_dict = OrgCreditWalletUpdateRequest.from_dict(org_credit_wallet_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


