# Technical Decisions Log

This document tracks all major technical choices for transparency and future reference.

## 1. Project Structure
- Modular folder-by-domain with clear separation for ETL, data, dashboards, and documentation.

## 2. ETL Tooling
- Python selected for flexibility and ecosystem (pandas, SQLAlchemy, etc).
- SQL scripts for set-based transforms.
- Clear code style: PEP8 for Python, ANSI for SQL.

## 3. Visualization Layer
- Power BI chosen for rich dashboarding, multi-language, and enterprise-readiness.
- Light/dark themes implemented for user preference.

## 4. Testing
- Data validation via Great Expectations or custom pytest scripts.

## 5. Documentation
- All docs versioned and written in client-facing language.

*Add new decisions as the project evolves.*