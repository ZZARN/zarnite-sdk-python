# GuardrailsConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_languages** | **List[Optional[str]]** | Languages the agent is allowed to use when responding | [optional] [default to []]
**blocked_topics** | **List[Optional[str]]** | Topics the agent must never discuss | [optional] [default to []]
**max_response_length** | **int** | Maximum token count per response | [optional] 
**content_filters** | **List[Optional[str]]** | Content filter labels (e.g. profanity, pii) | [optional] [default to []]
**custom_rules** | **Dict[str, object]** | Freeform custom guardrail rules | [optional] 

## Example

```python
from zarnite.models.guardrails_config import GuardrailsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GuardrailsConfig from a JSON string
guardrails_config_instance = GuardrailsConfig.from_json(json)
# print the JSON string representation of the object
print(GuardrailsConfig.to_json())

# convert the object into a dict
guardrails_config_dict = guardrails_config_instance.to_dict()
# create an instance of GuardrailsConfig from a dict
guardrails_config_from_dict = GuardrailsConfig.from_dict(guardrails_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


