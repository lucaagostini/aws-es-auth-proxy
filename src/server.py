import argparse
import aws_proxy
import logging
import boto3
import config

if __name__ == "__main__":
    logging.info("Proxy started")

    parser = argparse.ArgumentParser()
    parser.add_argument("--aws_service_region", help="AWS service region used for AWS API calls (eg. authentication)", default="eu-west-1")
    parser.add_argument("--aws_service_endpoint", help="AWS service domain endpoint")
    args = parser.parse_args()

    config.aws_service_region = args.aws_service_region
    config.aws_service_endpoint = args.aws_service_endpoint

    config.aws_service_credentials = boto3.session.Session().get_credentials()
    logging.info("Loading AWS credentials from: " + config.aws_service_credentials.method)
    aws_proxy.start()
