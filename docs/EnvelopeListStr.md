# EnvelopeListStr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[str]** | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_list_str import EnvelopeListStr

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeListStr from a JSON string
envelope_list_str_instance = EnvelopeListStr.from_json(json)
# print the JSON string representation of the object
print(EnvelopeListStr.to_json())

# convert the object into a dict
envelope_list_str_dict = envelope_list_str_instance.to_dict()
# create an instance of EnvelopeListStr from a dict
envelope_list_str_from_dict = EnvelopeListStr.from_dict(envelope_list_str_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


