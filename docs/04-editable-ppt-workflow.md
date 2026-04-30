# 04 高质量可编辑 PPT 工作流

## 核心观点

不要直接要求 GPT “生成 PPT”。应先生成 `slide_blueprint.json`，再根据蓝图生成 PPTX。

```text
资料 → PPT 大纲 → slide_blueprint.json → 可编辑 PPTX → 审查 → 局部更新
```

## 可编辑 PPT 标准

1. 所有标题、正文、页脚、备注都是可编辑文本。
2. 表格使用 PPT 原生表格。
3. 流程图、架构图、关系图使用原生形状、线条和箭头。
4. 不把整页做成图片。
5. 每页只表达一个核心观点。
6. 每页有讲稿备注。
7. 每页有 `source_id`。
8. 最后一页有参考资料。

## slide_blueprint.json 字段

```json
{
  "slide_no": 1,
  "section": "章节名称",
  "layout_type": "title|section|content|comparison|process|diagram|case|exercise|summary|references",
  "title": "页面标题",
  "core_message": "本页只表达一个核心观点",
  "visible_content": {
    "bullets": [],
    "table": null,
    "diagram": null,
    "chart": null
  },
  "visual_design": {
    "recommended_layout": "左右结构/上下结构/中心流程图/三栏对比",
    "editable_elements": ["文本框", "形状", "箭头", "表格"],
    "avoid": ["整页截图", "不可编辑图片", "大段文字"]
  },
  "speaker_notes": "教师讲解备注",
  "source_ids": [],
  "update_instruction": "keep|rewrite|new|delete|merge",
  "revision_notes": "与旧PPT相比的修改说明"
}
```

## 局部更新指令

```markdown
请只修改 slide_no 为 8、9、10 的页面，其他页面不要改。

要求：
1. 保持整体风格不变。
2. 保留已有 source_id。
3. 新增事实必须补充 source_id。
4. 重新输出 slide_blueprint.json 中这三页的内容。
5. 重新生成 PPTX。
```
