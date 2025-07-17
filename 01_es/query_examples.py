from client import ESClient
from settings import DEFAULT_INDEX

es = ESClient().get_client()


# 1. match 查询（全文匹配，适合文字搜索）
def match_query(field, keyword, index_name=DEFAULT_INDEX):
    query = {
        "match": {
            field: keyword
        }
    }
    res = es.search(index=index_name, query=query)
    print("🔍 match 查询结果：")
    for hit in res["hits"]["hits"]:
        print(hit["_source"])


# 2.range 查询（范围筛选, 数值或者时间）
def range_query(field, gte=None, lte=None, index_name=DEFAULT_INDEX):
    range_cond = {}  # 这里必须是 dict，不是 list！

    if gte is not None:
        range_cond["gte"] = gte
    if lte is not None:
        range_cond["lte"] = lte

    query = {
        "range": {
            field: range_cond
        }
    }

    res = es.search(index=index_name, query=query)
    print("📊 range 查询结果：")
    for hit in res["hits"]["hits"]:
        print(hit["_source"])


# 3. term 精确匹配,不分词
def term_query(field, value, index_name=DEFAULT_INDEX):
    query = {
        "term": {
            field: {
                "value": value
            }
        }
    }
    res = es.search(index=index_name, query=query)
    print("🔍 term 查询结果：")
    for hit in res["hits"]["hits"]:
        print(hit["_source"])


# 4. bool 查询（多条件组合）
def bool_query(index_name=DEFAULT_INDEX):
    query = {
        "bool": {
            "must": [
                {"term": {"name": {"value": "橙"}}},
                {"match": {"message": "Python"}}
            ],
            "must_not": [
                {"term": {"age": {"value": 30}}}
            ]
        }
    }
    res = es.search(index=index_name, query=query)
    print("🤖 bool 查询结果：")
    for hit in res["hits"]["hits"]:
        print(hit["_source"])