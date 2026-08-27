# LearnerCsvResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_rows** | **int** | Total rows in CSV | 
**imported** | **int** | Rows successfully imported | 
**failed** | **int** | Rows that failed | 
**rows** | [**List[LearnerCsvRow]**](LearnerCsvRow.md) | Per-row results | 

## Example

```python
from zarnite.models.learner_csv_result import LearnerCsvResult

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerCsvResult from a JSON string
learner_csv_result_instance = LearnerCsvResult.from_json(json)
# print the JSON string representation of the object
print(LearnerCsvResult.to_json())

# convert the object into a dict
learner_csv_result_dict = learner_csv_result_instance.to_dict()
# create an instance of LearnerCsvResult from a dict
learner_csv_result_from_dict = LearnerCsvResult.from_dict(learner_csv_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


