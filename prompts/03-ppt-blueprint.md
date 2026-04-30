请基于《{课程名}》第 {课次} 讲教案，生成第 {课次} 讲 PPT 的 `slide_blueprint.json`。

要求：
1. 先不要生成 PPTX。
2. 每页只讲一个核心点。
3. 普通内容页不超过 5 个 bullet。
4. 每页都要有 `speaker_notes`。
5. 每页技术事实必须标注 `source_id`。
6. 说明旧 PPT 中哪些页保留、重写、删除或合并。
7. 输出 `slide_blueprint.json` 和 `slide_change_log.md`。

每页格式：

```json
{
  "slide_no": 1,
  "section": "",
  "layout_type": "title|section|content|comparison|process|diagram|case|exercise|summary|references",
  "title": "",
  "core_message": "",
  "visible_content": {
    "bullets": [],
    "table": null,
    "diagram": null,
    "chart": null
  },
  "visual_design": {
    "recommended_layout": "",
    "editable_elements": [],
    "avoid": []
  },
  "speaker_notes": "",
  "source_ids": [],
  "update_instruction": "keep|rewrite|new|delete|merge",
  "revision_notes": ""
}
```
