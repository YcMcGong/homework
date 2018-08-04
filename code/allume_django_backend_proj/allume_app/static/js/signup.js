function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function signup(){
    var first_name = document.getElementById('first_name').value;
    var last_name = document.getElementById('last_name').value;
    var phone = document.getElementById('phone').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var confirm_password = document.getElementById('confirm_password').value;
    // Submit the form data
    var formData = new FormData();
    var url = signupUrl
    formData.append('first_name', first_name);
    formData.append('last_name', last_name);
    formData.append('phone', phone);
    formData.append('email', email);
    formData.append('password', password);
    formData.append('confirm_password', confirm_password);
    var xhr = new XMLHttpRequest({mozSystem: true});
    xhr.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var response = JSON.parse(this.responseText);
            var status = response.status;
            if (status != 'success'){
                alert(status);
            }
            else{
                window.location.assign(response.redirect_url)
            }
        }
    }
    xhr.open('POST', url);
    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    xhr.send(formData);
}