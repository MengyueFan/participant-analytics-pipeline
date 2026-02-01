# Participant Analytics Pipeline

## Overview

This repository presents a Python-based analytics pipeline designed to extract structured insights from real-world participant data. The project integrates **geospatial analysis** and **free-text occupation classification** to produce country-level and employment-sector statistics from noisy, unstructured inputs.

The work follows both **academic research standards** (clarity, reproducibility, interpretability) and **engineering best practices** (modular design, error handling, scalability awareness).

---

## Project Components

### 1. Geolocation → Country Inference

Participants’ latitude and longitude coordinates are converted into country-level labels using reverse geocoding.

**Key steps:**
* Parse raw coordinate pairs
* Perform reverse geocoding via OpenStreetMap Nominatim (GeoPy)
* Handle missing values, API failures, and ambiguous locations
* Apply request throttling to comply with API usage policies
* Aggregate country frequencies and percentage distributions

**Output:**
* Country label per participant
* Top-country statistics and cumulative distribution metrics

---

### 2. Occupation Classification from Free-Text Responses
Participants’ self-reported job titles are classified into standardized employment sectors.

The input text contains:

* Inconsistent formatting and capitalization
* Misspellings and abbreviations
* Mixed seniority levels (e.g., assistant vs director)
* Multilingual and compound job descriptions

To address this, a **rule-based text classification system** was developed.

**Key techniques:**
* Text normalization and missing-value handling
* Keyword-to-sector mapping using configurable dictionaries
* Regex-based word-boundary matching to reduce false positives
* Priority rules for specific roles (e.g., students, PhD researchers)
* Context-aware handling of management titles, distinguishing executive roles from technical managers
* Fallback classification for ambiguous cases

**Output:**
* Sector label per job title
* Sector-level frequency counts and percentage statistics

---

## Why Rule-Based Instead of Machine Learning?
This project intentionally uses a rule-based approach rather than a black-box ML model:

* Ensures **full interpretability** of classification decisions
* Performs robustly on small-to-medium datasets
* Avoids training-data bias in highly heterogeneous job titles
* Aligns with common practices in academic, policy, and government research

The design can be extended to supervised or hybrid NLP models if required.

---

## Technologies Used
* **Python**
* **GeoPy / OpenStreetMap Nominatim** (reverse geocoding)
* **Pandas** (data manipulation and aggregation)
* **Regular Expressions (re)** (text pattern matching)
* **Collections / Counter** (statistical summaries)

---

## Reproducibility & Structure
* Deterministic rule-based logic (no stochastic components)
* Clear separation between data, logic, and analysis
* Modular functions for geocoding and text classification
* Designed for easy extension to larger participant datasets

---

## Example Outputs
* Country distribution of participants (counts & percentages)
* Employment sector distribution tables
* Sample classified job titles per sector

---

## Potential Extensions
* Add spatial visualization (e.g., choropleth world maps)
* Integrate supervised NLP models for comparison
* Expand multilingual occupation dictionaries
* Package classification logic as a reusable Python module

---

## Author
Developed by the project author as part of a participant analytics and data analysis portfolio, demonstrating applied Python skills in geospatial data processing, text classification, and statistical analysis.



