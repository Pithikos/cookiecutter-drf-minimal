class TestUsers:
    def test_user_can_only_retrieve_self(self, db, client, user, user_factory):
        other_user = user_factory()
        client.force_login(user)

        resp = client.get(f"/api/users/{user.id}/")
        assert resp.status_code == 200

        resp = client.get(f"/api/users/{other_user.id}/")
        assert resp.status_code == 403

    def test_anon_has_no_access(self, db, client, user):
        resp = client.get(f"/api/users/")
        assert resp.status_code == 403
        resp = client.get(f"/api/users/{user.id}/")
        assert resp.status_code == 403

    def test_admin_has_full_access(self, db, client, user, admin):
        client.force_login(admin)
        assert client.get(f"/api/users/").status_code == 200
        assert client.get(f"/api/users/{user.id}/").status_code == 200
        assert client.get(f"/api/users/{admin.id}/").status_code == 200