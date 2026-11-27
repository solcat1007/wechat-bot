# -*- coding: utf-8 -*-
"""
SOLCAT 彩蛋模块 v2.0 — WeChatBot 专属彩蛋命令
================================================
独立模块，零外部依赖，不改动 bot.py 的原有命令体系。

对外接口：
  - handle_egg_command(text) -> str | None  命中彩蛋命令时返回回复文本
  - egg_banner() -> str                     返回 ASCII 署名横幅
  - EGG_COMMANDS                            彩蛋命令清单

触发命令：/solcat  /彩蛋  /egg  /42
"""

# SOLCAT ASCII 署名（与 SOLCAT v2.0 彩蛋协议一致）
ASCII_ART = r"""
  ____             _   _       _   _
 / ___|  ___  _ __| |_(_) __ _| |_| |__
 \___ \ / _ \| '__| __| |/ _` | __| '_ \
  ___) | (_) | |  | |_| | (_| | |_| | |
 |____/ \___/|_|   \__|_|\__,_|\__|_| |_|
"""

EGG_COMMANDS = ('/solcat', '/彩蛋', '/egg', '/42')

# 彩蛋回复语（随机池，纯标准库 random）
_REPLIES = [
    "☠ SOLCAT EASTER EGG PROTOCOL v2.0\n你找到了隐藏入口！\n"
    "通用秘籍：↑↑↓↓←→←→BA · 连点标题 5 次 · 输入 solcat · Ctrl+Shift+T",
    "喵～ 你输入了 /42。\n答案是 42，但问题是什么？（《银河系漫游指南》）",
    "彩蛋已解锁：今天也要元气满满呀！\n—— SOLCAT",
]


def egg_banner() -> str:
    """返回 SOLCAT ASCII 署名横幅，可用于控制台或消息回复"""
    return (ASCII_ART +
            "\n  SOLCAT EASTER EGG PROTOCOL v2.0"
            "\n  提示：↑↑↓↓←→←→BA · 连点标题 5 次 · 输入 solcat · Ctrl+Shift+T")


def handle_egg_command(text: str):
    """
    检测彩蛋命令并返回回复文本；未命中返回 None。
    仅做字符串匹配，绝不修改配置、文件与运行状态。
    """
    import random
    if not isinstance(text, str):
        return None
    normalized = text.strip().replace('：', ':').lower()
    if normalized not in EGG_COMMANDS:
        return None
    if normalized == '/42':
        return _REPLIES[1]
    if normalized == '/egg':
        return egg_banner()
    return random.choice((_REPLIES[0], _REPLIES[2]))


if __name__ == '__main__':
    print(egg_banner())
    print("\n可用彩蛋命令：" + "  ".join(EGG_COMMANDS))
