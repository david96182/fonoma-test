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

    Example request: `POST http://localhost:8000/solution`

    ```json
    {
      "orders": [
        {
          "id": 1,
          "item": "Item 1",
          "quantity": 2,
          "price": 10.0,
          "status": "completed"
        },
        {
          "id": 2,
          "item": "Item 2",
          "quantity": 3,
          "price": 15.0,
          "status": "pending"
        }
      ],
      "criterion": "completed"
    }
    ```

5. Review the API responses and interact with the API based on the available endpoints and their respective request/response formats.

## Running Tests

This project includes tests that verify the functionality of the FastAPI API. To run the tests, follow these steps:

1. Make sure you have completed the installation steps mentioned above.
2. Ensure that the FastAPI server is not running.
3. In your terminal, navigate to the project directory if you are not already there.
4. Run the following command to execute the tests:

```bash
pytest
```

This command will discover and run all the tests in the project.

**Note:** The tests may take a few moments to complete, as they involve API requests and asynchronous operations.

1. After the tests finish running, you will see a summary of the test results in your terminal.

- If all tests pass, you should see a message indicating that all tests have passed.
- If any tests fail, you will see detailed information about the failed tests, including the specific assertions that failed.



That's it! You can now use the FastAPI API and run the provided tests for this test project. If you have any questions or encounter any issues, feel free to reach out to me. Thank you for the opportunity to showcase my skills.
