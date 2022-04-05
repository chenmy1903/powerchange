"""电源计划解锁工具"""
# Copyright 2022 chenmy1903
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import random
import sys
import ctypes
import time
import tqdm
import platform
import argparse

WINDOWS = "nt"
LINUX = "linux"
JAVA = "java"

EAT_CHICKEN_MODE = "9d30256f-a178-40c8-84e1-69632c772462"  # 卓越性能
UP_MODE = "c7fda327-7423-460d-9cf3-2d427e4baea6"  # 高性能
DONT_PLAY_GAME_MODE = "a1841308-3541-4fab-bc81-f71556f20b4a"  # 节能模式
NONE_MODE = "381b4222-f694-41f0-9685-ff5bb260df2e"  # 平衡模式

__version__ = "1.1"  # 版本号


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def is_in_exe():
    """判断是否在exe中运行"""
    return not (sys.exec_prefix == os.path.dirname(sys.executable))


def _get_file_dir() -> str:
    """文件所在目录"""
    if is_in_exe():
        return os.path.dirname(os.path.abspath(sys.executable))
    return os.path.dirname(os.path.abspath(__file__))


BASE_DIR = _get_file_dir()


def pause(*, quit: bool = False) -> int:
    return_code = os.system("pause")
    sys.exit() if quit else None
    return return_code


def title(t: str) -> int:
    return os.system(f"title {t}")


def system_type():
    """判断系统类型
0为不可运行程序(linux或java虚拟机)
    """
    name = os.name
    if name == WINDOWS:
        win_version = platform.version().split(".")
        if win_version[0] in ["10"] and int(win_version[2]) > 1803:
            return 1  # 可以继续运行
        if win_version[0] in ["10"]:
            return 2  # 低于1803, 只可以调整到高性能模式
    return 0


def change(power_id: str):
    """切换电源计划"""
    command = "powercfg /SETACTIVE " + power_id
    return os.system(command)


def init_parser():
    parser = argparse.ArgumentParser("WindowsPowerChange (电源模式切换工具)")
    parser.add_argument("--upmode", "--高性能", "-up",
                        action="store_true", help="Change power mode to 高性能")
    if system_type() == 1:
        parser.add_argument("--supermode", "--烤鸡模式", "--卓越性能",
                            "-super", help="Change power mode to 烤鸡模式", action="store_true")
    parser.add_argument("--nonemode", "--平衡模式", "-none",
                        action="store_true", help="Change power mode to 平衡模式")
    parser.add_argument("--morepower", "--节电模式", "-mpower",
                        action="store_true", help="Change power mode to 节电模式")
    parser.add_argument("--version", "-v",
                        help="查看程序的版本(然后退出程序)", version=__version__, action="version")
    parser.add_argument("--noadmin", help="不使用管理员模式启动程序(不推荐, 可能出现权限问题)", action="store_true")
    return parser


def cmd_loop():
    title("PowerChangeTools-CmdLoop")
    print("准备载入CmdLoop, 请稍等")
    print("以下效果纯属娱乐, 如果无法正常进入请按Ctrl-C跳过")
    try:
        all_range = random.randint(500, 1000)
        for i in tqdm.tqdm(range(all_range), desc="呼叫王建国"):
            title(
                f"PowerChangeTools-CmdLoading {round((i / all_range) * 100)}%")
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("已为您跳过娱乐效果, 请操作")
    title("PowerChangeTools-CmdLoop")
    print("输入1切换至高性能模式")
    print("输入2切换到烤鸡模式 (可能不受支持)")
    print("输入3切换到节能模式")
    print("输入4切换到平衡模式")
    res = input("输入完按回车即可切换: ").replace(" ", "")
    error = 0
    if res == "1":
        if change(UP_MODE):
            error = 1
            print("切换失败, Windows出现了错误, 错误提示见上方")
    elif res == "2" and system_type() == 1:
        if change(EAT_CHICKEN_MODE):
            error = 1
            print("切换失败, Windows出现了错误, 错误提示见上方")
    elif res == "3":
        if change(DONT_PLAY_GAME_MODE):
            error = 1
            print("切换失败, Windows出现了错误, 错误提示见上方")
    elif res == "4":
        if change(NONE_MODE):
            error = 1
            print("切换失败, Windows出现了错误, 错误提示见上方")
    else:
        print("输入错误")
        return
    if not error:
        print("操作成功完成")


def main():
    title("PowerChangeTools")
    print("电源计划解锁工具正在启动, 请等待")
    print("验证操作系统中")
    if system_type() == 0:
        print("您的操作系统不受支持, 仅支持Windows 10和Windows 11")
        pause(quit=True)
    print("读取参数中")
    argv_parser = init_parser()
    argv = argv_parser.parse_args()
    if argv.upmode:
        print("读取到您要开启高性能模式, 准备开启")
        if change(UP_MODE):
            print("开启失败, 请检查权限")
    elif getattr(argv, "supermode", False):
        print("读取到您要开启烤鸡模式(卓越模式), 准备开启")
        if change(EAT_CHICKEN_MODE):
            print("开启失败, 请检查您的系统是否支持本模式, 或者是权限问题")
    elif argv.morepower:
        print("读取到您要开启节电模式(不能玩游戏模式), 准备开启")
        if change(DONT_PLAY_GAME_MODE):
            print("开启失败, 请检查权限")
    elif argv.nonemode:
        print("读取到您要开启节电模式(不能玩游戏模式), 准备开启")
        if change(NONE_MODE):
            print("开启失败, 请检查权限")
    else:
        cmd_loop()
    pause()


if __name__ == "__main__":
    if is_admin() or len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help", "--noadmin", "--version", "-v"]:
        main()
    else:
        if is_in_exe():
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv[1:]), None, 1)
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
