from ast import Num
from typing import Any, Callable, Dict, List, Optional, Tuple
from . import mw as m
version = '0.2.0-α+200612'
aka = 'Dark Elf'
data = None


########## 系统 ##########
def init(config: Optional[Dict[str, Any]] = None) -> None:
    """
    # 初始化引擎
    """
    m.init(config)
    # 兼容
    global data
    data = m.old_data()


def config(config: Optional[Dict[str, Any]] = None) -> None:
    """
    # （设置引擎参数） TODO
    """
    current_config = config


def entry(ui_func: Callable[[], None]) -> None:
    """
    # （注册入口界面） TODO
    """
    m.entry(ui_func)


def start() -> None:
    """
    # （启动引擎） TODO
    """
    m.start()


def exit(auto_save: bool = False) -> None:
    """
    # 退出程序 TODO
    """
    pass


########## 调试 ##########
def debug(*arg: str) -> None:
    """
    # 调试输出：Debug

    在任何情形下你都可以使用Debug级别进行调试输出，这会给你带来最为详细的

    debug()和Python的内置print()函数用法类似，但除了在命令行内输出带格式的输出信息之外，还会在`Erajs.log`中进行记录。

    调试等级从低到高分别是`debug`<`info`<`warn`<`error`<`critical`

    TODO 默认调试等级为`info`，即只有`info`或更高的等级会生效。

    TODO 可通过`config({debug_level: 'info'})`设置调试等级
    """
    m.debug(*arg)


def info(*arg: str) -> None:
    """
    # 调试输出：Info
    """
    m.info(*arg)


def warn(*arg: str) -> None:
    """
    # 调试输出
    """
    m.warn(*arg)


def error(*arg: str) -> None:
    """
    # 调试输出
    """
    m.error(*arg)


def critical(*arg: str) -> None:
    """
    # 调试输出
    """
    m.critical(*arg)


########## 窗口 ##########
def window(style: Dict[str, Any]) -> None:
    """
    # 设置窗口样式
    """
    m.window(style)


def title(text: str, style: Optional[Dict[str, str]] = None) -> object:
    """
    # 设置窗口标题
    """
    m.title(text, style)


def footer(text: str, style: Optional[Dict[str, str]] = None) -> object:
    """
    # 设置窗口脚注
    """
    m.footer(text, style)


def msg(text: str, duration: float = 3, style: Optional[Dict[str, str]] = None) -> None:
    """
    # 设置窗口脚注
    """
    m.msg(text, duration, style)


########## 页面管理 ##########
def page(style: Optional[Dict[str, str]] = None) -> object:
    """
    # 生成新的空白页面
    """
    m.page(style)


def cls(num: int = 0) -> None:
    """
    # 清屏
    """
    m.cls(num)


########## 块 ##########
def mode(type: Optional[str] = 'line', *arg: Any, **kw: Any) -> None:
    """
    # 设置新增控件排版模式
    """
    m.mode(type, *arg, **kw)


def divider(text: Optional[str] = None, style: Optional[Dict[str, str]] = None) -> object:
    """
    # 插入块级控件：分割线
    """
    return m.divider(text, style)


########## 行 ##########
def heading(text: Optional[str] = None, rank: int = 1, style: Optional[Dict[str, str]] = None) -> object:
    """
    # 插入行内控件：标题
    """
    return m.heading(text, rank, style)


h = heading


def text(text: Optional[str] = None, wait: bool = False, style: Optional[Dict[str, str]] = None) -> object:
    """
    # 插入行内控件：文本
    """
    return m.text(text, wait, style)


t = text


def button(text: Optional[str] = None, callback: Optional[Callable[[Any], None]] = None, *arg: Any, **kw: Any) -> object:
    """
    # 插入行内控件：按钮
    """
    return m.button(text, callback, *arg, **kw)


b = button


def link(text: Optional[str] = None, callback: Optional[Callable[[], None]] = None, style: Optional[Dict[str, str]] = None, *arg: Any, **kw: Any) -> object:
    """
    # 插入行内控件：链接
    """
    return m.link(text, callback, style, *arg, **kw)


l = link


def progress(now: float = 0, max: float = 100, style: Optional[List[Dict[str, str]]] = None) -> object:
    """
    # 插入行内控件：进度条
    """
    return m.progress(now, max, style)


def rate(now: int = 0, max: int = 5, callback: Optional[Callable[[int], None]] = None, style: Optional[Dict[str, str]] = None) -> object:
    """
    # 插入行内控件：评分
    """
    return m.rate(now, max, callback, style)


def check(text: Optional[str] = None, callback: Optional[Callable[[bool], None]] = None, default: bool = False, style: Optional[Dict[str, str]] = None) -> object:
    """
    # 插入行内控件：多选
    """
    return m.check(text, callback, default, style)


def radio(text_list: List[str], callback: Optional[Callable[[int], None]] = None, default_index: int = 0, style: Optional[Dict[str, str]] = None) -> object:
    """
    # 插入行内控件：单选
    """
    return m.radio(text_list, callback, default_index, style)


def input(callback: Optional[Callable[[str], None]] = None, default: str = '', is_area: bool = False, placeholder: str = '', style: Optional[Dict[str, str]] = None) -> object:
    """
    # 插入行内控件：输入框
    """
    return m.input(callback, default, is_area, placeholder, style)


def dropdown(text_list: Optional[List[str]] = None, callback: Optional[Callable[[int], None]] = None, default_index: int = 0, search: bool = False, multiple: bool = False, placeholder: str = '', allowAdditions: bool = False, style: Optional[Dict[str, str]] = None) -> object:
    """
    # 插入行内控件：下拉列表
    """
    return m.dropdown(text_list, callback, default_index, search,
                      multiple, placeholder, allowAdditions, style)


########## 样式管理 ##########
def set_style(widget: Callable[[], Any], style: Dict[str, str]) -> None:
    """
    # 设置样式
    """
    m.set_style(widget, style)


def reset_style(widget: Callable[[], Any]) -> None:
    """
    # 重置样式
    """
    m.reset_style(widget)


########## 界面逻辑 ##########
def goto(ui_func: Callable[[], Any], *arg: Any, **kw: Any) -> None:
    """
    # 将界面节点添加到界面栈的末尾，并触发
    """
    m.goto(ui_func, *arg, **kw)


def back(num: int = 1, *arg: Any, **kw: Any) -> None:
    """
    # 从界面栈删除n（默认为1）个界面节点，并触发删除之后的末尾节点
    """
    m.back(num, *arg, **kw)


def repeat(*arg: Any, **kw: Any) -> None:
    """
    # 不对界面栈进行修改，并触发末尾节点
    """
    m.repeat(*arg, **kw)


def clear(num: int = 0) -> None:
    """
    # 清空界面栈
    """
    m.clear(num)


def insert(ui_func: Callable[[], Any], *arg: Any, **kw: Any) -> None:
    """
    # 将界面节点添加到界面栈的末尾，但不触发
    """
    pass


def get_gui_stack() -> List[str]:
    """
    # 返回界面栈，以界面名称列表的格式
    """
    return m.get_gui_stack()


########## 数据管理 ##########
def cfg(dot_path: Optional[str] = None) -> Any:
    """
    # 返回设置数据
    """
    return m.cfg(dot_path)


def dat(dot_path: Optional[str] = None) -> Any:
    """
    # 返回静态数据
    """
    return m.dat(dot_path)


def sav(dot_path: Optional[str] = None) -> Any:
    """
    # 返回存档数据
    """
    return m.sav(dot_path)


def tmp(key: Optional[str] = None) -> Any:
    """
    # 返回临时数据
    """
    return m.tmp(key)


def dump_cfg(dot_path: Optional[str] = None, ext: str = 'yaml') -> None:
    """
    # 保存设置数据
    """
    return m.write_cfg(dot_path, ext)


def dump_dat(dot_path: Optional[str] = None, ext: str = 'json') -> None:
    """
    # 保存静态数据
    """
    return m.write_dat(dot_path, ext)


def save(filename_without_ext: Optional[str] = None, meta_info: Optional[Dict[str, str]] = None) -> None:
    """
    # 转储存档数据
    """
    m.save(filename_without_ext, meta_info)


def load(filename_without_ext: Optional[str] = None):
    """
    # 转储存档数据
    """
    m.load(filename_without_ext)


def scan_save_file():
    return m.scan_save_file()


########## 事件 ##########
def on(event_name: str, listener: Callable[[], Any]) -> None:
    """
    # 注册侦听器
    """
    pass


def once(event_name: str, listener: Callable[[], Any]) -> None:
    """
    # 注册一次性侦听器
    """
    pass


def off(event_name: str, listener: Callable[[], Any]) -> None:
    """
    # 注销侦听器
    """
    pass


def emit(event_name: str, *arg: Any, **kw: Any) -> None:
    """
    # 发布事件
    """
    pass


########## 实验性 ##########
def dangerously_get_engine_core() -> object:
    """
    # 获取引擎核心（危险）
    """
    return m.dangerously_get_engine_core()


########## 工具 ##########
def random_hash(level: int = 4) -> str:
    """
    # 获取随机哈希值
    """
    return m.random_hash(level)


def get_current_timestamp() -> str:
    """
    # 获取时间戳
    """
    return m.get_current_timestamp()


########## 预设控件 ##########
def widget_save() -> None:
    """
    # 插入块级复合控件：存档保存列表（单页）
    """
    def save_file(i, filename_without_ext):
        if i == -1:
            save(get_current_timestamp())
        else:
            save(filename_without_ext)
        repeat()
    mode()
    for i, each in enumerate(scan_save_file()):
        b('{}. {}'.format(i, each[0]), save_file, i, each[0])
        t()
    b('+', save_file, -1, '')
    t()


def widget_load(callback) -> None:
    """
    # 插入块级复合控件：存档加载列表（单页）
    """
    def load_file(i, filename_without_ext):
        load(filename_without_ext)
        callback()
    mode()
    for i, each in enumerate(scan_save_file()):
        b('{}. {}'.format(i, each[0]), load_file, i, each[0])
        t()


def ui_save() -> None:
    """
    # 插入块级复合控件：存档保存列表（单页）
    """
    page()
    h('保存存档')
    t()
    t()
    widget_save()
    t()
    b('返回', back)


def ui_load(callback) -> None:
    """
    # 插入块级复合控件：存档加载列表（单页）
    """
    page()
    h('加载存档')
    t()
    t()
    widget_load(callback)
    t()
    b('返回', back)


########## 弃用 ##########
def get_full_time():
    pass


def tick():
    pass


def save_data_to_file():
    """
    弃用
    现在用`save_cfg`，`save_dat`，`save_sav`代替
    """
    pass


def shake():
    pass


def generate_map():
    pass


# def clear(num=0):
#     """
#     # 初始化引擎
#     """
#     pass


def append_gui(ui_func, *arg: Any, **kw: Any):
    """
    # 添加界面节点但不触发
    """
    pass


def get_gui_list():
    """
    # 初始化引擎
    """
    pass
