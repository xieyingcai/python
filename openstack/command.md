- **ovs-vsctl**  
ovs-vsctl show #查看  
ovs-vsctl list port #查看端口  
ovs-vsctl list interface #查看接口  
ovs-vsctl list-br #查看网桥  
ovs-vsctl add-br br-int #增加名称为br-int的网桥  
ovs-vsctl del-br br-int #删除名称为br-int的网桥 
ovs-vsctl add-port br-ens224 ens224 #将端口（网卡）ens224添加到网桥br-ens224上  

-  **OpenStack命令行**   
    - neutron  
    - nova   
    nova list  #列出服务（虚机）  
    nova get-vnc-console uuid novnc #获取ui登录url  
