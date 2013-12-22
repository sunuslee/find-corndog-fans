use wbdb
db.cmts.count()
DBQuery.shellBatchSize = 1000
db.cmts.find({text: /.*KEYWORD.*/}).sort({cid: -1}).pretty()
