"""
example of loads and dump
"""
# Example of loads
import json

json_string = """
{"a":1, "b":2,"c":3}"""

print(type(json_string))

json_string_obj = json.loads(json_string)
print(json_string_obj)
print(type(json_string_obj))


