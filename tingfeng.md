#### src 1 收货地址
收货地址：查看、删除、保存 => 任意删除别人收货地址  

先获取地址信息再保存

#### src 2 短信轰炸 or 任意账号注册
短信轰炸：发十次的限制，绕过：前面加特殊字符，fuzzing，看是否依然识别为手机号  
字典：1881150xxxx%00 测试特殊字符绕过 00-ff 最后测试出26& 2b+ 2c, 34  
but：忘记密码时，短信接口并不同    
session内存储的，没办法注册为别人的手机号    
修改手机号处也存在短信轰炸，同一个接口，所以提交了也只是算一个洞。  

#### src 3 后台弱口令
- 先找没有验证码的
- 有立即注册的功能
- 用户名字典爆破
- 通过调试信息 找到是什么cms 然后搭建本地测试
- 上传文件测试，文件名是否随机命名，文件后缀是否限制
- 上传成功，但是.htaccess限制，phpx无法解析


#### src 4 git泄漏
- 邮箱后缀 @zhaopin.com.cn 找联系方式很容易找到
- 叮叮bot的token 内网信息：ssrf漏洞 内网渗透（看hosts etc文件等 得到一些新的域名）  
- 查询叮叮的接口 可以找到很多的bot的token
> https://oapi.dingtalk.com/

#### js文件接口泄漏
通过读登陆时的js文件，找到一些隐藏域名或者接口，或许有接口就没有做好授权呢？  

#### 面试 
业务逻辑漏洞：密码重置 四个环节（身份验证、关注）、越权、支付漏洞、按照逻辑的处理过程来说、接口（jsonp劫持 反射型XSS 越权 SQL注入 未授权）、同源策略  
通用漏洞：文件上传 SQL注入（Oracle SQL Server 常见的一些语句 可能会现场写） 提权exp的名字 CVE编号 ms-1-027 反序列化漏洞（原因） 
XXE、


实习能力培养：快速学习



