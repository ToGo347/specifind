import json

from specifind import Specifind


s = Specifind(debug=False)


text = "Upupa epops is an exotic bird. It is widely extended over Spain."

preds = s.analyze(text, coref=True)
# preds = s.analyze_file("tests/fixtures/573_574BSEA44NBSharpiarubida.pdf", coref=True)

# ensure output is JSON serializable
print(json.dumps(preds, indent=4))
# print(preds)