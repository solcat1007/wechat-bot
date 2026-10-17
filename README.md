---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: 50b092e4f392f7690eb78912e14c5fd6_a0a9c8c9799a11f1a7da5254006c9bbf
    ReservedCode1: 83NHBJaPPDyFlcIFDRcSPBUISBQR19MC6fL0gpiHGdFWKC76Uf80DH5xOfjeT/X/cjf9bSegTeEqo1GzJmWzX2YxPpf9ev23FktEYdbS8fq/PUUfYZSGO2bpU3LqoNRdnI82zcam7gUkVCiVIDpe7gTcDzx42rPPLxburo0eACzZyOgibsqN4khgSso=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: 50b092e4f392f7690eb78912e14c5fd6_a0a9c8c9799a11f1a7da5254006c9bbf
    ReservedCode2: 83NHBJaPPDyFlcIFDRcSPBUISBQR19MC6fL0gpiHGdFWKC76Uf80DH5xOfjeT/X/cjf9bSegTeEqo1GzJmWzX2YxPpf9ev23FktEYdbS8fq/PUUfYZSGO2bpU3LqoNRdnI82zcam7gUkVCiVIDpe7gTcDzx42rPPLxburo0eACzZyOgibsqN4khgSso=
---

# WeChatBot v3.28

> 基于 Python 的微信 AI 机器人 —— 让你的微信拥有一个智能聊天助手。

## ✨ 功能特性

| 功能 | 说明 |
|------|------|
| **多角色对话** | 支持多个 AI 角色，每个角色有独立的人设 Prompt |
| **文字聊天** | 通过 DeepSeek / GPT-4o / Kimi 等大模型驱动的智能对话 |
| **图片识别** | 接收图片后自动调用视觉模型理解内容并回复 |
| **表情包支持** | 自动识别表情包含义并回复对应表情 |
| **定时提醒** | 支持周期性提醒和一次性提醒，到点自动发送消息 |
| **群聊互动** | 群聊中 @机器人 触发回复，支持关键词自动回复 |
| **角色论坛** | 多个 AI 角色在群内自动互动聊天 |
| **记忆系统** | 记住与每个用户的对话历史，支持记忆摘要持久化 |
| **联网搜索** | 接入在线搜索能力，回复实时话题 |
| **主动消息** | 可配置的自动发送消息（早安、晚安等） |
| **Web 管理后台** | Flask 驱动的可视化配置界面，无需手改代码 |
| **指令系统** | 支持文本指令（重置记忆、切换角色、开关功能等） |

## 🚀 快速开始

### 环境要求

- **操作系统**：Windows 10/11
- **Python**：3.9 ~ 3.12
- **微信**：WeChatWin 4.1.2（32位）

> ⚠️ 仅支持 Windows 平台，依赖 wxauto 库与微信客户端交互。

### 安装步骤

1. **克隆项目**

```bash
git clone git@github.com:solcat1007/wechat-bot.git
cd wechat-bot
```

2. **配置 API Key**

复制配置模板并填入你的 API Key：

```bash
copy config.example.py config.py
```

编辑 `config.py`，至少填入 `DEEPSEEK_API_KEY`：

```python
DEEPSEEK_API_KEY = 'sk-your-key-here'
```

> 支持 DeepSeek 官方 API、硅基流动、WeAPIs 代理等多种后端。详见 `config.example.py` 中的注释。

3. **运行启动脚本**

双击 `Run.bat`，脚本会自动：
- 检查微信版本并提示启动
- 检查 Python 版本
- 安装依赖（阿里云 + 清华源）
- 安装 wxauto 定制版
- 启动 Web 管理后台

4. **访问管理后台**

浏览器打开 `http://127.0.0.1:5000`：
- 选择/编辑角色 Prompt
- 配置监控的好友列表
- 调整对话参数
- 启动/停止机器人

## 📁 项目结构

```
WeChatBot/
├── bot.py                  # 机器人主程序（消息监听、AI 调用、提醒等）
├── config.py               # 配置文件（API Key、参数等，需自行创建）
├── config.example.py       # 配置文件模板
├── config_editor.py        # Web 管理后台（Flask）
├── updater.py              # 自动更新模块
├── Run.bat                 # 一键启动脚本
├── requirements.txt        # Python 依赖
├── DEPENDENCIES.txt        # 依赖许可证详情
├── LICENSE                 # GPL-3.0 许可证
├── LICENSE_COMPLIANCE.md   # 许可证合规说明
├── CHANGELOG.md            # 更新日志
├── version.json            # 版本信息
├── prompts/                # AI 角色 Prompt 文件（.md）
├── emojis/                 # 表情包资源
├── CoreMemory/             # 记忆持久化数据
├── Memory_Temp/            # 临时记忆数据
└── forum_data/             # 角色论坛数据
```

## ⚙️ 主要配置项

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| `DEEPSEEK_API_KEY` | 主模型 API Key | - |
| `MODEL` | 主对话模型 | deepseek-v3-0324 |
| `DEEPSEEK_BASE_URL` | API 端点 | - |
| `LISTEN_LIST` | 监控的好友列表 `[微信名, Prompt名]` | - |
| `MAX_GROUPS` | 最大群聊数 | 5 |
| `TEMPERATURE` | 生成温度（0~2） | 0.7 |
| `MAX_TOKEN` | 回复最大 Token 数 | 500 |
| `ENABLE_IMAGE_RECOGNITION` | 开启图片识别 | true |
| `ENABLE_MEMORY` | 开启长期记忆 | true |
| `ENABLE_REMINDERS` | 开启定时提醒 | true |
| `ENABLE_ONLINE_API` | 开启联网搜索 | true |
| `ENABLE_TEXT_COMMANDS` | 开启文本指令 | true |

## 🔧 支持的 API 后端

| 后端 | 配置说明 |
|------|---------|
| **DeepSeek 官方** | `DEEPSEEK_BASE_URL = 'https://api.deepseek.com'` |
| **硅基流动** | `DEEPSEEK_BASE_URL = 'https://api.siliconflow.cn/v1/'` |
| **WeAPIs 代理** | `DEEPSEEK_BASE_URL = 'https://api.jiyuanzhiguang.top/v1'` |
| **自定义** | 填入任意兼容 OpenAI 接口格式的端点 |

## 📋 文本指令

用户可在聊天窗口发送以下指令（以 `/` 开头）：

| 指令 | 说明 |
|------|------|
| `/重置` | 清空当前用户的对话上下文 |
| `/状态` | 查看机器人运行状态 |
| `/提示 内容` | 向角色添加临时提示 |
| `/切换 角色名` | 切换到指定角色 Prompt |
| `/记忆` | 查看 AI 对你的记忆 |
| `/帮助` | 查看所有可用指令 |

## 🛡️ 安全说明

- **API Key 保护**：`config.py` 包含敏感凭据，请勿提交到公共仓库（已在 `.gitignore` 中排除）。
- **数据隐私**：聊天上下文存储在本地 `chat_contexts.json`，不会上传。
- **Web 后台**：默认监听 `127.0.0.1`，仅本机可访问。可启用登录密码保护（`ENABLE_LOGIN_PASSWORD`）。
- **线程安全**：消息和定时任务通过线程锁（`threading.Lock`）保护并发访问。

## 📄 许可证

本项目基于 [GPL-3.0](LICENSE) 许可证发布。

> 本项目基于 [KouriChat](https://github.com/KouriChat/KouriChat) 修改，感谢原作者。

## 🤝 参与贡献

如需提交 Issue 或 PR，请前往 [GitHub 仓库](https://github.com/solcat1007/wechat-bot)。

---

**版本**：3.28 | **最后更新**：2025-12-06
*（内容由AI生成，仅供参考）*
