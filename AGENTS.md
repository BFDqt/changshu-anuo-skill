# AGENTS.md

这个仓库是一个公开分发版 skill 仓库，核心交付物在 `./changshu-anuo/`。

## 目标

- 对外公开一版可安装、可维护的 `changshu-anuo` skill
- 公开规范化证据卡、样本、规则、脚本和 benchmark
- 不公开原始素材、未清洗研究文本和临时工作文件

## 入口

- 仓库入口说明: `./README.md`
- 快速上手: `./GETTING_STARTED.md`
- skill 本体: `./changshu-anuo/SKILL.md`
- 规范化证据卡: `./changshu-anuo/references/evidence-cards.md`

## 修改规则

- 修改 skill 行为时，优先改 `persona.md`、`cognition.md`、`runtime.md`
- 修改证据时，先更新 `references/evidence-cards.md`，再更新 `source_samples.md`
- 不要把原始素材文件名写回 skill-facing 文件
- 运行 `python .\\changshu-anuo\\scripts\\audit_skill_refs.py` 检查原始引用泄漏
- 运行 `python .\\changshu-anuo\\scripts\\build_skill.py` 重建 `SKILL.md`

## 禁止提交

- `原始素材/`
- `changshu-anuo/versions/`
- 未清洗转写、临时调研、私有截图、临时导出文件

## 发布前检查

1. `python .\\changshu-anuo\\scripts\\normalize_samples.py --strict`
2. `python .\\changshu-anuo\\scripts\\build_skill.py`
3. `python .\\changshu-anuo\\scripts\\audit_skill_refs.py`
4. `PYTHONUTF8=1 python <quick_validate.py> .\\changshu-anuo`

