from django.conf.urls import url
from django.db import connection


def show_user(request, username):
    with connection.cursor() as cursor:
        # BAD -- Using string formatting
        cursor.execute("SELECT * FROM users WHERE username = %s" % username)
        user = cursor.fetchone()

        # GOOD -- Using parameters
        cursor.execute("SELECT * FROM users WHERE username = %s", username)
        user = cursor.fetchone()

        # GOOD -- Using parameters
        cursor.execute("SELECT * FROM users WHERE username = %s", [username])
        user = cursor.fetchone()

        # GOOD - string literal
        cursor.execute("SELECT * FROM users WHERE username = 'johndoe'")
        user = cursor.fetchone()
urlpatterns = [url(r'^users/(?P<username>[^/]+)$', show_user)]
