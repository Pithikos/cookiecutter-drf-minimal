from rest_framework_roles.roles import is_user, is_anon, is_admin


def is_staff(request, view):
    return request.user.is_staff


ROLES = {

    # Django vanilla roles
    'admin': is_admin,
    'staff': is_staff,
    'user': is_user,
    'anon': is_anon,

    # Userbase roles
    # ..

}