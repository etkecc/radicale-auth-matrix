"""
Authentication backend that checks credentials with a matrix server.
"""

import json
import hashlib
import urllib
import urllib.request
from radicale import auth, config


class Auth(auth.BaseAuth):
    _server: str
    _cache: dict

    def __init__(self, configuration: config.Configuration) -> None:
        super().__init__(configuration)
        self._server = configuration.get("auth", "matrix_server")
        self._cache = {}

    def _loginURL(self) -> str:
        return "{}/_matrix/client/v3/login".format(self._server)
    def _logoutURL(self) -> str:
        return "{}/_matrix/client/v3/logout".format(self._server)

    def _payload(self, login: str, password: str) -> bytes:
        return json.dumps({
            "type": "m.login.password",
            "identifier": {
                "type": "m.id.user",
                "user": login.replace('@',''),
            },
            "password": password,
            "initial_device_display_name": "radicale",
        }).encode("utf-8")

    def _logout(self, token: str) -> None:
        req = urllib.request.Request(
            self._logoutURL(),
            headers={"Authorization": "Bearer {}".format(token)},
            method="POST"
        )
        try:
            urllib.request.urlopen(req)
        except urllib.error.HTTPError as e:
            print(e)

    def _loggedInHash(self, login: str, password: str) -> str:
        return hashlib.sha256("{} {}".format(login, password).encode("utf-8")).hexdigest()

    def _loggedIn(self, login: str, password: str) -> None:
        self._cache[self._loggedInHash(login, password)] = True

    def _isLoggedIn(self, login: str, password: str) -> bool:
        return self._loggedInHash(login, password) in self._cache.keys()

    def login(self, login: str, password: str) -> str:
        if self._isLoggedIn(login, password):
            return login

        req = urllib.request.Request(
            self._loginURL(),
            data=self._payload(login, password),
            headers={"Content-Type": "application/json; charset=utf8"},
            method="POST"
        )
        try:
            resp = urllib.request.urlopen(req)
            data = json.loads(resp.read().decode("utf-8"))
            self._logout(data['access_token'])
            self._loggedIn(login, password)
            return login
        except urllib.error.HTTPError as e:
            return ""
