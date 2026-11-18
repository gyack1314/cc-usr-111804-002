"""查询已收到的产品检测批次原文及其来源身份。"""
from .ledger import entities

def current(connection, collection):
    result = []
    for row in entities(connection, collection):
        if row['type'] != 'test_session':
            continue
        result.append({'id': row['id'], 'version': row['version'],
                       'source_sha256': row['source'], **row['payload']})
    return result
