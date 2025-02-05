# Python Selenium Project

This project contains **Python** scripts using **Selenium** for web interface automation testing.

## Project Structure

```
PythonSelenium/
│── .venv/                    # Python virtual environment
│   ├── Lib/
│   ├── Scripts/
│   ├── .gitignore
│   ├── pyvenv.cfg
│
├── basic_selenium/            # Basic Selenium scripts
│   ├── actionsDemo.py         # Demonstration of actions (click, drag, etc.)
│   ├── alerts.py              # Handling browser alerts
│   ├── childWindow.py         # Working with child windows
│   ├── dropdown.py            # Handling dropdown menus
│   ├── findElements.py        # Identifying web elements
│
├── intermediate_selenium/     # Intermediate Selenium scripts
│   ├── e2etest.py             # End-to-end test with Selenium
│   ├── explicit_waits.py      # Using explicit waits
│   ├── pytest_e2etest.py      # End-to-end tests with Pytest
│
├── External Libraries/        # External libraries used
├── Scratches and Consoles/    # Notes and temporary code
```

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone (https://github.com/Serin15/More-Selenium-Ex..git)
   cd repository-name
   ```

2. **Create and activate the virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   .venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- To run an individual test, e.g., `dropdown.py`:
  ```bash
  python basic_selenium/dropdown.py
  ```
- To run all tests with Pytest:
  ```bash
  pytest intermediate_selenium/
  ```

## Contributions

- Pull requests are welcome.
- Ensure you follow Python coding style and document any changes.

## License

This project is distributed under the MIT License.

---

If you have any questions or suggestions, feel free to open an issue on GitHub. 🚀

