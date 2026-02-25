title = "Test Automation Frameworks at Aurora Peak"

content = """
We use a layered automation approach: unit tests in pytest, API tests in
requests or httpx, and UI tests in Selenium or Playwright. All integrate
with our CI pipeline and produce standardized reports.

**Framework Selection:** Unit and integration tests use pytest for its
plugins, fixtures, and clear assertion model. API tests favor libraries
that integrate well with pytest and support authentication flows.
UI tests require reliability and maintainability; we prefer Playwright
for its stability and cross-browser support.

**Page Object Model (POM):** UI automation uses the Page Object pattern
to separate test logic from UI structure. Each page or component has a
class exposing actions; tests operate on these objects rather than raw
selectors. This reduces maintenance when the UI changes.

**Reporting and Traceability:** Every automated run produces a report
with passed/failed counts, execution time, and failure screenshots or
logs. Reports are archived and linked to release records for audit.
"""  # noqa: E501

version = "0.0.1"
