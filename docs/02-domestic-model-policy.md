# 02 国内模型与 token 策略

## 模型白名单

本项目默认只允许使用国内大模型或国内模型服务：

```text
Qwen / 通义千问
DeepSeek
GLM / 智谱 / Z.AI
Kimi / Moonshot
Doubao / 豆包 / 火山引擎
腾讯云 TokenHub
百度千帆 Qianfan
MiniMax
```

## 禁用模型

```text
OpenAI
Claude / Anthropic
Gemini / Google
OpenRouter
Perplexity
Mistral
Groq
Together AI
```

## 任务路由

| 任务 | 模型级别 | 说明 |
|---|---|---|
| 文件分类、目录抽取 | 低成本模型 | 输出短、低推理需求 |
| 来源卡片抽取 | 低成本或中等模型 | 要求稳定 JSON |
| 长 PDF / 大 PPT 整理 | 长上下文模型 | 不要把全量材料反复传入 |
| 教案最终稿 | 高质量模型 | 重视教学设计与表达 |
| PPT 讲稿备注 | 高质量模型 | 重视可讲授性 |
| 讲义最终稿 | 高质量模型 | 重视系统性和学生可读性 |
| 引用审查 | 中等模型，必要时高质量复核 | 多轮短任务 |

## token 节省规则

1. 不把整本教材、整份 PPT、整篇论文一次性塞进 prompt。
2. 所有资料先转为 `source_cards.jsonl`。
3. 按章节检索 top-k 来源，再生成内容。
4. 旧 PPT 先转 `old_slide_cards.json`。
5. 中间结果优先 JSON 化。
6. 按“课程-章节-课次”分批生成。
7. 缺来源时输出“来源不足，需教师确认”，不得编造。
8. 每次运行输出 `token_usage_report.md`。
