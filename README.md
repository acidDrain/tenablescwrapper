# tenablescwrapper

A simple API wrapper for Tenable Security Center written in Python.

This project is currently a work in progress and under development. The bare functionality included today is simply to:

- authenticate to Tenable Security Center's API
- query the /analysis API endpoint

## Getting Started

Clone this repository and open a shell to its location.

The example.py script can be used to demonstrate base functionality. It reads the hostname and authentication information for Security Center from a file called config.json, which should be placed in the base directory of this project.

You can copy and paste this data to a file called config.json, replacing the values with the actual login and host information.

```json
{
  "username": "some.user",
  "password": "the_password",
  "sc_host": "securitycenter.tld"
}
```

Install dependencies:

```shell
$ pipenv install
Installing dependencies from Pipfile.lock (23a88c)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 6/6 — 00:00:01
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```

Environment setup:

```python
$ pipenv shell
Launching subshell in virtual environment…
 . ~/.local/share/virtualenvs/tenablescwrapper-k6EfK19m/bin/activate
$  . ~/.local/share/virtualenvs/tenablescwrapper-k6EfK19m/bin/activate
```

```shell
$ python example.py
<Output>
```
