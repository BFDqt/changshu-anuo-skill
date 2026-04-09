# changshu-anuo-skill

> 那我问你，你要是想整一个阿诺味 skill，又不想整成只会复读几句语录的，那这个仓库你先看一下。

这是一版适合 GitHub 公开分发的 `changshu-anuo` skill。

- 安装目录在 [changshu-anuo](./changshu-anuo)
- 公开版现在只放 skill 成品，不放内部制作工程
- 原始素材、未清洗转写、临时调研，不进这个仓库

## 这到底是个什么

这不是语录合集。

这也不是把一堆脏转写、旧 prompt、二创梗图一股脑塞进去，然后让模型嗯学的那种东西。

这个仓库想做的是一版能公开、能直接装、看起来还不乱的阿诺 skill：

- 有 `语感核`
- 有 `脑回路核`
- 有 `扮演`
- 有 `改写`
- 有 `拆解`
- 该有的味道有
- 该收住的地方也收住

你要是只想找一句“那我问你”，那别急，这仓库不止那个。

## 这版有些什么

- `语感核`
  重复、回滚、反问、情绪推进、主场控制这些味道都还在。
- `脑回路核`
  反问防御、左右脑互搏、面子优先、流量优先、师承执念这些东西都被压进成品 skill 里了。
- `三模式`
  `扮演`、`改写`、`拆解` 都能单独用。
- `轻仓库`
  GitHub 上只放精简发行物，不把内部做料工程全摊开。

## 你先别急，怎么装

先把仓库拉下来，再把 `changshu-anuo/` 丢进你自己的 skill 目录。

- Codex: 放到你的 Codex skills 目录里
- Claude Code: 放到你的 Claude skills 目录里

最终要保证能以 `$changshu-anuo` 显式调用到它就行。

## 你怎么用

显式调用就行：

```text
$changshu-anuo 跟我聊这个事
$changshu-anuo 把这段话改成阿诺味
$changshu-anuo 分析这事阿诺会怎么想、怎么说
```

这几个就够你先试味道了。

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

说白了就是两点：

- 不是只会堆几句口头禅
- 也不是把仓库做成一坨内部工程文档

公开版现在只放成品 skill，但成品里保留了：

- `语感`
- `脑回路`
- `扮演 / 改写 / 拆解`
- `边界控制`

## 公开版策略

- GitHub 只放 skill 成品
- 原始素材和内部制作工程留在本地
- 所以仓库会更轻，也更接近大家平时看的那种开源 skill 样子

## 仓库结构

```text
changshu-anuo-skill/
├── README.md
├── LICENSE
├── .gitignore
└── changshu-anuo/
    ├── SKILL.md
    └── agents/
        └── openai.yaml
```

## 你别乱传什么

- 本项目是对公开文化符号和语言风格的抽象建模，不代表现实人物本人发言
- 仅供角色扮演、风格研究、提示工程和娱乐用途
- 请勿用于冒充、欺骗、骚扰或传播违法内容

## 给维护者

- 公开仓库只留发行物
- 内部研究、清洗、构建、评测链不随公开仓库发出
