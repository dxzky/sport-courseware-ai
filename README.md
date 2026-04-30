# QClaw Courseware AI

面向高校课程资源更新的 QClaw / OpenClaw 工作区模板。项目用于自动化更新教案、PPT 和学生讲义，适配以下课程：

- 《电路与电子技术基础》
- 《人体生理信号采集与分析》
- 《智能体育装备概论》

项目目标不是“一次性让模型生成一套课件”，而是建立可持续更新的课程资源流水线：

```text
旧资料 / 教学大纲 / 教材 / 参考资料
        ↓
来源卡片 source_cards.jsonl
        ↓
课程更新计划 course_update_plan.md
        ↓
教案 lesson_plan.docx / md
        ↓
PPT 蓝图 slide_blueprint.json
        ↓
可编辑 PPTX
        ↓
学生讲义 handout.docx / md
        ↓
引用审查 citation_report.md
        ↓
最终输出 output/
```

## 核心原则

1. 只使用国内大模型。
2. 默认使用低成本模型做分类、摘要、JSON 抽取。
3. 仅在最终写作、重大修复和长上下文任务中使用高质量模型。
4. 任何事实性内容必须有 `source_id`。
5. 不编造教材、论文、标准、URL、作者、出版社、页码。
6. 不覆盖 `input/` 中的旧资料。
7. PPT 必须可编辑：标题、正文、表格、流程图、架构图尽量使用 PPT 原生对象，不做整页图片。
8. 未通过 `citation-auditor`，不得发布最终版本。

## 仓库结构

```text
qclaw-courseware-ai/
  AGENTS.md                         # QClaw 总控规则
  openclaw.json.example             # 国内模型配置示例
  prompts/                          # 可直接复制给 QClaw 的提示词
  skills/                           # QClaw / OpenClaw workspace skills
  schemas/                          # source_cards / slide_blueprint 等 JSON Schema
  scripts/                          # 可选辅助脚本
  docs/                             # 新手说明、模型策略、多龙虾流程、PPT 可编辑规范
  workflows/                        # 单讲、单课程、三门课批量运行指令
  checklists/                       # 交付前检查表
  examples/                         # 示例 JSON
  templates/                        # 放学校教案/PPT/讲义模板
  courses/                          # 三门课程工作目录
```

## 新手快速开始

### 1. 复制项目

把本项目复制到你的课程工作区，例如：

```text
D:\Courseware-AI
```

或先在任意目录解压，再执行：

```bash
git init
git add .
git commit -m "init qclaw courseware ai project"
```

### 2. 放入课程资料

把旧资料放到对应课程的 `input/` 目录：

```text
courses/电路与电子技术基础/input/
courses/人体生理信号采集与分析/input/
courses/智能体育装备概论/input/
```

建议放入：

```text
旧教案.docx
旧PPT.pptx
课程教学大纲.docx
授课计划.docx
教材目录.docx 或 .pdf
实验指导书.docx 或 .pdf
考核方案.docx
```

把学校模板放入：

```text
templates/教案模板.docx
templates/PPT模板.pptx
templates/讲义模板.docx
```

### 3. 在 QClaw 中运行第一条指令

先不要一次处理三门课。建议从一门课的一讲开始：

```markdown
请进入 D:\Courseware-AI，按照 AGENTS.md 和 skills/ 中的规则，更新《电路与电子技术基础》第 1 讲。

要求：
1. 先整理来源卡片。
2. 再生成更新计划。
3. 再生成教案、PPT 蓝图、PPT、讲义。
4. 最后运行引用审查。
5. 不覆盖 input 文件。
6. 只使用国内大模型。
7. 不编造来源。
8. 所有事实性内容必须有 source_id。
9. 最终成果输出到 output 文件夹。
```

### 4. 检查成果

每门课最终应至少输出：

```text
新版教案.docx 或 .md
新版PPT.pptx
学生讲义.docx 或 .md
source_cards.jsonl
参考资料.md
更新说明.md
审查报告.md
token_usage_report.md
```

## 可选脚本

安装依赖：

```bash
pip install -r requirements.txt
```

创建课程目录：

```bash
python scripts/bootstrap_project.py --root .
```

校验来源卡片：

```bash
python scripts/validate_source_cards.py courses/电路与电子技术基础/source_cards/source_cards.jsonl
```

校验 PPT 蓝图：

```bash
python scripts/validate_slide_blueprint.py courses/电路与电子技术基础/ppt/slide_blueprint.json
```

从 PPT 蓝图生成基础可编辑 PPTX：

```bash
python scripts/generate_pptx_from_blueprint.py \
  --blueprint examples/sample_slide_blueprint.json \
  --output output/sample_presentation.pptx
```

说明：`generate_pptx_from_blueprint.py` 是基础脚本，重点演示“可编辑文本、表格、流程形状”的生成方式。正式课程 PPT 仍建议由 QClaw 使用模板和 `pptx-course-builder` skill 生成。

## 适合的 GitHub 使用方式

建议把仓库当成“课程资源生产线”，而不是只存最终 PPT。推荐提交：

```text
AGENTS.md
skills/
prompts/
schemas/
source_cards/
slide_blueprint.json
update_log.md
citation_report.md
```

不建议提交：

```text
学生隐私数据
未授权教材全文
未授权论文全文
教师个人敏感资料
学校内部保密文件
```

## 许可

默认使用 MIT License。正式发布前请确认学校、教材和课件版权要求。
