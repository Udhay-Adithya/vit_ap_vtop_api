from bs4 import BeautifulSoup
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
            var csrfValue = "fac74201-7ce3-4f2e-a13b-4b4f3674bf93";
            var id ="23BCE7625";
            var now = new Date();
            var params = csrfName + "=" + csrfValue + "&authorizedID=" + id + "&x=" + now.toUTCString();

            function home() {
                ajaxCall("/vtop/home", params, "page_outline");
            }

            /*]]>*/
        </script>
        <nav class="navbar navbar-expand-lg py-0 navbar-light bg-light headerBackgroundColor fixed-top shadow" id="vtopHeader">
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
                                    
                                    <i class="bi bi-star-half h4"></i>
                                    </span></button>
                            <div class="dropdown d-inline-block">
                                <button class="btn btn-outline-primary btn-sm dropdown-toggle text-light" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    <span class="text-light">Quick Links</span>
                                </button>
                                <ul class="dropdown-menu">
                                    
        <li data-linkid="594d9dc2-73f9-4b7f-9fd0-12c9b57e7680">
            <div class="d-flex justify-content-between">
                
                <a href="javascript:void(0);" data-url="finance/Payments" class="dropdown-item menuFontStyle quickMainMenu ">
                    <i class="fa fa-dot-circle-o iconSpace "></i><span>Payments</span></a>

                <button type="button" class="btn btn-sm btn-light text-dark deleteQuickLinkBtn" data-linkid="594d9dc2-73f9-4b7f-9fd0-12c9b57e7680">x</button>
            </div>
        </li>
        <li data-linkid="395e932f-1928-49c1-ba9d-0ae30c65f3c1">
            <div class="d-flex justify-content-between">
                
                <a href="javascript:void(0);" data-url="academics/common/StudentCoursePage" class="dropdown-item menuFontStyle quickMainMenu ">
                    <i class="fa fa-dot-circle-o iconSpace "></i><span>Course Page</span></a>

                <button type="button" class="btn btn-sm btn-light text-dark deleteQuickLinkBtn" data-linkid="395e932f-1928-49c1-ba9d-0ae30c65f3c1">x</button>
            </div>
        </li>
        <li data-linkid="a9b2a0b3-7056-4708-a3a9-00c06754ecef">
            <div class="d-flex justify-content-between">
                
                <a href="javascript:void(0);" data-url="academics/common/StudentAttendance" class="dropdown-item menuFontStyle quickMainMenu ">
                    <i class="fa fa-dot-circle-o iconSpace "></i><span>Class Attendance</span></a>

                <button type="button" class="btn btn-sm btn-light text-dark deleteQuickLinkBtn" data-linkid="a9b2a0b3-7056-4708-a3a9-00c06754ecef">x</button>
            </div>
        </li>
    
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
                                    <form class="text-center" id="logoutForm1" name="logoutForm1" method="post" action="/vtop/logout"><input type="hidden" name="_csrf" value="fac74201-7ce3-4f2e-a13b-4b4f3674bf93">
                                        <input type="hidden" name="_csrf" value="fac74201-7ce3-4f2e-a13b-4b4f3674bf93">
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
                            <form class="text-center" id="logoutForm1" name="logoutForm1" method="post" `="" action="/vtop/logout"><input type="hidden" name="_csrf" value="fac74201-7ce3-4f2e-a13b-4b4f3674bf93">
                                <input type="hidden" name="_csrf" value="fac74201-7ce3-4f2e-a13b-4b4f3674bf93">
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

                
                    <div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-phone-square iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown" style=""><a data-url="hrms/contactDetails" class="dropdown-item menuFontStyle systemB5BtnMenu *backColor*" href="javascript:void(0);"><i class="fa fa-phone-square iconSpace "></i> Contact Us</a></div></div>
                
                    <div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-briefcase iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown" style="position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate3d(38px, 88px, 0px);" data-popper-placement="right-start"><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> My Info </div>
                
                    <a data-url="studentsRecord/StudentProfileAllView" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Profile</a>
                
                    <a data-url="proctor/viewStudentCredentials" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Credentials</a>
                
                    <a data-url="admissions/studentVirtualAccountNo" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-bank iconSpace "></i> Virtual Account Number</a>
                
                    <a data-url="admissions/AcknowledgmentView" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Acknowledgement View</a>
                
                    <a data-url="studentBankInformation/BankInfoStudent" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Student Bank Info</a>
                
                    <a data-url="admissions/getStudentScholarshipDetails" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> My Scholarships</a>
                
                    <a data-url="others/photo/IdcardImageSelfUpload" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Students ID Card Image Upload</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-info-circle iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown" style=""><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Info Corner </div>
                
                    <a data-url="academics/common/FaqPreview" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> FAQ</a>
                
                    <a data-url="academics/biometriclogdisplay" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-info-circle iconSpace "></i> Biometric Log</a>
                
                    <a data-url="admissions/costCentreCircularsViewPageController" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> General</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-paw iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown" style="position: absolute; inset: 0px auto auto 0px; margin: 0px; transform: translate3d(38px, 142px, 0px);" data-popper-placement="right-start"><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Mentor </div>
                
                    <a data-url="proctor/viewProctorDetails" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Mentor Details</a>
                
                    <a data-url="proctor/viewMessagesSendByProctor" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Mentor Message</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-book iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown" style=""><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Course Enrollment </div>
                
                    <a data-url="academics/exc/studentRegistration" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-info-circle iconSpace "></i> EXC Registration</a>
                
                    <a data-url="academics/registration/wishlistRegPage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> WishList</a>
                
                    <a data-url="academics/common/WishlistStudent" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> WishList Registration Std</a>
                
                    <a data-url="academics/withdraw/courseWithdraw" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Course Withdraw</a>
                
                    <a data-url="summerInternship/summerInternshipRegistrationStdPage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Summer Internship Reg M Tech</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-graduation-cap iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown" style=""><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Academics </div>
                
                    <a data-url="hrms/viewHodDeanDetails" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> HOD and Dean Info</a>
                
                    <a data-url="hrms/employeeSearchForStudent" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Faculty Info</a>
                
                    <a data-url="academics/common/StudentClassGrievance" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Course Feedback 24x7</a>
                
                    <a data-url="academics/common/BiometricInfo" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Biometric Info</a>
                
                    <a data-url="academics/common/StudentClassMessage" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Class Messages</a>
                
                    <a data-url="academics/council/CouncilRegulationView/new" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Regulation</a>
                
                    <a data-url="academics/common/Curriculum" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> My Curriculum</a>
                
                    <a data-url="academics/common/CreditsDistribution" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> My Credits Distribution</a>
                
                    <a data-url="academics/creditAdjustment" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Credit Adjustment</a>
                
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
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-bank iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown" style=""><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Research </div>
                
                    <a data-url="examinations/invigilation/InvigilationDutyAllocationforfaculty" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-info-circle iconSpace "></i> Invigilation Duty Selection &amp; View</a>
                
                    <a data-url="research/researchProfile" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> My Research Profile</a>
                
                    <a data-url="research/ramanResearchAward/Award" class="dropdown-item menuFontStyle systemB5BtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-money iconSpace "></i> Raman Research Award</a>
                
                    <a data-url="admissions/semTransactionPageControllerGeneral" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> SEM Request</a>
                
                    <a data-url="research/CourseworkRegistration" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Course Work Registration</a>
                
                    <a data-url="research/CourseworkRegistrationViewtoScholar" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Registration Status</a>
                
                    <a data-url="research/scholarsMeetingView" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Meeting info</a>
                
                    <a data-url="hrms/bioForm/BioAttInfoEmp" class="dropdown-item menuFontStyle systemB5BtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-hourglass-end iconSpace "></i> Biometric Attendance Info</a>
                
                    <a data-url="hrms/researchStdLeaveRequest" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Research Std Leave Request</a>
                
                    <a data-url="research/researchLettersStudentView" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-file-text iconSpace "></i> Research Letters</a>
                
                    <a data-url="research/thesisSubmission" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Electronic Thesis Submission</a>
                
                    <a data-url="research/researchDocumentUpload" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Research Document Upload</a>
                
                    <a data-url="research/underGraduateResearchReg" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Under Graduate Research Reg</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-book iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown" style=""><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Examination </div>
                
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
                
                    </div></div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-bank iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown" style=""><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Library </div>
                
                    <a data-url="hrms/onlineBookRecommendation" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Online Book Recommendation</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-space-shuttle iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown" style=""><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Services </div>
                
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
                
                    </div></div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-certificate iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown" style=""><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Bonafide </div>
                
                    <a data-url="others/bonafide/StudentBonafidePageControl" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Apply Bonafide</a>
                
                    <a data-url="others/bonafide/StudentDemandLetterPageControl" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Apply Demand Letter</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-money iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown" style=""><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Online Payments </div>
                
                    <a data-url="finance/Payments" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Payments</a>
                
                    <a data-url="finance/getStudentWalletUpload" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Wallet Amount Add</a>
                
                    <a data-url="p2p/getReceiptsApplno" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Payment Receipts</a>
                
                    <a data-url="finance/getFeesIntimation" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Fees Intimation</a>
                
                    <a data-url="finance/getOnlineTransfer" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Online Transfer</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-home iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown" style=""><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Hostels </div>
                
                    <a data-url="hostel/StudentWeekendOuting" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Weekend Outing</a>
                
                    <a data-url="hostel/StudentGeneralOuting" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> General Outing</a>
                
                    <a data-url="hostels/HostelStudentRoomView" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Hostel Room Info 2023-24</a>
                
                    <a data-url="hostels/counsellingSlotTimings1" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> NCGPA RANK View 2024-25</a>
                
                    <a data-url="hostels/room/booking/NcgpaStudentCounselling" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> NCGPA Hostel Booking 2024-25</a>
                
                    <a data-url="hostels/student/counselling/registration/1" class="dropdown-item menuFontStyle systemB5BtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> NCGPA 2024-25 Consent Request</a>
                
                    <a data-url="hostels/online/room/allotment/open" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Online Booking</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-dot-circle-o iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown" style=""><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> Feedback </div>
                
                    <a data-url="feedback/feedbackform" class="dropdown-item menuFontStyle systemB5BtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-info-circle iconSpace "></i> Feedback Form</a>
                
                    <a data-url="feedback/mentorform" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Mentor Feedback</a>
                
                    <a data-url="feedback/generalfeedbackonvit" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> General Feedback on VIT-AP</a>
                
                    <a data-url="feedback/stdsatisfactionsurveyonvit" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-info-circle iconSpace "></i> Student Satisfaction Survey (NAAC)</a>
                
                    <a data-url="hostels/room/allotment/info/student/1" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> My Room Information</a>
                
                    <a data-url="hostels/student/counselling/registration/3" class="dropdown-item menuFontStyle systemBtnMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Freshers Hostel Registration</a>
                
                    </div></div><div class="btn-group dropend"><button type="button" class="btn btn-outline-primary p-1 border-0 text-dark SideBarMenuBtn" data-bs-toggle="dropdown" data-bs-auto-close="outside" aria-expanded="false"><i class="fa fa-book iconSpace"></i></button><div class="dropdown-menu border-0 py-0 shadow-lg dropdownMenuBoxWidth text-nowrap SideBarMenuDropDown" style=""><div class="fw-bold h6 py-3 text-center menuHeaderColor menuHeaderFontStyle"> ASC FDP </div>
                
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
                let csrfValue = "fac74201-7ce3-4f2e-a13b-4b4f3674bf93";
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
                let csrfValue = "fac74201-7ce3-4f2e-a13b-4b4f3674bf93";
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
<!--
  Author: SANTHOSH VG
  Date  : 03/12/2016
-->




	<div class="">
		<!-- Content Wrapper. Contains page content -->
		<div class="" id="main-section">
			<div class="container">
				<!-- Content Header (Page header) -->
								
				<!-- Main content -->
				<section class="content">
					<div class="col-sm-12">
						<div class="box">
							<div class="box-header with-border text-center">
								<h3 class="box-title"><b>View proctor details</b></h3>
							</div>
							<!-- /.box-header -->
							<!-- form start -->

						<form class="form-horizontal" method="post" action="addStudents" id="employeeForm" autocomplete="off">
							<div class="box-body">
								<div class="form-group text-center">
									<h4 style="color: green; font-weight: bold;"></h4>
								</div>
							</div>
							<!-- /.box-footer -->
						</form>

						<div class="" id="showDetails" style="margin: 20px 20px 20px 20px;">
							<div class=" table-responsive">
						 	<div>
								<table class="table">
									<tbody><tr>
										<td style="background-color: #aba6bf; font-weight: bold;"> Faculty ID</td>
										<td style="background-color: #f2dede;">70588</td>
 										<td style="background-color: #f2dede;" rowspan="9"> 
 											<img src="assets/img/navatar.png" class="img-rounded" alt="Image Not Available" width="150" height="180" style="border: solid 2px #3c8dbc;">
 										</td>
									</tr>
									<tr>
										<td style="background-color: #aba6bf; font-weight: bold;"> Faculty Name</td>
										<td style="background-color: #f2dede;">DR. SHAIKU SHAHIDA SAHEB</td>
 									</tr>
									<tr>
										<td style="background-color: #aba6bf; font-weight: bold;">Faculty Designation</td>
										<td style="background-color: #f2dede;">Associate Professor Grade-2</td>
 									</tr>
 									 <tr>
										<td style="background-color: #aba6bf; font-weight: bold;"> School</td>
										<td style="background-color: #f2dede;">VIT-AP School of Business</td>
 									</tr>
									<tr>
										<td style="background-color: #aba6bf; font-weight: bold;"> Cabin</td>
										<td style="background-color: #f2dede;">AB-1-422-E</td>
 									</tr>
									<tr>
										<td style="background-color: #aba6bf;font-weight: bold;">Faculty Department</td>
										<td style="background-color: #f2dede;">Department of Business School</td>
 									</tr>
									<tr>
										<td style="background-color: #aba6bf;font-weight: bold;"> Faculty Email</td>
										<td style="background-color: #f2dede;">shahid.sk@vitap.ac.in</td>
 									</tr>
 									<tr>
										<td style="background-color: #aba6bf;font-weight: bold;">Faculty intercom</td>
										<td style="background-color: #f2dede;"></td>
 									</tr>
 									
 									<tr>
										<td style="background-color: #aba6bf;font-weight: bold;">Faculty Mobile Number</td>
										<td style="background-color: #f2dede;">7569081253</td>
 									</tr>
								</tbody></table>								
								</div>								
								
							</div>
							</div>
						</div>
					</div>
				</section>
				
				<!-- /.content -->
				<noscript>
					<h2 class="text-red">Enable JavaScript to Access VTOP</h2>
				</noscript>

				<script>
					/*<![CDATA[*/

					/*]]>*/
				</script>
			</div>
		</div>
		<!-- /.content-wrapper -->
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
                            <div class="offcanvas offcanvas-start" tabindex="-1" id="expandedSideBar" aria-labelledby="expandedSideBarLabel">
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
            
                <a data-url="others/photo/IdcardImageSelfUpload" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Students ID Card Image Upload</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0065"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0065" aria-expanded="false" aria-controls="acMenuCollapseHDG0065"> <i class="fa fa-info-circle iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Info Corner </span></button></div><div id="acMenuCollapseHDG0065" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0065" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="academics/common/FaqPreview" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> FAQ</a>
            
                <a data-url="academics/biometriclogdisplay" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-info-circle iconSpace "></i> Biometric Log</a>
            
                <a data-url="admissions/costCentreCircularsViewPageController" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> General</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0066"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0066" aria-expanded="false" aria-controls="acMenuCollapseHDG0066"> <i class="fa fa-paw iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Mentor </span></button></div><div id="acMenuCollapseHDG0066" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0066" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="proctor/viewProctorDetails" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Mentor Details</a>
            
                <a data-url="proctor/viewMessagesSendByProctor" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Mentor Message</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemACD0291"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseACD0291" aria-expanded="false" aria-controls="acMenuCollapseACD0291"> <i class="fa fa-book iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Course Enrollment </span></button></div><div id="acMenuCollapseACD0291" class="accordion-collapse collapse" aria-labelledby="acMenuItemACD0291" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="academics/exc/studentRegistration" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-info-circle iconSpace "></i> EXC Registration</a>
            
                <a data-url="academics/registration/wishlistRegPage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> WishList</a>
            
                <a data-url="academics/common/WishlistStudent" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> WishList Registration Std</a>
            
                <a data-url="academics/withdraw/courseWithdraw" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Course Withdraw</a>
            
                <a data-url="summerInternship/summerInternshipRegistrationStdPage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Summer Internship Reg M Tech</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0067"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0067" aria-expanded="false" aria-controls="acMenuCollapseHDG0067"> <i class="fa fa-graduation-cap iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Academics </span></button></div><div id="acMenuCollapseHDG0067" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0067" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="hrms/viewHodDeanDetails" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> HOD and Dean Info</a>
            
                <a data-url="hrms/employeeSearchForStudent" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Faculty Info</a>
            
                <a data-url="academics/common/StudentClassGrievance" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Course Feedback 24x7</a>
            
                <a data-url="academics/common/BiometricInfo" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Biometric Info</a>
            
                <a data-url="academics/common/StudentClassMessage" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Class Messages</a>
            
                <a data-url="academics/council/CouncilRegulationView/new" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Regulation</a>
            
                <a data-url="academics/common/Curriculum" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> My Curriculum</a>
            
                <a data-url="academics/common/CreditsDistribution" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> My Credits Distribution</a>
            
                <a data-url="academics/creditAdjustment" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Credit Adjustment</a>
            
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
            
                <a data-url="research/ramanResearchAward/Award" class="dropdown-item menuFontStyle textColor2 systemB5MainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-money iconSpace "></i> Raman Research Award</a>
            
                <a data-url="admissions/semTransactionPageControllerGeneral" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> SEM Request</a>
            
                <a data-url="research/CourseworkRegistration" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Course Work Registration</a>
            
                <a data-url="research/CourseworkRegistrationViewtoScholar" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Registration Status</a>
            
                <a data-url="research/scholarsMeetingView" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Meeting info</a>
            
                <a data-url="hrms/bioForm/BioAttInfoEmp" class="dropdown-item menuFontStyle textColor2 systemB5MainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-hourglass-end iconSpace "></i> Biometric Attendance Info</a>
            
                <a data-url="hrms/researchStdLeaveRequest" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Research Std Leave Request</a>
            
                <a data-url="research/researchLettersStudentView" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-file-text iconSpace "></i> Research Letters</a>
            
                <a data-url="research/thesisSubmission" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Electronic Thesis Submission</a>
            
                <a data-url="research/researchDocumentUpload" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Research Document Upload</a>
            
                <a data-url="research/underGraduateResearchReg" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Under Graduate Research Reg</a>
            
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
            
                <a data-url="others/bonafide/StudentDemandLetterPageControl" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Apply Demand Letter</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0076"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0076" aria-expanded="false" aria-controls="acMenuCollapseHDG0076"> <i class="fa fa-money iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Online Payments </span></button></div><div id="acMenuCollapseHDG0076" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0076" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="finance/Payments" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Payments</a>
            
                <a data-url="finance/getStudentWalletUpload" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Wallet Amount Add</a>
            
                <a data-url="p2p/getReceiptsApplno" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Payment Receipts</a>
            
                <a data-url="finance/getFeesIntimation" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Fees Intimation</a>
            
                <a data-url="finance/getOnlineTransfer" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Online Transfer</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0077"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0077" aria-expanded="false" aria-controls="acMenuCollapseHDG0077"> <i class="fa fa-home iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Hostels </span></button></div><div id="acMenuCollapseHDG0077" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0077" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="hostel/StudentWeekendOuting" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Weekend Outing</a>
            
                <a data-url="hostel/StudentGeneralOuting" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> General Outing</a>
            
                <a data-url="hostels/HostelStudentRoomView" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Hostel Room Info 2023-24</a>
            
                <a data-url="hostels/counsellingSlotTimings1" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> NCGPA RANK View 2024-25</a>
            
                <a data-url="hostels/room/booking/NcgpaStudentCounselling" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> NCGPA Hostel Booking 2024-25</a>
            
                <a data-url="hostels/student/counselling/registration/1" class="dropdown-item menuFontStyle textColor2 systemB5MainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> NCGPA 2024-25 Consent Request</a>
            
                <a data-url="hostels/online/room/allotment/open" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Online Booking</a>
            
                </div></div></div><div class="accordion-item border-0"><div class="accordion-header" id="acMenuItemHDG0054"><button class="accordion-button collapsed py-2 ps-3 menuFontStyle bg-transparent" type="button" data-bs-toggle="collapse" data-bs-target="#acMenuCollapseHDG0054" aria-expanded="false" aria-controls="acMenuCollapseHDG0054"> <i class="fa fa-dot-circle-o iconSpaceHeader "></i><span class="ps-0 ms-0 fw-bold textColor1">  Feedback </span></button></div><div id="acMenuCollapseHDG0054" class="accordion-collapse collapse" aria-labelledby="acMenuItemHDG0054" data-bs-parent="#accordianMenuHead_1001"><div class="accordion-body py-0">
            
                <a data-url="feedback/feedbackform" class="dropdown-item menuFontStyle textColor2 systemB5MainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-info-circle iconSpace "></i> Feedback Form</a>
            
                <a data-url="feedback/mentorform" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Mentor Feedback</a>
            
                <a data-url="feedback/generalfeedbackonvit" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> General Feedback on VIT-AP</a>
            
                <a data-url="feedback/stdsatisfactionsurveyonvit" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-info-circle iconSpace "></i> Student Satisfaction Survey (NAAC)</a>
            
                <a data-url="hostels/room/allotment/info/student/1" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> My Room Information</a>
            
                <a data-url="hostels/student/counselling/registration/3" class="dropdown-item menuFontStyle textColor2 systemMainMenu " href="javascript:void(0);">&nbsp;&nbsp;&nbsp;<i class="fa fa-dot-circle-o iconSpace "></i> Freshers Hostel Registration</a>
            
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
                let csrfValue = "fac74201-7ce3-4f2e-a13b-4b4f3674bf93";
                var dataText = "verifyMenu=true&authorizedID=" + authorizedID + "&" + csrfName + '=' + csrfValue + "&nocache=@(new Date().getTime())"
                let url = this.dataset.url;
                ajaxCall(url, dataText);
            }

            function assembleDataForB5() {
                var authorizedID = $("#authorizedIDX").val();
                let csrfName = "_csrf";
                let csrfValue = "fac74201-7ce3-4f2e-a13b-4b4f3674bf93";
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
                let csrfValue = "fac74201-7ce3-4f2e-a13b-4b4f3674bf93";
                let id ="23BCE7625";
                let params = "authorizedID=" + id + "&" + csrfName + "=" + csrfValue + "&x=" + now.toUTCString();
                ajaxB5Call("show/login/history",params,"b5-pagewrapper");
                historyBtn1.addEventListener("click", showHistory);
            }

            function vtopDownload(urlText, dataToSend) {

                var params = null;
                var csrfName = "_csrf";
                var csrfValue = "fac74201-7ce3-4f2e-a13b-4b4f3674bf93";
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

        



<div id="34169D74-BFBC-E3BD-8438-2F4911CB4D0F"></div></body></html>"""
def mentor_details_parser(html):
    soup = BeautifulSoup(html, "html.parser")

    # Initialize the main dictionary
    mentor_details = {}

    # Temporary dictionary for collecting data
    temp_dict = {
        'faculty_id': None,
        'faculty_name': None,
        'faculty_designation': None,
        'school': None,
        'cabin': None,
        'faculty_department': None,
        'faculty_email': None,
        'faculty_intercom': None,
        'faculty_mobile_number': None
    }

    # Find the relevant table or structure
    rows = soup.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        values = [cell.get_text().strip() for cell in columns]

        # Skip rows that don't contain enough values or are headers
        if len(values) == 1:
            # Handle potential exam types or section headers
            current_exam_type = values[0]
            continue
        elif len(values) < 2:
            continue

        # Map values to the corresponding keys in temp_dict
        if 'Faculty ID' in values:
            temp_dict['faculty_id'] = values[1]
        elif 'Faculty Name' in values:
            temp_dict['faculty_name'] = values[1]
        elif 'Faculty Designation' in values:
            temp_dict['faculty_designation'] = values[1]
        elif 'School' in values:
            temp_dict['school'] = values[1]
        elif 'Cabin' in values:
            temp_dict['cabin'] = values[1]
        elif 'Faculty Department' in values:
            temp_dict['faculty_department'] = values[1]
        elif 'Faculty Email' in values:
            temp_dict['faculty_email'] = values[1]
        elif 'Faculty intercom' in values:
            temp_dict['faculty_intercom'] = values[1]
        elif 'Faculty Mobile Number' in values:
            temp_dict['faculty_mobile_number'] = values[1]

    # Construct the final dictionary from the temporary one
    mentor_details = {key: value for key, value in temp_dict.items() if value is not None}
    return mentor_details

mentor_details_parser(html)