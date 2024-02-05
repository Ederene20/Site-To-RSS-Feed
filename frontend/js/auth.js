function register() {

    let response;
    let xhr = new XMLHttpRequest();
    email = document.getElementById("email").value;
    password = document.getElementById("password").value;
    let data = {
        "email": email,
        "password": password
    }
    xhr.open("post", "http://127.0.0.1:8000/auth/register/");
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onload = function() {
        if (xhr.status === 201) {
            response = xhr.response;
            response = JSON.parse(response);

            localStorage.setItem("Access", response["access"]);
            localStorage.setItem("Refresh", response["refresh"]);

            window.location.href = "./feed.html"
        }

        else {
            alert(xhr.response);
        }
    }

    xhr.send(JSON.stringify(data))
}

function login() {
    let response;
    let xhr = new XMLHttpRequest();
    email = document.getElementById("email").value;
    password = document.getElementById("password").value;
    let data = {
        "email": email,
        "password": password
    }
    xhr.open("post", "http://127.0.0.1:8000/auth/login/");
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onload = function() {
        if (xhr.status === 200) {
            response = xhr.response;
            response = JSON.parse(response);

            localStorage.setItem("Access", response["access"]);
            localStorage.setItem("Refresh", response["refresh"]);

            window.location.href = "./feed.html"
        }

        else {
            alert(xhr.response);
        }
    }

    xhr.send(JSON.stringify(data))   
}

function refresh_token() {
    let response;
    let xhr = new XMLHttpRequest();

    let data = {
        "refresh": localStorage.getItem("Refresh")
    }

    xhr.open("post", "http://127.0.0.1:8000/auth/refresh/");
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onload = function() {
        if (xhr.status === 200) {
            response = xhr.response;
            response = JSON.parse(response);

            localStorage.setItem("Access", response["access"]);

        }

        else {
            alert(xhr.response);
        }
    }

    xhr.send(JSON.stringify(data))

}