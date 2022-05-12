from elasticsearch import Elasticsearch


def connect_elasticsearch():
    return Elasticsearch("https://elastic:kHzHALQb5lVG_VkJDxSw@localhost:9200", ca_certs="http_ca.crt")
