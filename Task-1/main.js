

    document.onreadystatechange = function() {
        if (document.readyState !== "complete") {
            document.querySelector(
              "body").style.visibility = "hidden";
            document.querySelector(
              "#loader").style.visibility = "visible";
        } else {
            document.querySelector(
              "#loader").style.display = "none";
            document.querySelector(
              "body").style.visibility = "visible";
        }
    };

    var LoginForm = document.getElementById("LoginForm");
    var RegForm = document.getElementById("RegForm");
    var indicator = document.getElementById("indicator");

    function register() {
      RegForm.style.transform = "translateX(0px)";
      LoginForm.style.transform = "translateX(0px)";
      indicator.style.transform = "translateX(100px)";
    }

    function login() {
      RegForm.style.transform = "translateX(300px)";
      LoginForm.style.transform = "translateX(300px)";
      indicator.style.transform = "translateX(0px)";
    }
