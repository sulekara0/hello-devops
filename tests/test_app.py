import app as app_module

def test_health_route():
    client = app_module.app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["status"] == "ok"
    assert data["service"] == "hello-devops"

def test_root():
    client = app_module.app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert "Hello DevOps" in resp.get_data(as_text=True)
