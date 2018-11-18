es = elasticsearch.Elasticsearch()
es.indices.delete(index="ratings",ignore=404)
deque(helpers.parallel_bulk(es,readRatings(),index="ratings",doc_type
es.indices.refresh()