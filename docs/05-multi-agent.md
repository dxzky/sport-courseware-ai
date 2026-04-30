# 05 多龙虾协同方案

## 角色分工

| 龙虾 | 职责 | 输出 |
|---|---|---|
| course-orchestrator | 总控、调度、汇总 | update_log.md |
| source-researcher | 资料读取、网页检索、来源卡片 | source_cards.jsonl |
| course-planner | 教学结构、课次蓝图 | course_update_plan.md / lesson_blueprint.json |
| lesson-writer | 教案生成 | lesson_plans/ |
| ppt-designer | PPT 蓝图和 PPTX | ppt/ |
| handout-writer | 讲义生成 | handouts/ |
| qa-auditor | 质量与引用审查 | review_reports/ |

## 权限建议

```text
qa-auditor：只读，不允许写最终稿
source-researcher：可写 source_cards，不允许写 output
lesson-writer：只写 lesson_plans
ppt-designer：只写 ppt
handout-writer：只写 handouts
course-orchestrator：负责复制通过审查的文件到 output
```

## 多龙虾启动提示词

```markdown
请使用多龙虾协同方式处理 Courseware-AI 中的三门课程。

角色分工：
1. course-orchestrator：负责总体调度和输出汇总。
2. source-researcher：只负责资料读取、网页检索、source_cards。
3. course-planner：只负责课程更新计划和 lesson_blueprint。
4. lesson-writer：只负责教案。
5. ppt-designer：只负责 PPT 蓝图和 PPTX。
6. handout-writer：只负责讲义。
7. qa-auditor：只负责审查，不允许直接改最终稿。

模型要求：
- 资料整理和 JSON 抽取使用低成本国内模型。
- 最终教案、讲义、PPT 讲稿使用高质量国内模型。
- 审查先用中等模型，重大问题再用高质量模型复核。
- 不得调用任何国外模型或中转模型。
```
