# PyBites Tools

A repo to commit common Python utility scripts and snippets

## Use in your project

```
pip install pybites-tools
```

Use command line scripts (for some scripts you need to set environment variables), for example:

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

Make a fork and clone it, for example:

```
git clone git@github.com:bbelderbos/pybites-tools.git
cd pybites-tools
```

To get started run: `make setup`. This will create a virtual environment and install the dependencies.

We recommend running the `black` code formatter before committing, to set this up run `pre-commit install`.

For some tools you will need environment variables. You can set them by copying over the `.env-template` file to `.env`.

## Useful tools

In no particular order:

### Send email

Configure the `EMAIL_*` environment variables, then you can run it like this:

```
$ python -m pybites_tools.email -s "test subject" -m "test message" --email recipient@example.com
```

If you set `EMAIL_DEFAULT_TO_EMAIL`, you can leave off the `--email` switch. This is useful if you want to send yourself a reminder often.

For example you could add something like this in your `.zshrc`:

```
function remind {
    (cd $HOME/code/pybites-tools && source venv/bin/activate && python -m pybites_tools.email -s "$1" -m "$2")
}
```

Then you can send yourself a quick email like this:

```
$ remind "blog post" "git stats"
```

### Upload files to an S3 bucket

For this you need to set the `AWS_*` configuration variables in `.env`.

Then you can upload a file using:

```
$ python -m pybites_tools.aws -f file-path (-b bucket) (-a acl)
```

### Copy Zen of Python to clipboard

Why not send it to a coder friend from time to time? Easy:

```
$ python -m pybites_tools.zen
The Zen of Python has been copied to your clipboard
```
