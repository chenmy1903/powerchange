<!--
 Copyright 2022 chenmy1903
 
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 
     http://www.apache.org/licenses/LICENSE-2.0
 
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
-->
# PowerChangeTools (PCT)-电源计划解锁工具

> 已知问题: 使用本工具切换后并不是真正的解锁, 只是替换第二个电源选项位, 可以通过本工具改回平衡来隐藏解锁的模式

## 1.1版本修复问题

1. 修复查看版本会出现UAC界面的bug
## 下载

[GitHub Releases](https://github.com/chenmy1903/powerchange/releases)

## 命令行

> 可以通过`PowerChangeTools.exe -h`获得帮助

```
usage: WindowsPowerChange (电源模式切换工具) [-h] [--upmode] [--supermode] [--nonemode] [--morepower] [--version]
                                     [--noadmin]

options:
  -h, --help            show this help message and exit
  --upmode, --高性能, -up  Change power mode to 高性能
  --supermode, --烤鸡模式, --卓越性能, -super
                        Change power mode to 烤鸡模式
  --nonemode, --平衡模式, -none
                        Change power mode to 平衡模式
  --morepower, --节电模式, -mpower
                        Change power mode to 节电模式
  --version, -v         查看程序的版本(然后退出程序)
  --noadmin             不使用管理员模式启动程序(不推荐, 可能出现权限问题)
```

## 模式说明

1. [高性能](#高性能)
2. [卓越模式](#烤鸡模式)
3. [平衡](#平衡模式)
4. [节电模式](#节电模式)

### 高性能

其实这个模式在Windows7中就出现了, 但是在Windows10中被隐藏了, 笔记本是阉割版的高性能模式 (被本工具强制解锁之后)

### 烤鸡模式

是微软在Windows 10-1809中加入的隐藏电源选项, 可以通过本工具解锁 (如果受支持运行`PowerChangeTools.exe -h`会出现以下的提示)

```
--supermode, --烤鸡模式, --卓越性能, -super
                        Change power mode to 烤鸡模式
```

## 平衡模式

默认的电源模式

## 节电模式

Windows 10中已被移到右下角的电池图标里边的一个选项, 本工具可以在台式机上强制解锁节电模式
