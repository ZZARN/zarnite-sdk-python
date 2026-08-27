# LearnerCsvRow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**row** | **int** | CSV row number | 
**success** | **bool** | Whether the row was imported successfully | 
**learner_id** | **str** | Created learner ID | [optional] 
**error** | **str** | Error message if failed | [optional] 

## Example

```python
from zarnite.models.learner_csv_row import LearnerCsvRow

# TODO update the JSON string below
json = "{}"
# create an instance of LearnerCsvRow from a JSON string
learner_csv_row_instance = LearnerCsvRow.from_json(json)
# print the JSON string representation of the object
print(LearnerCsvRow.to_json())

# convert the object into a dict
learner_csv_row_dict = learner_csv_row_instance.to_dict()
# create an instance of LearnerCsvRow from a dict
learner_csv_row_from_dict = LearnerCsvRow.from_dict(learner_csv_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


