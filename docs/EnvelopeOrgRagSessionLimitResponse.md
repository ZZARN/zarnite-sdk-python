# EnvelopeOrgRagSessionLimitResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OrgRagSessionLimitResponse**](OrgRagSessionLimitResponse.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_org_rag_session_limit_response import EnvelopeOrgRagSessionLimitResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeOrgRagSessionLimitResponse from a JSON string
envelope_org_rag_session_limit_response_instance = EnvelopeOrgRagSessionLimitResponse.from_json(json)
# print the JSON string representation of the object
print(EnvelopeOrgRagSessionLimitResponse.to_json())

# convert the object into a dict
envelope_org_rag_session_limit_response_dict = envelope_org_rag_session_limit_response_instance.to_dict()
# create an instance of EnvelopeOrgRagSessionLimitResponse from a dict
envelope_org_rag_session_limit_response_from_dict = EnvelopeOrgRagSessionLimitResponse.from_dict(envelope_org_rag_session_limit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


