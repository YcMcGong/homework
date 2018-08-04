$("#signinBox").modal('show')

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

function signin(){
    var user_id = document.getElementById('userid').value;
    var password = document.getElementById('password').value;
    // Submit the form data
    var formData = new FormData();
    var url = signinUrl;
    formData.append('user_id', user_id);
    formData.append('password', password);
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