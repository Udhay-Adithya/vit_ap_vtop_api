Authentication
==============

There are two separate things called a key here, and they are unrelated:

* the **API key**, an ``X-API-Key`` header, which gates the service
* the student's **VTOP credentials**, sent once to ``/auth/login``

Log in once
-----------

``POST /auth/login`` takes the credentials and returns a session:

.. code-block:: json

   {
     "status": "authenticated",
     "session": {
       "registration_number": "...",
       "cookie": "JSESSIONID=...",
       "csrf_token": "...",
       "user_agent": "..."
     }
   }

Send that ``session`` object back, unchanged, with every data request. Do not
send credentials again.

This is not only about speed, though the difference is large — VTOP's login
costs a captcha solve and around a dozen requests, so the same call went from
1570ms to 129ms once the session was reused. It is also the only arrangement in
which the OTP flow can work.

The OTP gate
------------

VTOP asks for a one-time password after a period of inactivity, or when the
login comes from an IP address it has not seen. A deployed server is a new IP
address by definition, so this is not an edge case.

That is a normal outcome rather than a failure, so it is a **200**:

.. code-block:: json

   {
     "status": "otp_required",
     "otp_challenge": { "...": "..." }
   }

Collect the OTP from the student and post it back with the challenge, unchanged:

.. code-block:: text

   POST /auth/verify_otp

.. code-block:: json

   {
     "otp_challenge": { "...": "..." },
     "otp": "123456"
   }

The response is the same shape as a login that was never challenged.

If the OTP expires, call ``POST /auth/resend_otp`` with the same challenge
rather than logging in again — a fresh login invalidates this challenge and
makes the student wait through another captcha-gated attempt. The challenge
stays valid, so keep using it.

.. warning::

   An ``otp_challenge`` is a credential. Credentials and captcha have already
   been accepted by the time you hold one, so anyone with it can finish the
   login as soon as they have the OTP. Treat it like the session.

Why the challenge travels
-------------------------

The service keeps **no state**. A challenge is raised while answering one
request and the OTP arrives on the next, so if the service held it in memory it
would be lost on a restart, and would not work at all across more than one
instance. Handing it to the caller and taking it back is what makes the flow
survive both.
