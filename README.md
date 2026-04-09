# changshu-anuo-skill

`changshu-anuo-skill` 是一个面向 Codex / Claude Code 的角色风格 skill，用来复刻常熟阿诺的语感和脑回路。

这版公开仓库只保留可直接安装和分发的成品：

- [changshu-anuo/SKILL.md](./changshu-anuo/SKILL.md)
- [changshu-anuo/agents/openai.yaml](./changshu-anuo/agents/openai.yaml)

内部研究材料、原始素材、清洗与构建流程不在公开仓库中。

## 能力

- 扮演：以阿诺风格直接回应当前话题
- 改写：把原句改成阿诺味表达
- 拆解：分析“他会怎么想、怎么说”

## 安装

把 [changshu-anuo](./changshu-anuo) 整个目录复制到你的 skills 目录中。

- Codex：复制到 `~/.codex/skills/changshu-anuo`
- Claude Code：复制到你的 skills 目录下

安装后请重启客户端，再开始新会话，让技能列表重新加载。

## 使用

显式调用：

```text
$changshu-anuo 跟我聊这个事
$changshu-anuo 把这段话改成阿诺味
$changshu-anuo 分析这事阿诺会怎么想、怎么说
```

这个 skill 默认不会隐式触发，不写 `$changshu-anuo` 时不会自动进入角色。

## 项目特点

- 重点不只是口头禅模仿，也包括冲突节奏、反问习惯和判断路径
- 公开仓库保持轻量，便于安装、阅读和二次分发
- 技能本体不直接暴露原始素材文件名或未整理文本

## 同类项目
同类链接，也不能说是友链，权当是友链吧
- [jackmath5261-bit/changshu-shengyitao-anuo](https://github.com/jackmath5261-bit/changshu-shengyitao-anuo)
- [Ricardo-Vv/changshu-anuo](https://github.com/Ricardo-Vv/changshu-anuo)

## 仓库结构

```text
changshu-anuo-skill/
├── README.md
├── LICENSE
└── changshu-anuo/
    ├── SKILL.md
    └── agents/
        └── openai.yaml
```

## 说明

- 本项目是对公开文化符号和语言风格的抽象建模，不代表现实人物本人发言
- 仅供角色扮演、风格研究、提示工程和娱乐用途
- 请勿用于冒充、欺骗、骚扰或传播违法内容
