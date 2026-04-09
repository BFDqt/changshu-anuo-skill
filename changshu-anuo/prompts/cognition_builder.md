# Cognition Builder Prompt

目标: 根据新增样本更新 `cognition.md`，只提炼“阿诺怎么想、怎么防御、怎么转移”。

## Input

- 新增样本
- 当前 `cognition.md`
- `references/evidence-matrix.md`

## Instructions

- 只保留稳定反应模型，不要扩写成名人顾问式人格分析
- 模型优先归入这六类:
- 反问防御
- 左右脑互搏
- 面子优先
- 流量优先
- 关系与师承执念
- 情绪先行，逻辑滞后
- 如果出现新模式，先判断是否只是上述六类的变体
- 每条模型和 heuristic 都要注明证据
- 不把 `borrowed` 直接提成核心模型
- 用户 correction 如果针对判断路径，追加到 `Cognition Corrections`

## Output Format

- 修改后的 `cognition.md`
- 新增或更新的模型/heuristic 列表
- 冲突列表

