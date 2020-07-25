# vim插件离线安装
因公司不能git clone代码只能通过下载离线安装包来安装  

1. 安装gcc python3
yum install gcc gcc-c++ python3 -y
确认gcc版本：gcc --version  
因公司的镜像源只能安装4.8.5版本，因此需要离线安装高版本的gcc  
## gcc离线安装
通过github下载gcc源码（我这里的版本是7.2.0），以及其依赖的安装包gmp-6.1.0  
mpfr-3.1.4 mpc-1.0.3  
依次编译其依赖包gmp mpfr mpc  
./configure  
make  
make install  
然后编译gcc，在编译前先通过which gcc来确认系统已有gcc的安装路径，我这里是/usr/bi
n/gcc  
然后执行  
./configure --prefix=/usr \
            --enable-languages=c,c++ \
            --disable-multilib       \
            --disable-bootstrap
make  
make install  
安装成功后通过gcc --version查看是否成功  

2. 升级vim  
因安装的YCM插件需要vim支持Python3，所以需要高版本vim支持，我这升级到了vim8.2  
git下载最新vim源码包,解压后进入到src目录下  
./configure --with-feature=huge \
            --enable-gui=gtk2  \
            --enable-python3interp=yes \
            --enable-cscope \
            --enablemultibyte \
            --prefix=/usr  
make  
make install
其中--prefix的路径需要和原vim的路劲保持一致，以便于覆盖掉之前的版本  
确认方法是which vim来确认，比如原有的是/usr/bin/vim 就需要制定prefix为/usr  
如果make过程有失败，一般是提示依赖包不存在通过yum install XX -y 来解决  

3. 部署插件  
下载vundle源码并解压到/root/.vim/bundle/Vundle.vim目录下  
根据/root/.vimrc配置文件下载相应插件的离线包，解压到/root/.vim/bundle目录下  
我这里使用的插件:  
vim-colors-solarized  
nerdtree  
tagbar  
YouCompleteMe  
syntastic  
vim-easymotion  
其中代码补全插件YouCompleteMe需要编译：
python3 ~/.vim/bundle/YouCompleteMe/install.py --clang-completer  

至此已安装完毕，通过vim 打开的文件将看到效果，并可以通过修改.vimrc配置文件来修改
相应插件的配置参数  

# 各插件说明
## vundle  
插件管理器 

## nerdtree 
显示目录插件  
q #关闭 nerdtree窗口  
:NERDTree #重新启动nerdtree  
快捷键:  
? #显示帮助,再次输入?为关闭帮助文档  
ctrl + w + h #光标跳至左侧窗口  
ctrl + w + l #光标跳至右侧窗口  

文件列表执行命令  
i #打开文件，多个文件水平分割  
gi #打开上一个i方式打开的文件  
s #打开文件，多个文件垂直排布  
gs #打开上一个s方式打开的文件  

路径节点命令  
:o #打开关闭目录  
:O #递归打开目录，也就是也打开子目录  
:t #打开新的节点  

## vim-easymotion
光标快速移动  
```vimrnc
let mapleader = ','
let g:EasyMotion_do_mapping = 0 " Disable default mappings

" Jump to anywhere you want with minimal keystrokes, with just one key binding.
" `s{char}{char}{label}`
" Need one more keystroke, but on average, it may be more comfortable.
nmap s <Plug>(easymotion-overwin-f2)

" Turn on case-insensitive feature
let g:EasyMotion_smartcase = 1

" JK motions: Line motions
map <Leader>j <Plug>(easymotion-j)
map <Leader>k <Plug>(easymotion-k)
```
s #跨窗口搜索字符，然后输入搜索位置，将光标快速移动到相应位置  
<leader>j #向上移动光标  
<leader>k #向下移动光标  

# vim命令  
[ctrl] + [f] 向下翻页  
[ctrl] + [b] 向上翻页  
G 移动到文档末尾  
gg 移动到文档开头  
/word 向下查询 n 查看下一个搜索结果 N查看上一个搜索结果  
?word 向下查询 n 查看下一个搜索结果 N查看上一个搜索结果  
:1,$s,/word1/word2/g 替换第一行到最后一行Word1为Word2  
:1,$s,/word1/word2/gc 替换第一行到最后一行Word1为Word2,并且在替换时需要确认  
:10,20s/^/#/g 10行到20行添加注释#  
:10,20s/#//g 10行到20行删除注释#  



