+ 参数化  
手工设置变量，通过{{variable_name}}引用  
通过获取响应，并将响应参数设置为环境变量  
举例：  
返回体为： 
```json
{
    "code": 0,
    "msg": "成功",
    "data": {
        "name": "图书",
        "type": 1,
        "foods": null
    }
}
```
将name字段值设置为categoryName环境变量：  
```JavaScrip
//获取返回值
var response =JSON.parse(responseBody);
//判断返回值是否有data参数
if (response.data) {
  //如果有则此次验证通过
  tests["first has data"] = true;
  //获取需要的参数
  var need = response.data;
  //打印获取的参数
  console.log("response.data-->" + need); 
  //将值写入当前选中的环境中 变成环境变量 
  postman.setEnvironmentVariable("categoryName", need.name);
  postman.setEnvironmentVariable("categoryType", need.type);
}
else {
  //如果无则此次验证不通过
  tests["first has data"] = false;
}
```
+ 循环执行  
支持循环执行folder里面的Request，配置执行次数和间隔时间  
当每次请求的数据不一致时，可通过引入参数文件(如：text文件)设置每次使用的参数  

+ 导出测试代码
只能导出发出的请求代码，不可能导出断言  
可自行实现通过导出的json生成适合自己框架的测试代码  
