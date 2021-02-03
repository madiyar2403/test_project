from django.contrib.auth.models import User


def test_auth(db, client):
    user = User.objects.create_user(username='testusername',
                                    password='LQmywfag')
    response = client.post('/auth/', {'username': 'testusername',
                                      'password': 'LQmywfag'})
    assert response.status_code == 200
    data = response.json()
    assert 'token' in data
    assert 'user_id' in data
