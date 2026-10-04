# Python API and Streamlit Starter Projects

This repository contains beginner-friendly Python applications demonstrating interactive web interfaces using [Streamlit](https://streamlit.io/) and RESTful APIs using [FastAPI](https://fastapi.tiangolo.com/).

## 📂 Repository Contents

*   **`Grade-app.py`**: A Streamlit web application that calculates student grades based on numerical marks (0-100). It features interactive UI elements like dropdowns and submission forms, providing dynamic feedback based on the score.
*   **`firstapi.py`**: A foundational FastAPI application demonstrating basic routing, path parameters (`/items/{item_id}`), and optional query parameters.
*   **`calculator.py`**: A complete FastAPI RESTful calculator API with dedicated GET endpoints for arithmetic operations (`/add`, `/subtract`, `/multiply`, `/divide`). Includes error handling for division by zero.

## 🚀 Prerequisites

Ensure you have Python 3.7+ installed. Install the required dependencies using `pip`:

```bash
pip install streamlit fastapi uvicorn
