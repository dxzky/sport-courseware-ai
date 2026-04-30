# 03 课程资源更新工作流

## 总流程

```text
扫描 input
  ↓
生成 source_cards.jsonl
  ↓
生成 source_index.json
  ↓
生成 course_update_plan.md
  ↓
生成 lesson_blueprint.json
  ↓
生成教案
  ↓
生成 slide_blueprint.json
  ↓
生成 PPTX
  ↓
生成学生讲义
  ↓
运行 citation-auditor
  ↓
修复问题
  ↓
输出到 output
```

## 每门课产物

```text
source_cards/source_cards.jsonl
source_index.json
source_gap_report.md
course_update_plan.md
lesson_blueprint.json
lesson_plans/*.md 或 *.docx
ppt/slide_blueprint.json
ppt/*.pptx
handouts/*.md 或 *.docx
review_reports/citation_report.md
output/
```

## 返工规则

出现以下情况必须返工：

1. 来源不明。
2. source_id 不存在。
3. 教案、PPT、讲义术语不一致。
4. PPT 页面不可编辑。
5. 讲义只是 PPT 文本复制。
6. 教学目标无法评价。
7. 形成性评价与教学目标不对应。
