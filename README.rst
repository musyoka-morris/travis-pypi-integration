Travis CI + Pypi Integration Guide
=====================================

This is a very short guide to using Travis CI with your GitHub hosted code repository
to automatically deploy a python package to Pypi.
If you’re new to continuous integration or would like some more information on what Travis CI does,
read `Travis CI Core Concepts for Beginners <https://docs.travis-ci.com/user/for-beginners>`_ first.

In this guide, we will be creating a Travis CI pipeline to automatically:

- Start mongodb service. Requires ``mongo>=4.0``
- Run ``pytest`` tests
- Distributes the package to pypi

All the code can be found on https://github.com/musyoka-morris/travis-pypi-integration

Prerequisites
******************

To proceed, make sure you have a Travis CI account.
You can easily create one by visiting https://travis-ci.org/ and then click the ``Sign in with Github`` button.

1. Install Travis CLI
***********************

First we need to install ``Travis CLI`` which is written in Ruby and published as a gem.
We will be using this tool to encrypt the Pypi password.


To install the gem:

    sudo gem install travis

ERROR: can't find header files for ruby ...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you run into the error **can't find header files for ruby**,
then you also need to have the ruby headers installed.

The `stack overflow answer <https://stackoverflow.com/questions/4304438/gem-install-failed-to-build-gem-native-extension-cant-find-header-files/4502672#4502672>`_
saved me. In summary, you need to install ruby development headers as follows:

For Debian, and other distributions using Debian style packaging:

    sudo apt-get install ruby-dev

For Ubuntu:

    sudo apt-get install ruby-all-dev

2. Create
2. Create a .travis.yml file
******************************

.travis.yml

.. code-block:: yaml

    language: python  # We are using Python language
    install: pip install -r requirements.txt  # Install requirements
    script: pytest  # Run pytest tests

Next we add instructions to start mongodb service

.. code-block:: yaml

    ...
    services:
      - mongodb
    before_script:
      - sleep 15  # Sleep for 15 seconds to ensure the service is started before we issue any commands

By default, travis loads ``mongo v2.*``. We instruct travis to load mongo v4.0

.. code-block:: yaml

    ...
    dist: xenial
    addons:
      apt:
        sources:
          - mongodb-4.0-xenial  # As defined on Travis Source safelist

Add instruction for deployment to pypi

.. code-block:: yaml

    ...
    deploy:
      provider: pypi
      user: musyoka-morris  # Replace this with your pypi username. Password will be provided later
      distributions: sdist bdist_wheel
      skip_existing: true

3. Add encrypted pypi password
********************************

Notice that so far we have not specified our pypi password.
The easiest way to add the password encrypted with the public key is to use Travis CLI:

    travis encrypt Your-Password-Here --add deploy.password

This command automatically adds your encrypted password on the .travis.yml file.

Note::

    We assumes you are running the command in your project directory. If not, add ``-r owner/project``.

4. Push to GIT
****************

Travis configuration is ready.
Simply push the code to the master branch and Travis will take care of the rest.


The complete ``.travis.yml`` file can be found on Github https://github.com/musyoka-morris/travis-pypi-integration