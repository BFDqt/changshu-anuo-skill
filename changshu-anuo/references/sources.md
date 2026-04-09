# Sources

## Intake Principle

- skill 不直接消费原始素材
- 原始素材必须先清洗成 `references/evidence-cards.md` 中的规范证据卡
- 证据卡再进入 `references/source_samples.md`、`references/evidence-matrix.md`、`persona.md` 和 `cognition.md`
- skill 内部只允许出现证据卡 ID，不允许直接出现原始文件名

## Source Tiers

### Tier 1. 一手观察卡

- 载体: `references/evidence-cards.md` 中的 `OBS-*`
- 用途: 核心事实、口气、节奏、反问、情绪推进、关系表达
- 规则: `persona.md` 和 `cognition.md` 的核心条目必须优先映射到这里

### Tier 2. 归纳整理卡

- 载体: `references/evidence-cards.md` 中的 `DER-*`
- 用途: 聚合高频梗、补足抽样视角、给边缘表达降噪
- 规则: 可辅助归纳，但不能推翻 `Tier 1`

### Tier 3. 借入候选卡

- 载体: `references/evidence-cards.md` 中的 `BOR-*`
- 用途: 候选词场、旧模板、反例、维护思路
- 规则: 只记为 `borrowed` 候选；未经 `Tier 1` 或 `Tier 2` 支持，不进入核心人格规则

### Tier 4. 外部方法与公开基线

- `https://github.com/titanwings/colleague-skill`
- `https://github.com/alchaincyf/nuwa-skill`
- `https://github.com/jackmath5261-bit/changshu-shengyitao-anuo`
- 用途:
- `colleague-skill`: 借鉴人格分层、增量合并、纠偏与版本化
- `nuwa-skill`: 借鉴框架提炼、证据分级、诚实边界
- `jackmath5261-bit/changshu-shengyitao-anuo`: 仅作公开基线与待超越对象
- 规则: 不作为阿诺事实源

## Evidence Classes

- `observed`: 直接来自一手语料
- `derived`: 由多条一手样本归纳
- `borrowed`: 来自旧 prompt、他人技能或公共样品，仅作候选

## Promotion Rules

- `borrowed` 不得直接进入核心人格规则
- 只有被 `observed` 或 `derived` 覆盖后，才允许升级到核心层
- 同层级冲突必须记录到 `pending_conflicts`
- 无法确认的断言只留在候选或备注，不写进最终技能行为指令

## Intake Rules

- 新增原始素材先脱敏、切段、去噪，再整理成新的证据卡
- 证据卡合格后，再增量写入 `references/source_samples.md`
- 然后运行 `scripts/normalize_samples.py`
- 再通过 `scripts/build_skill.py` 重建 `SKILL.md`
- 若出现同层级冲突，先写入 `pending_conflicts`，等人工裁决后再升版
