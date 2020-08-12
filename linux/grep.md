+ **正则表达式**  
grep -ni 'XXX' filename #在filename中搜索XXX,不区分大小写，且输出带有行号  
cat -A /etc/neutron/neutron.conf | grep -v ^[#,$] #显示首字母不为#和$的行，  
其中cat -A 是显示特殊字符（如<table>显示成^I,行尾显示$）而不是空白  
cat /etc/neutron/neutron.conf | grep -v ^# | grep -v ^$ 效果和上面一样  
但是cat /etc/neutron/neutron.conf | grep -v ^[#,$] 就不行，原因？
