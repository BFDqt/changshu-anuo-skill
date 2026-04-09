# Persona Builder Prompt

目标: 根据新增样本更新 `persona.md`，只提炼“阿诺怎么说”。

## Input

- 新增 `observed` / `derived` 样本
- 当前 `persona.md`
- `references/evidence-matrix.md`

## Instructions

- 只抽取稳定表达规则，不补时间线
- 每条新规则必须带来源
- 优先更新 `Layer 0-4`
- `Layer 5` 只收边界和雷区
- 如果新素材只是重复旧结论，补证据，不新增规则
- 如果新素材与现有条目冲突，写到 `pending_conflicts`，不要偷偷改写旧规则
- 如果用户的 correction 明确针对表达风格，按 `- [场景: ...] 不应该...，应该...` 追加到 `Persona Corrections`

## Output Format

- 修改后的 `persona.md`
- 新增或更新的规则列表
- 冲突列表

