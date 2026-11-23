<div align="center">
  <h1>Awesome Model Routing</h1>
  <p>A curated list of awesome LLM/AI model routing frameworks, gateways, inference engines, and tools.</p>

  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
  ![GitHub stars](https://img.shields.io/github/stars/yenanjing/awesome-model-routing?style=flat-square)
  ![Last Updated](https://img.shields.io/badge/last%20updated-2026-11-23-blue?style=flat-square)

  <p>Collected <strong>132</strong> repositories with <strong>1,000+</strong> stars across <strong>8</strong> categories.</p>
</div>

---

## Table of Contents

- [About](#-about)
- [🧠 LLM Routers & Smart Routing](#llm-routers--smart-routing)
- [🚪 AI Gateways & Unified APIs](#ai-gateways--unified-apis)
- [⚖️ LLM Proxy & Load Balancing](#llm-proxy--load-balancing)
- [⚡ Inference Serving Engines](#inference-serving-engines)
- [🎭 LLM Orchestration Frameworks](#llm-orchestration-frameworks)
- [📡 API Management & Distribution](#api-management--distribution)
- [💰 Cost Optimization & Observability](#cost-optimization--observability)
- [🔬 Research & Benchmarks](#research--benchmarks)
- [Stats](#-stats)
- [Contributing](#-contributing)

---

## About

Model routing is a critical infrastructure pattern for modern AI applications. It encompasses intelligent request routing across multiple LLM providers, cost-optimized model selection, load balancing for inference workloads, and unified API gateways that abstract away provider complexity.

This list covers the full spectrum: from smart routers that choose the optimal model per request, to high-performance inference engines, to unified gateways that provide a single endpoint for 100+ LLM APIs.

> **Criteria**: Repositories with 1,000+ stars, actively maintained, related to model routing.
> Last updated: 2026-11-23

---

## 🧠 LLM Routers & Smart Routing

> Tools that intelligently route LLM requests to different models based on cost, quality, complexity, or latency.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**tashfeenahmed/freellmapi**](https://github.com/tashfeenahmed/freellmapi) | 57,219 | `TypeScript` | 10.1 billion tokens per month. 87 free LLM providers. 1,313 free model endpoints. All behind one /v1 endpoint, plus a... |
| [**justlovemaki/AIClient2API**](https://github.com/justlovemaki/AIClient2API) | 8,999 | `JavaScript` | Self-hosted multi-protocol AI API proxy for Antigravity, Codex, Grok, Kiro, OpenAI, Claude, and custom providers. Sup... |
| [**BlockRunAI/ClawRouter**](https://github.com/BlockRunAI/ClawRouter) | 6,670 | `TypeScript` | The agent-native LLM router for autonomous agents. Every frontier model behind one wallet, <1ms local routing, USDC p... |
| [**lm-sys/RouteLLM**](https://github.com/lm-sys/RouteLLM) | 5,729 | `Python` | A framework for serving and evaluating LLM routers - save LLM costs without compromising quality |
| [**Continuum-AI-Corp/OrcaRouter-Lite**](https://github.com/Continuum-AI-Corp/OrcaRouter-Lite) | 3,060 | `Python` | Self-hosted LLM router with a managed safety net. OpenAI-compatible. BYOK. Single-workspace. Streaming. For more adva... |
| [**ENTERPILOT/GoModel**](https://github.com/ENTERPILOT/GoModel) | 1,326 | `Go` | AI gateway / AI control plane / AI proxy written in Go. Unified OpenAI-compatible and Anthropic-compatible API for Op... |
| [**nejib1/Free-LLM**](https://github.com/nejib1/Free-LLM) | 1,098 | `JavaScript` | 79 free LLM API providers & 460+ free models (limits, no-card options) + Free-LLM Router: all of them behind one Open... |

---

## 🚪 AI Gateways & Unified APIs

> Unified API gateways that provide a single interface to access multiple LLM providers with routing, failover, and load balancing.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**cheaper-inference/OmniRoute**](https://github.com/cheaper-inference/OmniRoute) | 89,845 | `TypeScript` | Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,400+ models Kimi, Claude, GPT, Gem... |
| [**BerriAI/litellm**](https://github.com/BerriAI/litellm) | 63,775 | `Python` | The fastest, litest AI Gateway. Rust core with Python SDK. Call 100+ LLM APIs in OpenAI (or native) format with cost ... |
| [**zhaoxuya520/reverse-skill**](https://github.com/zhaoxuya520/reverse-skill) | 45,136 | `PowerShell` | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-de... |
| [**Kong/kong**](https://github.com/Kong/kong) | 44,407 | `Lua` | 🦍 The API and AI Gateway |
| [**decolua/9router**](https://github.com/decolua/9router) | 32,790 | `JavaScript` | Unlimited FREE AI coding. Connect Claude Code, Codex, Cursor, Cline, Copilot, Antigravity to FREE Claude/GPT/Gemini v... |
| [**fosrl/pangolin**](https://github.com/fosrl/pangolin) | 23,958 | `TypeScript` | Modern networking and security platform providing secure access and connectivity to apps, infrastructure, and AI work... |
| [**apache/apisix**](https://github.com/apache/apisix) | 17,365 | `Lua` | The Cloud-Native API Gateway and AI Gateway |
| [**liketrek/TREK**](https://github.com/liketrek/TREK) | 15,902 | `TypeScript` | The most complete open-source travel planner: real-time collaboration, bookings, budgets, packing lists, journals, of... |
| [**Edge0-AI/Edge0**](https://github.com/Edge0-AI/Edge0) | 12,252 | `C++` | Device-native foundation models: 145B on a laptop, 35B on a phone. Latent MoE, SSD-streamed weights, a router that pr... |
| [**TykTechnologies/tyk**](https://github.com/TykTechnologies/tyk) | 10,897 | `Go` | Open Source API and AI Gateway supporting REST, GraphQL, TCP, gRPC and MCP (Model Context Protocol) |
| [**gamedev-skills/awesome-gamedev-agent-skills**](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) | 10,576 | `Python` | Make games with your AI coding agent: 79 game-dev skills and a router for Godot, Unity, Unreal, Roblox, three.js, Pha... |
| [**maximhq/bifrost**](https://github.com/maximhq/bifrost) | 9,970 | `Go` | Open-source, high-performance AI gateway that works as your LLM gateway, MCP gateway and agent gateway. One OpenAI-co... |
| [**higress-group/higress**](https://github.com/higress-group/higress) | 9,823 | `Go` | 🤖 AI Gateway \| AI Native API Gateway |
| [**mnfst/llm-gateway**](https://github.com/mnfst/llm-gateway) | 7,652 | `TypeScript` | Open Source LLM Gateway 🦚 |
| [**tbphp/gpt-load**](https://github.com/tbphp/gpt-load) | 7,249 | `Go` | Self-hosted AI gateway for multi-channel, multi-credential setups — API keys and subscription accounts, scheduling, f... |
| [**agentgateway/agentgateway**](https://github.com/agentgateway/agentgateway) | 6,385 | `Rust` | Next Generation Agentic Proxy for AI Agents and MCP servers |
| [**oomol-lab/open-connector**](https://github.com/oomol-lab/open-connector) | 6,283 | `TypeScript` | Open-source auth gateway connecting 1700+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI. |
| [**kgateway-dev/kgateway**](https://github.com/kgateway-dev/kgateway) | 5,752 | `Go` | The Cloud-Native API Gateway and AI Gateway |
| [**weave-os/router**](https://github.com/weave-os/router) | 5,620 | `Go` | Model router for agentic systems. Routes every prompt to the right model in <50ms. Cut costs 40-70% with just an endp... |
| [**looplj/axonhub**](https://github.com/looplj/axonhub) | 5,485 | `Go` | ⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, cost control & end-to-e... |
| [**AgnesAI-Labs/AgnesAI-Models**](https://github.com/AgnesAI-Labs/AgnesAI-Models) | 5,303 | `N/A` | Official Agnes AI gateway and model catalog for OpenAI-compatible text, image, video, and agent workflows. |
| [**NateBJones-Projects/OB1**](https://github.com/NateBJones-Projects/OB1) | 4,774 | `TypeScript` | Open Brain — The infrastructure layer for your thinking. One database, one AI gateway, one chat channel — any AI plug... |
| [**cerbos/cerbos**](https://github.com/cerbos/cerbos) | 4,668 | `Go` | Cerbos is an open-core authorization management platform for authorizing every identity and governing every action ac... |
| [**octelium/octelium**](https://github.com/octelium/octelium) | 4,199 | `Go` | A next-gen FOSS self-hosted unified zero trust secure access platform that can operate as a remote access VPN, a ZTNA... |
| [**elliothux/open-compute**](https://github.com/elliothux/open-compute) | 4,123 | `Rust` | Self-hosted Cloudflare Workers-compatible platform with Workers、KV、D1、R2、DO、Queues、Workflows、Cron、Cache、Images、Vector... |
| [**duolahypercho/codex-router**](https://github.com/duolahypercho/codex-router) | 3,983 | `JavaScript` | External-model router for Codex with guided Kimi OAuth/API, DeepSeek, safe migration, and rollback. |
| [**yvgude/lean-ctx**](https://github.com/yvgude/lean-ctx) | 3,960 | `Rust` | LeanCTX is the Context Gateway for AI Systems. Select task-relevant context, apply supported controls, connect local ... |
| [**nextlevelbuilder/goclaw**](https://github.com/nextlevelbuilder/goclaw) | 3,722 | `Go` | GoClaw - GoClaw is OpenClaw rebuilt in Go — with multi-tenant isolation, 5-layer security, and native concurrency. De... |
| [**NVIDIA-NeMo/Switchyard**](https://github.com/NVIDIA-NeMo/Switchyard) | 3,672 | `Rust` | Switchyard lets LLM applications route traffic across models and providers while preserving native OpenAI and Anthrop... |
| [**edison7009/EchoBird**](https://github.com/edison7009/EchoBird) | 3,583 | `Rust` | All-in-one AI desktop app: one-click install for Claude Code, Codex CLI, DeepSeek and more, manage AI accounts and qu... |
| [**wang2122/sprix-sage-router**](https://github.com/wang2122/sprix-sage-router) | 3,563 | `Python` | Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks. |
| [**cirosantilli/china-dictatorship**](https://github.com/cirosantilli/china-dictatorship) | 3,368 | `HTML` | 反中共政治宣传库。Anti Chinese government propaganda. 住在中国真名用户的网友请别给星星，不然你要被警察请喝茶。常见问答集，新闻集和饭店和音乐建议。卐习万岁卐。冠状病毒审查郝海东新疆改造中心六四事件法... |
| [**fuxicodex/Fuxi**](https://github.com/fuxicodex/Fuxi) | 3,182 | `Python` | FuXi is a fast, self-contained AI coding agent that lives in your terminal — edit code, run commands, and drive tools... |
| [**motiful/cc-gateway**](https://github.com/motiful/cc-gateway) | 3,096 | `TypeScript` | AI API identity gateway — reverse proxy that normalizes device fingerprints and telemetry for privacy-preserving API ... |
| [**ulab-uiuc/LLMRouter**](https://github.com/ulab-uiuc/LLMRouter) | 3,090 | `Python` | LLMRouter: An Open-Source Library for LLM Routing |
| [**butterbase-ai/butterbase**](https://github.com/butterbase-ai/butterbase) | 3,033 | `TypeScript` | Open-source backend-as-a-service. Postgres, auth, storage, functions, AI gateway, MCP. |
| [**supercorp-ai/supergateway**](https://github.com/supercorp-ai/supergateway) | 2,978 | `TypeScript` | Run MCP stdio servers over HTTP streamable, SSE and SSE over stdio. AI gateway. |
| [**kaitranntt/ccs**](https://github.com/kaitranntt/ccs) | 2,908 | `TypeScript` | Switch between Claude accounts, Gemini, Copilot, OpenRouter (300+ models) via CLIProxyAPI OAuth proxy. Visual dashboa... |
| [**bestruirui/octopus**](https://github.com/bestruirui/octopus) | 2,752 | `TypeScript` | One Hub All LLMs For You \| 为个人打造的 LLM API 聚合网关 |
| [**krakend/krakend-ce**](https://github.com/krakend/krakend-ce) | 2,704 | `Go` | KrakenD Community Edition: High-performance, stateless, declarative, API Gateway written in Go. |
| [**aimod-cc/Agent2API**](https://github.com/aimod-cc/Agent2API) | 2,665 | `Rust` | Local AI routing gateway with Agent client takeover — reuse existing client logins, call 50+ AI clients through one b... |
| [**Draculabo/AntigravityManager**](https://github.com/Draculabo/AntigravityManager) | 2,569 | `TypeScript` | Antigravity Manager is a desktop application for managing the Google accounts used by Antigravity clients (including ... |
| [**techa03/goodsKill**](https://github.com/techa03/goodsKill) | 2,458 | `Java` | 🐎基于SpringCloud 2025.x + Dubbo 3.x + AI构建的模拟秒杀微服务项目，集成了Elasticsearch🔍、Gateway、Mybatis-Plus、Sharding-JDBC等常用开源组件 |
| [**theagentrouter/agent-router**](https://github.com/theagentrouter/agent-router) | 2,438 | `Go` | Manages Unified Access to Generative AI Services built on Envoy Gateway |
| [**future-agi/future-agi**](https://github.com/future-agi/future-agi) | 2,290 | `Python` | Open-source, end-to-end platform for evaluating, observing, and improving LLM and AI agent applications. Tracing · Ev... |
| [**martin-ger/esp32_nat_router**](https://github.com/martin-ger/esp32_nat_router) | 2,288 | `C` | An AI-enabled NAT Router/Firewall for the ESP32 |
| [**crshdn/mission-control**](https://github.com/crshdn/mission-control) | 2,162 | `TypeScript` | The world's first Autonomous Product Engine (APE): AI agents research your market, generate features, and ship code a... |
| [**gege-circle/.github**](https://github.com/gege-circle/.github) | 2,122 | `N/A` | 这里是GitHub的草场，也是戈戈圈爱好者的交流地，主要讨论动漫、游戏、科技、人文、生活等所有话题，欢迎各位小伙伴们在此讨论趣事。This is GitHub grassland, and the community place fo... |
| [**open-compress/claw-compactor**](https://github.com/open-compress/claw-compactor) | 2,005 | `Python` | 14-stage Fusion Pipeline for LLM token compression — reversible compression, AST-aware code analysis, intelligent con... |
| [**TimefoldAI/timefold-solver**](https://github.com/TimefoldAI/timefold-solver) | 1,880 | `Java` | The open source Solver AI for Java and Kotlin to optimize scheduling and routing. Solve the vehicle routing problem, ... |
| [**APIParkLab/APIPark**](https://github.com/APIParkLab/APIPark) | 1,826 | `TypeScript` | Cloud native, ultra-high performance AI&API gateway, LLM API management, distribution system, open platform, supporti... |
| [**vercel-labs/coding-agent-template**](https://github.com/vercel-labs/coding-agent-template) | 1,801 | `TypeScript` | Multi-agent AI coding platform powered by Vercel Sandbox and AI Gateway |
| [**NVIDIA/Personal-AI-Router**](https://github.com/NVIDIA/Personal-AI-Router) | 1,786 | `Go` | Router that virtually distributes inference across connected devices in the home. |
| [**theopenco/llmgateway**](https://github.com/theopenco/llmgateway) | 1,758 | `TypeScript` | Route, manage, and analyze your LLM requests across multiple providers with a unified API interface. |
| [**mithun50/openclaw-termux**](https://github.com/mithun50/openclaw-termux) | 1,752 | `Dart` | Run OpenClaw AI Gateway on Android — standalone Flutter app with built-in terminal, web dashboard, and one-tap setup.... |
| [**Safe3/uusec-waf**](https://github.com/Safe3/uusec-waf) | 1,727 | `Shell` | Industry-leading free, high-performance, AI and semantic technology Web Application Firewall and API Security Gateway... |
| [**awtkns/fastapi-crudrouter**](https://github.com/awtkns/fastapi-crudrouter) | 1,698 | `Python` | A dynamic FastAPI router that automatically creates CRUD routes for your models |
| [**DEEIX-AI/DEEIX-Chat**](https://github.com/DEEIX-AI/DEEIX-Chat) | 1,640 | `Go` | An enterprise AI workspace for model routing, multimodal chat, files, tools, billing, identity, and operations. |
| [**astaxie/TokenHub**](https://github.com/astaxie/TokenHub) | 1,451 | `Go` | TokenHub gives enterprises a private gateway to unify AI model access and governance, making every request controllab... |
| [**Paritok-official/paritok-4b-v1**](https://github.com/Paritok-official/paritok-4b-v1) | 1,439 | `Python` | Non-destructive compression gateway for AI coding agents. Cuts token bills 25% on turn 1 to past 85% in long or satur... |
| [**wouterkool/attention-learn-to-route**](https://github.com/wouterkool/attention-learn-to-route) | 1,388 | `Jupyter Notebook` | Attention based model for learning to solve different routing problems |
| [**ntegrals/10x**](https://github.com/ntegrals/10x) | 1,367 | `TypeScript` | ⚡️ 10x - Up to 20x faster AI coding with multi-step Superpowers. Open-source agent with smart model routing, BYOK, fu... |
| [**kerpopule/hermes-jev-skills**](https://github.com/kerpopule/hermes-jev-skills) | 1,363 | `Python` | Jev-powered model routing, memory, compaction, skill selection, computer and browser use for Hermes agents (also Clau... |
| [**chubbyguan/chubbyskills**](https://github.com/chubbyguan/chubbyskills) | 1,345 | `Python` | 把中文全渠道内容（抖音 / B站 / 小红书 / 公众号 / X / 播客）采集进个人知识库的 14 个 AI Skill：图文存图、视频转文字稿、字幕优先免 GPU、RSS/YouTube 订阅调度与每日情报简报，附带知识库 MCP... |
| [**LiteLLM-Labs/litellm-agent-control-plane**](https://github.com/LiteLLM-Labs/litellm-agent-control-plane) | 1,336 | `Rust` | 1 place to call all your agents - OpenCode, Hermes, Claude Managed Agents, Cursor Agents API, DeepAgents. |
| [**kellyvv/PhoneClaw**](https://github.com/kellyvv/PhoneClaw) | 1,297 | `Swift` | PhoneClaw turns phones into local AI agent runtimes with on-device models, native mobile Skills, LiveLand, and option... |
| [**ASCIT31/Dark-Moon**](https://github.com/ASCIT31/Dark-Moon) | 1,294 | `Python` | Open-source autonomous AI penetration testing. 50 specialist agents across web, API, cloud, Active Directory, Kuberne... |
| [**fatwang2/search2ai**](https://github.com/fatwang2/search2ai) | 1,286 | `TypeScript` | Self-hosted search gateway for AI agents. Unified search, news and page extraction with provider fallback. REST API, ... |
| [**pnoker/iot-dc3**](https://github.com/pnoker/iot-dc3) | 1,276 | `Java` | IoT DC3 — Connect the Physical World to AI. An open-source Industrial IoT Runtime for Physical AI: 36 protocol driver... |
| [**modu-ai/moai-adk**](https://github.com/modu-ai/moai-adk) | 1,260 | `Go` | Agentic development harness for Claude Code — SPEC-driven plan/run/sync, TRUST 5 quality gates, model+effort routing,... |
| [**shadcn-ui/chatbot-template**](https://github.com/shadcn-ui/chatbot-template) | 1,214 | `TypeScript` | A minimal chatbot template built with Next.js, AI SDK, shadcn/ui, shadcn/react, shadcn/typeset. It runs on the Vercel... |
| [**fsbolero/Bolero**](https://github.com/fsbolero/Bolero) | 1,138 | `F#` | Bolero brings Blazor to F# developers with an easy to use Model-View-Update architecture, HTML combinators, hot reloa... |
| [**caozhiyuan/copilot-api**](https://github.com/caozhiyuan/copilot-api) | 1,131 | `TypeScript` | GitHub Copilot, OpenAI Codex, OpenCode Go, and third-party AI provider gateway with OpenAI and Anthropic API compatib... |
| [**kittors/CliRelay**](https://github.com/kittors/CliRelay) | 1,062 | `Go` | Self-hosted AI gateway for coding CLIs — one OpenAI/Claude/Gemini/Codex-compatible endpoint, with a multi-tenant web ... |
| [**w8123/EnterpriseAgentFramework**](https://github.com/w8123/EnterpriseAgentFramework) | 1,058 | `Java` | ReachAI企业级智能体开发平台：快速、安全完成已有业务系统智能化改造，让 AI 在 OA、ERP、CRM 等原系统中查数据、填表单、办业务。ReachAI: Quickly and securely bring AI to exi... |
| [**agentic-community/mcp-gateway-registry**](https://github.com/agentic-community/mcp-gateway-registry) | 1,055 | `Python` | Enterprise-ready MCP Gateway & Registry that centralizes AI development tools with secure OAuth authentication, dynam... |
| [**beizhu-1209/AIHelms**](https://github.com/beizhu-1209/AIHelms) | 1,039 | `Python` | 企业级 AI 资源纳管平台，提供统一 AI网关、Token调度能力，纳管 OpenAI、Azure、Claude、DeepSeek 等主流模型，并支持 MCP 工具与 Skill 的集中注册分发。具备内外双轨定价、成本归因、统一身份认... |
| [**Alice-Marx/dsh-model-router**](https://github.com/Alice-Marx/dsh-model-router) | 1,018 | `JavaScript` | Model Router and Bot plugin for DeepSeek Harness |
| [**respanai/respan-gateway**](https://github.com/respanai/respan-gateway) | 1,012 | `Rust` | Open-source LLM gateway in Rust. One endpoint for OpenAI, Anthropic, Gemini and every other vendor. Any SDK, any mode... |
| [**Azure-Samples/AI-Gateway**](https://github.com/Azure-Samples/AI-Gateway) | 1,011 | `Jupyter Notebook` | Labs to explore AI Models, MCP servers, and Agents with the AI Gateway powered by Azure API Management and Microsoft ... |
| [**zexadev/gemini-web2api-go**](https://github.com/zexadev/gemini-web2api-go) | 1,009 | `Go` | Gemini web → OpenAI-compatible + native Gemini API, self-hosted, no API key. Gemini 4 Argon from a paid account cooki... |

---

## ⚖️ LLM Proxy & Load Balancing

> Proxy servers and load balancers specifically designed for LLM API traffic management.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**QuantumNous/new-api**](https://github.com/QuantumNous/new-api) | 52,411 | `Go` | Open-source AI gateway. Self-hosted LLM gateway with OpenAI-, Claude- and Gemini-compatible APIs, model routing, acce... |
| [**lidge-jun/opencodex**](https://github.com/lidge-jun/opencodex) | 18,724 | `TypeScript` | Universal provider proxy for OpenAI Codex & Claude Code — use any LLM (Claude, Gemini, Grok, DeepSeek, Ollama…) with ... |
| [**Portkey-AI/gateway**](https://github.com/Portkey-AI/gateway) | 13,432 | `TypeScript` | A blazing fast AI Gateway with integrated guardrails. Route to 1,600+ LLMs, 50+ AI Guardrails with 1 fast & friendly ... |
| [**coaidev/coai**](https://github.com/coaidev/coai) | 9,344 | `TypeScript` | 🚀 Next Gen Multi-tenant AI One-Stop Solution. Builtin Admin & Billing System. Enterprise-Grade Unified LLM Gateway Su... |

---

## ⚡ Inference Serving Engines

> High-performance inference engines that serve LLM models with built-in routing and scheduling capabilities.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**ollama/ollama**](https://github.com/ollama/ollama) | 187,896 | `Go` | Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models. |
| [**vllm-project/vllm**](https://github.com/vllm-project/vllm) | 97,418 | `Python` | A high-throughput and memory-efficient inference and serving engine for LLMs |
| [**sgl-project/sglang**](https://github.com/sgl-project/sglang) | 38,987 | `Python` | SGLang is a high-performance serving framework for large language models and multimodal models. |
| [**GeeeekExplorer/nano-vllm**](https://github.com/GeeeekExplorer/nano-vllm) | 16,546 | `Python` | Nano vLLM |
| [**NVIDIA/TensorRT-LLM**](https://github.com/NVIDIA/TensorRT-LLM) | 15,120 | `Python` | TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and supports state-... |
| [**vllm-project/vllm-omni**](https://github.com/vllm-project/vllm-omni) | 7,922 | `Python` | A framework for efficient model inference with omni-modality models |
| [**vllm-project/semantic-router**](https://github.com/vllm-project/semantic-router) | 6,521 | `Go` | An open, programmable decision layer for models and compute. |
| [**sgl-project/mini-sglang**](https://github.com/sgl-project/mini-sglang) | 5,637 | `Python` | A compact implementation of SGLang, designed to demystify the complexities of modern LLM serving systems. |
| [**vllm-project/aibrix**](https://github.com/vllm-project/aibrix) | 5,201 | `Go` | Cost-efficient and pluggable Infrastructure components for GenAI inference |
| [**vllm-project/llm-compressor**](https://github.com/vllm-project/llm-compressor) | 3,986 | `Python` | State-of-the-art LLM compression, built for production inference with vLLM |
| [**vllm-project/vllm-ascend**](https://github.com/vllm-project/vllm-ascend) | 3,135 | `Python` | Community maintained hardware plugin for vLLM on Huawei Ascend |
| [**datawhalechina/zero-to-sglang**](https://github.com/datawhalechina/zero-to-sglang) | 2,353 | `Python` | Official SGLang x Datawhale course on LLM inference: understand inference, build a mini-sglang from scratch, then rea... |
| [**sgl-project/sglang-omni**](https://github.com/sgl-project/sglang-omni) | 1,920 | `Python` | High Performance Serving Runtime For Interactive Super Intelligence System |
| [**vllm-project/guidellm**](https://github.com/vllm-project/guidellm) | 1,804 | `Python` | Evaluate and Enhance Your LLM Deployments for Real-World Inference Needs |
| [**waybarrios/vllm-mlx**](https://github.com/waybarrios/vllm-mlx) | 1,658 | `Python` | High-performance OpenAI and Anthropic compatible LLM inference server for Apple Silicon. Native MLX, continuous batch... |
| [**1CatAI/1Cat-vLLM**](https://github.com/1CatAI/1Cat-vLLM) | 1,567 | `Python` | V100 / SM70-focused vLLM engineering fork for modern LLM inference. |
| [**Ksuriuri/index-tts-vllm**](https://github.com/Ksuriuri/index-tts-vllm) | 1,244 | `Python` | Added vLLM support to IndexTTS for faster inference. |
| [**weicj/vLLM-2080Ti-Definitive**](https://github.com/weicj/vLLM-2080Ti-Definitive) | 1,244 | `Python` | The definitive vLLM runtime for dual RTX 2080 Ti 22GB + NVLink, delivering Qwen 27B local inference with maximum 200+... |
| [**jmaczan/tiny-vllm**](https://github.com/jmaczan/tiny-vllm) | 1,208 | `C++` | Build your own high performance LLM inference engine in C++ and CUDA - a smaller version of vLLM |

---

## 🎭 LLM Orchestration Frameworks

> Frameworks for orchestrating multiple LLMs with routing, pipeline, and workflow capabilities.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**musistudio/claude-code-router**](https://github.com/musistudio/claude-code-router) | 38,336 | `TypeScript` | One local control plane for every AI agent: route across models, fuse new capabilities, orchestrate tools, and stay f... |
| [**deepset-ai/haystack**](https://github.com/deepset-ai/haystack) | 27,086 | `Python` | Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design mod... |
| [**neuml/txtai**](https://github.com/neuml/txtai) | 13,722 | `Python` | 💡 All-in-one AI framework for semantic search, LLM orchestration and language model workflows |
| [**katanemo/plano**](https://github.com/katanemo/plano) | 7,119 | `Rust` | Plano is an AI-native proxy server and data plane for agentic apps. Smart LLM routing, observability, agent orchestra... |
| [**IBM/mcp-context-forge**](https://github.com/IBM/mcp-context-forge) | 4,876 | `Python` | An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, or REST/gRPC APIs, exposing a unified endpoint... |
| [**archestra-ai/archestra**](https://github.com/archestra-ai/archestra) | 4,456 | `TypeScript` | Enterprise AI Platform with guardrails, MCP registry, gateway & orchestrator |
| [**foryourhealth111-pixel/Vibe-Skills**](https://github.com/foryourhealth111-pixel/Vibe-Skills) | 3,842 | `Python` | Intelligent Skill routing and workflow orchestration for AI agents — +21.12 pp reward, −29.6% tokens on SkillsBench w... |
| [**zhnt/loushang**](https://github.com/zhnt/loushang) | 2,105 | `Python` | AI-native agent harness for coding workflows by python: multi-model LLM orchestration, stateful sessions, tool govern... |
| [**DemonDamon/AgenticX**](https://github.com/DemonDamon/AgenticX) | 1,177 | `Python` | AgenticX is a unified, production-ready multi-agent platform — Python SDK + CLI (agx) + Studio server + Machi desktop... |
| [**AI-QL/tuui**](https://github.com/AI-QL/tuui) | 1,161 | `TypeScript` | A desktop MCP client designed as a tool unitary utility integration, accelerating AI adoption through the Model Conte... |
| [**proinsight-io/crewmeld**](https://github.com/proinsight-io/crewmeld) | 1,121 | `TypeScript` | CrewMeld — Enterprise AI Digital Workforce Platform. Manage AI employees like real team members. Visual SOP orchestra... |
| [**Zyrexnn/Cybermes**](https://github.com/Zyrexnn/Cybermes) | 1,061 | `Python` | Autonomous Offensive Security, Bug Bounty & Red Teaming Agent Framework powered by Hermes Agent, specialized reasonin... |

---

## 📡 API Management & Distribution

> Platforms for managing, distributing, and monitoring LLM API access across teams and applications.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**casdoor/casdoor**](https://github.com/casdoor/casdoor) | 14,931 | `Go` | An open-source Agent-first Identity and Access Management (IAM) /LLM MCP & agent gateway and auth server with web UI ... |
| [**InsForge/InsForge**](https://github.com/InsForge/InsForge) | 13,352 | `TypeScript` | The all-in-one, open-source backend platform for agentic coding. InsForge gives your coding agent database, auth, sto... |

---

## 💰 Cost Optimization & Observability

> Tools focused on reducing LLM costs through smart routing, caching, token optimization, and observability.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**langfuse/langfuse**](https://github.com/langfuse/langfuse) | 37,758 | `TypeScript` | 🪢 Open source AI engineering platform: AI Gateway, agent observability, evals, and prompt/skill management, built on ... |
| [**langwatch/langwatch**](https://github.com/langwatch/langwatch) | 5,052 | `TypeScript` | Open-Source Agent Observability & Evals for AI Platform teams. Trace, test, route and govern every agent & coding ass... |
| [**seakee/CPA-Manager-Plus**](https://github.com/seakee/CPA-Manager-Plus) | 4,104 | `Go` | A self-hosted CPA / CLIProxyAPI management panel and AI gateway observability dashboard for requests, usage, cost, qu... |
| [**ascending-llc/jarvis-registry**](https://github.com/ascending-llc/jarvis-registry) | 4,101 | `Python` | Connect any AI copilot or autonomous agent to your enterprise tools — through a single, secure MCP/Agent gateway with... |
| [**aklivity/zilla**](https://github.com/aklivity/zilla) | 1,681 | `Java` | 🦎 A lightweight, streaming-native, multi-protocol gateway for AI, APIs, and real-time data. Route LLM requests across... |
| [**bricks-cloud/BricksLLM**](https://github.com/bricks-cloud/BricksLLM) | 1,232 | `Go` | 🔒 Enterprise-grade API gateway that helps you monitor and impose cost or rate limits per API key. Get fine-grained ac... |
| [**jzyong/game-server**](https://github.com/jzyong/game-server) | 1,227 | `Java` | Distributed Java game server, including cluster management server, gateway server, hall server, game logic server, ba... |

---

## 🔬 Research & Benchmarks

> Academic research papers, frameworks, and benchmarks related to LLM routing strategies.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|

---

## Stats

- **Total repositories**: 132
- **Minimum stars**: 1,000
- **Languages covered**: C, C++, Dart, F#, Go, HTML, Java, JavaScript, Jupyter Notebook, Lua, PowerShell, Python, Rust, Shell, Swift, TypeScript
- **Last updated**: 2026-11-23

### Top 10 by Stars

| Rank | Repository | Stars |
|------|-----------|-------|
| 1 | [ollama/ollama](https://github.com/ollama/ollama) | 187,896 |
| 2 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | 97,418 |
| 3 | [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | 89,845 |
| 4 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | 63,775 |
| 5 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | 57,219 |
| 6 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | 52,411 |
| 7 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | 45,136 |
| 8 | [Kong/kong](https://github.com/Kong/kong) | 44,407 |
| 9 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | 38,987 |
| 10 | [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) | 38,336 |

---

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

To add a project:
1. Fork this repository
2. Add your project to the relevant section
3. Ensure it has 1,000+ stars and is actively maintained
4. Submit a Pull Request

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

This list is under the [CC0 1.0](LICENSE) license.

---

<div align="center">
  <sub>Generated with love using <a href="https://claude.ai/claude-code">Claude Code</a> | Auto-updated daily via GitHub Actions</sub>
</div>
