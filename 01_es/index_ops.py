from client import ESClient
from settings import DEFAULT_INDEX

es = ESClient().get_client()

def create_index(index_name=DEFAULT_INDEX):
    if es.indices.exists(index=index_name):
        print(f"⚠️ 索引 [{index_name}] 已存在")
    else:
        es.indices.create(index=index_name)
        print(f"✅ 索引 [{index_name}] 创建成功")

def delete_index(index_name=DEFAULT_INDEX):
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)
        print(f"🗑️ 索引 [{index_name}] 已删除")
    else:
        print(f"⚠️ 索引 [{index_name}] 不存在，无法删除")
