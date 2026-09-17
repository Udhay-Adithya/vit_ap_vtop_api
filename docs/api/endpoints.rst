Endpoint reference
==================

Generated from the service's own OpenAPI schema, so it cannot drift from the
routes. A running service serves the same thing interactively at ``/docs``.

Every endpoint is a ``POST``. Data travels in the body rather than the query
string, because it carries a session that must not end up in a URL, a proxy log
or a browser history.

Authentication
--------------

.. openapi:: ../openapi.json
   :paths:
      /auth/login
      /auth/verify_otp
      /auth/resend_otp

Student data
------------

.. openapi:: ../openapi.json
   :paths:
      /student/semesters
      /student/profile
      /student/all_data
      /student/attendance
      /student/attendance_detail
      /student/capstone_attendance
      /student/timetable
      /student/marks
      /student/exam_schedule
      /student/grade_history
      /student/grade_view
      /student/grade_view_detail
      /student/biometric
      /student/mentor

Calendar
--------

.. openapi:: ../openapi.json
   :paths:
      /student/calendar
      /student/calendar/class_groups
      /student/calendar/months
      /student/calendar/month

Faculty
-------

.. openapi:: ../openapi.json
   :paths:
      /student/faculty
      /student/faculty/search
      /student/faculty/details

Course page
-----------

.. openapi:: ../openapi.json
   :paths:
      /student/course_page/courses
      /student/course_page/slots
      /student/course_page/detail

Digital assignments
-------------------

.. openapi:: ../openapi.json
   :paths:
      /student/digital_assignments
      /student/digital_assignments/course

Payments and outing
-------------------

.. openapi:: ../openapi.json
   :paths:
      /student/pending_payments
      /student/payment_receipts
      /student/general_outing_requests
      /student/weekend_outing_requests
