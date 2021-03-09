# login_through_cookie
自动化过程中使用cookie去避免多次登录
**实现过程：**
- 打开网站——登录——获取token——将token存储到Python小型数据库——后续再需要登录时直接从本地数据库获取cookie即可
- cookie中有时候有过期时间，可以去掉，避免登录受影响
- 当cookie失效后，再次获取即可，此方法避免了每次都要去获取cookie，在有效期获取一次即可
**代码优化计划**
1.将cookie是否有效加一个判断，如果有效，直接登录，如果失效，再去获取即可
2.浏览器打开及退出等操作，可以放在setup和teardown中
3.username和password可以提取成变量
