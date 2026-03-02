# AI-Based Automated UML Diagram Generator

An AI-powered system that automatically converts Software Requirement
Specification (SRS) documents into UML Class Diagrams using Natural
Language Processing (NLP) and Machine Learning techniques.

------------------------------------------------------------------------

# Project Overview

The **AI-Based Automated UML Diagram Generator** is designed to reduce
manual effort in software design documentation by automatically
analyzing SRS documents and generating UML diagrams.

## Objectives

The system aims to:

1.  Automatically preprocess SRS documents.
2.  Perform syntactic and semantic analysis.
3.  Identify UML-relevant components.
4.  Classify relationships (association, aggregation, inheritance).
5.  Generate UML diagrams in standard formats (PlantUML, XML).
6.  Provide confidence score for each generated component.
7.  Allow human-in-the-loop corrections.

------------------------------------------------------------------------

# System Architecture

    SRS Input
       ↓
    Preprocessing (Cleaning + Tokenization)
       ↓
    NLP Analysis (POS Tagging + Dependency Parsing)
       ↓
    UML Component Extraction
       ↓
    Relationship Classification + Confidence Scoring
       ↓
    Human Feedback Module
       ↓
    Diagram Generation (PlantUML + XML)

------------------------------------------------------------------------

# Features

-   Automatic SRS preprocessing
-   Syntactic & semantic analysis using spaCy
-   Class detection from noun phrases
-   Relationship classification
-   Confidence scoring system
-   Human-in-the-loop correction mechanism
-   Export to PlantUML (.puml) and XML (.xml)

------------------------------------------------------------------------

# Tech Stack

-   Python 3.10+
-   spaCy
-   scikit-learn
-   lxml
-   PlantUML
-   NumPy

------------------------------------------------------------------------

# Project Structure

    UML-Gen/
    │
    ├── main.py
    ├── requirements.txt
    ├── README.md
    ├── output.puml
    ├── output.xml
    └── models/

------------------------------------------------------------------------

# Installation Guide

``` bash
git clone https://github.com/Itshardtofindagoodname/UML-Gen.git
cd UML-Gen
python -m venv venv
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

------------------------------------------------------------------------

# Running the Project

``` bash
python main.py
```

------------------------------------------------------------------------

# Output

-   output.puml → PlantUML diagram file\
-   output.xml → UML structured XML file

------------------------------------------------------------------------

# License

This project is intended for academic and research purposes.
