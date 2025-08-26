# MuMu Emulator Instance Management Software

## 📋 Overview / Tổng Quan

This repository contains a comprehensive instance management software for MuMu Emulator 12, including both the original command-line documentation and a new Python-based management interface.

**Repository includes:**
- 🔧 **Python Instance Manager** - Advanced wrapper for MuMuManager.exe
- 🖥️ **GUI Interface** - User-friendly graphical interface
- 📚 **Complete Documentation** - Vietnamese usage guide
- 🤖 **Automation Scripts** - Examples for common tasks
- ⚙️ **Configuration Management** - Flexible setup options

## 🚀 Quick Start

1. **Setup the software:**
   ```bash
   python setup.py
   ```

2. **Use CLI interface:**
   ```bash
   python instance_manager.py info
   ```

3. **Launch GUI:**
   ```bash
   python gui_manager.py
   ```

4. **View detailed guide:**
   See `HUONG_DAN_SU_DUNG.md` for comprehensive Vietnamese documentation.

## 📁 File Structure

- `instance_manager.py` - Core Python interface for MuMu management
- `gui_manager.py` - Graphical user interface  
- `examples.py` - Automation examples and scripts
- `setup.py` - Installation and configuration script
- `config.json` - Configuration file
- `test_instance_manager.py` - Test suite
- `HUONG_DAN_SU_DUNG.md` - Vietnamese user guide
- `README.md` - This file + original MuMu documentation

---

# Original MuMu Manager Documentation

MuMuManager命令行开发者使用说明
最新更新时间：2024-07-26
　　MuMuManager.exe是MuMu模拟器12新加入的工具，可以用来操控模拟器，查询模拟器或应用状态。当前仅支持以下命令，后续会完善其他命令支持。

　　注：模拟器版本需要V4.0.0.3179及以上版本模拟器才可使用该功能。>>点击获取<<

　　另外，MuMu模拟器12的调用程序MuMuManager.exe在模拟器的安装目录下可以找到，如“X:\Program Files\Netease\MuMuPlayer-12.0\shell>MuMuManager.exe”

　　开发者任何问题可加入MuMu模拟器开发者微信群沟通反馈

　　（该群只处理开发者问题，模拟器使用问题请咨询在线客服）



　　

【目录】

　　一、获取模拟器信息

　　二、创建模拟器

　　三、复制模拟器

　　四、删除模拟器

　　五、重命名模拟器

　　六、导入模拟器

　　七、备份模拟器

　　八、控制模拟器

　　九、配置模拟器

　　十、ADB便捷命令

　　十一、模拟器机型属性

　　十二、模拟器窗口排序

　　十三、模拟器驱动管理

　　十四、兼容大部分旧命令参数（后面可能会废弃，谨慎使用）

 

一、获取模拟器信息(info)

　　使用：

　　info [--vmindex <vmindex>]

　　参数：

　　-v, --vmindex <vmindex> 选择指定的模拟器索引

　　1. 获取指定某个模拟器信息

　　举例：获取索引为0的模拟器的信息

　　MuMuManager.exe info -v 0



　　2. 获取多个模拟器的信息

　　举例：获取索引为 0,2,4 的模拟器信息

　　MuMuManager.exe info -v 0,2,4



　　3. 获取所有模拟器的信息

　　举例：获取所有模拟器信息

　　MuMuManager.exe info -v all



　　4. 获取信息字段说明

　　{

　　"adb_host_ip": "127.0.0.1", // adb 域名，只有启动才会有

　　"adb_port": 16384, // adb端口，只有启动才会有

　　"created_timestamp": 1721180910349678, // 模拟器创建时间戳

　　"disk_size_bytes": 284192948, // 模拟器磁盘占用大小，以字节为单位

　　"error_code": 0, // 模拟器列表错误码

　　"headless_pid": 20868, // 虚拟机进程PID，只有启动才会有

　　"hyperv_enabled": false, // HyperV是否开启

　　"index": "0", // 模拟器索引

　　"is_android_started": false, // 是否安卓启动成功

　　"is_main": true, // 是否是主模拟器

　　"is_process_started": true, // 是否进程启动

　　"launch_err_code": 0, // 启动错误码，只有启动才会有

　　"launch_err_msg": "", // 启动错误描述，只有启动才会有

　　"main_wnd": "00840F4E", // 主窗口句柄，只有启动才会有

　　"name": "MuMu模拟器12", // 模拟器名称

　　"pid": 15112, // 模拟器外壳进程PID，只有启动才会有

　　"player_state": "starting_rom", // 模拟器外壳启动阶段状态，只有启动才会有

　　"render_wnd": "00B30C7A", // 渲染窗口句柄，只有启动才会有

　　"vt_enabled": true // 是否开启VT虚拟化，只有启动才会有

　　}

 

二、创建模拟器(create)

　　使用：

　　create [--vmindex <vmindex>] [--number <number>]

　　参数：

　　-v, --vmindex <vmindex> 选择指定的模拟器索引

　　-n, --number <number> 创建次数

　　1. 创建一个模拟器，自动分配索引

　　举例：创建一个模拟器，索引自动分配

　　MuMuManager.exe create



　　2. 批量创建(--number)

　　举例：创建10个模拟器，索引自动分配

　　MuMuManager.exe create -n 10



　　3. 指定创建模拟器的索引(--vmindex)

　　举例：创建索引为10的模拟器

　　MuMuManager.exe create -v 10



　　举例：从索引3开始，创建10次模拟器，索引依次递增(即创建3-12索引的模拟器)

　　MuMuManager.exe create -v 3 -n 10



　　举例：从索引 3,20 开始，分别创建10次模拟器，索引依次递增(即创建3-12,20-29索引的模拟器)

　　MuMuManager.exe create -v 3,20 -n 10



三、复制模拟器(clone)

　　使用：

　　clone [--vmindex <vmindex>] [--number <number>]

　　参数：

　　-v, --vmindex <vmindex> 选择要复制的模拟器索引

　　-n, --number <number> 复制次数

　　1. 复制指定模拟器(--vmindex)

　　举例：复制索引为2的模拟器

　　MuMuManager.exe clone -v 2



　　举例：复制索引为 2,4,6 的模拟器

　　MuMuManager.exe clone -v 2,4,6



　　举例：复制所有的模拟器

　　MuMuManager.exe clone -v all



　　2. 批量复制(--number)

　　举例：复制索引为2的模拟器，复制10次

　　MuMuManager.exe clone -v 2 -n 10



四、删除模拟器(delete)

　　使用：

　　delete [--vmindex <vmindex>]

　　参数：

　　-v, --vmindex <vmindex> 选择要删除的模拟器索引

　　删除指定模拟器(--vmindex)

　　举例：删除索引为2的模拟器

　　MuMuManager.exe delete -v 2



　　举例：删除索引为2,4,6的模拟器

　　MuMuManager.exe delete -v 2,4,6



　　举例：删除所有的模拟器

　　MuMuManager.exe delete -v all



 

五、重命名模拟器(rename)

　　使用：

　　rename [--vmindex <vmindex>]

　　参数：

　　-v, --vmindex <vmindex> 选择要重命名的模拟器索引

　　-n, --name <name> 名称

　　1. 重命名指定模拟器(--vmindex)

　　举例：重命名索引为2的模拟器为“测试”

　　MuMuManager.exe rename -v 2 -n 测试



　　举例：重命名索引为2,4,6的模拟器为“测试”

　　MuMuManager.exe rename -v 2,4,6 -n 测试



　　举例：重命名所有的模拟器为“测试”

　　MuMuManager.exe rename -v all -n 测试



 

六、导入模拟器

　　使用：

　　import [--path <path>] [--number <number>]

　　参数：

　　-p, --path <path> 要导入的 mumudata 文件路径

　　-n, --number <number> 导入次数

　　1. 文件导入(--path)

　　举例：导入C盘下的 test.mumudata 并创建模拟器

　　MuMuManager.exe import -p C:\test.mumudata



　　2. 文件导入多次(--number)

　　举例：导入C盘下的 test.mumudata 并创建模拟器，导入10次

　　MuMuManager.exe import -p C:\test.mumudata -n 10



　　3. 多文件同时导入(--path)

　　举例：导入C盘下的 test.mumudata 和D盘下的 test2.mumudata 并创建模拟器，分别导入10次

　　MuMuManager.exe import -p C:\test.mumudata -p D:\test2.mumudata -n 10



 

七、备份模拟器

　　使用：

　　export [--vmindex <vmindex>] [--dir <dir>] [--name <name>] [--zip]

　　参数：

　　-v, --vmindex <vmindex> 选择要备份的模拟器索引

　　-d, --dir <dir> 备份的目录

　　-n, --name <name> 备份文件的名称

　　-z, --zip 备份文件是否压缩

　　1. 备份指定模拟器(--vmindex)

　　举例：备份索引为2的模拟器到C盘目录 backup 下，名称为 test.mumudata，以非压缩的格式

　　MuMuManager.exe export -v 2 -d C:\backup -n test



　　举例：备份索引为2,4,6的模拟器到C盘目录 backup 下，文件名基于 test 自动加后缀，以非压缩的格式

　　MuMuManager.exe export -v 2,4,6 -d C:\backup -n test



　　举例：备份所有的模拟器到C盘目录 backup 下，文件名基于 test 自动加后缀，以压缩的格式

　　MuMuManager.exe export -v all -d C:\backup -n test --zip



 

八、控制模拟器(control)

　　使用：

　　control [--vmindex <vmindex>] <subcommand>

　　参数：

　　-v, --vmindex <vmindex> 选择要控制的模拟器索引

　　1. 启动模拟器(launch)

　　使用：

　　control [--vmindex <vmindex>] launch [--package <package>]

　　参数：

　　-v, --vmindex <vmindex> 选择要启动的模拟器索引

　　-pkg, --package <package> 启动时自动启动应用的应用包名

　　（1）启动指定模拟器(--vmindex)

　　举例：

　　启动索引为2的模拟器

　　MuMuManager.exe control -v 2 launch



　　启动索引2,4,6的模拟器

　　MuMuManager.exe control -v 2,4,6 launch



　　启动所有模拟器

　　MuMuManager.exe control -v all launch



　　（2）启动时自动启动应用(--package)

　　举例：启动索引为2的模拟器，并自动启动原神(com.miHoYo.Yuanshen)

　　MuMuManager.exe control -v 2 launch -pkg com.miHoYo.Yuanshen



　　2. 关闭模拟器(shutdown)

　　使用：

　　control [--vmindex <vmindex>] shutdown

　　参数：

　　-v, --vmindex <vmindex> 选择要关闭的模拟器索引

　　（1）关闭指定模拟器(--vmindex)

　　举例：

　　关闭索引为2的模拟器

　　MuMuManager.exe control -v 2 shutdown



　　关闭索引2,4,6的模拟器

　　MuMuManager.exe control -v 2,4,6 shutdown



　　关闭所有模拟器

　　MuMuManager.exe control -v all shutdown



　　3. 重启模拟器(restart)

　　使用：

　　control [--vmindex <vmindex>] restart

　　参数：

　　-v, --vmindex <vmindex> 选择要重启的模拟器索引

　　（1）重启指定模拟器(--vmindex)

　　举例：

　　重启索引为2的模拟器

　　MuMuManager.exe control -v 2 restart



　　重启索引2,4,6的模拟器

　　MuMuManager.exe control -v 2,4,6 restart



　　重启所有模拟器

　　MuMuManager.exe control -v all restart



　　4. 显示模拟器(show_window)

　　使用：

　　control [--vmindex <vmindex>] show_window

　　参数：

　　-v, --vmindex <vmindex> 选择要显示的模拟器索引

　　（1）显示指定模拟器(--vmindex)

　　举例：

　　显示索引为2的模拟器

　　MuMuManager.exe control -v 2 show_window



　　显示索引2,4,6的模拟器

　　MuMuManager.exe control -v 2,4,6 show_window



　　显示所有模拟器

　　MuMuManager.exe control -v all show_window



　　5. 隐藏模拟器(hide_window)

　　使用：

　　control [--vmindex <vmindex>] hide_window

　　参数：

　　-v, --vmindex <vmindex> 选择要隐藏的模拟器索引

　　（1）隐藏指定模拟器(--vmindex)

　　举例：

　　隐藏索引为2的模拟器

　　MuMuManager.exe control -v 2 hide_window



　　隐藏索引2,4,6的模拟器

　　MuMuManager.exe control -v 2,4,6 hide_window



　　隐藏所有模拟器

　　MuMuManager.exe control -v all hide_window



　　6. 设置模拟器窗口位置和大小(layout_window)

　　使用：

　　control [--vmindex <vmindex>] layout_window

　　参数：

　　-v, --vmindex <vmindex> 选择要修改窗口的模拟器索引

　　-px, --pos_x <pos_x> 选择修改窗口的X轴位置，以屏幕左上角为原点

　　-py, --pos_y <pos_y> 选择修改窗口的Y轴位置，以屏幕左上角为原点

　　-sw, --size_w <size_w> 选择修改窗口的宽度

　　-sh, --size_h <size_h> 选择修改窗口的高度

　　（1）修改指定模拟器窗口(--vmindex)

　　举例：

　　修改索引为2的模拟器窗口位置为(100,100)，大小不变；

　　MuMuManager.exe control -v 2 layout_window -px 100 -py 100



　　修改索引2,4,6的模拟器窗口位置不变，大小为(1600,900)；

　　MuMuManager.exe control -v 2,4,6 layout_window -sw 1600 -sh 900



　　修改所有模拟器窗口位置为(100,100)，大小为(1600, 900)；

　　MuMuManager.exe control -v all layout_window -px 100 -py 100 -sw 1600 -sh 900



　　（2）只修改X坐标位置(--pos_x)

　　举例：修改索引为2的模拟器窗口X轴为100，其他不变

　　MuMuManager.exe control -v 2 layout_window -px 100



　　（3）只修改Y坐标位置(--pos_y)

　　举例：修改索引为2的模拟器窗口Y轴为200，其他不变

　　MuMuManager.exe control -v 2 layout_window -py 200



　　（4）只修改窗口宽度(--size_w)

　　举例：修改索引为2的模拟器窗口宽度为1600，其他不变

　　MuMuManager.exe control -v 2 layout_window -sw 1600



　　（5）只修改窗口高度(--size_h)

　　举例：修改索引为2的模拟器窗口高度为900，其他不变

　　MuMuManager.exe control -v 2 layout_window -sh 900



　　7. 控制模拟器里的应用(app)

　　使用：

　　control [--vmindex <vmindex>] app <subcommand>

　　参数：

　　-v, --vmindex <vmindex> 选择要控制的模拟器索引

　　（1）安装应用到模拟器里(install)

　　使用：

　　control [--vmindex <vmindex>] app install [--apk <apk>]

　　参数：

　　-v, --vmindex <vmindex> 选择要控制的模拟器索引

　　-apk, --apk <apk> 选择要安装的应用apk文件路径（支持apk/xapk/apks后缀）

　　举例：

　　安装 C 盘下 test.apk 的应用到索引为2的模拟器中；

　　MuMuManager.exe control -v 2 app install -apk C:\test.apk



　　安装 C 盘下 test.apk 的应用到索引为2,4,6的模拟器中；

　　MuMuManager.exe control -v 2,4,6 app install -apk C:\test.apk



　　安装 C 盘下 test.apk 的应用到所有模拟器中；

　　MuMuManager.exe control -v all app install -apk C:\test.apk



　　（2）卸载模拟器里的应用(uninstall)

　　使用：

　　control [--vmindex <vmindex>] app uninstall [--package <package>]

　　参数：

　　-v, --vmindex <vmindex> 选择要控制的模拟器索引

　　-pkg, --package <package> 选择要卸载的应用包名

　　举例：

　　在索引为2的模拟器中卸载应用原神(com.miHoYo.Yuanshen)；

　　MuMuManager.exe control -v 2 app uninstall -pkg com.miHoYo.Yuanshen



　　在索引为2,4,6的模拟器中卸载应用原神(com.miHoYo.Yuanshen)；

　　MuMuManager.exe control -v 2,4,6 app uninstall -pkg com.miHoYo.Yuanshen



　　在所有模拟器中卸载应用原神(com.miHoYo.Yuanshen)；

　　MuMuManager.exe control -v all app uninstall -pkg com.miHoYo.Yuanshen



　　（3）启动模拟器里的应用(launch)

　　使用：

　　control [--vmindex <vmindex>] app launch [--package <package>]

　　参数：

　　-v, --vmindex <vmindex> 选择要控制的模拟器索引

　　-pkg, --package <package> 选择要启动的应用包名

　　举例：

　　在索引为2的模拟器中启动应用原神(com.miHoYo.Yuanshen)；

　　MuMuManager.exe control -v 2 app launch -pkg com.miHoYo.Yuanshen



　　在索引为2,4,6的模拟器中启动应用原神(com.miHoYo.Yuanshen)；

　　MuMuManager.exe control -v 2,4,6 app launch -pkg com.miHoYo.Yuanshen



　　在所有模拟器中启动应用原神(com.miHoYo.Yuanshen)；

　　MuMuManager.exe control -v all app launch -pkg com.miHoYo.Yuanshen



　　（4）关闭模拟器里的应用(close)

　　使用：

　　control [--vmindex <vmindex>] app close [--package <package>]

　　参数：

　　-v, --vmindex <vmindex> 选择要控制应用的模拟器索引

　　-pkg, --package <package> 选择要关闭的应用包名

　　举例：

　　在索引为2的模拟器中关闭应用原神(com.miHoYo.Yuanshen)；

　　MuMuManager.exe control -v 2 app close -pkg com.miHoYo.Yuanshen



　　在索引为2,4,6的模拟器中关闭应用原神(com.miHoYo.Yuanshen)；

　　MuMuManager.exe control -v 2,4,6 app close -pkg com.miHoYo.Yuanshen



　　在所有模拟器中关闭应用原神(com.miHoYo.Yuanshen)；

　　MuMuManager.exe control -v all app close -pkg com.miHoYo.Yuanshen



　　（5）获取模拟器里的应用信息(info)

　　使用：

　　control [--vmindex <vmindex>] app info [--package <package>] [--installed]

　　参数：

　　-v, --vmindex <vmindex> 选择要控制的模拟器索引

　　-pkg, --package <package> 选择要查询的应用包名

　　-i, --installed 是否查询已安装应用列表和当前激活应用

　　①获取指定包名应用的状态(--package)

　　举例：

　　在索引为2的模拟器中查询应用原神(com.miHoYo.Yuanshen)信息；

　　MuMuManager.exe control -v 2 app info -pkg com.miHoYo.Yuanshen



　　在索引为2,4,6的模拟器中查询应用原神(com.miHoYo.Yuanshen)信息；

　　MuMuManager.exe control -v 2,4,6 app info -pkg com.miHoYo.Yuanshen



　　在所有模拟器中查询应用原神(com.miHoYo.Yuanshen)信息；

　　MuMuManager.exe control -v all app info -pkg com.miHoYo.Yuanshen



　　查询数据返回字段值说明：

　　{

　　"state": "stopped"

　　}

　　/*

　　running 代表应用正在运行

　　stopped 代表应用已安装但未启动

　　not_installed 代表应用未安装

　　*/

　　②获取当前已安装的应用集和当前激活应用(--installed)

　　举例：

　　在索引为2的模拟器中查询已安装应用信息；

　　MuMuManager.exe control -v 2 app info -i



　　在索引为2,4,6的模拟器中查询已安装应用信息；

　　MuMuManager.exe control -v 2,4,6 app info -i



　　在所有模拟器中查询已安装应用信息；

　　MuMuManager.exe control -v all app info -i



　　查询已安装应用数据返回字段值说明：

　　{

　　"active": "com.mumu.launcher", // 当前激活应用的包名

　　"com.netease.onmyoji": { // 阴阳师包名，表示已安装了阴阳师

　　"app_name": "阴阳师", // 阴阳师应用名称

　　"version": "1.7.69" // 阴阳师应用版本号

　　}

　　}

　　8.控制模拟器工具栏(tool)

　　使用：

　　control [--vmindex <vmindex>] tool <subcommand>

　　参数：

　　-v, --vmindex <vmindex> 选择要控制的模拟器索引

　　（1）触发工具栏功能(func)

　　使用：

　　control [--vmindex <vmindex>] tool func [--name <name>]

　　参数：

　　-v, --vmindex <vmindex> 选择要控制的模拟器索引

　　-n, --name <name> 要触发的工具栏功能名称

　　举例：

　　在索引为2的模拟器中点击工具栏屏幕旋转；

　　MuMuManager.exe control -v 2 tool func -n rotate



　　在索引为2,4,6的模拟器中点击工具栏屏幕旋转；

　　MuMuManager.exe control -v 2,4,6 tool func -n rotate



　　在所有模拟器中点击工具栏屏幕旋转；

　　MuMuManager.exe control -v all tool func -n rotate



　　①工具栏功能名称目前支持列表

　　MuMuManager.exe control -v 2 tool func -n rotate // 屏幕旋转

　　MuMuManager.exe control -v 2 tool func -n go_home // 主页

　　MuMuManager.exe control -v 2 tool func -n go_back // 返回

　　MuMuManager.exe control -v 2 tool func -n top_most // 窗口置顶

　　MuMuManager.exe control -v 2 tool func -n fullscreen // 窗口全屏

　　MuMuManager.exe control -v 2 tool func -n shake // 摇一摇

　　MuMuManager.exe control -v 2 tool func -n screenshot // 截屏

　　MuMuManager.exe control -v 2 tool func -n volume_up // 音量增加

　　MuMuManager.exe control -v 2 tool func -n volume_down // 音量减少

　　MuMuManager.exe control -v 2 tool func -n volume_mute // 切换静音

　　（2）限制CPU(downcpu)

　　使用：

　　control [--vmindex <vmindex>] tool downcpu [--cap <cap>]

　　参数：

　　-v, --vmindex <vmindex> 选择要控制的模拟器索引

　　-c, --cap <cap> 要限制CPU的百分比，1 ~ 100 之间整数有效

　　举例：

　　在索引为2的模拟器中限制CPU为50%；

　　MuMuManager.exe control -v 2 tool downcpu -c 50



　　在索引为2,4,6的模拟器中限制CPU为50%；

　　MuMuManager.exe control -v 2,4,6 tool downcpu -c 50



　　在所有模拟器中限制CPU为50%；

　　MuMuManager.exe control -v all tool downcpu -c 50



　　（3）修改虚拟定位(location)

　　使用：

　　control [--vmindex <vmindex>] tool location [--longitude <longitude>]

　　[--latitude <latitude>]

　　参数：

　　-v, --vmindex <vmindex> 选择要控制的模拟器索引

　　-lon, --longitude <longitude> 要修改虚拟定位的经度，-180 ~ 180 之间浮点有效

　　-lat, --latitude <latitude> 要修改虚拟定位的纬度，-90 ~ 90 之间浮点有效

　　举例：

　　在索引为2的模拟器中修改虚拟定位为经度114.1，纬度-23；

　　MuMuManager.exe control -v 2 tool location -lon 114.1 -lat -23



　　在索引为2,4,6的模拟器中修改虚拟定位为经度114.1，纬度-23；

　　MuMuManager.exe control -v 2,4,6 tool location -lon 114.1 -lat -23



　　在所有模拟器中修改虚拟定位为经度114.1，纬度-23；

　　MuMuManager.exe control -v all tool location -lon 114.1 -lat -23



　　（4）修改重力感应(gyro)

　　使用：

　　control [--vmindex <vmindex>] tool gyro [--gyro_x <gyro_x>]

　　[--gyro_y <gyro_y>] [--gyro_z <gyro_z>]

　　参数：

　　-v, --vmindex <vmindex> 选择要控制的模拟器索引

　　-gx, --gyro_x <gyro_x> 要修改重力感应的X轴，浮点，单位为角度

　　-gy, --gyro_y <gyro_y> 要修改重力感应的Y轴，浮点，单位为角度

　　-gz, --gyro_z <gyro_z> 要修改重力感应的Z轴，浮点，单位为角度

　　举例：

　　在索引为2的模拟器中修改重力感应X=40，Y=20，Z=30；

　　MuMuManager.exe control -v 2 tool gyro -gx 40 -gy 20 -gz 30



　　在索引为2,4,6的模拟器中修改重力感应X=40，Y=20，Z=30；

　　MuMuManager.exe control -v 2,4,6 tool gyro -gx 40 -gy 20 -gz 30



　　在所有模拟器中修改重力感应X=40，Y=20，Z=30；

　　MuMuManager.exe control -v all tool gyro -gx 40 -gy 20 -gz 30



　　9. 控制模拟器快捷方式(shortcut)

　　使用：

　　control [--vmindex <vmindex>] shortcut <subcommand>

　　参数：

　　-v, --vmindex <vmindex> 选择要控制的模拟器索引

　　（1）创建桌面快捷方式(create)

　　使用：

　　control [--vmindex <vmindex>] shortcut create [--name <name>]

　　[--icon <icon>] [--package <package>]

　　参数：

　　-v, --vmindex <vmindex> 选择要控制的模拟器索引

　　-n, --name <name> 创建快捷方式的名称

　　-i, --icon <icon> 创建快捷方式的图标路径

　　-pkg, --package <package> 创建自动启动应用的快捷方式

　　举例：

　　在桌面创建索引为2的模拟器的快捷方式 test，图标用 C 盘的 test.ico，自动启动原神；

　　MuMuManager.exe control -v 2 shortcut create -n test -i C:\test.ico -pkg com.miHoYo.Yuanshen



　　在桌面创建索引为2,4,6的模拟器的快捷方式，图标用 C 盘的 test.ico，自动启动原神；

　　MuMuManager.exe control -v 2,4,6 shortcut create -i C:\test.ico -pkg com.miHoYo.Yuanshen



　　在桌面创建所有模拟器的快捷方式，图标用 C 盘的 test.ico，自动启动原神；

　　MuMuManager.exe control -v all shortcut create -i C:\test.ico -pkg com.miHoYo.Yuanshen



　　（2）删除桌面快捷方式(delete)

　　使用：

　　control [--vmindex <vmindex>] shortcut delete

　　参数：

　　-v, --vmindex <vmindex> 选择要控制的模拟器索引

　　举例：

　　在桌面删除索引为2的模拟器的所有快捷方式；

　　MuMuManager.exe control -v 2 shortcut delete



　　在桌面删除索引为2,4,6的模拟器的所有快捷方式；

　　MuMuManager.exe control -v 2,4,6 shortcut delete



　　在桌面删除所有模拟器的所有快捷方式；

　　MuMuManager.exe control -v all shortcut delete



 

九、配置模拟器(setting)

　　使用：

　　setting [--vmindex <vmindex>] [--key <key>] [--value <value>] [--all]

　　[--all_writable] [--info] [--path <path>]

　　参数：

　　-v, --vmindex <vmindex> 选择要配置的模拟器索引

　　-k, --key <key> 选择要读取或修改的配置

　　-val, --value <value> 选择要修改的配置值

　　-a, --all 选择所有配置

　　-aw, --all_writable 选择所有可修改配置

　　-i, --info 查询配置属性

　　-p, --path <path> 选择JSON配置文件，根据配置文件批量修改配置值

　　1. 获取所有配置(--all)

　　举例：获取索引为2的模拟器的所有配置的值；

　　MuMuManager.exe setting -v 2 -a



　　2. 获取所有可写配置(--all_writable)

　　举例：获取索引为2的模拟器的所有可修改配置的值；

　　MuMuManager.exe setting -v 2 -aw



　　目前所有的可修改配置描述如下：

　　{

　　 "apk_asscciation": "true", // 设置中心-其他-APK关联-是否关联APK文件

　　 "app_keptlive": "false", // 设置中心-其他-应用运行-是否后台挂机保活

　　 "dynamic_adjust_frame_rate": "false", // 设置中心-显示-帧率设置-是否动态调整帧率

　　 "dynamic_low_frame_rate_limit": "15", // 设置中心-显示-帧率设置-动态调整帧率-降低帧率

　　 "force_discrete_graphics": "true", // 设置中心-显示-强制使用独立显卡

　　 "gpu_mode": "middle", // 设置中心-机型-GPU型号-型号类型

　　 "gpu_model.custom": "Adreno (TM) 640", // 设置中心-机型-GPU型号-自定义型号

　　 "joystick_auto_connect": "true", // 设置中心-其他-手柄功能-是否开启手柄自动连接

　　 "max_frame_rate": "60", // 设置中心-显示-帧率设置-最高帧率限制的值

　　 "mouse_style": "true", // 设置中心-其他-鼠标指针-是否使用模拟器定制鼠标

　　 "net_bridge_card": "", // 设置中心-网络-桥接网卡名称

　　 "net_bridge_dns1": "", // 设置中心-网络-桥接网络DNS1

　　 "net_bridge_dns2": "", // 设置中心-网络-桥接网络DNS2

　　 "net_bridge_gateway": "", // 设置中心-网络-桥接网络网关

　　 "net_bridge_ip_addr": "", // 设置中心-网络-桥接网络IP地址

　　 "net_bridge_ip_mode": "dhcp", // 设置中心-网络-桥接网络模式选择

　　 "net_bridge_open": "false", // 设置中心-网络-是否开启桥接模式

　　 "net_bridge_subnet_mask": "", // 设置中心-网络-桥接网络掩码

　　 "performance_cpu.custom": "4", // 设置中心-性能-自定义CPU

　　 "performance_mem.custom": "6.000000", // 设置中心-性能-自定义内存

　　 "performance_mode": "middle", // 设置中心-性能-性能配置策略

　　 "phone_brand": "HUAWEI", // 设置中心-机型-手机品牌

　　 "phone_imei": "352070100579777", // 设置中心-机型-IMEI编码

　　 "phone_miit": "NCO-AL00", // 设置中心-机型-入网型号

　　 "phone_model": "畅享 50 Pro", // 设置中心-机型-手机型号

　　 "phone_number": "", // 设置中心-机型-手机号码

　　 "player_name": "MuMu模拟器12", // 模拟器名称

　　 "prevent_sleep": "true", // 设置中心-其他-电脑休眠-是否开启

　　 "quit_confirm": "true", // 设置中心-其他-退出设置-是否弹窗确认

　　 "renderer_mode": "vk", // 设置中心-性能-显卡渲染模式选择

　　 "renderer_strategy": "auto", // 设置中心-性能-显存使用策略

　　 "resolution_dpi.custom": "240.000000", // 设置中心-显示-分辨率设置-自定义DPI

　　 "resolution_height.custom": "900.000000", // 设置中心-显示-分辨率设置-自定义高

　　 "resolution_mode": "tablet.1", // 设置中心-显示-分辨率设置-模式选择

　　 "resolution_width.custom": "1600.000000", // 设置中心-显示-分辨率设置-自定义宽

　　 "root_permission": "false", // 设置中心-其他-ROOT权限-是否开启

　　 "screen_brightness": "50", // 设置中心-显示-画面设置-画面亮度

　　 "show_frame_rate": "false", // 设置中心-显示-帧率设置-是否显示帧率

　　 "system_disk_readonly": "true", // 设置中心-磁盘-磁盘共享-是否使用只读系统盘

　　 "system_volume_close": "false", // 设置中心-声音-系统声音-是否关闭系统声音

　　 "vertical_sync": "false", // 设置中心-显示-帧率设置-是否开启垂直同步

　　 "window_auto_rotate": "true", // 设置中心-显示-屏幕旋转-是否自动旋转

　　 "window_save_rect": "false", // 设置中心-显示-窗口位置和大小-是否记住上次位置和大小

　　 "window_size_fixed": "false" // 设置中心-显示-窗口位置和大小-是否固定大小静止拉伸

　　 }

　　3. 获取配置属性(--info)

　　举例：

　　获取索引为2的模拟器的所有配置的属性（可读/可写/可选值/描述）；

　　MuMuManager.exe setting -v 2 -i

　　获取索引为2的模拟器的配置 window_size_fixed 的属性；

　　MuMuManager.exe setting -v 2 -k window_size_fixed -i



　　获取索引为2的模拟器的配置 window_size_fixed 和 window_save_rect 的属性；

　　MuMuManager.exe setting -v 2 -k window_size_fixed -k window_save_rect -i



　　4. 获取指定一个或多个配置(--key)

　　举例：

　　获取索引为2的模拟器的配置 window_size_fixed 的值；

　　MuMuManager.exe setting -v 2 -k window_size_fixed



　　获取索引为2的模拟器的配置 window_size_fixed 和 window_save_rect 的值；

　　MuMuManager.exe setting -v 2 -k window_size_fixed -k window_save_rect



　　5. 修改一个或多个配置(--value)

　　举例：

　　修改索引为2的模拟器的配置 window_size_fixed 的值为 true；

　　MuMuManager.exe setting -v 2 -k window_size_fixed -val true



　　修改索引为2的模拟器的配置 window_size_fixed 的值为 false，配置 window_save_rect 的值为 true；

　　MuMuManager.exe setting -v 2 -k window_size_fixed -val false -k window_save_rect -val true



　　6. 根据JSON文件内容修改配置(--path)

　　举例：

　　一个 utf8 格式 test.json 文件在C盘下，文件内容如下：

　　{

　　"window_save_rect": "true",

　　"window_size_fixed": "false"

　　}

　　修改索引为2的模拟器的配置，通过JSON文件方式修改，和 9.5.(2) 达到的效果一样；

　　MuMuManager.exe setting -v 2 -p C:\test.json



　　7. 获取全局配置默认值（新建模拟器使用默认值）

　　举例：

　　获取模拟器的所有配置的默认值；

　　MuMuManager.exe setting -a



　　获取模拟器的所有可修改配置的默认值；

　　MuMuManager.exe setting -aw



　　获取模拟器的配置 window_size_fixed 的默认值；

　　MuMuManager.exe setting -k window_size_fixed



　　8. 修改全局配置默认值（新建模拟器使用默认值）

　　举例：

　　修改模拟器的配置 window_size_fixed 的默认值；

　　MuMuManager.exe setting -k window_size_fixed -val true



　　修改模拟器的配置默认值，以 JSON 文件格式；

　　MuMuManager.exe setting -p C:\test.json



 

十、ADB便捷命令(adb)

　　使用：

　　adb [--vmindex <vmindex>] [--cmd <cmd>]

　　参数：

　　-v, --vmindex <vmindex> 选择要连接的模拟器索引

　　-c, --cmd <cmd> 选择要执行的命令

　　举例：

　　ADB 连接索引为2的模拟器，并执行命令输入文本“哈哈 嘻嘻”；

　　MuMuManager.exe adb -v 2 -c input_text 哈哈 嘻嘻



　　ADB 连接索引为2,4,6的模拟器，并执行命令输入文本“哈哈 嘻嘻”；

　　MuMuManager.exe adb -v 2,4,6 -c input_text 哈哈 嘻嘻



　　ADB 连接所有模拟器，并执行命令输入文本“哈哈 嘻嘻”；

　　MuMuManager.exe adb -v all -c input_text 哈哈 嘻嘻



　　1. 快捷命令目前支持列表

　　MuMuManager.exe adb -v 2 -c input_text 哈哈 // 文本输入

　　MuMuManager.exe adb -v 2 -c connect // 连接

　　MuMuManager.exe adb -v 2 -c disconnect // 断开连接

　　MuMuManager.exe adb -v 2 -c getprop ro.opengles.version // 获取安卓属性

　　MuMuManager.exe adb -v 2 -c setprop ro.opengles.version xxx // 修改安卓属性

　　MuMuManager.exe adb -v 2 -c go_back // 按下安卓返回键

　　MuMuManager.exe adb -v 2 -c go_home // 按下安卓首页键

　　MuMuManager.exe adb -v 2 -c go_task // 按下安卓任务键

　　MuMuManager.exe adb -v 2 -c volume_up // 按下音量加键

　　MuMuManager.exe adb -v 2 -c volume_down // 按下音量减键

　　MuMuManager.exe adb -v 2 -c volume_mute // 按下静音键

　　2. 其他 shell 命令调用

　　MuMuManager.exe adb -v 2 -c "shell pm list package | grep onmyoji"

 

十一、模拟器机型属性(simulation)

　　使用：

　　simulation [--vmindex <vmindex>] [--simu_key <simu_key>] [--simu_value <simu_value>]

　　参数：

　　-v, --vmindex <vmindex> 选择要修改的模拟器索引

　　-sk, --simu_key <simu_key> 选择要修改的模拟器配置

　　-sv, --simu_value <simu_value> 选择修改的配置值

　　1. 目前机型属性支持列表

　　{

　　"imei": "", // IMEI，安卓12不允许应用获取IMEI

　　"imsi": "", // IMSI，安卓12不允许应用获取IMSI

　　"android_id": "", // Android ID

　　"model": "", // 设备

　　"brand": "", // 主板

　　"solution": "", // 硬件

　　"phone_number": "", // 手机号码，安卓12不允许应用获取手机号码

　　"mac_address": "" // MAC 地址，安卓12不允许应用获取MAC

　　}

　　举例：

　　设置索引为2的模拟器机型属性 MAC 地址为 08:fb:5f:84:40:00；

　　MuMuManager.exe simulation -v 2 -sk mac_address -sv "08:fb:5f:84:40:00"



　　设置索引为2,4,6的模拟器机型属性 MAC 地址为 08:fb:5f:84:40:00；

　　MuMuManager.exe simulation -v 2,4,6 -sk mac_address -sv "08:fb:5f:84:40:00"



　　设置所有模拟器机型属性 MAC 地址为 08:fb:5f:84:40:00；

　　MuMuManager.exe simulation -v all -sk mac_address -sv "08:fb:5f:84:40:00"



　

十二、模拟器窗口排序(sort)

　　使用：

　　sort

　　参数：

　　无

　　举例：排列所有模拟器窗口

　　MuMuManager.exe sort



 

十三、模拟器驱动管理(driver)

　　使用：

　　driver <subcommand>

　　参数：

　　无

　　1. 安装驱动

　　使用：

　　driver install [--name <name>]

　　参数：

　　-n, --name <name> 要安装的驱动名，目前只支持网络桥接驱动(lwf)

　　举例：安装网络桥接驱动（需要管理员权限）

　　MuMuManager.exe driver install -n lwf



　　2. 卸载驱动

　　使用：

　　driver uninstall [--name <name>]

　　参数：

　　-n, --name <name> 要卸载的驱动名，目前只支持网络桥接驱动(lwf)

　　举例：卸载网络桥接驱动（需要管理员权限）

　　MuMuManager.exe driver uninstall -n lwf



 

十四、兼容大部分旧命令参数（后面可能会废弃，谨慎使用）

　　查看/连接模拟器adb端口：

　　查询指定模拟器adb端口

　　MuMuManager.exe adb -v [模拟器序号]



　　连接指定模拟器adb端口

　　MuMuManager.exe adb -v [模拟器序号] connect



　　进入指定模拟器adb shell

　　MuMuManager.exe adb -v [模拟器序号] shell



　　启动/关闭模拟器：

　　启动模拟器

　　MuMuManager.exe api -v [模拟器序号] launch_player



　　关闭模拟器

　　MuMuManager.exe api -v [模拟器序号] shutdown_player



　　app安装/卸载/启动/关闭：

　　安装本地apk，带文件路径参数

　　MuMuManager.exe api -v [模拟器序号] install_apk [path]



　　卸载app，带包名

　　MuMuManager.exe api -v [模拟器序号] uninstall_app [package]



　　启动app，带包名

　　MuMuManager.exe api -v [模拟器序号] launch_app [package]



　　关闭app，带包名

　　MuMuManager.exe api -v [模拟器序号] close_app [package]



　　获取app运行状态，带包名

　　MuMuManager.exe api -v [模拟器序号] app_state [package]



　　模拟器显示：

　　显示指定模拟器窗口（顶部）

　　MuMuManager.exe api -v [模拟器序号] show_player_window



　　隐藏指定模拟器窗口（无任务栏）

　　MuMuManager.exe api -v [模拟器序号] hide_player_window



　　设置窗口大小和位置

　　MuMuManager.exe api set_window_pos [模拟器序号] [x,y,w,h]



　　获取状态：

　　获取VT状态

　　MuMuManager.exe api -v [模拟器序号] vt_enabled



　　获取HyperV状态

　　MuMuManager.exe api -v [模拟器序号] hyperv_enabled



　　获取模拟器状态

　　MuMuManager.exe api -v [模拟器序号] player_state



　　获取模拟器列表

　　MuMuManager.exe api get_player_list



　　配置模拟器:

　　获取模拟器配置属性

　　MuMuManager.exe setting -v [模拟器序号] keys

　　获取模拟器配置

　　MuMuManager.exe setting -v [模拟器序号] get_key [配置]



　　获取模拟器配置

　　MuMuManager.exe setting -v [模拟器序号] get_keys [配置1],[配置2],...



　　修改模拟器配置值

　　MuMuManager.exe setting -v [模拟器序号] set_key [配置] [配置值]



　　修改模拟器配置值

　　MuMuManager.exe setting -v [模拟器序号] set_keys [配置1]=[配置值1],[配置2]=[配置值2],...



　　获取模拟器全局默认配置属性

　　MuMuManager.exe setting keys

　　获取模拟器全局默认配置

　　MuMuManager.exe setting get_key [配置]



　　获取模拟器全局默认配置

　　MuMuManager.exe setting get_keys [配置1],[配置2],...



　　修改模拟器全局默认配置值

　　MuMuManager.exe setting set_key [配置] [配置值]



　　修改模拟器全局默认配置值

　　MuMuManager.exe setting set_keys [配置1]=[配置值1],[配置2]=[配置值2],...



　　设置窗口大小和位置

　　MuMuManager.exe setting -v [模拟器序号] set_window_pos [x,y,w,h]
