# Runtime Builder Prompt

目标: 维护 `runtime.md`，保证 skill 的入口、模式和 recovery 稳定。

## Instructions

- 只维护调用方式、模式路由、输出契约、evidence discipline 和 recovery
- 不要把具体名句写成 runtime 规则
- 扮演、改写、拆解三模式必须始终保留
- recovery 要优先防止:
- 机械反问
- 粗口堆叠
- borrowed 模板直抄
- 普通助手腔
- 新增规则若会影响输出范围，必须写明原因

## Output Format

- 修改后的 `runtime.md`
- 受影响的模式
- 对 benchmark 的预期影响

