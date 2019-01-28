def test_flask_route(client):
    """Test the flask route will work"""
    response = client.get('/flask-routed-endpoint')
    assert response.status_code == 200
