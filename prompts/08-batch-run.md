请按照 `Courseware-AI/AGENTS.md` 的规则，批量更新以下三门课程：

1. 《电路与电子技术基础》
2. 《人体生理信号采集与分析》
3. 《智能体育装备概论》

工作区：

```text
D:\Courseware-AI
```

请对每门课执行：
1. 扫描 input 文件夹。
2. 更新 `source_cards.jsonl`。
3. 更新 `source_index.json`。
4. 生成 `course_update_plan.md`。
5. 按课次生成教案。
6. 按课次生成 PPT 蓝图。
7. 生成 PPTX。
8. 生成学生讲义。
9. 运行 citation-auditor。
10. 修复所有 critical 和 major 问题。
11. 输出最终成果到 output 文件夹。

硬性要求：
- 只使用国内大模型。
- 默认使用低成本模型做资料整理和 JSON 抽取。
- 只在最终写作和重大修复时使用高质量模型。
- 不覆盖 input 文件。
- 不编造来源。
- 所有事实性内容必须有 source_id。
- 每门课都输出 `update_log.md`、`citation_report.md`、`token_usage_report.md`。
