# EnvelopeListUsageLogEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UsageLogEntry]**](UsageLogEntry.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_list_usage_log_entry import EnvelopeListUsageLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeListUsageLogEntry from a JSON string
envelope_list_usage_log_entry_instance = EnvelopeListUsageLogEntry.from_json(json)
# print the JSON string representation of the object
print(EnvelopeListUsageLogEntry.to_json())

# convert the object into a dict
envelope_list_usage_log_entry_dict = envelope_list_usage_log_entry_instance.to_dict()
# create an instance of EnvelopeListUsageLogEntry from a dict
envelope_list_usage_log_entry_from_dict = EnvelopeListUsageLogEntry.from_dict(envelope_list_usage_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


