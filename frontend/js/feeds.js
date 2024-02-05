function get_feeds() {
    let response;
    let xhr = new XMLHttpRequest();
    let data = {};
    xhr.open("get", "http://127.0.0.1:8000/feeds/")
    xhr.setRequestHeader("Authorization", "Bearer " + localStorage.getItem("Access"));
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onload = function() {
        if (xhr.status === 200) {
            response = xhr.response;
            response = JSON.parse(response);
            console.log(response);

            response.forEach((element) => {
                alert(element["feed_title"]);
                let div = document.createElement("div");

                let feed_title = document.createElement("h4");
                feed_title.innerHTML = element["feed_title"];

                let feed_link = document.createElement("h4");
                feed_link.innerHTML = element["url"];

                div.appendChild(feed_title);
                div.appendChild(feed_link);

                document.querySelector("body").appendChild(div);
            })

        }

        else {
            refresh_token();
        }
    }

    xhr.send()
}

get_feeds();