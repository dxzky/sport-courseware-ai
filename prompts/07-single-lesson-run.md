请进入 `D:\Courseware-AI`，按照 `AGENTS.md` 和 `skills/` 中的规则，更新《{课程名}》第 {课次} 讲。

本次只处理一讲，不处理全课程。

要求：
1. 扫描该课程 `input/` 文件夹。
2. 生成或更新 `source_cards/source_cards.jsonl`。
3. 生成 `source_index.json` 和 `source_gap_report.md`。
4. 生成第 {课次} 讲教案。
5. 生成第 {课次} 讲 `slide_blueprint.json`。
6. 生成第 {课次} 讲 PPTX。
7. 生成第 {课次} 讲学生讲义。
8. 运行 citation-auditor。
9. 修复所有 critical 和 major 问题。
10. 最终成果输出到该课程 `output/` 文件夹。

硬性要求：
- 只使用国内大模型。
- 不覆盖 input 文件。
- 不编造来源。
- 所有事实性内容必须有 source_id。
