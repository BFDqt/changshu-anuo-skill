# changshu-anuo-skill

常熟阿诺风格的中文角色 skill，适用于 Codex、Claude Code 等支持自定义 skill 的客户端。

它不追求只模仿几句口头禅，而是复刻一套更稳定的表达方式：反问起手、节奏回滚、情绪顶上、逻辑后补，以及“他会怎么想、怎么说”的判断路径。

## Features

- `扮演`：直接用阿诺式语感回应当前话题
- `改写`：把原句改成阿诺味表达
- `拆解`：分析这个人设在当前场景下会怎么想、怎么说
- 显式触发：只在使用 `$changshu-anuo` 时进入角色

## Install

把这个仓库作为 `changshu-anuo` skill 目录放到本地 skills 路径即可。

### Codex

```powershell
git clone <repo-url> "$env:USERPROFILE\.codex\skills\changshu-anuo"
```

### Claude Code

```powershell
git clone <repo-url> ".\.claude\skills\changshu-anuo"
```

## Usage

```text
$changshu-anuo 跟我聊这个事
$changshu-anuo 把这段话改成阿诺味
$changshu-anuo 分析这事阿诺会怎么想、怎么说
```

## Files

```text
changshu-anuo-skill/
├── README.md
├── LICENSE
├── SKILL.md
└── agents/
    └── openai.yaml
```

- `SKILL.md`：skill 主定义
- `agents/openai.yaml`：客户端展示信息和默认提示

## Notes

- 公开仓库只保留可直接安装和分发的 skill 成品
- `.internal/` 和 `原始素材/` 用于本地研究，不属于开源发布内容

## Disclaimer

- 本项目是对公开文化符号和语言风格的抽象建模，不代表现实人物本人发言
- 仅供角色扮演、风格研究、提示工程和娱乐用途
- 请勿用于冒充、欺骗、骚扰或传播违法内容
