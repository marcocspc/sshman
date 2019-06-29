from setuptools import setup

setup(
    name = "sshman",
    packages = ["sshman"],
    entry_points = {
        "console_scripts": ['sshman=sshman.sshman_cmd:main']
        },
    version = "0.0.2",
    description = "SSH Connection manager.",
    long_description = "SSH Connection manager.",
    author = "Marco Antonio",
    author_email = "marcocspc@hotmail.com",
    url = "https://github.com/marcocspc/sshman",
)
