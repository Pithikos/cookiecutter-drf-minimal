class TestUsers:
    def test_user_can_only_retrieve_self(self, db, client, user, user_factory):
        other_user = user_factory()
        client.force_login(user)

        resp = client.get(f"/api/users/{user.id}/")
        assert resp.status_code == 200

        resp = client.get(f"/api/users/{other_user.id}/")
        assert resp.status_code in (400, 401)