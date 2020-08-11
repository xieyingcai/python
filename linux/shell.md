+ **sed**  
sed -i 's/pattern1/pattern2/g' inputfile  
sed一般使用单引号，sed引用shell变量时使用双引号即可，因为双引号时弱引用，不会去除$的变量表示功能，而单引号为强制转义，会把$作为一般符号表示。  
sed -i "s/$pattern1/$pattern2/g" inputfile   
sed -i '/controller/d' /etc/hosts #删除hosts文件中含controller的行    
sed -i '$a 'CONTROLLER_HOSTIP' '$CONTROLLER_HOSTNAME'' /etc/hosts #在hosts文件末尾添加CONTROLLER_HOSTIP和CONTROLLER_HOSTNAME两个变量的值  
sed -i '/^DEVICE=/cDEVICE="ens192"' $ifcfgDir #匹配文件中首行为DEVICE=的行，并替换为DEVICE="ens192"  
sed -i '/^匹配字符/i\添加内容' /etc/chrony.conf #在匹配行前新添加一行数据   
sed -i '/^匹配字符/a\添加内容' /etc/chrony.conf #在匹配行后新添加一行数据  

+ **env set expport**  
env属于外部程序，通过which env或者type env看出来，而set和export都属于shell内的bulid-in命令    
bash实际就是linux下的一个进程，在执行一些命令（如：ls -al) 就会fork和exec一个子进程,执行之后返回。当执行build-in命令不需要启动子进程    
在当前shell下执行一个shell脚本会默认在子进程中执行，通过sorce ./XXX.sh执行脚本，可以不用在子程序中执行，即在当前shell中执行，因此脚本中的export可以改变当前shell的环境变量     
echo $SHLVL #显示当前所在bash层级，初次登陆linux所在的bash层级是1  
env #显示出当前用户的环境变量；环境变量在父子进程中具有默认继承关系  
set #显示当前shell下的变量；执行name=value在当前shell下设置变量，unset name删除变量  
export XXX#用户将当前shell下变量XXX设置为全局变量，子shell下也生效  
