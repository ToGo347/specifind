<p align="center">
  <img alt="Specifind logo" src="https://raw.githubusercontent.com/ToGo347/specifind/refs/heads/master/specifind_logo.png" />
</p>

**Specifind** is a Python toolkit built to automatically extract **species occurrence information** from unstructured ecological literature. It identifies scientific species names, geographic entities, and the relations connecting them—unlocking occurrence data hidden in text.

The toolkit integrates **OCR**, **layout analysis**, **Named Entity Recognition**, **Coreference Resolution**, and **Relation Extraction** into a unified and traceable pipeline. It is powered by a newly developed, expertly annotated dataset of 1,000+ ecological abstracts spanning **biogeography, botany, entomology, mycology, and zoology**.

---
## 🌿 Key Features

* 📄 **Science-OCR** for domain-optimized OCR of scientific papers
* 🔍 **NER** for scientific species names & geographic entities
* 🌍 **Relation Extraction** connecting species to locations
* 🧠 **FastCOREF** for high-performance coreference resolution
* 🧩 **Built on spaCy** for extensibility, speed, and NLP interoperability
* 🧱 Full pipeline for **text & PDF** extraction
* 🧭 **Traceability** that links extractions back to the original text

---

## 📦 Installation

```bash
pip install specifind
```

---

## 🚀 Quick Start

### **Basic Usage**

```python
from specifind import Specifind

s = Specifind()

s.analyze("Upupa epops is an exotic bird. It is widely extended over Spain.")

# or

s.analyze_file("path/to/file.pdf")

# Output:
# {
#     "species": [
#         "Upupa epops"
#     ],
#     "geography": [
#         "Spain"
#     ],
#     "occurrences": {
#         "Upupa epops": [
#             "Spain"
#         ]
#     },
#     "evidence": {
#         "Upupa epops": {
#             "Spain": [
#                 "It is widely extended over Spain."
#             ]
#         }
#     }
# }
```

### **R Example (via reticulate)**

```bash
python3.11 -m venv venv
source venv/bin/activate
```

**Install Specifind**
```bash
pip install --upgrade pip
pip install specifind
```

**Open R, load the reticulate library and configure the virtual environment.**
```R
# Load reticulate package
library(reticulate)
use_virtualenv("venv", required = TRUE)
```

**Import Specifind and run the analysis.**
```R
# Import the Specifind class
Specifind <- import("specifind")$Specifind

# Create an instance
s <- Specifind(use_gpu=TRUE)

# Option A: Run the analysis on a text string
text <- "Upupa epops is an exotic bird. It is widely extended over Spain."
result <- s$analyze(text, coref = TRUE, return_doc = FALSE)

# Option B: Run analysis on a PDF file
result <- s$analyze_file("path/to/document.pdf", coref = TRUE, dpi = 96L)
```

---

## 📘 API Reference
### `class Specifind(...)`

Initializes the OCR engine.

| Parameter | Type | Default | Description                                                                                                                                  |
|-----------|------|---------|----------------------------------------------------------------------------------------------------------------------------------------------|
| use_gpu   | bool | True    | If `True`, uses GPU if available. If `False`, forces CPU usage, which may be slower but more stable on some systems and avoid memory issues. |
| debug     | bool | False   | If `True`, opens the displaCy visualizer with the results                                                                                    |

### `analyze_file(...)`

Process and extract information from a **PDF file**.

**Parameters**

| Name         | Type | Default                          | Description                                                                                            |
|--------------| ---- |----------------------------------|--------------------------------------------------------------------------------------------------------|
| `path`       | str  | —                                | Path to the file to analyze.                                                                           |
| `first_page` | int  | 0                                | First page to process (inclusive).                                                                     |
| `last_page`  | int  | PDF page length                  | Last page to process (exclusive).                                                                      |
| `coref`      | bool | True                             | Enable coreference resolution.                                                                         |
| `dpi`        | int  | `192` if GPU available else `96` | Rendering DPI for PDF pages. Consider lowering the value if running out of memory (OOM).               |
| `return_doc` | bool | False                            | If `True`, return Spacy Doc object with the annotations available in `doc.ents` and `doc._.relations`. |
| `store_ocr`  | bool | True                             | If `True`, saves OCR results into a txt file                                                           |

**Returns**

* Dictionary including parsed entities, relations and evidences.
* *(optional)* internal doc object (if `return_doc=True`)

---

### `analyze(...)`

Process and extract information directly from **raw text**.

**Parameters**

| Name         | Type | Default | Description                                              |
| ------------ | ---- | ------- |----------------------------------------------------------|
| `text`       | str  | —       | Raw text to analyze.                                     |
| `coref`      | bool | True    | Enable coreference resolution.                           |
| `return_doc` | bool | False   | If `True`, return Spacy Doc object with the annotations. |

**Returns**

* Dictionary including parsed entities, relations and evidences.
* *(optional)* internal doc object

---

## 🚀 **Benchmarks**

### **Named Entity Recognition (NER)**

*Species & Locations*

| 🔍 Match Type         | 🎯 Precision | 📈 Recall | 🏆 F1 |
| --------------------- | ------------ | --------- | ----- |
| **Exact**             | 0.904        | 0.935     | 0.919 |
| **Partial/Intersect** | 0.938        | 0.969     | 0.958 |

---

### **Relation Extraction (RE)**

*Occurrences*

| 🎯 Precision | 📈 Recall | 🏆 F1 |
| ------------ | --------- | ----- |
| 0.964        | 0.993     | 0.978 |


---

## 🤝 Contributing

Contributions, issue reports, and feature suggestions are welcome.
Feel free to open a Pull Request or discussion.

---

## 📄 License

**Specifind** is licensed under **AGPL-3.0**. See [LICENSE](LICENSE) for details.

---

## 📚 Citing **Specifind**

If you use **Specifind** in your research, please cite our pre-print:

### APA
Tomas, G. D., Josep, F. A., Anna, D., María, B., Alejandro, R., Noemi, C., & Tommaso, C. (2025). *Specifind: A Natural Language Processing Tool for Automating Species Occurrence (Re-) Discovery from Scientific Literature*. bioRxiv, 2025-12.

### BibTeX

```bibtex
@article{specifind2025,
  title   = {Specifind: A Natural Language Processing Tool for Automating Species Occurrence (Re-)Discovery from Scientific Literature},
  author  = {Golomb Durán Tomás, Díaz Anna, Barroso María, Far Antoni Josep, Roldán Alejandro, Cancellario Tommaso},
  year    = {2025},
  journal = {BioRxiv},
  url     = {https://doi.org/10.64898/2025.12.24.696373}
}
```
