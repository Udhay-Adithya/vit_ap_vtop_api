import pandas as pd
from io import StringIO
from bs4 import BeautifulSoup
import json

html="""<html><head id="configHead">
    

        <meta charset="utf-8">
        <base href="https://vtop.vitap.ac.in/vtop/">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>VIT-AP - VTOP</title>
        <meta name="description" content="">
        <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
        <meta charset="ISO-8859-1">
        <meta name="description" content="vtop">
        <meta name="robots" content="NOODP,NOYDIR">
        <meta name="keywords" content=" vtop ">
        <meta name="robots" content="index, follow">
        <link rel="icon" type="image/png" href="assets/img/favicon.ico">
        <meta http-equiv="cache-control" content="max-age=0">
        <meta http-equiv="cache-control" content="no-cache">
        <meta http-equiv="expires" content="0">
        <meta http-equiv="X-UA-Compatible" content="IE-Edge">
    
    
        <link rel="stylesheet" type="text/css" href="/vtop/get/bs/css/1">
        <link rel="stylesheet" type="text/css" href="/vtop/assets/css/bootstrap3-iso.css">
        <link rel="stylesheet" type="text/css" href="/vtop/get/ic/css/1">
        <link rel="stylesheet" type="text/css" href="/vtop/get/ic/css/2">
        <link rel="stylesheet" type="text/css" href="/vtop/get/jq/css/1">
        <link rel="stylesheet" type="text/css" href="/vtop/get/bs/css/2">
        <link rel="stylesheet" type="text/css" href="/vtop/assets/css/menu.css">
        <link rel="stylesheet" type="text/css" href="/vtop/assets/css/AdminLteCompatibility.css">
        <link rel="stylesheet" type="text/css" href="/vtop/assets/css/scrollableTable.css">
        <link rel="stylesheet" type="text/css" href="/vtop/assets/css/VTop.css">
        <script type="text/javascript" src="/vtop/get/jq/js/1"></script>

    
<style data-jss="" data-meta="MuiDialog">
@media print {
  .MuiDialog-root {
    position: absolute !important;
  }
}
.MuiDialog-scrollPaper {
  display: flex;
  align-items: center;
  justify-content: center;
}
.MuiDialog-scrollBody {
  overflow-x: hidden;
  overflow-y: auto;
  text-align: center;
}
.MuiDialog-scrollBody:after {
  width: 0;
  height: 100%;
  content: "";
  display: inline-block;
  vertical-align: middle;
}
.MuiDialog-container {
  height: 100%;
  outline: 0;
}
@media print {
  .MuiDialog-container {
    height: auto;
  }
}
.MuiDialog-paper {
  margin: 32px;
  position: relative;
  overflow-y: auto;
}
@media print {
  .MuiDialog-paper {
    box-shadow: none;
    overflow-y: visible;
  }
}
.MuiDialog-paperScrollPaper {
  display: flex;
  max-height: calc(100% - 64px);
  flex-direction: column;
}
.MuiDialog-paperScrollBody {
  display: inline-block;
  text-align: left;
  vertical-align: middle;
}
.MuiDialog-paperWidthFalse {
  max-width: calc(100% - 64px);
}
.MuiDialog-paperWidthXs {
  max-width: 444px;
}
@media (max-width:507.95px) {
  .MuiDialog-paperWidthXs.MuiDialog-paperScrollBody {
    max-width: calc(100% - 64px);
  }
}
.MuiDialog-paperWidthSm {
  max-width: 600px;
}
@media (max-width:663.95px) {
  .MuiDialog-paperWidthSm.MuiDialog-paperScrollBody {
    max-width: calc(100% - 64px);
  }
}
.MuiDialog-paperWidthMd {
  max-width: 960px;
}
@media (max-width:1023.95px) {
  .MuiDialog-paperWidthMd.MuiDialog-paperScrollBody {
    max-width: calc(100% - 64px);
  }
}
.MuiDialog-paperWidthLg {
  max-width: 1280px;
}
@media (max-width:1343.95px) {
  .MuiDialog-paperWidthLg.MuiDialog-paperScrollBody {
    max-width: calc(100% - 64px);
  }
}
.MuiDialog-paperWidthXl {
  max-width: 1920px;
}
@media (max-width:1983.95px) {
  .MuiDialog-paperWidthXl.MuiDialog-paperScrollBody {
    max-width: calc(100% - 64px);
  }
}
.MuiDialog-paperFullWidth {
  width: calc(100% - 64px);
}
.MuiDialog-paperFullScreen {
  width: 100%;
  height: 100%;
  margin: 0;
  max-width: 100%;
  max-height: none;
  border-radius: 0;
}
.MuiDialog-paperFullScreen.MuiDialog-paperScrollBody {
  margin: 0;
  max-width: 100%;
}
</style></head>

<body class="overflow-auto" style="padding-top: 61px;">

    <input type="hidden" name="authorizedIDX" id="authorizedIDX" value="23BCE7625">

    <div class="container-fluid">
        <div class="row">
            <div class="col-xs-12  trim vh-100 vw-100 " id="page_outline">
                
                    <div id="page-holder">
                        
        <script>
            /*<![CDATA[*/

            var csrfName = "_csrf";
            var csrfValue = "0a2c7ca9-63f9-4419-ac9b-0cb93d3c9189";
            var id ="23BCE7625";
            var now = new Date();
            var params = csrfName + "=" + csrfValue + "&authorizedID=" + id + "&x=" + now.toUTCString();

            function home() {
                ajaxCall("/vtop/home", params, "page_outline");
            }

            /*]]>*/
        </script>
        <nav class="navbar navbar-expand-lg py-0 navbar-light bg-light headerBackgroundColor fixed-top shadow" id="vtopHeader" style="">
            <div class="container-fluid ms-0 ps-2">
                <button class="btn btn-sm bg-transparent d-none d-sm-block ms-0" type="button" data-bs-toggle="offcanvas" data-bs-target="#expandedSideBar" aria-controls="offcanvasExample">
                    <span class="text-light h4">☰ </span>
                </button>
                <button class="btn btn-sm bg-transparent d-block d-sm-none ms-0" type="button" onclick="javascript:getButtonBar();">
                    <span class="text-light h4">☰ </span>
                </button>
                <!-- <a class="navbar-brand px-0 pe-sm-1 mx-0 mx-sm-1" href="javacript:void(0);">
                    <img th:src="@{/assets/img/VITLogoEmblem.png}" class="img-responsive VITEmblem" alt="" />
                </a> -->
                
                <a class="navbar-brand" href="javacript:void(0);">
                    <img src="/vtop/assets/img/VIT_AP_logo.png" width="170px" alt="">
                </a>
                
                <!-- <a class="navbar-brand VITLogoStyle px-0 mx-0 text-light" href="javacript:void(0);"><span
                        class="h1 fw-bold">VIT</span>
                </a>
                <span class="navbar-text px-0 px-sm-2 mx-0 mx-sm-1 text-light">(AP Campus)</span> -->
                
                <a class="navbar-text" href="javascript:void(0);" onclick="javascript:home();"><i class="bi bi-house-door text-light ps-sm-3 h4" aria-hidden="true"></i></a>
                <a class="navbar-text" href="javascript:void(0);" id="printVTOPCoreDocument"><i class="bi bi-printer text-light ps-sm-3 h4" aria-hidden="true"></i></a>

                <button class="navbar-toggler mx-0 px-0" type="button" data-bs-toggle="collapse" data-bs-target="#vtopHeaderBarControl" aria-controls="vtopHeaderBarControl" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse navbar-collapse" id="vtopHeaderBarControl">
                    <div class="d-inline-block me-auto" id="quickLinks">
                        
                            <button class="btn btn-sm btn-outline ps-3 " data-bs-toggle="tooltip" data-bs-placement="top" title="add this menu to favourites" id="favouriteBtn"><span class="text-light">
                                    <i class="bi bi-star h4"></i>
                                    
                                    </span></button>
                            <div class="dropdown d-inline-block">
                                <button class="btn btn-outline-primary btn-sm dropdown-toggle text-light" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    <span class="text-light">Quick Links</span>
                                </button>
                                <ul class="dropdown-menu">
                                    
        
    
                                </ul>
                            </div>
                            <script type="text/javascript" src="/vtop/assets/js/favourite.js"></script>
                            
                        
                    </div>
                    <strong class="mx-auto fw-bold text-light bg-danger"></strong>
                    <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                        <li class="nav-item d-none d-sm-inline-block">
                            <img src="/vtop/users/image/?id=23BCE7625" class="img-circle img_icon_size" alt="User Image">
                        </li>
                        <li class="nav-item dropdown d-none d-sm-inline-block">
                            <a class="nav-link dropdown-toggle text-light" href="javascript:void(0);" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                <span class="navbar-text text-light small fw-bold">23BCE7625 (STUDENT)</span>
                            </a>
                            <ul class="dropdown-menu dropdown-menu-end headerBackgroundColor dropdownMenuBoxWidth" aria-labelledby="navbarDropdown">
                                <li class="dropdown-item disabled text-center"><img src="/vtop/users/image/?id=23BCE7625" class="img-circle img_stamp_size" alt="User Image"></li>
                                <li class="dropdown-item disabled text-center"><span class="dropdown-item text-light"></span></li>
                                <li>
                                    <hr class="dropdown-divider">
                                </li>
                                <li class="dropdown-item bg-transparent">
                                    <form class="text-center" id="logoutForm1" name="logoutForm1" method="post" action="/vtop/logout"><input type="hidden" name="_csrf" value="0a2c7ca9-63f9-4419-ac9b-0cb93d3c9189">
                                        <input type="hidden" name="_csrf" value="0a2c7ca9-63f9-4419-ac9b-0cb93d3c9189">
                                        <input type="hidden" name="authorizedID" id="authorizedID" value="23BCE7625">
                                        <div class="d-grid gap-2">
                                            
                                                <button class="btn btn-sm btn-info" id="historyBtn1" type="button">Login History</button>
                                                
                                            
                                            <button class="btn btn-success " type="submit">Sign out</button>
                                            
                                        </div>
                                    </form>
                                </li>
                            </ul>
                        </li>
                        <li class="nav-item disabled text-center  d-block d-sm-none"><img src="/vtop/users/image/?id=23BCE7625" class="img-circle img_stamp_size" alt="User Image"></li>
                        <li class="nav-item disabled text-center d-block d-sm-none"><span class="dropdown-item text-light"></span></li>
                        <li class="nav-item disabled text-center d-block d-sm-none">
                            <span class="navbar-text text-light small fw-bold">23BCE7625 (STUDENT)</span>
                        </li>
                        <li class="nav-item bg-transparent d-block d-sm-none">
                            <form class="text-center" id="logoutForm1" name="logoutForm1" method="post" `="" action="/vtop/logout"><input type="hidden" name="_csrf" value="0a2c7ca9-63f9-4419-ac9b-0cb93d3c9189">
                                <input type="hidden" name="_csrf" value="0a2c7ca9-63f9-4419-ac9b-0cb93d3c9189">
                                <input type="hidden" name="authorizedID" id="authorizedID" value="23BCE7625">
                                <div class="d-grid gap-2">
                                    
                                        <button class="btn btn-sm btn-info" id="historyBtn" type="button">Login History</button>
                                        
                                    
                                    <button class="btn btn-sm btn-success " type="submit">Sign out</button>
                                    
                                </div>
                            </form>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        <script type="text/javascript" src="/vtop/assets/js/vtopheader.js"></script>
    
                        
                            <div class="hstack">
                                <div class="vh-100 btnBarColor bg-opacity-25 shadow d-none d-sm-block" id="sidePanel">
                                    

        <div class="btn-toolbar mx-1" role="toolbar" aria-label="Toolbar with button groups">
            <div class="btn-group-vertical" role="group" aria-label="First group">

                
                    <div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-phone-square iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown"><a data-url="hrms/contactDetails" class="dropdown-item menuFontStyle systemB5BtnMenu *backColor*" href="javascript:void(0);"><i class="fa fa-phone-square iconSpace "></i> Contact Us</a></div></div>
                
                    <div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-briefcase iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown"><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> My Info </div>
                
                    <a data-url="studentsRecord/StudentProfileAllView" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Profile</a>
                
                    <a data-url="proctor/viewStudentCredentials" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Credentials</a>
                
                    <a data-url="admissions/studentVirtualAccountNo" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-bank iconSpace "></i> Virtual Account Number</a>
                
                    <a data-url="admissions/AcknowledgmentView" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Acknowledgement View</a>
                
                    <a data-url="studentBankInformation/BankInfoStudent" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Student Bank Info</a>
                
                    <a data-url="admissions/getStudentScholarshipDetails" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> My Scholarships</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-info-circle iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown"><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Info Corner </div>
                
                    <a data-url="academics/common/FaqPreview" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> FAQ</a>
                
                    <a data-url="academics/biometriclogdisplay" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-info-circle iconSpace "></i> Biometric Log</a>
                
                    <a data-url="admissions/costCentreCircularsViewPageController" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> General</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-paw iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown"><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Mentor </div>
                
                    <a data-url="proctor/viewProctorDetails" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Mentor Details</a>
                
                    <a data-url="proctor/viewMessagesSendByProctor" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Mentor Message</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-book iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown"><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Course Enrollment </div>
                
                    <a data-url="academics/exc/studentRegistration" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-info-circle iconSpace "></i> EXC Registration</a>
                
                    <a data-url="academics/mooc/studentRegistration" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> MOOC Registration</a>
                
                    <a data-url="academics/registration/wishlistRegPage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> WishList</a>
                
                    <a data-url="academics/withdraw/courseWithdraw" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Course Withdraw</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-graduation-cap iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown"><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Academics </div>
                
                    <a data-url="hrms/viewHodDeanDetails" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> HOD and Dean Info</a>
                
                    <a data-url="hrms/employeeSearchForStudent" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Faculty Info</a>
                
                    <a data-url="academics/common/StudentClassGrievance" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Course Feedback 24x7</a>
                
                    <a data-url="academics/common/BiometricInfo" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Biometric Info</a>
                
                    <a data-url="academics/common/StudentClassMessage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Class Messages</a>
                
                    <a data-url="academics/council/CouncilRegulationView/new" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Regulation</a>
                
                    <a data-url="academics/common/Curriculum" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> My Curriculum</a>
                
                    <a data-url="academics/additionalLearning/AdditionalLearningStudentView" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Minor/ Honour</a>
                
                    <a data-url="academics/common/StudentTimeTable" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Time Table</a>
                
                    <a data-url="academics/common/StudentAttendance" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Class Attendance</a>
                
                    <a data-url="academics/common/StudentCoursePage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Course Page</a>
                
                    <a data-url="internship/InternshipRegistration" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Industrial Internship </a>
                
                    <a data-url="academics/common/ProjectView" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Project</a>
                
                    <a data-url="examinations/StudentDA" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Digital Assignment Upload</a>
                
                    <a data-url="academics/common/QCMStudentLogin" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> QCM View </a>
                
                    <a data-url="set/setRegistrationViewPage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> SET Conference Registration</a>
                
                    <a data-url="academics/common/ExtraCurricular" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Co-Extra Curricular</a>
                
                    <a data-url="academics/common/CalendarPreview" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Academics Calendar</a>
                
                    <a data-url="academics/common/StudentRegistrationScheduleAllocation" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Registration Schedule &amp; Allocation</a>
                
                    <a data-url="academics/student/PJTReg/loadRegistrationPage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Project Course</a>
                
                    <a data-url="ecs/ecsRegistrationViewPage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> ECS Registration</a>
                
                    <a data-url="ecs/ecsHodViewDetailsPage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Faculty Acceptance Status</a>
                
                    <a data-url="ecs/StudentViewEcsReviewMarks" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> ECS Review  Marks</a>
                
                    <a data-url="inc/IncRegistration" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> INC Registration</a>
                
                    <a data-url="mooc/moocRegistration" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Mooc Course Regsitration</a>
                
                    <a data-url="capstone/capstoneRegistrationStdPage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Capstone Registration</a>
                
                    <a data-url="capstone/capstoneAcceptanceStdPage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Capstone Acceptance Status</a>
                
                    <a data-url="capstone/capstoneReviewMarksStdPage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Capstone Review Marks</a>
                
                    <a data-url="sdp/sdpRegistrationViewPage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> SDP Registration</a>
                
                    <a data-url="sdp/StudentViewSdpReviewMarks" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> SDP Review Marks</a>
                
                    <a data-url="sdp/sdpHodViewDetailsPage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> SDP Acceptance Status</a>
                
                    <a data-url="academics/summerInternship" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Summer Internship</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-bank iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown"><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Research </div>
                
                    <a data-url="examinations/invigilation/InvigilationDutyAllocationforfaculty" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-info-circle iconSpace "></i> Invigilation Duty Selection &amp; View</a>
                
                    <a data-url="research/researchProfile" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> My Research Profile</a>
                
                    <a data-url="admissions/semTransactionPageControllerGeneral" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> SEM Request</a>
                
                    <a data-url="research/CourseworkRegistration" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Course Work Registration</a>
                
                    <a data-url="research/CourseworkRegistrationViewtoScholar" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Registration Status</a>
                
                    <a data-url="research/scholarsMeetingView" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Meeting info</a>
                
                    <a data-url="hrms/bioForm/BioAttInfoEmp" class="dropdown-item menuFontStyle systemB5BtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-hourglass-end iconSpace "></i> Biometric Attendance Info</a>
                
                    <a data-url="hrms/researchStdLeaveRequest" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Research Std Leave Request</a>
                
                    <a data-url="research/researchLettersStudentView" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-file-text iconSpace "></i> Research Letters</a>
                
                    <a data-url="research/thesisSubmission" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Electronic Thesis Submission</a>
                
                    <a data-url="research/researchDocumentUpload" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Research Document Upload</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-book iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown"><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Examination </div>
                
                    <a data-url="examinations/StudExamSchedule" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Exam Schedule</a>
                
                    <a data-url="examinations/StudentMarkView" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Marks</a>
                
                    <a data-url="examinations/examGradeView/StudentGradeView" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Grades</a>
                
                    <a data-url="examinations/paperSeeing/PaperSeeing" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Paper See/Rev</a>
                
                    <a data-url="examinations/examGradeView/StudentGradeHistory" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Grade History</a>
                
                    <a data-url="examinations/projectFileUpload/ProjectView" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Project File Upload</a>
                
                    <a data-url="examinations/gotToMoocCourseInitial" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> MOOC File upload</a>
                
                    <a data-url="examinations/ecaUpload/viewCourse" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> ECA File Upload</a>
                
                    <a data-url="compre/eptScheduleShow" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> EPT schedule</a>
                
                    <div class="accordion" id="accordianHead_1001"><div class="accordion-item border-0"><div class="accordion-header" id="acItemHDG0071"><button class="accordion-button collapsed menuFontStyle py-2 ps-2 text-center bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acCollapseHDG0071" aria-expanded="false" aria-controls="acCollapseHDG0071"> &nbsp;&nbsp;&nbsp; <i class="fa fa-dot-circle-o iconSpace "></i><span class="ps-2 ms-1 fw-bold textColor1"> Comprehensive <span></span></span></button></div><div id="acCollapseHDG0071" class="accordion-collapse collapse" aria-labelledby="acItemHDG0071" data-bs-parent="#accordianHead_1001"><div class="accordion-body py-0 px-2">
                
                    <a data-url="compre/registrationForm" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Comprehensive Exam</a>
                
                    <a data-url="compre/studentExamInfo" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Exam Information</a>
                
                    </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acItemHDG0072"><button class="accordion-button collapsed menuFontStyle py-2 ps-2 text-center bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acCollapseHDG0072" aria-expanded="false" aria-controls="acCollapseHDG0072"> &nbsp;&nbsp;&nbsp; <i class="fa fa-dot-circle-o iconSpace "></i><span class="ps-2 ms-1 fw-bold textColor1"> Arrear/ReFAT Details <span></span></span></button></div><div id="acCollapseHDG0072" class="accordion-collapse collapse" aria-labelledby="acItemHDG0072" data-bs-parent="#accordianHead_1001"><div class="accordion-body py-0 px-2">
                
                    <div class="accordion" id="accordianHead_1002"><div class="accordion-item border-0"><div class="accordion-header" id="acItemHDG0074"><button class="accordion-button collapsed menuFontStyle py-2 ps-2 text-center bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acCollapseHDG0074" aria-expanded="false" aria-controls="acCollapseHDG0074"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <i class="fa fa-dot-circle-o iconSpace "></i><span class="ps-2 ms-1 fw-bold textColor1"> Regular Arrear/ReFAT <span></span></span></button></div><div id="acCollapseHDG0074" class="accordion-collapse collapse" aria-labelledby="acItemHDG0074" data-bs-parent="#accordianHead_1002"><div class="accordion-body py-0 px-2">
                
                    <a data-url="examinations/arrearRegistration/RegularArrearStudentReg" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Registration</a>
                
                    <a data-url="examinations/arrearRegistration/LoadRegularArrearViewPage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Registration Details</a>
                
                    <a data-url="examinations/arrearRegistration/viewRARExamSchedule" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Exam Schedule</a>
                
                    <a data-url="examinations/arrearRegistration/StudentArrearGradeView" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Grade View</a>
                
                    <a data-url="examinations/regularArrear/RegularArrearPaperSeeing" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Paper See/Rev</a>
                
                    </div></div></div></div></div></div></div><a data-url="examinations/reFAT/StudentReFATRequestPageController" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Re-Exam Application</a>
                
                    </div></div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-bank iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown"><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Library </div>
                
                    <a data-url="hrms/onlineBookRecommendation" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Online Book Recommendation</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-space-shuttle iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown"><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Services </div>
                
                    <a data-url="phyedu/facilityAvailable" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Facility Registration</a>
                
                    <a data-url="transport/transportRegistration" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Transport Registration</a>
                
                    <a data-url="pat/PatRegistrationProcess" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> PAT Registration</a>
                
                    <a data-url="internship/CollectOfferLetter" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Upload Offer Letter</a>
                
                    <a data-url="alumni/alumniTranscriptPageControl" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Transcript Request</a>
                
                    <a data-url="admissions/scholarshipPageController" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Financial Assistance Scholarship</a>
                
                    <a data-url="admissions/SpecialAchieversAwards" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Achievements</a>
                
                    <a data-url="admissions/programmeMigration" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Programme Migration</a>
                
                    <a data-url="hostels/late/hour/student/request/1" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Late Hour Request</a>
                
                    <a data-url="vitaa/finalyearcheck" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Final Year Registration</a>
                
                    <div class="accordion" id="accordianHead_1003"><div class="accordion-item border-0"><div class="accordion-header" id="acItemOTH0049"><button class="accordion-button collapsed menuFontStyle py-2 ps-2 text-center bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acCollapseOTH0049" aria-expanded="false" aria-controls="acCollapseOTH0049"> &nbsp;&nbsp;&nbsp; <i class="fa fa-dot-circle-o iconSpace "></i><span class="ps-2 ms-1 fw-bold textColor1"> SAP Application <span></span></span></button></div><div id="acCollapseOTH0049" class="accordion-collapse collapse" aria-labelledby="acItemOTH0049" data-bs-parent="#accordianHead_1003"><div class="accordion-body py-0 px-2">
                
                    <a data-url="sap/SapManage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> SAP Project</a>
                
                    <a data-url="sap/SapCreditManage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Apply Credit Transfer</a>
                
                    </div></div></div><a data-url="admissions/reserachFresherCertUpload" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Certificate Upload</a>
                
                    <a data-url="others/esanad/doApply" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> eSanad Request</a>
                
                    </div></div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-certificate iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown"><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Bonafide </div>
                
                    <a data-url="others/bonafide/StudentBonafidePageControl" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Apply Bonafide</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-money iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown"><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Online Payments </div>
                
                    <a data-url="finance/Payments" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Payments</a>
                
                    <a data-url="p2p/getReceiptsApplno" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Payment Receipts</a>
                
                    <a data-url="finance/getFeesIntimation" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Fees Intimation</a>
                
                    <a data-url="finance/getOnlineTransfer" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Online Transfer</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-home iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown"><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Hostels </div>
                
                    <a data-url="hostel/StudentWeekendOuting" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Weekend Outing</a>
                
                    <a data-url="hostel/StudentGeneralOuting" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> General Outing</a>
                
                    <a data-url="hostels/HostelStudentRoomView" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Hostel Room Info 2023-24</a>
                
                    <a data-url="hostels/counsellingSlotTimings1" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> NCGPA RANK View 2023-24</a>
                
                    <a data-url="hostels/room/booking/NcgpaStudentCounselling" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> NCGPA Hostel Booking 23-24</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-book iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown"><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> ASC FDP </div>
                
                    <a data-url="events/ASC/EventsRegistration" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> FDP Registration</a>
                
                    <a data-url="events/ASC/EventsCertificateDownload" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Participant Certificate</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-shield iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown"><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Events </div>
                
                    <a data-url="events/sixsigma/loadStudentViewPage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> SixSigma Certificate</a>
                
                    <div class="accordion" id="accordianHead_1004"><div class="accordion-item border-0"><div class="accordion-header" id="acItemEVE0075"><button class="accordion-button collapsed menuFontStyle py-2 ps-2 text-center bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acCollapseEVE0075" aria-expanded="false" aria-controls="acCollapseEVE0075"> &nbsp;&nbsp;&nbsp; <i class="fa fa-dot-circle-o iconSpace "></i><span class="ps-2 ms-1 fw-bold textColor1"> University Day <span></span></span></button></div><div id="acCollapseEVE0075" class="accordion-collapse collapse" aria-labelledby="acItemEVE0075" data-bs-parent="#accordianHead_1004"><div class="accordion-body py-0 px-2">
                
                    <a data-url="event/uday/certificates" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> eCertificates</a>
                
                    </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acItemOTH0040"><button class="accordion-button collapsed menuFontStyle py-2 ps-2 text-center bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acCollapseOTH0040" aria-expanded="false" aria-controls="acCollapseOTH0040"> &nbsp;&nbsp;&nbsp; <i class="fa fa-graduation-cap iconSpace "></i><span class="ps-2 ms-1 fw-bold textColor1"> Convocation <span></span></span></button></div><div id="acCollapseOTH0040" class="accordion-collapse collapse" aria-labelledby="acItemOTH0040" data-bs-parent="#accordianHead_1004"><div class="accordion-body py-0 px-2">
                
                    <a data-url="convocation/entryPage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Registration</a>
                
                    </div></div></div></div></div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-trophy iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown"><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> SW Events </div>
                
                    <a data-url="event/swf/student/loadClubChapterEnrollmentPage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Club/Chapter Enrollment</a>
                
                    <a data-url="event/swf/loadRequisitionPage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Event Requisition</a>
                
                    <a data-url="event/swf/loadEventAttendance" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Event Attendance</a>
                
                    <a data-url="event/swf/loadEventRegistration" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Event Registration</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-lock iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown"><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> My Account </div>
                
                    <a data-url="controlpanel/ChangePassword" class="dropdown-item menuFontStyle systemB5BtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-lock iconSpace "></i> Change Password</a>
                
                    <a data-url="controlpanel/ChangePreferredUser" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-lock iconSpace "></i> Update LoginID</a></div></div>
                

            </div>
        </div>

        <script>
            /*<![CDATA[*/

            var actionButton = document.getElementsByClassName("systemBtnMenu"); 
            for (let i = 0; i < actionButton.length; i++) {
                actionButton[i].addEventListener('click', assembleData, false);
            }

            var actionButton2 = document.getElementsByClassName("systemB5BtnMenu"); 
            for (let i = 0; i < actionButton2.length; i++) {
                actionButton2[i].addEventListener('click', assembleDataForB5, false);
            }

            function assembleData() {
                var authorizedID = $("#authorizedIDX").val();
                let csrfName = "_csrf";
                let csrfValue = "0a2c7ca9-63f9-4419-ac9b-0cb93d3c9189";
                var dataText = "verifyMenu=true&authorizedID=" + authorizedID +"&"+ csrfName + '=' + csrfValue+"&nocache=@(new Date().getTime())"
                let url = this.dataset.url;
                ajaxCall(url, dataText);
                $(this).closest('.dropdown-menu.show').removeClass('show');
                $(this).closest('.btn-group.dropend').children(".SideBarMenuBtn.show").removeClass('show');
                $(this).closest('.btn-group.dropend').children(".SideBarMenuBtn").attr("aria-expanded","false");
                var btnBarElem=document.getElementById("sidePanel");
                if(!btnBarElem.classList.contains("d-none")) {
                    btnBarElem.classList.add("d-none");
                }
            }

            function assembleDataForB5() {
                var authorizedID = $("#authorizedIDX").val();
                let csrfName = "_csrf";
                let csrfValue = "0a2c7ca9-63f9-4419-ac9b-0cb93d3c9189";
                var dataText = "verifyMenu=true&authorizedID=" + authorizedID +"&"+ csrfName + '=' + csrfValue+"&nocache=@(new Date().getTime())"
                let url = this.dataset.url;
                ajaxB5Call(url, dataText);
                //$(this).parents().find('.show').removeClass('show');
                $(this).closest('.dropdown-menu.show').removeClass('show');
                $(this).closest('.btn-group.dropend').children(".SideBarMenuBtn.show").removeClass('show');
                $(this).closest('.btn-group.dropend').children(".SideBarMenuBtn").attr("aria-expanded","false");
                
                
                var btnBarElem=document.getElementById("sidePanel");
                if(!btnBarElem.classList.contains("d-none")) {
                    btnBarElem.classList.add("d-none");
                }

            }


            /*]]>*/
        </script>


    
                                </div>
                                <div class="vh-100 vw-100 p-0 mx-0 mt-0" id="core-container">
                                    <div class="overflow-auto vh-100 pb-5 mb-5 showBlock" id="b3wrapper">
                                        <div class="bootstrap3-iso" id="page-wrapper">


		
		<link rel="stylesheet" href="assets/css/validationEngine.jquery.css">	
		<link rel="stylesheet" href="assets/css/sweetalert.css">	
				<style>h3.box-title{ text-transform: capitalize;}</style>
		
    		
		<script src="assets/js/jquery.validationEngine.js"></script>
		<script src="assets/js/sweetalert.min.js"></script>
		<script src="assets/js/validate2.js"></script>	
		<script type="text/javascript" src="/vtop/assets/js/jquery.validationEngine-en.js"></script>		
   	
    


<div id="main-section">

		<section class="content">
			<div class="col-sm-12">
				
				<div class="box box-info">
					<div class="box-header with-border">
						<h3 class="box-title">Time Table</h3>
					</div>

					<div class="box-body">
												
							<form class="form-horizontal" method="post" id="studentTimeTable" name="studentTimeTable" autocomplete="off">
								<input type="hidden" name="_csrf" value="0a2c7ca9-63f9-4419-ac9b-0cb93d3c9189">
								<input type="hidden" name="authorizedID" id="authorizedID" value="23BCE7625">
								
									<!-- Semester Sub Id -->
									<div class="form-groups">
										<label for="semesterSubId" class="col-md-3 control-label" style="text-align: left;">Semester &nbsp;
											<br><span style="color: red; font-weight: normal;">* Only Registered Semester</span>
										</label>
											
										<div class="col-md-9 form-group">
											<select class="form-select" name="semesterSubId" id="semesterSubId" data-validation-engine="validate[required]" onchange="processViewTimeTable();">
												<option value="" selected="selected">--Choose Semester--</option>
												<option value="AP2023247">WIN  SEM (2023-24) FRESHERS</option>
												<option value="AP2023243">FALL SEM (2023-24) Freshers</option>
											</select>

										</div>
									</div>
									
							</form>

						<!-- loadMyFragment -->
						<div class="form-group" id="loadMyFragment"><div class="form-group" id="getStudentDetails">
								
								<div id="studentDetailsList">
										
									<div>
										<span style="font-size: 12px;"><b style="color: red;">Note:</b></span>
										<ul style="font-size: 12px;"> 
											<li style="text-align: justify;">Students are required to generate the invoice and then proceed to pay 
												the required course fee.  Registration is confirmed only if status of the course is 
												<strong style="color: green;">'Registered and Approved'</strong> (in regular cases) or 
												<strong style="color: green;">'Registered, Invoice Generated, Fees Paid and Approved'</strong> 
												(when there is a requirement for course fee payment).</li>
											
										</ul>
									</div><br>
									
									<div class="table-responsive">
										<table class="table" style="background-color: #fff; border: 1px solid #ddd; font-size: 12px; padding: 4px; text-align: center;">
										<tbody><tr>
												
												
										</tr>
									
										
											<tr style="background-color: #3c8dbc; color: #fff;border:1px solid #b2b2b2;">
												<th style="vertical-align: middle; text-align: center; border-right: 1px solid #b2b2b2; padding: 5px; width: 1%;">Sl.No</th>
												<th style="vertical-align: middle; text-align: center; border-right: 1px solid #b2b2b2; padding: 5px; width: 5%;">Class Group</th>
												<th style="vertical-align: middle; text-align: center; border-right: 1px solid #b2b2b2; padding: 5px; width: 20%;">Course</th>
												<th style="vertical-align: middle; text-align: center; border-right: 1px solid #b2b2b2; padding: 5px; width:0%;">L T P J C</th>
												<th style="vertical-align: middle; text-align: center; border-right: 1px solid #b2b2b2; padding: 5px; width:5%;">Category</th>
												<th style="vertical-align: middle; text-align: center; border-right: 1px solid #b2b2b2; padding: 5px; width:5%;">Course Option</th>
												<th style="vertical-align: middle; text-align: center; border-right: 1px solid #b2b2b2; padding: 5px; width:5%;">Class Nbr</th>	
												<th style="vertical-align: middle; text-align: center; border-right: 1px solid #b2b2b2; padding: 5px; width:10%;">Slot  - <br>Venue</th>
												<th style="vertical-align: middle; text-align: center; border-right: 1px solid #b2b2b2; padding: 5px; width:15%;">Faculty Details</th>
												<th style="vertical-align: middle; text-align: center; border-right: 1px solid #b2b2b2; padding: 5px; width:10%;">
													Registered / Updated Date &amp; Time 
												</th>
												<th style="vertical-align: middle; text-align: center; border-right: 1px solid #b2b2b2; padding: 5px; width:10%;">
													Attendance Date - Type</th>
												<th style="vertical-align: middle; text-align: center; border-right: 1px solid #b2b2b2; padding: 5px; width:10%;">Status &amp; Ref No </th>
											</tr>
										
										<tr>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">1</p>
											</td>
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">General (Semester)</p>
											</td>
											
											<td style="padding: 3px; font-size: 12px; border-color: #b2b2b2;vertical-align: middle;">
												<p style="margin: 0px;">CHY1009 - Chemistry and Environmental Studies</p>
												<p style="margin: 0px; font-weight: bolder;"> ( Embedded Theory ) </p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">3 0 0 0 3.0</p>
											</td>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												
												
													<span>-</span>
												
												
										
												
										
											
											</td>																
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">Regular</p>
																								
											</td>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">AP2023247000169</p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">D1+TD1 - </p><br>
												<p style="margin: 0px; font-weight: bolder;">105-AB-2</p>
											</td>
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">			
												
													<p style="margin: 0px;">Prof.V V Sreenivasu M - </p><br>
													<p style="margin: 0px; font-weight: bolder;">SAS</p>
												
																							
											</td>
											
										
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;white-space: nowrap;">
												<p style="margin: 0px;">05-Feb-2024 00:00</p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 3px; white-space: nowrap;">
												<p style="margin: 0px;">
													<span>06-Feb-2024</span><br>
													<strong> - Biometric</strong>
												</p>
												
											</td>
											
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; border-right :2px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">
													<span style="color:red;">Subject to Offering</span><br>
													 
												</p>
												
											</td>
										</tr>
										
										<tr>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">2</p>
											</td>
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">General (Semester)</p>
											</td>
											
											<td style="padding: 3px; font-size: 12px; border-color: #b2b2b2;vertical-align: middle;">
												<p style="margin: 0px;">CHY1009 - Chemistry and Environmental Studies</p>
												<p style="margin: 0px; font-weight: bolder;"> ( Embedded Lab ) </p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">0 0 2 0 1.0</p>
											</td>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												
												
													<span>-</span>
												
												
										
												
										
											
											</td>																
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">Regular</p>
																								
											</td>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">AP2023247000533</p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">L51+L52 - </p><br>
												<p style="margin: 0px; font-weight: bolder;">123-CB</p>
											</td>
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">			
												
													<p style="margin: 0px;">Prof.Sabeel M Basheer - </p><br>
													<p style="margin: 0px; font-weight: bolder;">SAS</p>
												
																							
											</td>
											
										
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;white-space: nowrap;">
												<p style="margin: 0px;">07-Feb-2024 00:00</p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 3px; white-space: nowrap;">
												<p style="margin: 0px;">
													<span>08-Feb-2024</span><br>
													<strong> - Biometric</strong>
												</p>
												
											</td>
											
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; border-right :2px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">
													<span style="color:red;">Subject to Offering</span><br>
													 
												</p>
												
											</td>
										</tr>
										
										<tr>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">3</p>
											</td>
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">General (Semester)</p>
											</td>
											
											<td style="padding: 3px; font-size: 12px; border-color: #b2b2b2;vertical-align: middle;">
												<p style="margin: 0px;">CSE2005 - Object Oriented Programming</p>
												<p style="margin: 0px; font-weight: bolder;"> ( Embedded Theory ) </p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">3 0 0 0 3.0</p>
											</td>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												
												
													<span>-</span>
												
												
										
												
										
											
											</td>																
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">Regular</p>
																								
											</td>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">AP2023247000024</p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">A1+TA1 - </p><br>
												<p style="margin: 0px; font-weight: bolder;">420-AB-1</p>
											</td>
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">			
												
													<p style="margin: 0px;">DR. SANJEEV KUMAR DWIVEDI - </p><br>
													<p style="margin: 0px; font-weight: bolder;">SCOPE</p>
												
																							
											</td>
											
										
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;white-space: nowrap;">
												<p style="margin: 0px;">05-Feb-2024 00:00</p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 3px; white-space: nowrap;">
												<p style="margin: 0px;">
													<span>06-Feb-2024</span><br>
													<strong> - Biometric</strong>
												</p>
												
											</td>
											
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; border-right :2px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">
													<span style="color:red;">Subject to Offering</span><br>
													 
												</p>
												
											</td>
										</tr>
										
										<tr>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">4</p>
											</td>
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">General (Semester)</p>
											</td>
											
											<td style="padding: 3px; font-size: 12px; border-color: #b2b2b2;vertical-align: middle;">
												<p style="margin: 0px;">CSE2005 - Object Oriented Programming</p>
												<p style="margin: 0px; font-weight: bolder;"> ( Embedded Lab ) </p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">0 0 2 0 1.0</p>
											</td>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												
												
													<span>-</span>
												
												
										
												
										
											
											</td>																
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">Regular</p>
																								
											</td>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">AP2023247000641</p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">L57+L58 - </p><br>
												<p style="margin: 0px; font-weight: bolder;">119-AB-1</p>
											</td>
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">			
												
													<p style="margin: 0px;">VODDELLI SRILAKSHMI - </p><br>
													<p style="margin: 0px; font-weight: bolder;">SCOPE</p>
												
																							
											</td>
											
										
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;white-space: nowrap;">
												<p style="margin: 0px;">07-Feb-2024 00:00</p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 3px; white-space: nowrap;">
												<p style="margin: 0px;">
													<span>08-Feb-2024</span><br>
													<strong> - Biometric</strong>
												</p>
												
											</td>
											
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; border-right :2px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">
													<span style="color:red;">Subject to Offering</span><br>
													 
												</p>
												
											</td>
										</tr>
										
										<tr>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">5</p>
											</td>
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">General (Semester)</p>
											</td>
											
											<td style="padding: 3px; font-size: 12px; border-color: #b2b2b2;vertical-align: middle;">
												<p style="margin: 0px;">ECE1003 - Digital Logic Design</p>
												<p style="margin: 0px; font-weight: bolder;"> ( Embedded Theory ) </p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">3 0 0 0 3.0</p>
											</td>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												
												
													<span>-</span>
												
												
										
												
										
											
											</td>																
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">Regular</p>
																								
											</td>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">AP2023247000213</p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">C1+TC1 - </p><br>
												<p style="margin: 0px; font-weight: bolder;">135-AB-1</p>
											</td>
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">			
												
													<p style="margin: 0px;">Prof.Suseela Vappangi - </p><br>
													<p style="margin: 0px; font-weight: bolder;">SENSE</p>
												
																							
											</td>
											
										
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;white-space: nowrap;">
												<p style="margin: 0px;">05-Feb-2024 00:00</p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 3px; white-space: nowrap;">
												<p style="margin: 0px;">
													<span>06-Feb-2024</span><br>
													<strong> - Biometric</strong>
												</p>
												
											</td>
											
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; border-right :2px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">
													<span style="color:red;">Subject to Offering</span><br>
													 
												</p>
												
											</td>
										</tr>
										
										<tr>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">6</p>
											</td>
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">General (Semester)</p>
											</td>
											
											<td style="padding: 3px; font-size: 12px; border-color: #b2b2b2;vertical-align: middle;">
												<p style="margin: 0px;">ECE1003 - Digital Logic Design</p>
												<p style="margin: 0px; font-weight: bolder;"> ( Embedded Lab ) </p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">0 0 2 0 1.0</p>
											</td>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												
												
													<span>-</span>
												
												
										
												
										
											
											</td>																
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">Regular</p>
																								
											</td>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">AP2023247000555</p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">L41+L42 - </p><br>
												<p style="margin: 0px; font-weight: bolder;">201-AB-2</p>
											</td>
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">			
												
													<p style="margin: 0px;">MR TIMITI VAMSI KRISHNA - </p><br>
													<p style="margin: 0px; font-weight: bolder;">SENSE</p>
												
																							
											</td>
											
										
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;white-space: nowrap;">
												<p style="margin: 0px;">07-Feb-2024 00:00</p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 3px; white-space: nowrap;">
												<p style="margin: 0px;">
													<span>08-Feb-2024</span><br>
													<strong> - Biometric</strong>
												</p>
												
											</td>
											
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; border-right :2px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">
													<span style="color:red;">Subject to Offering</span><br>
													 
												</p>
												
											</td>
										</tr>
										
										<tr>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">7</p>
											</td>
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">General (Semester)</p>
											</td>
											
											<td style="padding: 3px; font-size: 12px; border-color: #b2b2b2;vertical-align: middle;">
												<p style="margin: 0px;">ENG2001 - English for Professional Communication</p>
												<p style="margin: 0px; font-weight: bolder;"> ( Embedded Theory ) </p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">2 0 0 0 2.0</p>
											</td>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												
												
													<span>-</span>
												
												
										
												
										
											
											</td>																
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">Regular</p>
																								
											</td>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">AP2023247000348</p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">F1 - </p><br>
												<p style="margin: 0px; font-weight: bolder;">416-AB-1</p>
											</td>
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">			
												
													<p style="margin: 0px;">Prof.Rakhi N K - </p><br>
													<p style="margin: 0px; font-weight: bolder;">VISH</p>
												
																							
											</td>
											
										
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;white-space: nowrap;">
												<p style="margin: 0px;">05-Feb-2024 00:00</p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 3px; white-space: nowrap;">
												<p style="margin: 0px;">
													<span>06-Feb-2024</span><br>
													<strong> - Biometric</strong>
												</p>
												
											</td>
											
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; border-right :2px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">
													<span style="color:red;">Subject to Offering</span><br>
													 
												</p>
												
											</td>
										</tr>
										
										<tr>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">8</p>
											</td>
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">General (Semester)</p>
											</td>
											
											<td style="padding: 3px; font-size: 12px; border-color: #b2b2b2;vertical-align: middle;">
												<p style="margin: 0px;">ENG2001 - English for Professional Communication</p>
												<p style="margin: 0px; font-weight: bolder;"> ( Embedded Lab ) </p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">0 0 2 0 1.0</p>
											</td>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												
												
													<span>-</span>
												
												
										
												
										
											
											</td>																
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">Regular</p>
																								
											</td>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">AP2023247000472</p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">L33+L34 - </p><br>
												<p style="margin: 0px; font-weight: bolder;">117-AB-2</p>
											</td>
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">			
												
													<p style="margin: 0px;">DR.PRAGNYA PARIMITA CHAYANI - </p><br>
													<p style="margin: 0px; font-weight: bolder;">VISH</p>
												
																							
											</td>
											
										
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;white-space: nowrap;">
												<p style="margin: 0px;">08-Feb-2024 00:00</p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 3px; white-space: nowrap;">
												<p style="margin: 0px;">
													<span>08-Feb-2024</span><br>
													<strong> - Biometric</strong>
												</p>
												
											</td>
											
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; border-right :2px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">
													<span style="color:red;">Subject to Offering</span><br>
													 
												</p>
												
											</td>
										</tr>
										
										<tr>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">9</p>
											</td>
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">General (Semester)</p>
											</td>
											
											<td style="padding: 3px; font-size: 12px; border-color: #b2b2b2;vertical-align: middle;">
												<p style="margin: 0px;">MAT1002 - Applications of differential and difference equations</p>
												<p style="margin: 0px; font-weight: bolder;"> ( Theory Only ) </p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">4 0 0 0 4.0</p>
											</td>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												
												
													<span>-</span>
												
												
										
												
										
											
											</td>																
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">Regular</p>
																								
											</td>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">AP2023247000093</p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">B1+TB1+TBB1 - </p><br>
												<p style="margin: 0px; font-weight: bolder;">115-AB-2</p>
											</td>
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">			
												
													<p style="margin: 0px;">Prof.Soumen Kundu - </p><br>
													<p style="margin: 0px; font-weight: bolder;">SAS</p>
												
																							
											</td>
											
										
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;white-space: nowrap;">
												<p style="margin: 0px;">05-Feb-2024 00:00</p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 3px; white-space: nowrap;">
												<p style="margin: 0px;">
													<span>06-Feb-2024</span><br>
													<strong> - Biometric</strong>
												</p>
												
											</td>
											
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; border-right :2px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">
													<span style="color:red;">Subject to Offering</span><br>
													 
												</p>
												
											</td>
										</tr>
										
										<tr>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">10</p>
											</td>
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">General (Semester)</p>
											</td>
											
											<td style="padding: 3px; font-size: 12px; border-color: #b2b2b2;vertical-align: middle;">
												<p style="margin: 0px;">STS1009 - Introduction to Quantitative, Logical and Verbal Ability</p>
												<p style="margin: 0px; font-weight: bolder;"> ( Theory Only ) </p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">3 0 0 0 3.0</p>
											</td>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												
												
													<span>-</span>
												
												
										
												
										
											
											</td>																
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">Regular</p>
																								
											</td>
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">AP2023247000297</p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">E1+TEE1 - </p><br>
												<p style="margin: 0px; font-weight: bolder;">135-AB-1</p>
											</td>
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;">			
												
													<p style="margin: 0px;">Prof Hariharan - </p><br>
													<p style="margin: 0px; font-weight: bolder;">VISH</p>
												
																							
											</td>
											
										
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px;white-space: nowrap;">
												<p style="margin: 0px;">05-Feb-2024 00:00</p>
											</td>
											
											<td style="vertical-align: middle; border: 1px solid #b2b2b2; padding: 3px; white-space: nowrap;">
												<p style="margin: 0px;">
													<span>06-Feb-2024</span><br>
													<strong> - Biometric</strong>
												</p>
												
											</td>
											
											<td style="text-align:left; vertical-align: middle; border: 1px solid #b2b2b2; border-right :2px solid #b2b2b2; padding: 5px;">
												<p style="margin: 0px;">
													<span style="color:red;">Subject to Offering</span><br>
													 
												</p>
												
											</td>
										</tr>
										<tr>
											<td style="background-color: #3c8dbc; color: #fff;vertical-align: middle; border: 1px solid #b2b2b2; padding: 5px; font-size: 14px;" colspan="16"><span>Total Number Of Credits: </span> <b><span>22.0</span></b></td>
										</tr>
										
									<tr>
										
										
									</tr>
									
									</tbody></table>
									</div>						
									
	
									<div class="table table-responsive" id="ttview" style="margin-top: 20px;float: left;width: 100%;">
										 
   		 
   		 			 
   		 					  		 							
							<table id="timeTableStyle" class="w3-table-all w3-card-4 w3-hoverable" style="border: 2px solid #3c8dbc; text-align: center; font-size: 12px; margin-bottom: 20px;width:100%;">
								
								
									
								<tbody><tr>	
									<td rowspan="2" bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
										vertical-align: middle; padding: 3px; width: 50px;">THEORY</td>
									
									<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
										vertical-align: middle; padding: 3px; width: 50px;">Start</td>
									
									
										
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">08:00</td>
										
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">09:00</td>
										
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">09:01</td>
										
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">10:00</td>
										
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">10:01</td>
										
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">11:00</td>
										
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">11:01</td>
										
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">12:00</td>
										
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">13:00</td>
											
										
										
											
										
										
										
									
										
										
											
										
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">Lunch</td>
											
										
										
										
									
										
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">14:00</td>
										
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">14:01</td>
										
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">15:00</td>
										
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">15:01</td>
										
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">16:00</td>
										
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">16:01</td>
										
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">17:00</td>
										
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">18:00</td>
										
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">19:00</td>
											
										
										
											
										
										
										
									
								</tr>
								
								<tr>
									<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
										vertical-align: middle; padding: 3px; width: 50px;">End</td>
																		
									
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">08:50</td>
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">09:50</td>
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">09:51</td>
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">10:50</td>
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">10:51</td>
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">11:50</td>
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">11:51</td>
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">12:50</td>
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">13:50</td>
											
										
										
											
										
										
											
									
										
											
										
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">Lunch</td>
											
										
										
											
									
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">14:50</td>
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">14:51</td>
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">15:50</td>
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">15:51</td>
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">16:50</td>
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">16:51</td>
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">17:50</td>
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">18:50</td>
										<td bgcolor="#CCCCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">19:50</td>
											
										
										
											
										
										
											
									
									
								</tr>
								
									
								<tr>	
									<td rowspan="2" bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
										vertical-align: middle; padding: 3px; width: 50px;">LAB</td>
									
									<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
										vertical-align: middle; padding: 3px; width: 50px;">Start</td>
									
									
										
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">08:00</td>
										
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">08:50</td>
										
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">08:51</td>
										
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">10:00</td>
										
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">10:01</td>
										
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">10:50</td>
										
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">10:51</td>
										
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">12:00</td>
										
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">12:50</td>
											
										
										
											
										
										
										
									
										
										
											
										
										
											
										
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">Lunch</td>
										
									
										
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">14:00</td>
										
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">14:01</td>
										
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">14:50</td>
										
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">14:51</td>
										
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">16:00</td>
										
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">16:01</td>
										
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">16:50</td>
										
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">18:00</td>
										
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">18:50</td>
											
										
										
											
										
										
										
									
								</tr>
								
								<tr>
									<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
										vertical-align: middle; padding: 3px; width: 50px;">End</td>
																		
									
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">08:50</td>
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">09:40</td>
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">09:41</td>
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">10:50</td>
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">10:51</td>
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">11:40</td>
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">11:41</td>
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">12:50</td>
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">13:30</td>
											
										
										
											
										
										
											
									
										
											
										
										
											
										
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">Lunch</td>
											
									
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">14:50</td>
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">14:51</td>
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">15:40</td>
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">15:41</td>
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">16:50</td>
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">16:51</td>
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">17:40</td>
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">18:50</td>
										<td bgcolor="#99CCFF" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">19:30</td>
											
										
										
											
										
										
											
									
									
								</tr>
								
								
								
									
									
										
									<tr style="background-color: #FFFFCC;">
									
										<td rowspan="2" bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">TUE</td>
										<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">THEORY</td>
											
										
										
											
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TF1</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TA1-CSE2005-ETH-420-AB-1-ALL</td>
													
												
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">_</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">E1-STS1009-TH-135-AB-1-ALL</td>
													
												
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">STC2</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">D1-CHY1009-ETH-105-AB-2-ALL</td>
													
												
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">__</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">B1-MAT1002-TH-115-AB-2-ALL</td>
													
												
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">___</td>
													
											
											
											
											
										
											
											
											
											
											<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
												vertical-align: middle; padding: 3px; width: 50px;">Lunch</td>
										
											
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TA2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">____</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">E2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">STC1</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">D2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">_____</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">B2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TF2</td>
													
											
											
											<td style="border: 1px solid #3c8dbc; text-align: center; 
												vertical-align: middle; padding: 3px; width: 50px;">-</td>
											
										
										
									</tr>
									
									
									
										
									<tr style="background-color: #FFFFCC;">
									
										
										<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">LAB</td>
											
										
										
											
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L1</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L2</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">-</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L3</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">--</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L4</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">---</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L5</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L6</td>
													
											
											
											
											
										
											
											
											
											
											<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
												vertical-align: middle; padding: 3px; width: 50px;">Lunch</td>
										
											
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L31</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">----</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L32</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">-----</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L33-ENG2001-ELA-117-AB-2-ALL</td>
													
												
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">------</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L34-ENG2001-ELA-117-AB-2-ALL</td>
													
												
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L35</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L36</td>
													
											
											
											
											
										
										
									</tr>
									
									
									
								
									
									
										
									<tr style="background-color: #FFFFCC;">
									
										<td rowspan="2" bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">WED</td>
										<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">THEORY</td>
											
										
										
											
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TCC1</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">E1-STS1009-TH-135-AB-1-ALL</td>
													
												
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">STA2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">G1</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TFF1</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TBB1-MAT1002-TH-115-AB-2-ALL</td>
													
												
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">_</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TDD1</td>
													
											
											
											<td style="border: 1px solid #3c8dbc; text-align: center; 
												vertical-align: middle; padding: 3px; width: 50px;">-</td>
											
										
											
											
											
											
											<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
												vertical-align: middle; padding: 3px; width: 50px;">Lunch</td>
										
											
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">E2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">STA1</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">G2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TFF2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TBB2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">_____</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TDD2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TCC2</td>
													
											
											
											<td style="border: 1px solid #3c8dbc; text-align: center; 
												vertical-align: middle; padding: 3px; width: 50px;">-</td>
											
										
										
									</tr>
									
									
									
										
									<tr style="background-color: #FFFFCC;">
									
										
										<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">LAB</td>
											
										
										
											
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L7</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L8</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">-</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L9</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">--</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L10</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">---</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L11</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L12</td>
													
											
											
											
											
										
											
											
											
											
											<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
												vertical-align: middle; padding: 3px; width: 50px;">Lunch</td>
										
											
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L37</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">----</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L38</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">-----</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L39</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">------</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L40</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L41-ECE1003-ELA-201-AB-2-ALL</td>
													
												
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L42-ECE1003-ELA-201-AB-2-ALL</td>
													
												
													
											
											
											
											
										
										
									</tr>
									
									
									
								
									
									
										
									<tr style="background-color: #FFFFCC;">
									
										<td rowspan="2" bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">THU</td>
										<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">THEORY</td>
											
										
										
											
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TE1</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">C1-ECE1003-ETH-135-AB-1-ALL</td>
													
												
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">_</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">A1-CSE2005-ETH-420-AB-1-ALL</td>
													
												
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">__</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">F1-ENG2001-ETH-416-AB-1-ALL</td>
													
												
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">___</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">D1-CHY1009-ETH-105-AB-2-ALL</td>
													
												
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">____</td>
													
											
											
											
											
										
											
											
											
											
											<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
												vertical-align: middle; padding: 3px; width: 50px;">Lunch</td>
										
											
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">C2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">_____</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">A2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">______</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">F2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">_______</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">D2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TE2</td>
													
											
											
											<td style="border: 1px solid #3c8dbc; text-align: center; 
												vertical-align: middle; padding: 3px; width: 50px;">-</td>
											
										
										
									</tr>
									
									
									
										
									<tr style="background-color: #FFFFCC;">
									
										
										<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">LAB</td>
											
										
										
											
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L13</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L14</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">-</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L15</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">--</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L16</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">---</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L17</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L18</td>
													
											
											
											
											
										
											
											
											
											
											<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
												vertical-align: middle; padding: 3px; width: 50px;">Lunch</td>
										
											
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L43</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">----</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L44</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">-----</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L45</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">------</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L46</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L47</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L48</td>
													
											
											
											
											
										
										
									</tr>
									
									
									
								
									
									
										
									<tr style="background-color: #FFFFCC;">
									
										<td rowspan="2" bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">FRI</td>
										<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">THEORY</td>
											
										
										
											
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TAA1</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TD1-CHY1009-ETH-105-AB-2-ALL</td>
													
												
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">_</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">B1-MAT1002-TH-115-AB-2-ALL</td>
													
												
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">__</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">G1</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TEE1-STS1009-TH-135-AB-1-ALL</td>
													
												
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">C1-ECE1003-ETH-135-AB-1-ALL</td>
													
												
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">___</td>
													
											
											
											
											
										
											
											
											
											
											<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
												vertical-align: middle; padding: 3px; width: 50px;">Lunch</td>
										
											
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TD2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">____</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">B2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">_____</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">G2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TEE2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">C2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TAA2</td>
													
											
											
											<td style="border: 1px solid #3c8dbc; text-align: center; 
												vertical-align: middle; padding: 3px; width: 50px;">-</td>
											
										
										
									</tr>
									
									
									
										
									<tr style="background-color: #FFFFCC;">
									
										
										<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">LAB</td>
											
										
										
											
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L19</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L20</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">-</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L21</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">--</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L22</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">---</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L23</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L24</td>
													
											
											
											
											
										
											
											
											
											
											<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
												vertical-align: middle; padding: 3px; width: 50px;">Lunch</td>
										
											
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L49</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">----</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L50</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">-----</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L51-CHY1009-ELA-123-CB-ALL</td>
													
												
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">------</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L52-CHY1009-ELA-123-CB-ALL</td>
													
												
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L53</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L54</td>
													
											
											
											
											
										
										
									</tr>
									
									
									
								
									
									
										
									<tr style="background-color: #FFFFCC;">
									
										<td rowspan="2" bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">SAT</td>
										<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">THEORY</td>
											
										
										
											
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TG1</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TB1-MAT1002-TH-115-AB-2-ALL</td>
													
												
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">_</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TC1-ECE1003-ETH-135-AB-1-ALL</td>
													
												
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">__</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">A1-CSE2005-ETH-420-AB-1-ALL</td>
													
												
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">___</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">F1-ENG2001-ETH-416-AB-1-ALL</td>
													
												
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">____</td>
													
											
											
											
											
										
											
											
											
											
											<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
												vertical-align: middle; padding: 3px; width: 50px;">Lunch</td>
										
											
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TB2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">_____</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TC2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">______</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">A2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">_______</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">F2</td>
													
											
												
												
													
												<td style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">TG2</td>
													
											
											
											<td style="border: 1px solid #3c8dbc; text-align: center; 
												vertical-align: middle; padding: 3px; width: 50px;">-</td>
											
										
										
									</tr>
									
									
									
										
									<tr style="background-color: #FFFFCC;">
									
										
										<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
											vertical-align: middle; padding: 3px; width: 50px;">LAB</td>
											
										
										
											
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L25</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L26</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">-</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L27</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">--</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L28</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">---</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L29</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L30</td>
													
											
											
											
											
										
											
											
											
											
											<td bgcolor="#e2e2e2" style="border: 1px solid #3c8dbc; text-align: center; 
												vertical-align: middle; padding: 3px; width: 50px;">Lunch</td>
										
											
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L55</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">----</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L56</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">-----</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L57-CSE2005-ELA-119-AB-1-ALL</td>
													
												
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">------</td>
													
											
												
												<td bgcolor="#CCFF33" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L58-CSE2005-ELA-119-AB-1-ALL</td>
													
												
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L59</td>
													
											
												
												
													
												<td bgcolor="#f9efa4" style="border: 1px solid #3c8dbc; text-align: center; 
														vertical-align: middle; padding: 3px; width: 50px;">L60</td>
													
											
											
											
											
										
										
									</tr>
									
									
									
								
							</tbody></table>
															
										
									</div>
									
								</div>

								
							</div></div>
					</div>
					</div>
				</div>
				</section>

				<noscript>
					<h2 class="text-red">Enable JavaScript to Access VTOP</h2>
				</noscript>
				
				<script type="text/javascript">
					/*<![CDATA[*/
					function processViewTimeTable()
					{						
						var id = "23BCE7625";
						var now = new Date();
						var csrfName = "_csrf";
			            var csrfValue = "0a2c7ca9-63f9-4419-ac9b-0cb93d3c9189";
						var semesterSubId = document.getElementById("semesterSubId").value;
						
							$.blockUI({
								message : '<img src="assets/img/482.GIF"> loading... Just a moment...'
							});
							
							$.ajax({
								url : "processViewTimeTable",
								type : "POST",
								data : csrfName + "=" + csrfValue +"&semesterSubId="+ semesterSubId 
											+'&authorizedID='+ id +'&x='+ now.toUTCString(),
								success : function(response) {
									$("#loadMyFragment").html(response);
									$.unblockUI();
								},
								error : function(jqXHR, textStatus, errorMessage) {
									$.unblockUI();
								}
							});
	
							$("html, body").animate({
								scrollTop : 0
							});
						
					}

					function processViewInvoice()
					{
						var id = "23BCE7625";
						var now = new Date();
						var csrfName = "_csrf";
			            var csrfValue = "0a2c7ca9-63f9-4419-ac9b-0cb93d3c9189";
						var semesterSubId = document.getElementById("semesterSubId").value;
						var vldFlag = 1;
						
						if (semesterSubId == ''){
							vldFlag=0;
							swal("Select Semester","","warning");
						}
						
						
						if(vldFlag == 1)
						{
							$.blockUI({
								message : '<img src="assets/img/482.GIF"> loading... Just a moment...'
							});
							
							$.ajax({
								url : "processViewInvoice",
								type : "POST",
								data : csrfName + "=" + csrfValue +"&semesterSubId="+ semesterSubId 
											+'&authorizedID='+ id +'&x='+ now.toUTCString(),
								success : function(response) {
									$("#studentDetailsList").html(response);
									$.unblockUI();
								},
								error : function(jqXHR, textStatus, errorMessage) {
									$.unblockUI();
								}
							});

							$("html, body").animate({
								scrollTop : 0
							});	
						}
					}

					function cancleInvoiceGenerate()
					{
						var id = "23BCE7625";
						var now = new Date();
						var csrfName = "_csrf";
			            var csrfValue = "0a2c7ca9-63f9-4419-ac9b-0cb93d3c9189";
						var semesterSubId = document.getElementById("semesterSubId").value;
						var vldFlag = 1;
						
						if (semesterSubId == ''){
							vldFlag=0;
							swal("Select Semester","","warning");
						}
						
						
						if(vldFlag == 1)
						{
							$.blockUI({
								message : '<img src="assets/img/482.GIF"> loading... Just a moment...'
							});
							
							$.ajax({
								url : "cancleInvoiceGenerate",
								type : "POST",
								data : csrfName + "=" + csrfValue +"&semesterSubId="+ semesterSubId 
											+'&authorizedID='+ id +'&x='+ now.toUTCString(),
								success : function(response) {
									$("#studentDetailsList").html(response);
									$.unblockUI();
								},
								error : function(jqXHR, textStatus, errorMessage) {
									$.unblockUI();
								}
							});

							$("html, body").animate({
								scrollTop : 0
							});	
						}
					}

					/*]]>*/
				</script>

	</div>

</div>
                                        <div class="d-flex flex-column w-100 text-center d-block" id="b3endmarker">
                                            <p class="invisible"> End of Page Bootstrap 3 // should not be removed </p>
                                        </div>
                                    </div>
                                    <div class="overflow-auto vh-100 pb-5 mb-5 noshow" id="b5wrapper">
                                        <div class="w-100 mb-5" id="b5-pagewrapper"></div>
                                        <div class="d-flex flex-column w-100 text-center" id="b5endmarker">
                                            <p class="invisible"> End of Page Bootstrap 5 // should not be removed </p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="offcanvas offcanvas-start" tabindex="-1" id="expandedSideBar" aria-labelledby="expandedSideBarLabel" style="visibility: hidden;" aria-hidden="true">
                                <div class="offcanvas-header headerBackgroundColor text-light">
                                    <h5 class="offcanvas-title" id="expandedSideBarLabel">VTOP Menu</h5>
                                    <button type="button" class="text-reset bg-transparent border-0 h4" data-bs-dismiss="offcanvas" aria-label="Close">☰</button>
                                </div>
                                <div class="offcanvas-body">
                                    <div>
                                        



        

            
                <div class="fw-bold h6 menuFontStyle"><a data-url="hrms/contactDetails" class="dropdown-item menuFontStyle textColor2 systemB5MainMenu *backColor*" href="javascript:void(0);"><i class="fa fa-phone-square iconSpace "></i> Contact Us</a></div>
            
                <div class="accordion" id="accordianMenuHead_1001"><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0064"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0064" aria-expanded="false" aria-controls="acMenuCollapseHDG0064"> <i class="fa fa-briefcase iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  My Info </span></button></div><div id="acMenuCollapseHDG0064" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0064" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="studentsRecord/StudentProfileAllView" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Profile</a>
            
                <a data-url="proctor/viewStudentCredentials" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Credentials</a>
            
                <a data-url="admissions/studentVirtualAccountNo" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-bank iconSpace "></i> Virtual Account Number</a>
            
                <a data-url="admissions/AcknowledgmentView" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Acknowledgement View</a>
            
                <a data-url="studentBankInformation/BankInfoStudent" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Student Bank Info</a>
            
                <a data-url="admissions/getStudentScholarshipDetails" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> My Scholarships</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0065"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0065" aria-expanded="false" aria-controls="acMenuCollapseHDG0065"> <i class="fa fa-info-circle iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Info Corner </span></button></div><div id="acMenuCollapseHDG0065" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0065" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="academics/common/FaqPreview" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> FAQ</a>
            
                <a data-url="academics/biometriclogdisplay" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-info-circle iconSpace "></i> Biometric Log</a>
            
                <a data-url="admissions/costCentreCircularsViewPageController" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> General</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0066"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0066" aria-expanded="false" aria-controls="acMenuCollapseHDG0066"> <i class="fa fa-paw iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Mentor </span></button></div><div id="acMenuCollapseHDG0066" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0066" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="proctor/viewProctorDetails" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Mentor Details</a>
            
                <a data-url="proctor/viewMessagesSendByProctor" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Mentor Message</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemACD0291"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseACD0291" aria-expanded="false" aria-controls="acMenuCollapseACD0291"> <i class="fa fa-book iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Course Enrollment </span></button></div><div id="acMenuCollapseACD0291" class="accordion-collapse collapse" aria-labelledby="acMenuItemACD0291" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="academics/exc/studentRegistration" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-info-circle iconSpace "></i> EXC Registration</a>
            
                <a data-url="academics/mooc/studentRegistration" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> MOOC Registration</a>
            
                <a data-url="academics/registration/wishlistRegPage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> WishList</a>
            
                <a data-url="academics/withdraw/courseWithdraw" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Course Withdraw</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0067"><button class="accordion-button py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0067" aria-expanded="true" aria-controls="acMenuCollapseHDG0067"> <i class="fa fa-graduation-cap iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Academics </span></button></div><div id="acMenuCollapseHDG0067" class="accordion-collapse collapse show" aria-labelledby="acMenuItemHDG0067" data-bs-parent="#accordianMenuHead_1001" style=""><div class="accordion-body py-0">
            
                <a data-url="hrms/viewHodDeanDetails" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> HOD and Dean Info</a>
            
                <a data-url="hrms/employeeSearchForStudent" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Faculty Info</a>
            
                <a data-url="academics/common/StudentClassGrievance" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Course Feedback 24x7</a>
            
                <a data-url="academics/common/BiometricInfo" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Biometric Info</a>
            
                <a data-url="academics/common/StudentClassMessage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Class Messages</a>
            
                <a data-url="academics/council/CouncilRegulationView/new" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Regulation</a>
            
                <a data-url="academics/common/Curriculum" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> My Curriculum</a>
            
                <a data-url="academics/additionalLearning/AdditionalLearningStudentView" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Minor/ Honour</a>
            
                <a data-url="academics/common/StudentTimeTable" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Time Table</a>
            
                <a data-url="academics/common/StudentAttendance" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Class Attendance</a>
            
                <a data-url="academics/common/StudentCoursePage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Course Page</a>
            
                <a data-url="internship/InternshipRegistration" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Industrial Internship </a>
            
                <a data-url="academics/common/ProjectView" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Project</a>
            
                <a data-url="examinations/StudentDA" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Digital Assignment Upload</a>
            
                <a data-url="academics/common/QCMStudentLogin" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> QCM View </a>
            
                <a data-url="set/setRegistrationViewPage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> SET Conference Registration</a>
            
                <a data-url="academics/common/ExtraCurricular" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Co-Extra Curricular</a>
            
                <a data-url="academics/common/CalendarPreview" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Academics Calendar</a>
            
                <a data-url="academics/common/StudentRegistrationScheduleAllocation" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Registration Schedule &amp; Allocation</a>
            
                <a data-url="academics/student/PJTReg/loadRegistrationPage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Project Course</a>
            
                <a data-url="ecs/ecsRegistrationViewPage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> ECS Registration</a>
            
                <a data-url="ecs/ecsHodViewDetailsPage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Faculty Acceptance Status</a>
            
                <a data-url="ecs/StudentViewEcsReviewMarks" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> ECS Review  Marks</a>
            
                <a data-url="inc/IncRegistration" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> INC Registration</a>
            
                <a data-url="mooc/moocRegistration" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Mooc Course Regsitration</a>
            
                <a data-url="capstone/capstoneRegistrationStdPage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Capstone Registration</a>
            
                <a data-url="capstone/capstoneAcceptanceStdPage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Capstone Acceptance Status</a>
            
                <a data-url="capstone/capstoneReviewMarksStdPage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Capstone Review Marks</a>
            
                <a data-url="sdp/sdpRegistrationViewPage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> SDP Registration</a>
            
                <a data-url="sdp/StudentViewSdpReviewMarks" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> SDP Review Marks</a>
            
                <a data-url="sdp/sdpHodViewDetailsPage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> SDP Acceptance Status</a>
            
                <a data-url="academics/summerInternship" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Summer Internship</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0062"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0062" aria-expanded="false" aria-controls="acMenuCollapseHDG0062"> <i class="fa fa-bank iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Research </span></button></div><div id="acMenuCollapseHDG0062" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0062" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="examinations/invigilation/InvigilationDutyAllocationforfaculty" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-info-circle iconSpace "></i> Invigilation Duty Selection &amp; View</a>
            
                <a data-url="research/researchProfile" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> My Research Profile</a>
            
                <a data-url="admissions/semTransactionPageControllerGeneral" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> SEM Request</a>
            
                <a data-url="research/CourseworkRegistration" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Course Work Registration</a>
            
                <a data-url="research/CourseworkRegistrationViewtoScholar" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Registration Status</a>
            
                <a data-url="research/scholarsMeetingView" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Meeting info</a>
            
                <a data-url="hrms/bioForm/BioAttInfoEmp" class="dropdown-item menuFontStyle textColor2 systemB5MainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-hourglass-end iconSpace "></i> Biometric Attendance Info</a>
            
                <a data-url="hrms/researchStdLeaveRequest" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Research Std Leave Request</a>
            
                <a data-url="research/researchLettersStudentView" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-file-text iconSpace "></i> Research Letters</a>
            
                <a data-url="research/thesisSubmission" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Electronic Thesis Submission</a>
            
                <a data-url="research/researchDocumentUpload" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Research Document Upload</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0070"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0070" aria-expanded="false" aria-controls="acMenuCollapseHDG0070"> <i class="fa fa-book iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Examination </span></button></div><div id="acMenuCollapseHDG0070" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0070" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="examinations/StudExamSchedule" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Exam Schedule</a>
            
                <a data-url="examinations/StudentMarkView" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Marks</a>
            
                <a data-url="examinations/examGradeView/StudentGradeView" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Grades</a>
            
                <a data-url="examinations/paperSeeing/PaperSeeing" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Paper See/Rev</a>
            
                <a data-url="examinations/examGradeView/StudentGradeHistory" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Grade History</a>
            
                <a data-url="examinations/projectFileUpload/ProjectView" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Project File Upload</a>
            
                <a data-url="examinations/gotToMoocCourseInitial" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> MOOC File upload</a>
            
                <a data-url="examinations/ecaUpload/viewCourse" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> ECA File Upload</a>
            
                <a data-url="compre/eptScheduleShow" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> EPT schedule</a>
            
                <div class="accordion" id="accordianMenuHead_1002"><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0071"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0071" aria-expanded="false" aria-controls="acMenuCollapseHDG0071"> &nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Comprehensive </span></button></div><div id="acMenuCollapseHDG0071" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0071" data-bs-parent="#accordianMenuHead_1002"><div class="accordion-body py-0">
            
                <a data-url="compre/registrationForm" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Comprehensive Exam</a>
            
                <a data-url="compre/studentExamInfo" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Exam Information</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0072"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0072" aria-expanded="false" aria-controls="acMenuCollapseHDG0072"> &nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Arrear/ReFAT Details </span></button></div><div id="acMenuCollapseHDG0072" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0072" data-bs-parent="#accordianMenuHead_1002"><div class="accordion-body py-0">
            
                <div class="accordion" id="accordianMenuHead_1003"><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0074"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0074" aria-expanded="false" aria-controls="acMenuCollapseHDG0074"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Regular Arrear/ReFAT </span></button></div><div id="acMenuCollapseHDG0074" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0074" data-bs-parent="#accordianMenuHead_1003"><div class="accordion-body py-0">
            
                <a data-url="examinations/arrearRegistration/RegularArrearStudentReg" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Registration</a>
            
                <a data-url="examinations/arrearRegistration/LoadRegularArrearViewPage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Registration Details</a>
            
                <a data-url="examinations/arrearRegistration/viewRARExamSchedule" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Exam Schedule</a>
            
                <a data-url="examinations/arrearRegistration/StudentArrearGradeView" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Grade View</a>
            
                <a data-url="examinations/regularArrear/RegularArrearPaperSeeing" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Paper See/Rev</a>
            
                </div></div></div></div></div></div></div><a data-url="examinations/reFAT/StudentReFATRequestPageController" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Re-Exam Application</a>
            
                </div></div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0044"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0044" aria-expanded="false" aria-controls="acMenuCollapseHDG0044"> <i class="fa fa-bank iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Library </span></button></div><div id="acMenuCollapseHDG0044" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0044" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="hrms/onlineBookRecommendation" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Online Book Recommendation</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0075"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0075" aria-expanded="false" aria-controls="acMenuCollapseHDG0075"> <i class="fa fa-space-shuttle iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Services </span></button></div><div id="acMenuCollapseHDG0075" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0075" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="phyedu/facilityAvailable" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Facility Registration</a>
            
                <a data-url="transport/transportRegistration" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Transport Registration</a>
            
                <a data-url="pat/PatRegistrationProcess" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> PAT Registration</a>
            
                <a data-url="internship/CollectOfferLetter" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Upload Offer Letter</a>
            
                <a data-url="alumni/alumniTranscriptPageControl" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Transcript Request</a>
            
                <a data-url="admissions/scholarshipPageController" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Financial Assistance Scholarship</a>
            
                <a data-url="admissions/SpecialAchieversAwards" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Achievements</a>
            
                <a data-url="admissions/programmeMigration" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Programme Migration</a>
            
                <a data-url="hostels/late/hour/student/request/1" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Late Hour Request</a>
            
                <a data-url="vitaa/finalyearcheck" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Final Year Registration</a>
            
                <div class="accordion" id="accordianMenuHead_1004"><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemOTH0049"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseOTH0049" aria-expanded="false" aria-controls="acMenuCollapseOTH0049"> &nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  SAP Application </span></button></div><div id="acMenuCollapseOTH0049" class="accordion-collapse collapse" aria-labelledby="acMenuItemOTH0049" data-bs-parent="#accordianMenuHead_1004"><div class="accordion-body py-0">
            
                <a data-url="sap/SapManage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> SAP Project</a>
            
                <a data-url="sap/SapCreditManage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Apply Credit Transfer</a>
            
                </div></div></div><a data-url="admissions/reserachFresherCertUpload" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Certificate Upload</a>
            
                <a data-url="others/esanad/doApply" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> eSanad Request</a>
            
                </div></div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0008"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0008" aria-expanded="false" aria-controls="acMenuCollapseHDG0008"> <i class="fa fa-certificate iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Bonafide </span></button></div><div id="acMenuCollapseHDG0008" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0008" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="others/bonafide/StudentBonafidePageControl" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Apply Bonafide</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0076"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0076" aria-expanded="false" aria-controls="acMenuCollapseHDG0076"> <i class="fa fa-money iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Online Payments </span></button></div><div id="acMenuCollapseHDG0076" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0076" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="finance/Payments" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Payments</a>
            
                <a data-url="p2p/getReceiptsApplno" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Payment Receipts</a>
            
                <a data-url="finance/getFeesIntimation" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Fees Intimation</a>
            
                <a data-url="finance/getOnlineTransfer" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Online Transfer</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0077"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0077" aria-expanded="false" aria-controls="acMenuCollapseHDG0077"> <i class="fa fa-home iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Hostels </span></button></div><div id="acMenuCollapseHDG0077" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0077" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="hostel/StudentWeekendOuting" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Weekend Outing</a>
            
                <a data-url="hostel/StudentGeneralOuting" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> General Outing</a>
            
                <a data-url="hostels/HostelStudentRoomView" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Hostel Room Info 2023-24</a>
            
                <a data-url="hostels/counsellingSlotTimings1" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> NCGPA RANK View 2023-24</a>
            
                <a data-url="hostels/room/booking/NcgpaStudentCounselling" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> NCGPA Hostel Booking 23-24</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0100"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0100" aria-expanded="false" aria-controls="acMenuCollapseHDG0100"> <i class="fa fa-book iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  ASC FDP </span></button></div><div id="acMenuCollapseHDG0100" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0100" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="events/ASC/EventsRegistration" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> FDP Registration</a>
            
                <a data-url="events/ASC/EventsCertificateDownload" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Participant Certificate</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0003"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0003" aria-expanded="false" aria-controls="acMenuCollapseHDG0003"> <i class="fa fa-shield iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Events </span></button></div><div id="acMenuCollapseHDG0003" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0003" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="events/sixsigma/loadStudentViewPage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> SixSigma Certificate</a>
            
                <div class="accordion" id="accordianMenuHead_1005"><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemEVE0075"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseEVE0075" aria-expanded="false" aria-controls="acMenuCollapseEVE0075"> &nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  University Day </span></button></div><div id="acMenuCollapseEVE0075" class="accordion-collapse collapse" aria-labelledby="acMenuItemEVE0075" data-bs-parent="#accordianMenuHead_1005"><div class="accordion-body py-0">
            
                <a data-url="event/uday/certificates" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> eCertificates</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemOTH0040"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseOTH0040" aria-expanded="false" aria-controls="acMenuCollapseOTH0040"> &nbsp;&nbsp;&nbsp;<i class="fa fa-graduation-cap iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Convocation </span></button></div><div id="acMenuCollapseOTH0040" class="accordion-collapse collapse" aria-labelledby="acMenuItemOTH0040" data-bs-parent="#accordianMenuHead_1005"><div class="accordion-body py-0">
            
                <a data-url="convocation/entryPage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Registration</a>
            
                </div></div></div></div></div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0101"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0101" aria-expanded="false" aria-controls="acMenuCollapseHDG0101"> <i class="fa fa-trophy iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  SW Events </span></button></div><div id="acMenuCollapseHDG0101" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0101" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="event/swf/student/loadClubChapterEnrollmentPage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Club/Chapter Enrollment</a>
            
                <a data-url="event/swf/loadRequisitionPage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Event Requisition</a>
            
                <a data-url="event/swf/loadEventAttendance" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Event Attendance</a>
            
                <a data-url="event/swf/loadEventRegistration" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Event Registration</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemCNTXXX0"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseCNTXXX0" aria-expanded="false" aria-controls="acMenuCollapseCNTXXX0"> <i class="fa fa-lock iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  My Account </span></button></div><div id="acMenuCollapseCNTXXX0" class="accordion-collapse collapse" aria-labelledby="acMenuItemCNTXXX0" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="controlpanel/ChangePassword" class="dropdown-item menuFontStyle textColor2 systemB5MainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-lock iconSpace "></i> Change Password</a>
            
                <a data-url="controlpanel/ChangePreferredUser" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-lock iconSpace "></i> Update LoginID</a></div></div></div></div>
            

        


        <script>
            /*<![CDATA[*/

            var actionButton = document.getElementsByClassName("systemMainMenu");
            for (let i = 0; i < actionButton.length; i++) {
                actionButton[i].addEventListener('click', assembleData, false);
            }

            var actionButton2 = document.getElementsByClassName("systemB5MainMenu"); 
            for (let i = 0; i < actionButton2.length; i++) {
                actionButton2[i].addEventListener('click', assembleDataForB5, false);
            }

            function assembleData() {
                var authorizedID = $("#authorizedIDX").val();
                let csrfName = "_csrf";
                let csrfValue = "0a2c7ca9-63f9-4419-ac9b-0cb93d3c9189";
                var dataText = "verifyMenu=true&authorizedID=" + authorizedID + "&" + csrfName + '=' + csrfValue + "&nocache=@(new Date().getTime())"
                let url = this.dataset.url;
                ajaxCall(url, dataText);
            }

            function assembleDataForB5() {
                var authorizedID = $("#authorizedIDX").val();
                let csrfName = "_csrf";
                let csrfValue = "0a2c7ca9-63f9-4419-ac9b-0cb93d3c9189";
                var dataText = "verifyMenu=true&authorizedID=" + authorizedID +"&"+ csrfName + '=' + csrfValue+"&nocache=@(new Date().getTime())"
                let url = this.dataset.url;
                ajaxB5Call(url, dataText);
            }

            /*]]>*/
        </script>


    
                                    </div>
                                </div>
                            </div>
                            <script type="text/javascript" src="/vtop/assets/js/menu.js"></script>
                        
                    </div>

                    
                    
                    

        
    
                
            <div class="row noshow" id="popup" style="cursor: default;">
            <div class="col-12">
                <div class="card">
                    <div class="card-header">
                        <span class="h6 fw-bold">Loading... Please Wait</span>
                    </div>
                    <div class="card-body">
                        <img src="assets/gif/ajax-loader_bert.gif" class="img-fluid">
                    </div>
                </div>
            </div>
        </div></div>
        </div>
        <div class="row">
            <div class="col-12" id="messageBox">

            </div>
        </div>
    </div>
    
    

        <div class="modal" id="myModalFooter" role="dialog">
            <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                <!-- Modal content-->
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="close" data-bs-dismiss="modal">×</button>
                        <h4 class="modal-title text-primary">Sorry !!!</h4>
                    </div>
                    <div class="modal-body">
                        <p class="text-danger"> This page is under Construction !!! Please try later</p>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-default" data-bs-dismiss="modal">Close</button>
                    </div>
                </div>

            </div>
        </div>

        <div class="modal b3ModalLayer" id="accessDeniedModal" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered modal-sm b3ModalLayer">
                <div class="modal-content b3ModalLayer">
                    <div class="modal-header">
                        <h4 class="modal-title text-primary" id="staticBackdropLabel">Sorry !!!</h4>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <h3 class="text-danger"> Access Denied</h3>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-outline-danger" data-bs-dismiss="modal">Close</button>
                    </div>
                </div>
            </div>
        </div>


        <script type="text/javascript" src="/vtop/get/ms/js/1"></script> <!--moment.js -->
        <script type="text/javascript" src="/vtop/get/jq/js/2"></script> <!-- jquery hotkey-->
        <script type="text/javascript" src="/vtop/get/jq/js/3"></script> <!--  block ui -->
        <script type="text/javascript" src="/vtop/get/jq/js/4"></script> <!--  jquery ui -->
        <script type="text/javascript" src="/vtop/get/bs/js/3"></script> <!-- bootstrap.bundle min 5.0.1 -->
        <script type="text/javascript" src="/vtop/assets/js/custom-bootstrap.js"></script>



        <script type="text/javascript" src="/vtop/get/bs/js/1"></script> <!-- bootstrapvalidator.js -->
        <script type="text/javascript" src="/vtop/assets/js/vtop-validation.js"></script>
        <script type="text/javascript" src="/vtop/assets/js/vit-custom.js"></script>
        <script type="text/javascript" src="/vtop/assets/js/validate2.js"></script>
        <script type="text/javascript" src="/vtop/assets/js/pdf.js"></script>
        <script type="text/javascript" src="/vtop/assets/js/app.js"></script>



        <script>
            /*<![CDATA[*/

            $(document).ready(function () {
                var offsetHeight = document.getElementById('vtopHeader').offsetHeight;
                document.body.style.paddingTop = offsetHeight + 'px';
                const historyBtn=document.getElementById("historyBtn");
                const historyBtn1=document.getElementById("historyBtn1");
                historyBtn.addEventListener("click", showHistory);
                historyBtn1.addEventListener("click", showHistory);
            });


            function showHistory() {
                let csrfName = "_csrf";
                let csrfValue = "0a2c7ca9-63f9-4419-ac9b-0cb93d3c9189";
                let id ="23BCE7625";
                let params = "authorizedID=" + id + "&" + csrfName + "=" + csrfValue + "&x=" + now.toUTCString();
                ajaxB5Call("show/login/history",params,"b5-pagewrapper");
                historyBtn1.addEventListener("click", showHistory);
            }

            function vtopDownload(urlText, dataToSend) {

                var params = null;
                var csrfName = "_csrf";
                var csrfValue = "0a2c7ca9-63f9-4419-ac9b-0cb93d3c9189";
                var id ="23BCE7625";
                var now = new Date();
                if (dataToSend === 'null' || dataToSend === undefined || dataToSend === null || dataToSend === '') {
                    params = "authorizedID=" + id + "&" + csrfName + "=" + csrfValue + "&x=" + now.toUTCString();
                } else {
                    params = dataToSend + "&" + csrfName + "=" + csrfValue + "&authorizedID=" + id + "&x=" + now.toUTCString();
                }

                window.open(urlText + '?' + params);
                $.unblockUI();
            }


            history.pushState(null, null, document.URL);
            window.addEventListener('popstate', function () {
                history.pushState(null, null, document.URL);
            });


            /*]]>*/
        </script>

        



<div id="DCC77AE7-1E3A-2563-6D23-AB6A7F5CB4EF"></div></body></html>

"""
time_table = {"Tuesday": {'Theory':{'08:00-08:50':'TF1','09:00-09:50':'TA1-CSE2005-ETH-420-AB-1-ALL'}}, "Wednesday": {},
              "Thursday": {}, "Friday": {}, "Saturday": {}, "Sunday": {}}

soup = BeautifulSoup(html, 'html.parser')

# Find the table with id 'timeTableStyle'
time_table = soup.find(id='timeTableStyle')
list1, list2, list3, list4, list5 = [], [], [], [], []
lst_table=[]
if time_table:
    # Find all <tr> tags within the 'timeTableStyle' table starting from Tue
    tr_tags = time_table.find_all('tr')[4:]
    
    for tr_tag in tr_tags:
        tr_string = str(tr_tag.get_text(strip=False))
        # Split the string into lines
        lines=tr_string.split('\n')
        lines= list(filter(None, lines))
        lst_table.append(lines)
else:
    print("No table with id 'timeTableStyle' found.")
print(lst_table)