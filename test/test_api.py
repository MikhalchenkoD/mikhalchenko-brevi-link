def test_create_short_url(client):
    response = client.post('/create-short-url', data={
        'original_url': 'https://www.google.kz/',
        'short_url': 'google'
    })

    assert response.status_code == 200


def test_create_duplicate_short_url(client):
    response = client.post('/create-short-url', data={
        'original_url': 'https://www.google.com',
        'short_url': 'google'
    })

    assert response.status_code == 403


def test_get_site_with_shor_url(client):
    response = client.get('/google')

    assert response.status_code == 302


def test_get_bad_site_with_shor_url(client):
    response = client.get('/gogle')

    assert response.status_code == 404
