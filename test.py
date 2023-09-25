from fastapi.testclient import TestClient
from main import app
import pytest


@pytest.fixture
def test_client():
    # Initialize the FastAPI app with Redis server for testing
    with TestClient(app) as client:
        yield client

@pytest.fixture(autouse=True)
async def override_redis_cache():
    import main
    # Initialize the Redis server for testing
    await main.startup()
    yield
    await main.shutdown()


@pytest.mark.asyncio
async def test_root(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_solution_with_valid_input(test_client):
    valid_input = {
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
            },
            {
                "id": 3,
                "item": "Item 3",
                "quantity": 1,
                "price": 5.0,
                "status": "completed"
            }
        ],
        "criterion": "completed"
    }

    response = test_client.post("/solution", json=valid_input)
    assert response.status_code == 200
    assert response.json() == '25.0'

    valid_input2 = {
            "orders": [
                {
                    "id": 1,
                    "item": "Laptop",
                    "quantity": 1,
                    "price": 999.99,
                    "status": "completed"
                },
                {   "id": 2,
                    "item": "Smartphone",
                    "quantity": 2, 
                    "price": 499.95, 
                    "status": "pending"
                },
                {   
                    "id": 3, 
                    "item": "Headphones", 
                    "quantity": 3, 
                    "price": 99.90, 
                    "status": "completed"
                },
                {
                    "id": 4, 
                    "item": "Mouse", 
                    "quantity": 4, 
                    "price": 24.99, 
                    "status": "canceled"
                },
            ],
            "criterion": "completed"
        }

    response = test_client.post("/solution", json=valid_input2)
    assert response.status_code == 200
    assert response.json() == '1299.69'

@pytest.mark.asyncio
async def test_solution_with_invalid_input(test_client):
    invalid_price = {
        "orders": [
            {
                "id": 1,
                "item": "Item 1",
                "quantity": 2,
                "price": -10.0,  # Invalid price (less than 0)
                "status": "completed"
            }
        ],
        "criterion": "completed"
    }

    response = test_client.post("/solution", json=invalid_price)
    assert response.status_code == 422  # Unprocessable Entity

    invalid_status = {
        "orders": [
            {
                "id": 2,
                "item": "Item 2",
                "quantity": 3,
                "price": 15.0,
                "status": "invalid"  # Invalid status
            }
        ],
        "criterion": "completed"
    }

    response = test_client.post("/solution", json=invalid_status)
    assert response.status_code == 422  # Unprocessable Entity


