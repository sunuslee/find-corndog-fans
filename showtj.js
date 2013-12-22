use wbdb
db.cmts.count()
DBQuery.shellBatchSize = 1000
//db.cmts.runCommand( "text", {search: "天津 哏 杭州 柳州 上海 吃喝嫖"})
db.cmts.find({text: /.*KEYWORD.*/}).sort({cid: -1}).pretty()
