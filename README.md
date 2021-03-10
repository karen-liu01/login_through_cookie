# login_through_cookie
自动化过程中使用cookie去避免多次登录
**实现过程：**
- 打开网站——登录——获取cookie——将cookie存储到Python小型数据库——后续再需要登录时直接从本地数据库获取cookie即可
- cookie中有时候有过期时间，可以去掉，避免登录受影响
- 当cookie失效后，再次获取即可，此方法避免了每次都要去获取cookie，在有效期获取一次即可
- 如果失效，重新获取即可
