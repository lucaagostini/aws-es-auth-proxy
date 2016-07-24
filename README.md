# aws-es-auth-proxy

## Objective

Create a proxy to be able to connect to the AWS managed Elasticsearch 
cluster with the AWS authentication to access kibana and other stuffs
without authentication.

## How to run

When you lunch the application you have to set some parameter in the
command line.

For example:

```
python server.py \
    --proxy_port 8080
    --aws_service_region eu-west-1 \ 
    --aws_service_endpoint search-mydomain-id.eu-west-1.es.amazonaws.com
```

The AWS authentication key is loaded with the boto3 priority 
(http://boto3.readthedocs.io/en/latest/guide/configuration.html#configuring-credentials)

For security purpose the service listen only in localhost.

## Libraries

* http://boto3.readthedocs.io/en/latest/reference/core/session.html
* https://pypi.python.org/pypi/requests-aws4auth

