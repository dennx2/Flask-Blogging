from website.models.users import User

def test_home_without_login(client):
    response = client.get("/")
    assert response.status_code == 302

def test_registration(client, app):

    response = client.post("/sign-up", data = {"username": "test", "email":"test@test.com", "password1":"testpassword", "password2":"testpassword"})

    with app.app_context():
        assert User.query.count() == 1
        assert User.query.first().email == "test@test.com"