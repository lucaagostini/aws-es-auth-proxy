import argparse
import aws_proxy
import logging
import boto3
import config

if __name__ == "__main__":
    logging.info("Proxy started")

    parser = argparse.ArgumentParser()
    parser.add_argument("--aws_service_region", default="eu-west-1", help="AWS service region used for AWS API calls (eg. authentication)")
    parser.add_argument("--aws_service_endpoint", help="AWS service domain endpoint")
    parser.add_argument("--proxy_host", default="127.0.0.1", help="The proxy listening host")
    parser.add_argument("--proxy_port", type=int, default=8080, help="The proxy listening port")
    args = parser.parse_args()

    config.aws_service_region = args.aws_service_region
    config.aws_service_endpoint = args.aws_service_endpoint
    config.proxy_host = args.proxy_host
    config.proxy_port = args.proxy_port

    config.aws_service_credentials = boto3.session.Session().get_credentials()
    logging.info("Loading AWS credentials from: " + config.aws_service_credentials.method)
    aws_proxy.start()
