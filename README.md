# fonoma-test

Thank you for considering me for the Backend Developer position at Fonoma. This repository contains a simple FastAPI API that serves as a test project. Below you will find instructions on how to use the application and run the provided tests.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)

## Requirements
To run this application, you need to have the following installed:
- Python 3.8+
- `pip` package manager

## Installation
1. Clone this repository to your local machine or download the ZIP file.
2. Navigate to the project directory:
    ```bash
    cd fonoma-test
    ```

3. It is recommended to create a virtual environment to isolate project dependencies. Run the following command to create and activate a virtual environment (optional):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # for macOS/Linux
    venv\Scripts\activate  # for Windows
    ```

4. Install the project dependencies using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To use the FastAPI API, follow these steps:

1. Make sure you have completed the installation steps mentioned above.

2. Start the FastAPI server by running the following command:
    ```bash
    uvicorn main:app --reload
    ```
   This will start the server at `http://localhost:8000`.

3. Open your preferred API testing tool (e.g., Postman, cURL, or any web browser).

4. Send requests to the available endpoints based on your needs.

5. Review the API responses and interact with the API based on the available endpoints and their respective request/response formats.

That's it! You can now use the FastAPI API and run the provided tests for this test project. If you have any questions or encounter any issues, feel free to reach out to me. Thank you for the opportunity to showcase my skills.
