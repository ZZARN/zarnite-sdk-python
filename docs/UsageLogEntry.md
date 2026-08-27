# UsageLogEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Usage log entry ID | 
**agent_id** | **str** | Agent that generated usage | 
**user_id** | **str** | User who triggered the request | 
**endpoint** | **str** | API endpoint that generated usage | 
**tokens_used** | **int** | Tokens consumed | 
**created_at** | **datetime** | Timestamp of the usage event | 

## Example

```python
from zarnite.models.usage_log_entry import UsageLogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of UsageLogEntry from a JSON string
usage_log_entry_instance = UsageLogEntry.from_json(json)
# print the JSON string representation of the object
print(UsageLogEntry.to_json())

# convert the object into a dict
usage_log_entry_dict = usage_log_entry_instance.to_dict()
# create an instance of UsageLogEntry from a dict
usage_log_entry_from_dict = UsageLogEntry.from_dict(usage_log_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


