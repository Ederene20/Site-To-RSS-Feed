window.onload = () => {

    let forms = document.getElementsByTagName("form");

    Array.from(forms).forEach(form => {
        form.addEventListener('submit', e => {
            e.preventDefault();
        })
    })
}

function reload() {
    let response;
    let xhr = new XMLHttpRequest();
    let url = document.getElementById("url").value;
    let data = {
        "url": url
    }
    xhr.open("post", "http://127.0.0.1:8000/")
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onload = function() {
        if (xhr.status === 200) {
            response = xhr.response;
            response = JSON.parse(response);

            let html_code = document.getElementById("html_code");
            let reload_status = document.getElementById("reload_status")
            let info_for_step_two = document.getElementById("info_for_step_two")

            html_code.value = response;
            reload_status.innerHTML = ">> Page loaded successfully."
            info_for_step_two.innerHTML = "Below is the HTML source of the retrieved page. Use it to setup extraction rules (see next step)."
        }
    }

    xhr.send(JSON.stringify(data))
}

function extract_pattern() {
    let response;
    let xhr = new XMLHttpRequest();
    let html_code = document.getElementById("html_code").value;
    let global_search_pattern = document.getElementById("global_search_pattern").value;

    let search_pattern = document.getElementById("search_pattern").value;
    let data = {
        "html_code": html_code,
        "global_search_pattern": global_search_pattern,
        "search_pattern": search_pattern
    }

    xhr.open("post", "http://127.0.0.1:8000/extract_pattern/");
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onload = function() {
        if (xhr.status === 200) {
            response = xhr.response;
            response = JSON.parse(response);

            let snippet = document.getElementById("snippet");
            snippet.value = ""
            let info_for_step_three = document.getElementById("info_for_step_three");
            let extraction_status = document.getElementById("extraction_status")

            // snippet.value = response;
            info_for_step_three.innerHTML = "Below is a list of extracted text snippets ({%N}). You can reference them when setting up item properties (see next step)."

            response.forEach(element => {

                for (const [key, value] of Object.entries(element)) {
                    snippet.value = snippet.value + `${key} = ${value}` + "\n";
                }

                snippet.value += "\n";
                 
            })
        }
    }

    xhr.send(JSON.stringify(data))
}

function get_preview() {
    let response;

    let xhr = new XMLHttpRequest();
    let feed_title = document.getElementById("feed_title").value;
    let feed_link = document.getElementById("feed_link").value;
    let feed_description = document.getElementById("feed_description").value;

    let global_search_pattern = document.getElementById("global_search_pattern").value;
    let search_pattern = document.getElementById("search_pattern").value;
    let html_code = document.getElementById("html_code").value;
    
    let data = {
        "feed_title": feed_title,
        "feed_link": feed_link,
        "feed_description": feed_description,
        "item_title_template": document.getElementById("item_title_template").value,
        "item_link_template": document.getElementById("item_link_template").value,
        "item_content_template": document.getElementById("item_content_template").value,
        "html_code": html_code,
        "global_search_pattern": global_search_pattern,
        "search_pattern": search_pattern,
    };

    console.log(data);

    xhr.open("post", "http://127.0.0.1:8000/preview/");
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onload = function() {
        if (xhr.status === 200) {
            response = xhr.response;
            response = JSON.parse(response);

            let preview = document.getElementById("preview");
            
            preview.innerHTML = response;
        }
    }

    xhr.send(JSON.stringify(data));
    
}