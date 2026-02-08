from app import create_app

def test_add():
    app = create_app()
    app.testing = True
    client = app.test_client()

    response = client.post("/add", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.get_json()["result"] == 8
