from application import application
with application.test_client() as c:
    response = c.get('/')
    assert response.data == b'This Flask App Works!'
    assert response.status_code == 200
    response2 = c.get('/hello')
    assert response2.data == b'Hello Hello App User!'
    assert response2.status_code == 200

