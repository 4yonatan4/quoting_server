import json


# Example input
# {
#   "term”: 10,
#   "coverage”: 250000,
#   "age”: 25,
#   "height: "5 ft 1”,
#   "weight”: 160
# }

def parse_json(json_file):
    height = json_file["height"]
    height_foot, height_inch = height.split()[0], height.split()[2]
    json_file["height_foot"], json_file["height_inch"] = height_foot, height_inch
    del json_file["height"]
    return json_file


json_file_input = {
    "term": 10,
    "coverage": 250000,
    "age": 25,
    "height": "5 ft 1",
    "weight": 160
}

parsed = parse_json(json_file_input)
print(parsed)
