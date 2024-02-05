from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import re
from bs4 import BeautifulSoup as bs


@api_view(["POST"])
def get_html_code(request):
    url = request.data["url"]
    x = requests.get(url)

    text = x.text

    soup = bs(text, "html.parser")
    pretty_html = soup.prettify()

    return Response(pretty_html)


@api_view(["POST"])
def get_search_pattern(request):

    html_code = request.data["html_code"]
    global_search_pattern = request.data["global_search_pattern"]
    search_pattern = request.data["search_pattern"]

    result = get_matches(html_code, global_search_pattern, search_pattern)

    print(result)

    return Response(result)


@api_view(["POST"])
def preview(request):
    feed_title = request.data["feed_title"]
    feed_link = request.data["feed_link"]
    feed_description = request.data["feed_description"]
    item_title_template = request.data["item_title_template"]
    item_link_template = request.data["item_link_template"]
    item_content_template = request.data["item_content_template"]

    html_code = request.data["html_code"]
    global_search_pattern = request.data["global_search_pattern"]
    search_pattern = request.data["search_pattern"]

    result = get_matches(html_code, global_search_pattern, search_pattern)

    feed_html_code = f"""
    <h3 style="margin-bottom: 7px">{feed_title}</h3>
    
    <a href="{feed_link}" target="_blank">{feed_link}</a>
    
    <p style="margin: 0">{feed_description}</p>
    <br>
    """

    for data in result:


        feed_html_code += f"""
        <div style="margin-left: 25px; border-top: 1px solid #808080">
            <h4 style="margin: 0; color: #202020">{data[item_title_template]}</h4>
            <a style="margin: 0" href="{data[item_link_template]}" target="_blank">{data[item_link_template]}</a>
            <p style="margin: 0"; color: #404040>{data[item_content_template]}</p>
        </div>
        <br>
        """

    return Response(feed_html_code)


def get_matches(html_code, global_search_pattern, search_pattern):

    result = []

    regex_global_search_pattern = global_search_pattern.replace("{%}", "(.*)").replace("{*}", ".*")
    regex_global_search_pattern = re.sub(r"\s+", r"\\s*", regex_global_search_pattern)

    global_match = re.search(regex_global_search_pattern, html_code, re.DOTALL).group()

    regex_search_pattern = search_pattern.replace("{%}", "(.*?)").replace("{*}", ".*?")
    regex_search_pattern = re.sub(r"\s+", r"\\s*", regex_search_pattern)

    matches = re.findall(regex_search_pattern, global_match, re.DOTALL)

    index = 1

    for match in matches:
        print(match)
        count = 1
        print(index)

        snippet = dict()
        snippet["Item"] = index

        if type(match) != str:
            for element in match:
                snippet_index = "{%" + str(count) + "}"
                snippet[snippet_index] = element
                count += 1
        else:
            snippet_index = "{%" + str(count) + "}"
            snippet[snippet_index] = match
            count += 1

        index += 1
        result.append(snippet)

    return result
