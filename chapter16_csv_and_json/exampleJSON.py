import json

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)

pythonValue = {'isCat': True,'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
stringOfJsonData_new = json.dumps(pythonValue)
print(stringOfJsonData_new, '/n', stringOfJsonData)