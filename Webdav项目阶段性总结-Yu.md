=== Webdav项目阶段性总结

    Author:Wenyan Yu
    Date:2017.01.13
    
临近春节，项目进行到此，也该好好做一个阶段性总结。<br>
首先说一下一定取得的一些进展：

    1.客户端的前端代码已基本编写完成。
    2.后端webdav通讯协议的封装基本思路已经有了，详细封装过程及编码还在进行中。
    （目前list命令已初步封装完成，后续还有download,upload,cd,mkdir, rm...）
    
其次说一下下一步的的工作：

    1.进一步封装webdav通讯协议，完成基本的命令封装。
    2.webdav通讯协议封装完成后，将其和前端整合在一起，成为一个客户端软件。
    3.将小韩的XFDU模块添加进来。
    4.对客户端软件进行优化，包括前端的显示以及后端的通讯。  
    5.编写测试程序，对软件进行测试。

附录1：关于开发技术的一些记录：
    
    1.前端采用pyqt4开发
    2.后端采用Python封装webdav协议，并实现逻辑层代码，python版本为python2.7
    3.开发环境是Ubuntu16.04 + Pycharm2016.2.3
    4.工程代码采用Git管理工具，并同步在GitHub上，GitHub库地址为：https://github.com/52ai/ccsds-webdav


附录2：为什么要采用webdav?
附录3：利用Python封装webdav通讯协议的技巧
    