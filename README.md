# **An Approach to Capture Attack Descriptions via a Controlled Natural Language**

This repository contains the implementation of a translation pipeline that takes cyber attack descriptions written in a **Controlled Natural Language (CNL)** and produces a formal attack model (Petri Net) of the described attack. The CNL is focused on describing attacks from the system's perspective in a structured, machine-readable form, addressing the gaps and ambiguities in existing threat intelligence formats. The parsed description is translated into a _Technique Model_ that preserves the described attack features, and is used to formally model the system behavior under attack as a Petri Net.

## Translation Pipeline Architecture

```
CNL text
   |  ANTLR4 lexer + parser
   v
Parse tree
   |  Visitor  (produces a raw dictionary)
   v
Raw string dictionary
   |  Translator  (typed construction + reference resolution)
   v
Technique Model
   |  PetriNetBuilder  (downstream modeling via pm4py)
   v
Petri net
```

Each artifact produced by each stage, is stored separately, in different formats. The CNL text and Parse Tree in TXT, the raw string dictionary and Technique Model in JSON, and the Petri net in PNML and SVG (its graphical representation).


## Requirements

- Python 3.12
- [Graphviz](https://graphviz.org/) system package (required by pm4py for Petri net visualization)
- Python dependencies in `requirements.txt`

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate 
pip install -r requirements.txt
```


## Usage

### Command line

Run the pipeline on a description file in `data/example_descriptions/`. From the repository root, run:

```bash
python -m main content_injection.txt
```

Optional flags:

- `--validate` structurally compares the CNL-produced Technique Model against its expert-built reference Technique Model
- `--build_domain` builds and visualizes the reference model's Petri net

```bash
python -m main lsass_memory.txt --validate --build_domain
```

Generated Petri nets (PNML + SVG) are written to `data/generated_petri_nets/`, parse trees to `data/parse_trees/`, and logs to `logs/`.

### Web app

The Streamlit app lets you type a CNL description and see the resulting Petri net, along with any grammar and translation errors if parsing fails:

```bash
streamlit run web_app.py
```

### Regenerating the parser

Editing `CNL.g4` requires the ANTLR4 tool itself. To install ANTLR4, follow the [official getting started guide](https://github.com/antlr/antlr4/blob/master/doc/getting-started.md).

Once ANTLR4 is installed, regenerate the Python lexer and parser (targeting Python 3) after any grammar change, following the command:

```bash
antlr4 -Dlanguage=Python3 CNL.g4
```
To generate the visitor, simply run the same command with the flag `-visitor` as such:
```bash
antlr4 -Dlanguage=Python3 -visitor CNL.g4
```

## License

Apache License 2.0. See [LICENSE](LICENSE).
