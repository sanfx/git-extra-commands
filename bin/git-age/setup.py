import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name = "git-age",
    version = "0.1",
    packages = find_packages(),
    package_dir = {'':'.'},
    package_data = {
        'gitage': ['data/*'],
    },

    zip_safe = True,

    install_requires = [],
    scripts=['git-age'],

    # metadata for upload to PyPI
    author = "Kristoffer Gronlund",
    author_email = "kristoffer.gronlund@purplescout.se",
    description = "A git-blame viewer, written using PyGTK.",
    license = "GPL",
    keywords = "git viewer pygtk",
    url = "http://github.com/krig/git-age/wikis",
)

