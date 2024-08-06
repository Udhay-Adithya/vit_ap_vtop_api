HEADERS = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
           'Connection':'close'}

#Main URL
VTOP_BASE_URL = 'https://vtop.vitap.ac.in'
VTOP_URL = 'https://vtop.vitap.ac.in/vtop/open/page'

#Login Page URL
VTOP_PRELOGIN_URL = 'https://vtop.vitap.ac.in/vtop/prelogin/setup'
VTOP_PRELOGIN_INIT_URL = 'https://vtop.vitap.ac.in/vtop/init/page'
VTOP_LOGIN_URL = 'https://vtop.vitap.ac.in/vtop/login'
VTOP_LOGIN_INIT_URL = 'https://vtop.vitap.ac.in/vtop/init/page'
VTOP_LOGIN_ERROR_URL = 'https://vtop.vitap.ac.in/vtop/login/error'

#Home Page URL
VTOP_HOME_URL ='https://vtop.vitap.ac.in/vtop/home'

#Content Page URL
VTOP_CONTENT_URL ='https://vtop.vitap.ac.in/vtop/content'

#Profile URL
PROFILE_URL = 'https://vtop.vitap.ac.in/vtop/studentsRecord/StudentProfileAllView'
STUDENT_IMAGE_UPLOAD_URL = 'https://vtop.vitap.ac.in/vtop/others/photo/getStudentIdPhotoAndSign1'

#Biometric Log URL
BIOMETRIC_LOG_URL='https://vtop.vitap.ac.in/vtop/academics/biometriclogdisplay'
GET_BIOMETRIC_LOG_URL='https://vtop.vitap.ac.in/vtop/getStudBioHistory'

#Proctor Details URL
MENTOR_DETAILS_URL = 'https://vtop.vitap.ac.in/vtop/proctor/viewProctorDetails'

#HOD Details URL
HOD_DETAILS_URL = 'https://vtop.vitap.ac.in/vtop/hrms/viewHodDeanDetails'

#Payment URL
PAYMENTS_URL = 'https://vtop.vitap.ac.in/vtop/finance/Payments'
PAYMENT_RECEIPT_URL = 'https://vtop.vitap.ac.in/vtop/p2p/getReceiptsApplno'
PRINT_PAYMENT_RECEIPT_URL = 'https://vtop.vitap.ac.in/vtop/finance/dupReceiptNewP2P'
VIRTUAL_ACCOUNT_URL = 'https://vtop.vitap.ac.in/vtop/admissions/studentVirtualAccountNo '

#Curriculum URL
CURRICULUM_URL = 'https://vtop.vitap.ac.in/vtop/academics/common/Curriculum'

#Time Table URL
TIME_TABLE_URL = 'https://vtop.vitap.ac.in/vtop/academics/common/StudentTimeTable'
GET_TIME_TABLE_URL = 'https://vtop.vitap.ac.in/vtop/processViewTimeTable'

#Exam Schedule URL
EXAM_SCHEDULE_URL = 'https://vtop.vitap.ac.in/vtop/examinations/StudExamSchedule'
GET_EXAM_SCHEDULE_URL = 'https://vtop.vitap.ac.in/vtop/examinations/doSearchExamScheduleForStudent'

#Attendance URL
ATTENDANCE_URL = 'https://vtop.vitap.ac.in/vtop/academics/common/StudentAttendance'
VIEW_ATTENDANCE_URL = 'https://vtop.vitap.ac.in/vtop/processViewStudentAttendance'

#Course Page URL
COURSE_PAGE_URL = 'https://vtop.vitap.ac.in/vtop/academics/common/StudentCoursePage'

#Makrs URL
MARKS_URL = 'https://vtop.vitap.ac.in/vtop/examinations/StudentMarkView'

#Grades URL
GRADE_HISTORY_URL = 'https://vtop.vitap.ac.in/vtop/examinations/examGradeView/StudentGradeHistory'

#Weekend Outing URL
WEEKEND_OUTING_URL = 'https://vtop.vitap.ac.in/vtop/hostel/StudentWeekendOuting'
SAVE_WEEKEND_OUTING_URL = 'https://vtop.vitap.ac.in/vtop/hostel/saveOutingForm'
EDIT_WEEKEND_OUTING_FORM = 'https://vtop.vitap.ac.in/vtop/hostel/updateBookingInfo'
DELETE_WEEKEND_OUTING_FORM = 'https://vtop.vitap.ac.in/vtop/hostel/deleteBookingInfo'


#General Outing URL
GENERAL_OUTING_URL = 'https://vtop.vitap.ac.in/vtop/hostel/StudentGeneralOuting'
SAVE_GENERAL_OUTING_URL='https://vtop.vitap.ac.in/vtop/hostel/saveGeneralOutingForm'
DELETE_GENERAL_OUTING_URL='https://vtop.vitap.ac.in/vtop/hostel/deleteGeneralOutingInfo'

#NCGPA Rank URL
NCGPA_RANK_URL='https://vtop.vitap.ac.in/vtop/hostels/counsellingSlotTimings1'


#Responses
{200:"Success",
404:'The origin server did not find a current representation for the target resource or is not willing to disclose that one exists'}

#Profile image path
PFP_PATH = "https://vtop.vitap.ac.in/vtop/users/image/?id="

#Semester Sub ID's
SemSubID = {'Short Summer Semester2 2023-24':'AP2023249'
,           'Fast Track Fall 2024-25':'AP2024251',
            'Long Summer Semester 2023-24':'AP20232410',
            'Short Summer Semester1 2023-24':'AP2023248',
          'WINTER SEM(2023-24) FRESHERS' : 'AP2023247',
          'WIN SEM (2023-24)':'AP2023246',
          'INTRA SEM (2023-24':'AP2023245',
          'Preference Purpose (2023-24':'AP2022233',
          'FALL SEM (2023-24) Freshers':'AP2023243',
          'FALL SEM (2023-24) Regular':'AP2023242',
          'FAST TRACK FALL II(2023-24)':'AP2023244',
          'SHORT SUMMER SEMESTER II (2022-23)':'AP20222310',
          'FAST TRACK FALL (2023-24':'AP2023241',
          'SHORT SUMMER SEMESTER I (2022-23)':'AP2022239',
          'LONG SUMMER SEMESTER (2022-23)':'AP2022238',
          'WIN SEM (2022-23) Freshers':'AP2022237',
          'WIN SEM (2022-23)':'AP2022236',
          'INTRA SEM (2022-23':'AP2022235',
          'FALL SEM (2022-23) Freshers':'AP2022234',
          'FALL SEM (2022-23)':'AP2022232',
          'FAST TRACK FALL (2022-23)':'AP2022231',
          'Short-Summer Semester 2021-22':'AP2021227',
          'Long-Summer Semester 2021-22':'AP2021228',
          'INTRA SEM (2021-22)':'AP2021229',
          'WIN SEM (2021-22) EAPCET':'AP2021226',
          'WIN SEM (2021-22)':'AP2021225',
          'FALL SEM (2021-22) EAPCET':'AP2021223',
          'FALL SEM (2021-22':'AP2021222',
          'SUMMER SEM1 (2020-21)':'AP2020217',
          'FAST TRACK FALL SEM (2021-22)':'AP2021221',
          'WIN SEM (2020-21)':'AP2020215',
          'INTRA SEM (2020-21)':'AP2020213',
          'FALL SEM (2020-21)':'AP2020211',
          'SUMMER SEM1 (2019-20)':'AP2019207',
          'WIN SEM  (2019-20)':'AP2019205',
          'FALL SEM (2019-20)':'AP2019201',
          'SUMMER SEM2 (2018-19)':'AP2018198',
          'SUMMER SEM1 (2018-19)':'AP2018197',
          'LONG SEM (2018-19)':'AP2018199',
          'WIN SEM (2018-19)':'AP2018195',
          'FALL SEM (2018-19)':'AP2018191',
          'SUMMER SEM2 (2017-18)':'AMR2018198',
          'SUMMER SEM1 (2017-18)':'AMR2018197',
          'WIN SEM (2017-18)':'AMR2017182',
          'FALL SEM (2017-18)':'AMR2017181',
          'TESTING':'AP20101101'
}