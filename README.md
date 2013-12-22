#find-corndog-fans

[@性感玉米](http://weibo.com/corndog) 在微博组织了一个活动.

[交(gou)友(da)](http://weibo.com/1676582524/AolOP9bZ8)

大家都很踊跃, 但是人太多找不到和自己坐标相同的朋友

于是我会写了点代码, 帮助下大家. 点开文件: __城市名.txt__ 查看即可

```
{
	"_id" : ObjectId("52b6e3460de7deec5cc0efd7"),
	"text" : "回复@有顶猫家族:呃.. 我只是在天津读书而已..",
	"cid" : NumberLong("3658413890687757"),
	"uid" : "1871360692",
	"uname" : "sunusLee"
}
```

* text为用户发出的评论
* http://weibo.com/ + uid 即是对应用户的微博主页
    * 比如我是 [@sunuslee](http://weibo.com/1871360692/)
    * [http://weibo.com/1871360692/](http://weibo.com/1871360692/)

##最后

我,90年. 坐标天津, 明年去杭州.

##技术细节

估计大家没兴趣:) 有兴趣的看代码吧.

部署好python & Mongodb的环境之后

```bash
chmod +x run.sh
./run.sh 北京
```

即输出所有带有「北京」的评论
