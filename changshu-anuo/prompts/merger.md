# Incremental Merger Prompt

目标: 把新样本增量并入 skill，不重写整套人格。

## Workflow

1. 读取 `references/source_samples.md` 与最新归一化索引
2. 比对 `persona.md`、`cognition.md`、`references/evidence-matrix.md`
3. 把重复样本作为补证据处理
4. 只对真正新增的信息生成 patch
5. 遇到同层级冲突时写入 `pending_conflicts`
6. 生成可审阅的变更摘要

## Merge Rules

- 优先保留高置信旧规则
- 新 `observed` 可增强或纠正旧 `derived`
- `borrowed` 只能进候选池
- 不要清空 correction 历史
- 不要删除旧版本快照

## Output Format

- patch summary
- updated files
- pending conflicts

