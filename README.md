# matrix.org authentication plugin for Radicale

[Radicale](https://radicale.org) is a CalDAV and CardDAV server, for storing calendars and contacts.
That module provides an authentication plugin for Radicale to make use of Matrix server as auth backend.


## How To Use

You must login with **localpart** as login:

**Correct:**
* Login: user
* Password: super-secret-password

**Incorrect:**
* Login: @user:example.com
* Password: super-secret-password


**Why?** Because Radicale's default UI's behavior is to send the provided credentials as basic auth in url, eg: `https://user:super-secret-password@radicale.example.com`, so if you provide full MXID, it will cut it and place `@user` as username and `example.com:super-secret-password` as password

## Configuration

```toml
[auth]
type = "radicale_auth_matrix" # auth method
matrix_server = "https://matrix.example.com" # matrix server to use for authentication
```
