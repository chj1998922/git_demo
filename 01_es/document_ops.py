from client import ESClient
from settings import DEFAULT_INDEX

es = ESClient().get_client()

def insert_doc(doc:dict, index_name=DEFAULT_INDEX):
    res = es.index(index=index_name, document=doc)
    print(f"📥 文档已插入，ID: {res['_id']}")

def get_doc_by_id(doc_id: str, index_name=DEFAULT_INDEX):
    res = es.get(index=index_name, id=doc_id)
    print("📄 查询结果：", res['_source'])
    return res['_source']

def delete_doc_by_id(doc_id: str, index_name=DEFAULT_INDEX):
    es.delete(index=index_name, id=doc_id)
    print(f"🗑️ 文档 {doc_id} 已删除")

