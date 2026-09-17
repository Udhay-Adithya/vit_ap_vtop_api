Sessions
========

A session is the four values ``/auth/login`` returns. VTOP keeps the actual
session on its own server, keyed by the cookie inside it; this service stores
nothing.

.. warning::

   A session is a credential. Anyone holding one can read the student's records
   for as long as VTOP keeps it alive. Store it the way you would store a
   password, and never put it in a URL, a log line or a query string — which is
   why every endpoint here is a ``POST`` with a body.

How long one lasts
------------------

VTOP decides, and does not say. A session survived 90 seconds of idling
comfortably during testing, but there is no documented timeout and no way to
ask. Treat expiry as normal rather than exceptional.

When it expires
---------------

You get a **401** with a message saying to log in again:

.. code-block:: json

   {
     "detail": "VTOP rejected the request with a 404, which is what it does
                when the session or CSRF token has expired. Log in again
                before retrying."
   }

Handle it by going back through ``/auth/login``. The service cannot renew a
session for you: it holds no password, deliberately. Re-logging in may need an
OTP that only the student can supply, so a silent retry is not something the
service can do on their behalf.

.. code-block:: python

   r = requests.post(f"{BASE}/student/attendance", headers=HEAD,
                     json={"session": session, "sem_sub_id": sem_id})

   if r.status_code == 401:
       session = log_in_again()      # may require an OTP
       r = requests.post(...)

One session, many calls
-----------------------

Sessions are cheap to use and expensive to create, so get one and keep it. The
service restores the caller's session per request, which costs no login and no
extra round trip, because VTOP is holding it server side already.
