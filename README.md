# changshu-anuo-skill

> 常熟阿诺的语感核 + 脑回路核。不是语录合集，是一套可维护、可校正、可公开分发的人格 skill。

这个仓库提供一版适合 GitHub 公开的 `changshu-anuo` skill。

推荐仓库名: `changshu-anuo-skill`

- 安装用的 skill 目录在 [changshu-anuo](./changshu-anuo)
- 公开版只保留规范化后的证据卡、样本、规则、脚本和基准题
- 原始素材、未清洗转写、临时研究文件不进入开源仓库

## 这版是怎么开的

我参考了三种已经公开跑通的模式：

- [jackmath5261-bit/changshu-shengyitao-anuo](https://github.com/jackmath5261-bit/changshu-shengyitao-anuo)
  一个角色一个仓库，结构很轻：`README + SKILL + LICENSE`，重点放在安装、触发词和免责声明。
- [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill)
  README 更完整，强调安装、用法、演进、项目结构和社区传播。
- [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) / [alchaincyf/mrbeast-skill](https://github.com/alchaincyf/mrbeast-skill)
  单人物 skill 公开时会把“方法论、研究摘要、可运行脚本、示例对话”一起开放，但不会把脏原料直接塞进 skill。

这版采用的是三者结合的做法：

- 保留单 skill 仓库的轻量入口
- 增加方法、证据、脚本和 benchmark，优于纯 README + SKILL 的公共样品
- 用“证据卡”替代原始文件名，避免把未清洗素材直接暴露给开源版

## 特点

- 双核建模：
  - `语感核`：重复、回滚、反问、情绪推进、主场控制
  - `脑回路核`：反问防御、左右脑互搏、面子优先、流量优先、师承执念
- 三种模式：
  - `扮演`
  - `改写`
  - `拆解`
- 可维护：
  - 规范化证据卡
  - 负例约束
  - benchmark 题库
  - correction 语法
  - 构建与版本脚本

## 不包含什么

- 不包含原始直播转写、未清洗文本、临时调研草稿
- 不把原始素材文件名直接写进 `SKILL.md`
- 不把现实人物包装成“本人在线”

## 快速开始

1. 克隆 `changshu-anuo-skill`
2. 把 `changshu-anuo/` 复制到你的 skill 目录
3. 用 `$changshu-anuo` 显式调用

更快的上手说明见 [GETTING_STARTED.md](./GETTING_STARTED.md)。

## 安装

先把仓库拉到本地，再把 `changshu-anuo/` 目录复制到你的 skill 目录。

### Codex

```powershell
Copy-Item -Recurse .\changshu-anuo "$env:USERPROFILE\.codex\skills\changshu-anuo"
```

### Claude Code

```powershell
Copy-Item -Recurse .\changshu-anuo ".\.claude\skills\changshu-anuo"
```

## 使用

显式调用：

```text
$changshu-anuo 跟我聊这个事
$changshu-anuo 把这段话改成阿诺味
$changshu-anuo 分析这事阿诺会怎么想、怎么说
```

更多示例见 [examples/demo-prompts.md](./examples/demo-prompts.md)。

## 仓库结构

```text
changshu-anuo-skill/
├── README.md
├── LICENSE
├── .gitignore
├── examples/
│   └── demo-prompts.md
└── changshu-anuo/
    ├── SKILL.md
    ├── persona.md
    ├── cognition.md
    ├── runtime.md
    ├── agents/
    ├── references/
    ├── prompts/
    └── scripts/
```

## 公开版证据策略

- skill 只消费规范化后的证据卡
- 规则层只引用 `OBS-* / DER-* / BOR-*`
- 原始素材留在本地，不进开源仓库
- 若新增原始素材，先清洗成证据卡，再进入样本库和规则层

## 与公共样品的差异

相对 [jackmath5261-bit/changshu-shengyitao-anuo](https://github.com/jackmath5261-bit/changshu-shengyitao-anuo)，这版额外公开了：

- `persona + cognition + runtime` 三层拆分
- `negative-examples` 压制低质量模仿
- `evidence-cards` 和 `evidence-matrix` 追溯机制
- `benchmark-prompts` 固定评测题库
- `normalize_samples.py` / `build_skill.py` / `audit_skill_refs.py` / `version_manager.py`

## 免责声明

- 本项目是对公开文化符号和语言风格的抽象建模，不代表现实人物本人发言
- 仅供角色扮演、风格研究、提示工程和娱乐用途
- 请勿用于冒充、欺骗、骚扰或传播违法内容

## 给协作者

- 仓库级说明见 [AGENTS.md](./AGENTS.md)
- 首次安装和验证见 [GETTING_STARTED.md](./GETTING_STARTED.md)
