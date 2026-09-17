VIT-AP VTOP API
===============

A FastAPI service wrapping `vitap-vtop-client
<https://udhay-adithya.github.io/vitap-vtop-client/>`_, so an application can
read a student's VTOP data over HTTP instead of scraping the portal itself.

There is no VTOP API. Everything here is scraped out of a JSP application that
changes without warning, and the portal's behaviour leaks into this one in ways
worth knowing before you build on it — start with :doc:`guide/authentication`.

.. code-block:: bash

   # 1. log in once
   curl -X POST https://your-host/auth/login \
     -H "X-API-Key: $API_KEY" -H "Content-Type: application/json" \
     -d '{"registration_number": "REGNO", "password": "..."}'

   # 2. send the session back on every call after that
   curl -X POST https://your-host/student/attendance \
     -H "X-API-Key: $API_KEY" -H "Content-Type: application/json" \
     -d '{"session": {...}, "sem_sub_id": "AP2026272"}'

.. toctree::
   :maxdepth: 2
   :caption: Getting started

   getting-started

.. toctree::
   :maxdepth: 2
   :caption: Guide

   guide/authentication
   guide/sessions
   guide/errors

.. toctree::
   :maxdepth: 2
   :caption: Reference

   api/endpoints

Indices
-------

* :ref:`genindex`
* :ref:`search`
