# Data Quality & Testing Strategy

## Goals

- Ensure all data transformations are accurate and reproducible.
- Validate data before it reaches Power BI.

## Approach

1. **Automated Data Validation**
   - Use Great Expectations or custom Python scripts (`/tests/`) to check:
     - Data types
     - Nulls / missing values
     - Referential integrity
     - Business logic checks (e.g., no negative inventory)

2. **Continuous Integration**
   - GitHub Actions workflow triggers tests on push.

3. **Manual Spot Checks**
   - Visual inspection of Power BI dashboards with test data.

## Example

- `test_data_quality.py` validates all processed datasets before dashboard refresh.

*Expand with more details as your pipeline grows.*