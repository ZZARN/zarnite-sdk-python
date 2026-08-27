# EnvelopeLearnerCsvResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**LearnerCsvResult**](LearnerCsvResult.md) | Response payload | 
**meta** | [**Meta**](Meta.md) | Request metadata | 

## Example

```python
from zarnite.models.envelope_learner_csv_result import EnvelopeLearnerCsvResult

# TODO update the JSON string below
json = "{}"
# create an instance of EnvelopeLearnerCsvResult from a JSON string
envelope_learner_csv_result_instance = EnvelopeLearnerCsvResult.from_json(json)
# print the JSON string representation of the object
print(EnvelopeLearnerCsvResult.to_json())

# convert the object into a dict
envelope_learner_csv_result_dict = envelope_learner_csv_result_instance.to_dict()
# create an instance of EnvelopeLearnerCsvResult from a dict
envelope_learner_csv_result_from_dict = EnvelopeLearnerCsvResult.from_dict(envelope_learner_csv_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


