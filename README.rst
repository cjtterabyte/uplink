Uplink
******
|PyPI Version| |Build Status| |Coverage Status| |Code Climate| |Documentation Status|
|Gitter| |Code Style|

- Builds Reusable Objects for Consuming Web APIs.
- Works with **Requests**, **asyncio**, and **Twisted**.
- Inspired by `Retrofit <http://square.github.io/retrofit/>`__.

A Quick Walkthrough, with GitHub API v3
=======================================
Uplink turns your HTTP API into a Python class.

.. code-block:: python

   from uplink import Consumer, get, headers, Path, Query

   class GitHub(Consumer):

      @get("users/{user}/repos")
      def get_repos(self, user: Path, sort_by: Query("sort")):
         """Retrieves the user's public repositories."""

Build an instance to interact with the webservice.

.. code-block:: python

   github = GitHub(base_url="https://api.github.com/")

Then, executing an HTTP request is as simply as invoking a method.

.. code-block:: python

   repos = github.get_repos("octocat", sort_by="created")

The returned object is a friendly |requests.Response|_:

.. |requests.Response| replace:: ``requests.Response``
.. _requests.Response: http://docs.python-requests.org/en/master/api/#requests.Response

.. code-block:: python

   print(repos.json())
   # Output: [{'id': 64778136, 'name': 'linguist', ...

For sending non-blocking requests, Uplink comes with support for
|aiohttp and twisted|_.

.. |aiohttp and twisted| replace:: ``aiohttp`` and ``twisted``
.. _`aiohttp and twisted`: https://github.com/prkumar/uplink/tree/master/examples/async-requests

Features
========

- **Quickly Define Structured API Clients**

  - Use decorators and function annotations to describe the HTTP request.
  - URL parameter replacement, request headers, and query parameter support.
  - JSON, URL-encoded, and multipart request body and file upload.

- **Bring Your Own HTTP Library**

  - Use Requests by default.
  - Send non-blocking HTTP requests with Aiohttp or Twisted.
  - Supply your own ``requests.Session`` or ``aiohttp.ClientSession`` object
    for greater control.

- **Directly Convert Response Bodies into Python Objects**

  - Built-in support for |marshmallow|_ schemas.
  - Define `custom converters`_ for your own objects.
  - Built-in support for `converting collections`_ (e.g., list of Users).

- **Extendable**

  - Inject `custom response and error handling`_ as middleware.
  - Install optional plugins for additional features (e.g., `protobuf support`_)

- **Authentication**

  - Built-in support for Basic Authentication.
  - Works with external auth support for Requests or Aiohttp.

Uplink officially supports Python 2.7 & 3.3-3.7.

.. |marshmallow| replace:: ``marshmallow``
.. _`marshmallow`: https://github.com/prkumar/uplink/tree/master/examples/marshmallow
.. _`custom converters`: https://uplink.readthedocs.io/en/latest/quickstart.html#deserializing-the-response-body
.. _`converting collections`: https://uplink.readthedocs.io/en/latest/converters.html#converting-collections
.. _`custom response and error handling`: https://uplink.readthedocs.io/en/latest/quickstart.html#custom-response-and-error-handling
.. _`protobuf support`: https://github.com/prkumar/uplink-protobuf

Installation
============

To install the latest stable release, you can use ``pip`` (or ``pipenv``):

::

    $ pip install -U uplink

If you are interested in the cutting-edge, preview the upcoming release with:

::

   $ pip install https://github.com/prkumar/uplink/archive/master.zip

Extra! Extra!
-------------

Further, uplink has optional integrations and features. You can view a full list 
of available extras `here <http://uplink.readthedocs.io/en/latest/install.html#extras>`_.

When installing Uplink with ``pip``, you can select extras using the format:

::

   $ pip install -U uplink[extra1, extra2, ..., extraN]


For instance, to install ``aiohttp`` and ``marshmallow`` support:

::

   $ pip install -U uplink[aiohttp, marshmallow]


User Testimonials
===============

**Michael Kennedy** (`@mkennedy`_), host of `Talk Python`_ and `Python Bytes`_ podcasts-

    Of course our first reaction when consuming HTTP resources in Python is to
    reach for Requests. But for *structured* APIs, we often want more than ad-hoc
    calls to Requests. We want a client-side API for our apps. Uplink is
    the quickest and simplest way to build just that client-side API.
    Highly recommended.

.. _@mkennedy: https://twitter.com/mkennedy
.. _`Talk Python`: https://twitter.com/TalkPython
.. _`Python Bytes`: https://twitter.com/pythonbytes

**Or Carmi** (`@liiight`_), notifiers_ maintainer-

    Uplink’s intelligent usage of decorators and typing leverages the most
    pythonic features in an elegant and dynamic way. If you need to create an
    API abstraction layer, there is really no reason to look elsewhere.

.. _@liiight: https://github.com/liiight
.. _notifiers: https://github.com/notifiers/notifiers


Documentation
=============
Ready to create an API client with Uplink? Get started with this
quickstart_ guide! For more details, check out the documentation at
https://uplink.readthedocs.io/.

.. _quickstart: https://uplink.readthedocs.io/en/stable/quickstart.html

Contributing
============
Want to report a bug, request a feature, or contribute code to Uplink?
Checkout the `Contribution Guide`_ for where to start.
Thank you for taking the time to improve an open source project 💜

.. |Build Status| image:: https://travis-ci.org/prkumar/uplink.svg?branch=master
   :target: https://travis-ci.org/prkumar/uplink
.. |Code Climate| image:: https://api.codeclimate.com/v1/badges/d5c5666134763ff1d6c0/maintainability
   :target: https://codeclimate.com/github/prkumar/uplink/maintainability
   :alt: Maintainability
.. |Code Style| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: Code style: black
.. |Coverage Status| image:: https://img.shields.io/codecov/c/github/prkumar/uplink.svg   
   :alt: Codecov   
   :target: https://codecov.io/gh/prkumar/uplink
.. |Documentation Status| image:: https://readthedocs.org/projects/uplink/badge/?version=latest
   :target: http://uplink.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. |Gitter| image:: https://badges.gitter.im/python-uplink/Lobby.svg
   :target: https://gitter.im/python-uplink/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
   :alt: Join the chat at https://gitter.im/python-uplink/Lobby
.. |License| image:: https://img.shields.io/github/license/prkumar/uplink.svg
   :target: https://github.com/prkumar/uplink/blob/master/LICENSE
.. |PyPI Version| image:: https://img.shields.io/pypi/v/uplink.svg
   :target: https://pypi.python.org/pypi/uplink

.. _`Contribution Guide`: https://github.com/prkumar/uplink/blob/master/CONTRIBUTING.rst
