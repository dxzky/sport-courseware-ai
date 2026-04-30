# 01 新手快速开始

## 第 1 步：准备 QClaw

安装 QClaw，登录并绑定账号。进入模型配置时，只启用国内模型服务，例如 Qwen、DeepSeek、GLM、Kimi、Doubao、腾讯云、百度千帆、MiniMax 等。

不要启用 OpenAI、Claude、Gemini、OpenRouter、Perplexity 等国外或中转模型。

## 第 2 步：复制项目

将本项目放到：

```text
D:\Courseware-AI
```

## 第 3 步：放入旧资料

每门课的旧资料放入对应 `input/`：

```text
courses/电路与电子技术基础/input/
courses/人体生理信号采集与分析/input/
courses/智能体育装备概论/input/
```

## 第 4 步：放入模板

```text
templates/教案模板.docx
templates/PPT模板.pptx
templates/讲义模板.docx
```

## 第 5 步：先跑一讲

复制以下指令给 QClaw：

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

## 第 6 步：检查结果

重点检查：

1. `source_cards.jsonl` 有没有编造来源。
2. 教案目标是否具体且可评价。
3. PPT 是否可编辑，是否存在整页图片。
4. 讲义是否比 PPT 更详细。
5. `citation_report.md` 是否通过。
