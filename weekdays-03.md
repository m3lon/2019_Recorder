### 2019-1-14
- 刘二狗出得xxe+docx题目
- js2学习 主要包括一些基本知识：注释、变量、数组、（宿主）对象、循环
- pythonchallenge
    - 移位加密：maketrans函数
    - 统计字符出现的次数：简单的循环+列表即可 列表统计字符出现的频率l.count()
    - re.findall()+正则， [a-z]{3} 限制数目
    - 正则的分组与捕获、零宽断言(?=x)

### 2019-1-16
- bug bounty 文章阅读：从blind xxe到root level 任意文件读取
    - 关注报错信息（xml格式）
    - 修改GET为POST，添加content-type:application/xml
    - 测试是否可以引入外部实体
    - 利用内部资源域名+ssrf漏洞将内部网络流量引出到外网，实现root权限下的任意文件读取

###  2019-1-17
- [xxe实验](https://xz.aliyun.com/t/2249 )
    - PEReference的规则：参数实体的引用不允许在内部DTD的标记声明里。在外部DTD中，是可以的   
    - %不允许出现在Entity的value中，利用Unicode编码&#37;
    - vim或者echo自动添加的0a换行符导致的invaild url -> 避免特殊字符的干扰，利用php://filter或者其他协议如ftp