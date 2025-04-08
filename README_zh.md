# 🧩 Wordle Helper CLI 工具

一个简单实用的命令行工具，帮助你快速在 Wordle 游戏中找出可能的单词组合！支持按位置匹配、必须包含/排除字母、自动多轮交互等功能。

---

## 🚀 功能介绍

- 支持使用 `_` 表示未知字母的匹配模式（如 `_a_im_`）
- 支持指定必须包含的字母（黄字母）
- 支持指定不能出现的字母（灰字母）
- 自动下载英文词库（首次使用）
- 支持多轮问答式交互

---

## 📦 安装方法

### 1. 创建虚拟环境（推荐）

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

---

## 🕹️ 使用方法

直接运行脚本进入问答模式：

```bash
python wordle_helper.py
```

然后你会看到：

```txt
请输入模式字符串（使用 _ 表示未知字母，例如 _a_im_）：
请输入必须包含的字母（用逗号分隔，例如 e,o）：
请输入必须排除的字母（用逗号分隔，例如 t,s,r）：
```

程序会给出匹配的单词列表，并询问你是否进行下一轮。

---

## 📂 项目结构

```txt
wordle-helper/
├── wordle_helper.py      # 主程序
├── requirements.txt      # 依赖列表
├── .gitignore            # Git 忽略配置
└── README.md             # 项目说明文档
```

---

## 📌 依赖说明

- Python 3.7+
- nltk（用于英文词库）

首次运行会自动下载英文词库，无需手动操作。

---

## 🧠 TODO（可选扩展）

- 支持绿色字母（严格位置匹配）
- 按单词频率排序（优先输出常见单词）
- 导出结果为 txt 文件
- GUI 版本 or 网页版

欢迎 PR！🚀

---

## 📜 License

MIT License
