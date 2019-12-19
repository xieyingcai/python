+ **sed**  
sed -i 's/pattern1/pattern2/g' inputfile  
sed一般使用单引号，sed引用shell变量时使用双引号即可，因为双引号时弱引用，不会去除$的变量表示功能，而单引号为强制转义，会把$作为一般符号表示。  
sed -i "s/$pattern1/$pattern2/g" inputfile   

sed -i '/controller/d' /etc/hosts #删除hosts文件中含controller的行    
sed -i '$a 'CONTROLLER_HOSTIP' '$CONTROLLER_HOSTNAME'' /etc/hosts #在hosts文件末尾添加CONTROLLER_HOSTIP和CONTROLLER_HOSTNAME两个变量的值  
sed -i '/^DEVICE=/cDEVICE="ens192"' $ifcfgDir #匹配文件中首行为DEVICE=的行，并替换为DEVICE="ens192"  
sed -i '/^匹配字符/i\添加内容' /etc/chrony.conf #在匹配行前新添加一行数据   
sed -i '/^匹配字符/a\添加内容' /etc/chrony.conf #在匹配行后新添加一行数据  
