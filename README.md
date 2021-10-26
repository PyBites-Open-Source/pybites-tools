[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# build

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Pybites-Open-Source/pybites-tools/main.svg)](https://results.pre-commit.ci/latest/github/rhyspowell/pybites-tools/main)
[![CI test](https://github.com/Pybites-Open-Source/pybites-tools/actions/workflows/test.yml/badge.svg)](https://github.com/rhyspowell/pybites-tools/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/Pybites-Open-Source/pybites-tools/branch/main/graph/badge.svg)](https://codecov.io/gh/rhyspowell/pybites-tools)

# Can be added to correct path after

[![PyPI version](https://badge.fury.io/py/build.svg)](https://)

# PyBites Tools

Welcome to PyBites Tools repo!

This is a collection repo for all things python that we have found helpful to get your modern Python project up and going.

## Get started

### Using this repo in your project

```
pip install pybites-tools
```

To use the command-line scripts (some scripts you need to set environment variables), for example:

```
(venv) $ zen
The Zen of Python has been copied to your clipboard

(venv) $ s3
usage: s3 [-h] -f FILE [-b BUCKET] [-a ACL]
s3: error: the following arguments are required: -f/--file

(venv) $ email
usage: email [-h] -s SUBJECT -m MESSAGE [-e EMAIL]
email: error: the following arguments are required: -s/--subject, -m/--message
```

Or use tools by importing them in your scripts, for example:

```
>>> from pybites_tools.license import generate_license_key
>>> generate_license_key()
'35HN2KIW-K3ON4F94-IGJ1UN32-EAXSRZLF'
```

## Developer setup

If you want to contribute or modify the repo, make a fork and clone it, for example:

```
git clone git@github.com:bbelderbos/pybites-tools.git
cd pybites-tools
```

To get started run: \
`make setup` \
This will create a virtual environment and install the dependencies.

Before committing any code, you should install and run pre-commit. [Why pre-commit?](https://talkpython.fm/episodes/show/282/pre-commit-framework)

Just run  `pre-commit install`.

For some tools, you will need environment variables. You can set them by copying over the `.env-template` file to `.env`.

## Useful tools

### Send email

Configure the `EMAIL_*` environment variables; then you can run it like this:

```
$ python -m pybites_tools.sendemail -s "test subject" -m "test message" --email recipient@example.com
```

If you set `EMAIL_DEFAULT_TO_EMAIL`, you can leave off the `--email` switch. This is useful if you want to send yourself a reminder often.

For example, you could add something like this in your `.zshrc`:

```
function remind {
    (cd $HOME/code/pybites-tools && source venv/bin/activate && python -m pybites_tools.sendemail -s "$1" -m "$2")
}
```

Then you can send yourself a quick email like this:

```
$ remind "blog post" "git stats"
```

### Uploading files to an S3 bucket

For this, you need to set the `AWS_*` configuration variables in `.env`.

Then you can upload a file using:

```
$ python -m pybites_tools.aws -f file-path (-b bucket) (-a acl)
```

### WorldClock from the command line

Add the timezones that you would like displayed to the TIMEZONE_LIST configuration variable in `.env`. (List of all timezones [here](https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568).)

Like this:

```
TIMEZONE_LIST=["America/Los_Angeles","CET","Australia/Sydney"]
```

Then:
```
$ python -m pybites_tools.worldclock
America/Los_Angeles       08:35PM
CET                       05:35AM
Australia/Sydney          02:35PM
```

Or specify a time in some other timezone to be converted
(e.g. to convert 10:55PM in London):
```
$ python -m pybites_tools.worldclock -hr 22 -min 55 -tz Europe/London
America/Los_Angeles       02:55PM
CET                       11:55PM
Australia/Sydney          08:55AM
```

### Copy Zen of Python to clipboard

Why not send it to a coder friend from time to time?

```
$ python -m pybites_tools.zen
The Zen of Python has been copied to your clipboard
```
