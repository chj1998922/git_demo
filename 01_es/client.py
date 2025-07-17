from elasticsearch import Elasticsearch
from settings import ES_CONFIG

class ESClient:
    def __init__(self):
        self.client = Elasticsearch(
            ES_CONFIG["host"],
            basic_auth=(ES_CONFIG["username"], ES_CONFIG["password"]),
            verify_certs=ES_CONFIG["verify_certs"]
        )
        if self.client.ping():
            print("Elasticsearch 连接成功")
        else:
            raise Exception("无法连接es")

    def get_client(self):
        return self.client