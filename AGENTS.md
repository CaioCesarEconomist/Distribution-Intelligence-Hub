
# AGENTS.md

## Distribution Intelligence Hub
### Full Agent Instruction & Execution Framework

## Project Vision

Build a scalable, reusable, production-grade analytics platform for distribution companies. The project will serve as both a real-world portfolio and a simulation of enterprise data consulting delivery.

All agents (human, AI, or mixed) will follow this framework to ensure consistency, clean code, and high business value output.

## Core Architecture

Layer | Technology | Notes
----- | ---------- | -----
Data Source | Real-world public datasets or anonymized company data | Distribution sector
ETL / Transformation | Power Query M + SQL + Python (optional) | Clean Code principles
Data Modeling | DAX, Tabular Model | Documented calculations
Dashboard Layer | Power BI Desktop / Service | Light/Dark UI, Multi-language
Testing | Great Expectations (Python) or Custom Validation Scripts | Data quality assurance
Documentation | Markdown + Diagrams + Decision Logs | GitHub-managed

## Repository Structure

- data/: Anonymized datasets, raw and processed
- etl/: ETL scripts (Power Query M, SQL, Python)
- modeling/: DAX measures, data models
- testing/: Data validation scripts
- dashboards/: Power BI dashboards (.pbix)
- docs/: Diagrams, decision logs, translations
- AGENTS.md: This document
- README.md: Project overview
- LICENSE

## Business Insights Required

- Sales trends and revenue forecasting
- Inventory optimization
- Client segmentation
- Profit margin monitoring
- Supply chain alerts
- Scenario simulation

Each insight must be visually highlighted, business-contextualized, and multi-language ready.

## Execution Phases

1. Data Acquisition: Public data search, validation, documentation.
2. ETL Pipeline Build: Clean Code ETL development.
3. Data Modeling: Logical star schema, DAX measures.
4. Testing Layer: Data integrity validation.
5. Dashboard Development: Themed, multi-language, alert-driven dashboards.
6. Documentation: Full technical and business documentation.

## Documentation Requirements

Document | File | Purpose
-------- | ---- | -------
General Overview | README.md | Project intro
Agent Instructions | AGENTS.md | This file
Data Sources | data_sources.md | Dataset origin
Diagrams | diagrams/ | Architecture
Decision Log | decision_logs/ | Technical decisions

## Sample Data Sources

- Kaggle: https://www.kaggle.com/datasets
- dados.gov.br: https://dados.gov.br
- World Bank: https://databank.worldbank.org
- OECD: https://data.oecd.org

## Testing & QA

- Automated and manual data validations.
- Power BI validation pages.
- Simulated stakeholder QA sessions.

## Clean Code Principles

- No hard-coded credentials
- Parameterized queries
- Consistent naming
- Business logic comments
- Git version control

## Multi-Language Structure

- Power BI Translation Tables
- docs/translations/ for files
- Full validation on language switching

## Target Outcome

A full Distribution Intelligence Hub demonstrating:
- Data Engineering, Modeling, Analytics, Testing, BI Delivery
- Reusable for consulting, interviews, and clients.

Agent’s Responsibility: Always work as if delivering to a paying client.
