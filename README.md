# changshu-anuo-skill

> 那我问你，你要是想整一个阿诺味 skill，又不想整成只会复读几句语录的，那这个仓库你先看一下。

这是一版适合 GitHub 公开分发的 `changshu-anuo` skill。

- 安装目录在 [changshu-anuo](./changshu-anuo)
- 开源版只放规范化证据卡、样本、规则、脚本和 benchmark
- 原始素材、未清洗转写、临时调研，不进这个仓库

## 这到底是个什么

这不是语录合集。

这也不是把一堆脏转写、旧 prompt、二创梗图一股脑塞进去，然后让模型嗯学的那种东西。

这个仓库想做的是一版能公开、能维护、能继续长的阿诺 skill：

- 有 `语感核`
- 有 `脑回路核`
- 有 `扮演`
- 有 `改写`
- 有 `拆解`
- 有负例
- 有 benchmark
- 有脚本

你要是只想找一句“那我问你”，那别急，这仓库不止那个。

## 这版有些什么

- `语感核`
  重复、回滚、反问、情绪推进、主场控制这些都单独拆出来了。
- `脑回路核`
  反问防御、左右脑互搏、面子优先、流量优先、师承执念，不是乱写，是拆成模型在管。
- `三模式`
  `扮演`、`改写`、`拆解` 都能单独用。
- `维护链`
  有证据卡、有样本库、有规则层、有构建脚本，不是一次性 prompt。

## 你先别急，怎么装

先把仓库拉下来，再把 `changshu-anuo/` 丢进你的 skill 目录。

### Codex

```powershell
Copy-Item -Recurse .\changshu-anuo "$env:USERPROFILE\.codex\skills\changshu-anuo"
```

### Claude Code

```powershell
Copy-Item -Recurse .\changshu-anuo ".\.claude\skills\changshu-anuo"
```

更快的上手流程看 [GETTING_STARTED.md](./GETTING_STARTED.md)。

## 你怎么用

显式调用就行：

```text
$changshu-anuo 跟我聊这个事
$changshu-anuo 把这段话改成阿诺味
$changshu-anuo 分析这事阿诺会怎么想、怎么说
```

更多演示题看 [examples/demo-prompts.md](./examples/demo-prompts.md)。

## 这版怎么开的

我不是凭空拍脑子硬写的，主要参考了几种已经公开跑通的路子：

- [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill)
  学它的人格分层、纠偏、版本演进。
- [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill)
  学它的框架提炼、证据分级、边界控制。
- [alchaincyf/mrbeast-skill](https://github.com/alchaincyf/mrbeast-skill)
  学它单人物仓库怎么把公开层做清楚。

所以这版不是只求“像一句”，而是想把“为什么像、怎么稳、怎么继续补”也一起开出来。

## 同类项目

这俩你也可以顺手看看。别说什么友链不友链了，反正都是同类开源仓库。

- [jackmath5261-bit/changshu-shengyitao-anuo](https://github.com/jackmath5261-bit/changshu-shengyitao-anuo)
- [Ricardo-Vv/changshu-anuo](https://github.com/Ricardo-Vv/changshu-anuo)

## 这版和普通公共样品有什么不一样

相对只放 `README + SKILL.md` 的轻量样品，这版额外公开了：

- `persona + cognition + runtime` 三层拆分
- `evidence-cards` 规范化证据卡
- `evidence-matrix` 规则追溯
- `negative-examples` 压制低质量模仿
- `benchmark-prompts` 固定评测题库
- `normalize_samples.py`
- `build_skill.py`
- `audit_skill_refs.py`
- `version_manager.py`

说白了就是：

- 不只会学几句
- 不只会堆口头禅
- 不直接吃脏原料
- 后面还能继续补

## 公开版证据策略

- skill 只消费规范化后的证据卡
- 规则层只引用 `OBS-* / DER-* / BOR-*`
- 原始素材留在本地，不进开源仓库
- 新素材先清洗成证据卡，再进入样本库和规则层

## 仓库结构

```text
changshu-anuo-skill/
├── README.md
├── AGENTS.md
├── GETTING_STARTED.md
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

## 你别乱传什么

- 本项目是对公开文化符号和语言风格的抽象建模，不代表现实人物本人发言
- 仅供角色扮演、风格研究、提示工程和娱乐用途
- 请勿用于冒充、欺骗、骚扰或传播违法内容

## 给协作者

- 仓库级说明看 [AGENTS.md](./AGENTS.md)
- 首次安装和验证看 [GETTING_STARTED.md](./GETTING_STARTED.md)
