Error handling
==============

Errors are a JSON object with a ``detail`` string:

.. code-block:: json

   {"detail": "'NOPE9999' is not a semester id. They look like 'AP2026272' ..."}

Status codes
------------

.. list-table::
   :header-rows: 1
   :widths: 12 88

   * - Code
     - Meaning
   * - ``400``
     - The request was malformed in a way we could see without asking VTOP —
       most often a ``sem_sub_id`` that is not ``AP`` followed by seven digits.
       Nothing was sent to the portal.
   * - ``401``
     - Either the ``X-API-Key`` is missing or wrong, or VTOP rejected the
       credentials, or the session has expired, or an OTP was wrong or expired.
       The ``detail`` says which.
   * - ``409``
     - VTOP accepted the credentials but wants a login OTP first. Retrying the
       same credentials cannot resolve it. See :doc:`authentication`.
   * - ``422``
     - The body is valid JSON but does not match the endpoint's model — a
       missing field, or the wrong type. FastAPI's own validation detail.
   * - ``500``
     - Something failed on our side, or a parser could not make sense of what
       VTOP returned. A parsing failure usually means VTOP changed a page.
   * - ``502``
     - VTOP could not be reached, or refused the request.

Two that are easy to confuse
----------------------------

**401 on a data endpoint** means the *session* died, not that the API key is
wrong — the key was already checked before the handler ran. Read the ``detail``.

**409 is not a failure.** It means the login is half done and needs the OTP. It
is the expected path whenever VTOP has not seen your IP before.

Empty is not an error
---------------------

Several results are legitimately empty, and none of them raise:

* ``/student/grade_view`` returns ``[]`` for a semester whose results have not
  published
* ``/student/capstone_attendance`` returns ``null`` for a student without one
* marks may be unpublished, and biometric can be genuinely empty for a day
* an **unknown semester id** also returns an empty result. VTOP does not reject
  it, so a wrong id is indistinguishable from a quiet semester. The shape check
  catches a typo; it cannot catch a stale id. Take ids from
  ``/student/semesters``.
