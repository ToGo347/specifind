import json
from pathlib import Path

def test_specifind_analyze_file(specifind_session):
	preds = specifind_session.analyze_file(
		str(Path(__file__).parent / "fixtures" / "573_574BSEA44NBSharpiarubida.pdf"),
		coref=True,
	)
	print(json.dumps(preds, indent=2))
