# Getting Started

## 1. 复制 skill

### Codex

```powershell
Copy-Item -Recurse .\changshu-anuo "$env:USERPROFILE\.codex\skills\changshu-anuo"
```

### Claude Code

```powershell
Copy-Item -Recurse .\changshu-anuo ".\.claude\skills\changshu-anuo"
```

## 2. 试用

```text
$changshu-anuo 跟我聊这个事
$changshu-anuo 把这段话改成阿诺味
$changshu-anuo 分析这事阿诺会怎么想、怎么说
```

## 3. 做一次本地校验

```powershell
python .\changshu-anuo\scripts\normalize_samples.py --strict
python .\changshu-anuo\scripts\build_skill.py
python .\changshu-anuo\scripts\audit_skill_refs.py
```

Windows 下跑 quick validate 时建议开 UTF-8：

```powershell
$env:PYTHONUTF8='1'
python 'C:\Users\Lenovo\.codex\skills\.system\skill-creator\scripts\quick_validate.py' '.\changshu-anuo'
```

## 4. 维护入口

- 证据卡: `./changshu-anuo/references/evidence-cards.md`
- 样本库: `./changshu-anuo/references/source_samples.md`
- 规则层: `./changshu-anuo/persona.md` / `./changshu-anuo/cognition.md` / `./changshu-anuo/runtime.md`
- 演示题: `./examples/demo-prompts.md`
