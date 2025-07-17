# main.py

from query_examples import match_query, term_query, range_query, bool_query

if __name__ == "__main__":
    # match 查询：搜索 message 包含“Python”
    # match_query("message", "Python")
    #
    # # term 查询：精确匹配 name=橙橙橙
    # term_query("name", "橙")
    # #
    # # # range 查询：筛选年龄 >= 25
    # range_query("age", gte=25)

    # bool 查询：name 是橙橙橙 且 message 包含 Python，且 age != 30
    bool_query()
