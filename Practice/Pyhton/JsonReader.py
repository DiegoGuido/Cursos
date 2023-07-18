import json

docentes = open('docentes.json')

docentes = json.loads(docentes.read())
print(docentes)