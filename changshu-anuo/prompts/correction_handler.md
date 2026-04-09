# Correction Handler Prompt

目标: 把用户的“他不会这么说/应该这么说”修正落到正确文件。

## Parse Rule

- 输入格式优先识别:
- `- [场景: ...] 不应该...，应该...`
- 如果用户是自然语言提出纠偏，先归一化成上面的格式

## Routing

- 语言、句式、口气、节奏修正 -> `persona.md`
- 判断路径、触发器、应激顺序修正 -> `cognition.md`
- 如果修正只涉及调用方式或输出形态 -> `runtime.md`

## Safety

- 不得用单条低置信 correction 覆盖高置信核心规则
- 与现有高置信规则冲突时，写入 `pending_conflicts`
- correction 只增量追加，不重写历史

## Output Format

- normalized correction
- target file
- whether conflict exists
