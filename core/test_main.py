from django.test import Client


def test_auth(db, client):
    # client.config['WTF_CSRF_ENABLED'] = False
    # print(client.object.all())
    # token = Token.objects.create(user=user)
    # print(token.key)
    # print(user)
    c = Client()
    response = c.post('/auth/', {'username': 'testusername', 'password': 'LQmywfag'})
    # print(response)
    # print(client)
    # print(db)
    # response = Response status_code=400 why? token and user_id
    # pytest:
    '''
    test_main.py <Response status_code=400, "application/json">
    <django.test.client.Client object at 0x053B2718>
    None
    {'non_field_errors': ['Unable to log in with provided credentials.']}
    '''
    # Also troubles with db
    assert response.status_code == 200
    data = response.json()
    # print(data)
    assert 'token' in data
    assert 'user_id' in data

    '''
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.pk})
    '''
    '''
    def post(self, request):
        user = authenticate(
            username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.pk})
        return Response('Invalid username or password', status=status.HTTP_400_BAD_REQUEST)
    '''