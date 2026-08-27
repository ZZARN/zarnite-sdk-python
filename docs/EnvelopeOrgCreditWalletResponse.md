# EnvelopeOrgCreditWalletResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrgCreditWalletResponse**](OrgCreditWalletResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_org_credit_wallet_response import EnvelopeOrgCreditWalletResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeOrgCreditWalletResponse from a JSON string
envelope_org_credit_wallet_response_instance = EnvelopeOrgCreditWalletResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeOrgCreditWalletResponse.to_json())

# convert the object into a dict
envelope_org_credit_wallet_response_dict = envelope_org_credit_wallet_response_instance.to_dict()
# create an instance of EnvelopeOrgCreditWalletResponse from a dict
envelope_org_credit_wallet_response_from_dict = EnvelopeOrgCreditWalletResponse.from_dict(envelope_org_credit_wallet_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


