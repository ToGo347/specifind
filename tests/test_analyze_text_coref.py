import json


def test_specifind_analyze(specifind_session):
	text = "Alytes muletensis and Upupa epops are crazy species. They live all around Mallorca."

	preds = specifind_session.analyze(text, coref=True)

	expected = {
		"species": [
			"Alytes muletensis",
			"Upupa epops"
		],
		"geography": [
			"Mallorca"
		],
		"occurrences": {
			"Upupa epops": [
				"Mallorca"
			],
			"Alytes muletensis": [
				"Mallorca"
			]
		},
		"evidence": {
			"Upupa epops": {
				"Mallorca": [
					"They live all around Mallorca."
				]
			},
			"Alytes muletensis": {
				"Mallorca": [
					"They live all around Mallorca."
				]
			}
		}
	}

	assert preds == expected, f"\nExpected:\n{json.dumps(expected, indent=2)}\n\nGot:\n{json.dumps(preds, indent=2)}"

