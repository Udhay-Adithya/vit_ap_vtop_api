from bs4 import BeautifulSoup

html = '''<html><head><meta http-equiv="origin-trial" content="Az520Inasey3TAyqLyojQa8MnmCALSEU29yQFW8dePZ7xQTvSt73pHazLFTK5f7SyLUJSo2uKLesEtEa9aUYcgMAAACPeyJvcmlnaW4iOiJodHRwczovL2dvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZyIsImV4cGlyeSI6MTcyNTQwNzk5OSwiaXNTdWJkb21haW4iOnRydWUsImlzVGhpcmRQYXJ0eSI6dHJ1ZX0=">

    

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
    <link rel="stylesheet" type="text/css" href="/vtop/get/ic/css/2">
    <link rel="stylesheet" type="text/css" href="/vtop/assets/css/PreLogin.css">
    <script type="text/javascript" async="" src="https://www.gstatic.com/recaptcha/releases/rz4DvU-cY2JYCwHSTck0_qm-/recaptcha__en.js" crossorigin="anonymous" integrity="sha384-eZG8e4nRp0gEpRB75JBNzhS0vVseDRBVprGQYHJNXJCYwHihzdLYpvGhxa6VAhNb"></script><script src="https://www.google.com/recaptcha/api.js" async="async" defer="defer"></script>

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


<body class="WhiteBackground" style="margin-top: 68px;">
    
        <nav class="navbar navbar-expand-lg bg-light headerBackgroundColor py-1 fixed-top shadow" id="vtopOpenPageHeader">
            <div class="container-fluid justify-content-start">
                <a class="navbar-brand" href="javacript:void(0);">
                    <img src="/vtop/assets/img/VIT_AP_logo.png" width="170px" alt="">
                </a>
                <!-- <a class="navbar-brand VITLogoStyle text-light" href="javacript:void(0);"><span
                        class="h1 fw-bold">VIT</span>
                </a>
                <span class="navbar-text text-light">(AP Campus)</span> -->

            </div>
        </nav>

    
    <div class="container-fluid">
        <div class="row">
            <div class="col-11 col-sm-8 col-md-6 col-lg-6 col-xl-4 WhiteBackground shadow-lg mx-auto p-0 mt-5" id="loginBox">
                
                    <div class="card border-0">
                        <div class="card-header loginBoxBorder">
                            <h4 class="fw-bold">VTOP Login</h4>
                        </div>
                        <div class="card-body" id="bodyContent">
                            <form id="vtopLoginForm" name="vtopLoginForm" class="form-signin" method="POST" action="/vtop/login"><input type="hidden" name="_csrf" value="8becd7f4-c011-4294-ae3f-85b4c15ac120">

                                <!-- USERID -->

                                <div class="input-group input-group-sm mb-3">
                                    <input type="text" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1" id="username" name="username" onkeyup="this.value = this.value.toUpperCase()" autocomplete="off">
                                    <span class="input-group-text" id="basic-addon1"><i class="fa fa-user text-primary" aria-hidden="true"></i></span>
                                </div>

                                <!-- PASSWORD -->

                                <div class="input-group input-group-sm mb-3">
                                    <input type="password" class="form-control" placeholder="Password" id="password" name="password" aria-describedby="basic-addon2">
                                    <button id="basic-addon2" class="btn btn-light border-secondary" type="button">
                                        <i class="fa fa-eye text-danger fw-bold" id="passwordIcon" onclick="javascript:toggleEye();" aria-hidden="false"></i>
                                    </button>
                                </div>

                                <!-- IN BUILT CAPTCHA  -->

                                

                                    <div class="row">
                                        <div class="col-7 mx-auto">
                                            <div class="input-group input-group-sm border  mb-3" id="captchaBlock">
                                                

                                                    <img class="form-control img-fluid bg-light border-0" height="325" src="data:image/jpeg;base64,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" aria-describedby="button-addon2">

                                                    <button class="btn btn-success" type="button" onclick="loadCaptcha()" id="button-addon2"> <i class="fa fa-refresh" aria-hidden="true"></i></button>
                                                
                                            </div>
                                        </div>
                                    </div>
                                    <div class="mb-3">
                                        <input type="text" class="form-control form-control-sm" autocomplete="off" maxlength="6" onkeyup="this.value = this.value.toUpperCase()" id="captchaStr" name="captchaStr" aria-describedby="captchaHelp" placeholder="Enter CAPTCHA shown above">
                                    </div>
                                

                                <!-- GOOGLE CAPTCHA  -->

                                

                                <button type="button" onclick="javascript:callBuiltValidation();" id="submitBtn" class="btn btn-sm btn-primary float-end">Submit</button>

                                
                            </form>
                        </div>
                        <span class="text-danger text-center" role="alert">
                            <strong> Invalid Captcha </strong>
                        </span>
                        

                        <div class="card-footer border-0 small">
                            <a class="fw-bold text-decoration-none" onclick="javascript:resetPassword()" href="javascript:void(0)">Forgot
                                Password</a><br>
                            <a class="fw-bold text-decoration-none " onclick="javascript:forgotUserID()" href="javascript:void(0)">Forgot
                                LoginId</a>
                            <div class="text-end">
                                <a class="fw-light fst-italic text-success" href="/vtop/open/page"><strong><i>Go to
                                            Home
                                            Page</i></strong></a>
                            </div>

                        </div>
                    </div>
                
            </div>
        </div>
    </div>

    
        <form id="sessionExpireCheckForm" action="/vtop/session/expired/out">

        </form>
        <div class="fixed-bottom text-center text-light py-0 footercolor">
            <span class="small">Copyright © <span class="trim d-none d-sm-inline-block">2024</span>
                Software Development Cell, VIT-AP University, Andhra Pradesh-522241.</span>
        </div>

        <div class="modal" tabindex="-1" id="sessionTimedOut">
            <div class="modal-dialog modal-dialog-centered modal-sm">
              <div class="modal-content">
                <div class="modal-header">
                  <h4 class="modal-title text-primary">Sorry !!!</h4>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <h3 class="text-danger"> Session Timed Out</h3>
                </div>
                <div class="modal-footer">
                  <button type="button" class="btn btn-outline-danger" data-bs-dismiss="modal">Close</button>
                </div>
              </div>
            </div>
          </div>

        <script type="text/javascript" src="/vtop/get/jq/js/1"></script>
        <script type="text/javascript" src="/vtop/get/jq/js/3"></script>
        <script type="text/javascript" src="/vtop/get/bs/js/3"></script>
        <script type="text/javascript" src="/vtop/get/jq/js/4"></script>

        <script>
            /*<![CDATA[*/

            var offsetHeight = document.getElementById('vtopOpenPageHeader').offsetHeight;
            document.body.style.marginTop = offsetHeight + 'px';

            function sessionExpiredCall() {
                var form = document.getElementById("sessionExpireCheckForm");
                form.submit();
            }

            history.pushState(null, null, document.URL);
            window.addEventListener('popstate', function () {
                history.pushState(null, null, document.URL);
            });

            /*]]>*/
        </script>

    

    <script>
        /*<![CDATA[*/

        var captchaType=1;

        $(document).ready(function () {
            $('input').keyup(function (event) {
                if (event.which === 13) {
                    event.preventDefault();
                    if(captchaType===1) {  // built-in captcha validation
                        callBuiltValidation();
                    }else if(captchaType===2) {
                        callGoogleValidation();  // google captcha validation
                    }
                }
            });
        });

        var isEyeOpened = false;

        function loadCaptcha() {
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    document.getElementById("captchaBlock").innerHTML = this.responseText;
                    document.getElementById("captchaStr").value = "";
                }
            };
            xhttp.open("GET", "/vtop/get/new/captcha", true);
            xhttp.send();
        }

        function callBuiltValidation() {

            var gvalue = document.getElementById("g-recaptcha-response");
            if (gvalue != null && gvalue != undefined && gvalue != '') {
                document.getElementById('gResponse').value = gvalue.value;
            }
            var form = document.getElementById('vtopLoginForm');
            form.submit();

        }

        function callGoogleValidation() {
            grecaptcha.execute();
        }

        function resetPassword() {
            $.blockUI({ message: '<h4><img src="assets/gif/ajax-loader_bert.gif" /> few moments...</h4>' });
            var csrfName = "_csrf";
            var csrfValue = "8becd7f4-c011-4294-ae3f-85b4c15ac120";
            var data = new FormData();
            data.append(csrfName, csrfValue);

            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    document.getElementById("loginBox").innerHTML = this.responseText;
                    $.unblockUI();
                }
            };
            xhttp.open("POST", "/vtop/resetPassword", true);
            xhttp.send(data);

        }

        function forgotUserID() {
            $.blockUI({ message: '<h4><img src="assets/gif/ajax-loader_bert.gif" /> few moments...</h4>' });
            var csrfName = "_csrf";
            var csrfValue = "8becd7f4-c011-4294-ae3f-85b4c15ac120";
            var data = new FormData();
            data.append(csrfName, csrfValue);

            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    document.getElementById("loginBox").innerHTML = this.responseText;
                    $.unblockUI();
                }
            };
            xhttp.open("POST", "/vtop/forgotUserID", true);
            xhttp.send(data);
        }

        function toggleEye() {
            if (isEyeOpened) {
                isEyeOpened = false;
                document.getElementById("passwordIcon").classList.remove('fa-eye-slash');
                document.getElementById("passwordIcon").classList.add('text-danger');
                document.getElementById("passwordIcon").classList.remove('text-primary');
                document.getElementById("passwordIcon").classList.add('fa-eye');
                document.getElementById("password").type = 'password';
            } else {
                isEyeOpened = true;
                document.getElementById("passwordIcon").classList.add('fa-eye-slash');
                document.getElementById("passwordIcon").classList.add('text-primary');
                document.getElementById("passwordIcon").classList.remove('text-danger');
                document.getElementById("passwordIcon").classList.remove('fa-eye');
                document.getElementById("password").type = 'text';
            }
        }

        function getOTP() {
            $.blockUI({ message: '<h4><img src="assets/gif/ajax-loader_bert.gif" /> few moments...</h4>' });
            var form = document.getElementById('forgetPasswordForm');
            var data = new FormData(form);
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    document.getElementById("loginBox").innerHTML = this.responseText;
                    $.unblockUI();
                }
            };
            xhttp.open("POST", "/vtop/generateOtp", true);
            xhttp.send(data);

        }

        function verifyOTP() {
            $.blockUI({ message: '<h4><img src="assets/gif/ajax-loader_bert.gif" /> few moments...</h4>' });
            var form = document.getElementById('otpVerificationForm');
            var data = new FormData(form);
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    var reqTarget = this.getResponseHeader('wrapper');
                    if (reqTarget === 'null' || reqTarget === undefined
                        || reqTarget === null || reqTarget === '') {
                        reqTarget = "loginBox";
                    }
                    document.getElementById(reqTarget).innerHTML = this.responseText;
                    $.unblockUI();
                    var btn = document.getElementById("changePasswordBtn");
                    if (btn != null) {
                        btn.addEventListener('click', doChangePassword, false);
                    }
                }
            };
            xhttp.open("POST", "/vtop/validateOtp", true);
            xhttp.send(data);

        }

        function regenerateOTP() {
            $.blockUI({ message: '<h4><img src="assets/gif/ajax-loader_bert.gif" /> few moments...</h4>' });
            var form = document.getElementById('otpVerificationForm');
            var data = new FormData(form);
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    var reqTarget = this.getResponseHeader('wrapper');
                    if (reqTarget === 'null' || reqTarget === undefined
                        || reqTarget === null || reqTarget === '') {
                        reqTarget = "loginBox";
                    }
                    document.getElementById(reqTarget).innerHTML = this.responseText;
                    $.unblockUI();
                }
            };
            xhttp.open("POST", "/vtop/resendOtp", true);
            xhttp.send(data);
        }

        function getUserIDOTP() {
            $.blockUI({ message: '<h4><img src="assets/gif/ajax-loader_bert.gif" /> few moments...</h4>' });
            var form = document.getElementById('forgetUserIDForm');
            var data = new FormData(form);
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    var reqTarget = this.getResponseHeader('wrapper');
                    if (reqTarget === 'null' || reqTarget === undefined
                        || reqTarget === null || reqTarget === '') {
                        reqTarget = "loginBox";
                    }
                    document.getElementById(reqTarget).innerHTML = this.responseText;
                    $.unblockUI();
                }
            };
            xhttp.open("POST", "/vtop/get/otp/for/forget/userid", true);
            xhttp.send(data);

        }

        function verifyUserIDOTP() {
            $.blockUI({ message: '<h4><img src="assets/gif/ajax-loader_bert.gif" /> few moments...</h4>' });
            var form = document.getElementById('forgetUserIDForm');
            var data = new FormData(form);
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    var reqTarget = this.getResponseHeader('wrapper');
                    if (reqTarget === 'null' || reqTarget === undefined
                        || reqTarget === null || reqTarget === '') {
                        reqTarget = "loginBox";
                    }
                    document.getElementById(reqTarget).innerHTML = this.responseText;
                    $.unblockUI();
                }
            };
            xhttp.open("POST", "/vtop/validate/user/id/otp", true);
            xhttp.send(data);

        }

        function resendUserIDOTP() {
            $.blockUI({ message: '<h4><img src="assets/gif/ajax-loader_bert.gif" /> few moments...</h4>' });
            var form = document.getElementById('forgetUserIDForm');
            var data = new FormData(form);
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    var reqTarget = this.getResponseHeader('wrapper');
                    if (reqTarget === 'null' || reqTarget === undefined
                        || reqTarget === null || reqTarget === '') {
                        reqTarget = "loginBox";
                    }
                    document.getElementById(reqTarget).innerHTML = this.responseText;
                    $.unblockUI();
                }
            };
            xhttp.open("POST", "/vtop/resend/otp/for/userid", true);
            xhttp.send(data);
        }


        function doChangePassword() {
            $.blockUI({ message: '<h4><img src="assets/gif/ajax-loader_bert.gif" /> few moments...</h4>' });
            var myform = document.getElementById("changePwdForm");
            var data = new FormData(myform);
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    var reqTarget = this.getResponseHeader('wrapper');
                    if (reqTarget === 'null' || reqTarget === undefined
                        || reqTarget === null || reqTarget === '') {
                        reqTarget = "loginBox";
                    }
                    document.getElementById(reqTarget).innerHTML = this.responseText;
                    $.unblockUI();
                }
            };
            xhttp.open("POST", "/vtop/allowChangePassword", true);
            xhttp.send(data);
        }


        function myFunction() {
            var newPassword = document.getElementById("newPassword");
            var confirmNewPassword = document.getElementById("confirmNewPassword");

            if (newPassword.type === "password" && confirmNewPassword.type === "password") {
                newPassword.type = "text";
                confirmNewPassword.type = "text";
            } else {
                newPassword.type = "password";
                confirmNewPassword.type = "password";
            }
        }

        /*]]>*/
    </script>




<div id="D5E61B3E-E631-51A5-F20E-C77BEA70DFD6"></div></body></html>'''


soup = BeautifulSoup(html,'html.parser')
err_msg=soup.find('strong')
print(err_msg.text)