Getting started
===============

Running it
----------

.. code-block:: bash

   git clone https://github.com/Udhay-Adithya/vit_ap_vtop_api.git
   cd vit_ap_vtop_api
   poetry install
   cp .env.example .env          # then set API_KEY
   poetry run fastapi dev src/main.py

The service listens on ``http://127.0.0.1:8000``. Interactive OpenAPI docs are
at ``/docs``.

Requires Python 3.13 or newer. There is nothing else to configure: the captcha
is solved locally by the client library, so there is no external service and no
key to obtain beyond your own ``API_KEY``.

The API key
-----------

Every endpoint requires an ``X-API-Key`` header matching the ``API_KEY`` in your
environment. It gates access to the service; it has nothing to do with VTOP
credentials.

.. code-block:: bash

   curl -X POST http://127.0.0.1:8000/student/semesters \
     -H "X-API-Key: $API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"session": {...}}'

A missing or wrong key is a ``401``.

The shape of a request
----------------------

Two steps, always:

1. **Log in once** at :doc:`/auth/login <guide/authentication>`. You get back a
   session.
2. **Send that session** with every data request afterwards.

.. code-block:: python

   import requests

   BASE = "http://127.0.0.1:8000"
   HEAD = {"X-API-Key": "your-api-key"}

   login = requests.post(f"{BASE}/auth/login", headers=HEAD, json={
       "registration_number": "REGNO",
       "password": "your-vtop-password",
   }).json()

   if login["status"] == "otp_required":
       otp = input("OTP sent to your registered email: ")
       login = requests.post(f"{BASE}/auth/verify_otp", headers=HEAD, json={
           "otp_challenge": login["otp_challenge"],
           "otp": otp,
       }).json()

   session = login["session"]

   semesters = requests.post(f"{BASE}/student/semesters", headers=HEAD,
                             json={"session": session}).json()
   sem_id = semesters["semesters"][0]["id"]

   attendance = requests.post(f"{BASE}/student/attendance", headers=HEAD,
                              json={"session": session, "sem_sub_id": sem_id}).json()

Credentials are sent exactly once. Everything after that carries the session,
which is both much faster and the only way the OTP flow can work at all — see
:doc:`guide/authentication`.

Semester ids
------------

Most endpoints take a ``sem_sub_id``. Do not hardcode one — ask for it:

.. code-block:: python

   requests.post(f"{BASE}/student/semesters", headers=HEAD,
                 json={"session": session}).json()

A malformed id is rejected with a ``400`` before anything is sent to VTOP. An id
that is well formed but wrong is **not**, and cannot be: VTOP answers an unknown
semester with an empty result rather than an error, so it is indistinguishable
from a semester with no data. Take ids from ``/student/semesters`` at the point
of use.

Being a good citizen
--------------------

Every call is a real request against a university server that is not built for
automation.

* Reuse one session for many calls rather than logging in per request.
* Never loop on a failed login. Repeated failures can lock a VTOP account.
* Treat an empty result as legitimate. Marks may be unpublished, biometric can
  be genuinely empty for a day, and grades do not exist until a semester ends.
