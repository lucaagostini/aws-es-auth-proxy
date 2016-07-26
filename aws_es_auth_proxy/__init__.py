from bottle import route, run, request, response
import config
import logging
import requests
from requests_aws4auth import AWS4Auth

PROXY_RESP_HEADERS_BLACKLIST = ["connection", "content-length", "content-encoding"]
PROXY_REQ_HEADERS_WHITELIST = ["content-type"]

@route('/<:re:.*>', method='GET')
@route('/<:re:.*>', method='POST')
@route('/<:re:.*>', method='PUT')
def index():

    auth = AWS4Auth(config.aws_service_credentials.access_key, config.aws_service_credentials.secret_key, config.aws_service_region, config.aws_service_name)
    endpoint = config.aws_service_protocol + "://" + config.aws_service_endpoint + request.path + "?" + request.query_string
    proxy_req_header = {}
    for header in request.headers:
        if header.lower() in PROXY_REQ_HEADERS_WHITELIST:
            proxy_req_header[header] = request.headers[header]

    if request.method == "HEAD":
        requests_response = requests.head(endpoint, auth=auth, headers=proxy_req_header)
    elif request.method == "GET":
        requests_response = requests.get(endpoint, auth=auth, headers=proxy_req_header)
    elif request.method == "POST":
        proxy_req_body = request.body.getvalue()
        requests_response = requests.post(
            endpoint,
            auth=auth,
            data=proxy_req_body,
            headers=proxy_req_header)
    elif request.method == "PUT":
        proxy_req_body = request.body.getvalue()
        requests_response = requests.put(
            endpoint,
            auth=auth,
            data=proxy_req_body,
            headers=proxy_req_header)
    else:
        logging.error("Method not allowed")
    response.body = requests_response.content
    for header in requests_response.headers:
        if not header.lower() in PROXY_RESP_HEADERS_BLACKLIST:
            response.add_header(header, requests_response.headers[header])
    return response

def start():
    run(host=config.proxy_host, port=config.proxy_port)