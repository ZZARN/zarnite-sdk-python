# ScoreBreakdown


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engagement** | **int** | Session engagement score (0-100) | 
**complexity** | **int** | Language complexity score (0-100) | 
**depth** | **int** | Conversation depth score (0-100) | 
**recency** | **int** | Recency bonus score (0-100) | 

## Example

```python
from zarnite.models.score_breakdown import ScoreBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of ScoreBreakdown from a JSON string
score_breakdown_instance = ScoreBreakdown.from_json(json)
# print the JSON string representation of the object
print(ScoreBreakdown.to_json())

# convert the object into a dict
score_breakdown_dict = score_breakdown_instance.to_dict()
# create an instance of ScoreBreakdown from a dict
score_breakdown_from_dict = ScoreBreakdown.from_dict(score_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


