from elasticsearch import Elasticsearch
es = Elasticsearch('http://localhost:9200', timeout=90)

es.index(index='my_index', doc_type='my_index', id=1, body={'text': 'this is a test'})
es.index(index='my_index', doc_type='my_index', id=2, body={'text': 'a second test'})

es.search(index='my_index', doc_type='my_index', body={'query': {'match': {'text': 'this test'}}})