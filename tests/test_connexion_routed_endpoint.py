def test_connexion_route(client):
    """Test the connexion route will work"""
    response = client.get('/connexion-routed-endpoint')
    assert response.status_code == 200
