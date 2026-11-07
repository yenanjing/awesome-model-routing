<div align="center">
  <h1>Awesome Model Routing</h1>
  <p>A curated list of awesome LLM/AI model routing frameworks, gateways, inference engines, and tools.</p>

  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
  ![GitHub stars](https://img.shields.io/github/stars/yenanjing/awesome-model-routing?style=flat-square)
  ![Last Updated](https://img.shields.io/badge/last%20updated-2026-11-07-blue?style=flat-square)

  <p>Collected <strong>129</strong> repositories with <strong>1,000+</strong> stars across <strong>8</strong> categories.</p>
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
> Last updated: 2026-11-07

---

## 🧠 LLM Routers & Smart Routing

> Tools that intelligently route LLM requests to different models based on cost, quality, complexity, or latency.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**tashfeenahmed/freellmapi**](https://github.com/tashfeenahmed/freellmapi) | 48,680 | `TypeScript` | 7.4 billion tokens per month. 34 free LLM providers. 635 free model endpoints. All behind one /v1 endpoint, plus any ... |
| [**justlovemaki/AIClient2API**](https://github.com/justlovemaki/AIClient2API) | 8,965 | `JavaScript` | Self-hosted multi-protocol AI API proxy for Antigravity, Codex, Grok, Kiro, OpenAI, Claude, and custom providers. Sup... |
| [**BlockRunAI/ClawRouter**](https://github.com/BlockRunAI/ClawRouter) | 6,653 | `TypeScript` | The agent-native LLM router for autonomous agents. Every frontier model behind one wallet, <1ms local routing, USDC p... |
| [**lm-sys/RouteLLM**](https://github.com/lm-sys/RouteLLM) | 5,688 | `Python` | A framework for serving and evaluating LLM routers - save LLM costs without compromising quality |
| [**Continuum-AI-Corp/OrcaRouter-Lite**](https://github.com/Continuum-AI-Corp/OrcaRouter-Lite) | 1,713 | `Python` | Self-hosted LLM router with a managed safety net. OpenAI-compatible. BYOK. Single-workspace. Streaming. For more adva... |
| [**ENTERPILOT/GoModel**](https://github.com/ENTERPILOT/GoModel) | 1,309 | `Go` | AI gateway / AI control plane / AI proxy written in Go. Unified OpenAI-compatible and Anthropic-compatible API for Op... |

---

## 🚪 AI Gateways & Unified APIs

> Unified API gateways that provide a single interface to access multiple LLM providers with routing, failover, and load balancing.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**cheaper-inference/OmniRoute**](https://github.com/cheaper-inference/OmniRoute) | 85,340 | `TypeScript` | Never stop coding. Free MIT AI gateway: one endpoint, 375 providers (150+ free), 1,400+ models Kimi, Claude, GPT, Gem... |
| [**BerriAI/litellm**](https://github.com/BerriAI/litellm) | 62,868 | `Python` | The fastest, litest AI Gateway. Rust core with Python SDK. Call 100+ LLM APIs in OpenAI (or native) format with cost ... |
| [**Kong/kong**](https://github.com/Kong/kong) | 44,365 | `Lua` | 🦍 The API and AI Gateway |
| [**zhaoxuya520/reverse-skill**](https://github.com/zhaoxuya520/reverse-skill) | 44,268 | `PowerShell` | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-de... |
| [**decolua/9router**](https://github.com/decolua/9router) | 32,069 | `JavaScript` | Unlimited FREE AI coding. Connect Claude Code, Codex, Cursor, Cline, Copilot, Antigravity to FREE Claude/GPT/Gemini v... |
| [**fosrl/pangolin**](https://github.com/fosrl/pangolin) | 23,343 | `TypeScript` | Modern networking and security platform providing secure access and connectivity to apps, infrastructure, and AI work... |
| [**apache/apisix**](https://github.com/apache/apisix) | 17,302 | `Lua` | The Cloud-Native API Gateway and AI Gateway |
| [**liketrek/TREK**](https://github.com/liketrek/TREK) | 15,421 | `TypeScript` | The most complete open-source travel planner: real-time collaboration, bookings, budgets, packing lists, journals, of... |
| [**TykTechnologies/tyk**](https://github.com/TykTechnologies/tyk) | 10,879 | `Go` | Open Source API and AI Gateway supporting REST, GraphQL, TCP, gRPC and MCP (Model Context Protocol) |
| [**higress-group/higress**](https://github.com/higress-group/higress) | 9,728 | `Go` | 🤖 AI Gateway \| AI Native API Gateway |
| [**maximhq/bifrost**](https://github.com/maximhq/bifrost) | 9,422 | `Go` | Open-source, high-performance AI gateway that works as your LLM gateway, MCP gateway and agent gateway. One OpenAI-co... |
| [**Edge0-AI/Edge0**](https://github.com/Edge0-AI/Edge0) | 9,125 | `Python` | Run 35B MoE models in ~2.5 GB of RAM. Weights stream from SSD; a trained router predicts loads a step ahead. Mac, iPh... |
| [**mnfst/llm-gateway**](https://github.com/mnfst/llm-gateway) | 7,624 | `TypeScript` | Open Source LLM Gateway 🦚 |
| [**gamedev-skills/awesome-gamedev-agent-skills**](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) | 7,475 | `Python` | 77 game-dev skills for AI coding agents — Godot, Unity, Unreal, Phaser, PixiJS, three.js, Bevy, pygame, LÖVE, Roblox.... |
| [**tbphp/gpt-load**](https://github.com/tbphp/gpt-load) | 7,200 | `Go` | Self-hosted AI gateway for multi-channel, multi-credential setups — API keys and subscription accounts, scheduling, f... |
| [**oomol-lab/open-connector**](https://github.com/oomol-lab/open-connector) | 6,197 | `TypeScript` | Open-source auth gateway connecting 1500+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI. |
| [**agentgateway/agentgateway**](https://github.com/agentgateway/agentgateway) | 6,018 | `Rust` | Next Generation Agentic Proxy for AI Agents and MCP servers |
| [**kgateway-dev/kgateway**](https://github.com/kgateway-dev/kgateway) | 5,735 | `Go` | The Cloud-Native API Gateway and AI Gateway |
| [**weave-os/router**](https://github.com/weave-os/router) | 5,616 | `Go` | Model router for agentic systems. Routes every prompt to the right model in <50ms. Cut costs 40-70% with just an endp... |
| [**looplj/axonhub**](https://github.com/looplj/axonhub) | 5,437 | `Go` | ⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, cost control & end-to-e... |
| [**AgnesAI-Labs/AgnesAI-Models**](https://github.com/AgnesAI-Labs/AgnesAI-Models) | 5,269 | `N/A` | Official Agnes AI gateway and model catalog for OpenAI-compatible text, image, video, and agent workflows. |
| [**withcoral/coral**](https://github.com/withcoral/coral) | 4,937 | `Rust` | The execution layer for AI agents. Act across more of your systems with precise controls: safer, faster and more effi... |
| [**NateBJones-Projects/OB1**](https://github.com/NateBJones-Projects/OB1) | 4,760 | `TypeScript` | Open Brain — The infrastructure layer for your thinking. One database, one AI gateway, one chat channel — any AI plug... |
| [**cerbos/cerbos**](https://github.com/cerbos/cerbos) | 4,648 | `Go` | Cerbos is an open-core authorization management platform for authorizing every identity and governing every action ac... |
| [**octelium/octelium**](https://github.com/octelium/octelium) | 4,157 | `Go` | A next-gen FOSS self-hosted unified zero trust secure access platform that can operate as a remote access VPN, a ZTNA... |
| [**duolahypercho/codex-router**](https://github.com/duolahypercho/codex-router) | 3,980 | `JavaScript` | External-model router for Codex with guided Kimi OAuth/API, DeepSeek, safe migration, and rollback. |
| [**yvgude/lean-ctx**](https://github.com/yvgude/lean-ctx) | 3,934 | `Rust` | LeanCTX is the Context Gateway for AI Systems. Select task-relevant context, apply supported controls, connect local ... |
| [**nextlevelbuilder/goclaw**](https://github.com/nextlevelbuilder/goclaw) | 3,708 | `Go` | GoClaw - GoClaw is OpenClaw rebuilt in Go — with multi-tenant isolation, 5-layer security, and native concurrency. De... |
| [**wang2122/sprix-sage-router**](https://github.com/wang2122/sprix-sage-router) | 3,562 | `Python` | Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks. |
| [**edison7009/EchoBird**](https://github.com/edison7009/EchoBird) | 3,523 | `Rust` | All-in-one AI desktop app: one-click install for Claude Code, Codex CLI, DeepSeek and more, manage AI accounts and qu... |
| [**NVIDIA-NeMo/Switchyard**](https://github.com/NVIDIA-NeMo/Switchyard) | 3,492 | `Rust` | Switchyard lets LLM applications route traffic across models and providers while preserving native OpenAI and Anthrop... |
| [**cirosantilli/china-dictatorship**](https://github.com/cirosantilli/china-dictatorship) | 3,323 | `HTML` | 反中共政治宣传库。Anti Chinese government propaganda. 住在中国真名用户的网友请别给星星，不然你要被警察请喝茶。常见问答集，新闻集和饭店和音乐建议。卐习万岁卐。冠状病毒审查郝海东新疆改造中心六四事件法... |
| [**fuxicodex/Fuxi**](https://github.com/fuxicodex/Fuxi) | 3,194 | `Python` | FuXi is a fast, self-contained AI coding agent that lives in your terminal — edit code, run commands, and drive tools... |
| [**elliothux/open-compute**](https://github.com/elliothux/open-compute) | 3,107 | `Rust` | Self-hosted Cloudflare Workers-compatible platform with Workers、KV、D1、R2、DO、Queues、Workflows、Cron、Cache、Images、Vector... |
| [**motiful/cc-gateway**](https://github.com/motiful/cc-gateway) | 3,086 | `TypeScript` | AI API identity gateway — reverse proxy that normalizes device fingerprints and telemetry for privacy-preserving API ... |
| [**ulab-uiuc/LLMRouter**](https://github.com/ulab-uiuc/LLMRouter) | 3,068 | `Python` | LLMRouter: An Open-Source Library for LLM Routing |
| [**butterbase-ai/butterbase**](https://github.com/butterbase-ai/butterbase) | 3,030 | `TypeScript` | Open-source backend-as-a-service. Postgres, auth, storage, functions, AI gateway, MCP. |
| [**supercorp-ai/supergateway**](https://github.com/supercorp-ai/supergateway) | 2,949 | `TypeScript` | Run MCP stdio servers over HTTP streamable, SSE and SSE over stdio. AI gateway. |
| [**kaitranntt/ccs**](https://github.com/kaitranntt/ccs) | 2,897 | `TypeScript` | Switch between Claude accounts, Gemini, Copilot, OpenRouter (300+ models) via CLIProxyAPI OAuth proxy. Visual dashboa... |
| [**bestruirui/octopus**](https://github.com/bestruirui/octopus) | 2,742 | `TypeScript` | One Hub All LLMs For You \| 为个人打造的 LLM API 聚合网关 |
| [**krakend/krakend-ce**](https://github.com/krakend/krakend-ce) | 2,701 | `Go` | KrakenD Community Edition: High-performance, stateless, declarative, API Gateway written in Go. |
| [**Draculabo/AntigravityManager**](https://github.com/Draculabo/AntigravityManager) | 2,476 | `TypeScript` | Antigravity Manager is a desktop application for managing the Google accounts used by Antigravity clients (including ... |
| [**techa03/goodsKill**](https://github.com/techa03/goodsKill) | 2,455 | `Java` | 🐎基于SpringCloud 2025.x + Dubbo 3.x + AI构建的模拟秒杀微服务项目，集成了Elasticsearch🔍、Gateway、Mybatis-Plus、Sharding-JDBC等常用开源组件 |
| [**theagentrouter/agent-router**](https://github.com/theagentrouter/agent-router) | 2,366 | `Go` | Manages Unified Access to Generative AI Services built on Envoy Gateway |
| [**martin-ger/esp32_nat_router**](https://github.com/martin-ger/esp32_nat_router) | 2,259 | `C` | An AI-enabled NAT Router/Firewall for the ESP32 |
| [**future-agi/future-agi**](https://github.com/future-agi/future-agi) | 2,254 | `Python` | Open-source, end-to-end platform for evaluating, observing, and improving LLM and AI agent applications. Tracing · Ev... |
| [**crshdn/mission-control**](https://github.com/crshdn/mission-control) | 2,159 | `TypeScript` | The world's first Autonomous Product Engine (APE): AI agents research your market, generate features, and ship code a... |
| [**gege-circle/.github**](https://github.com/gege-circle/.github) | 2,082 | `N/A` | 这里是GitHub的草场，也是戈戈圈爱好者的交流地，主要讨论动漫、游戏、科技、人文、生活等所有话题，欢迎各位小伙伴们在此讨论趣事。This is GitHub grassland, and the community place fo... |
| [**open-compress/claw-compactor**](https://github.com/open-compress/claw-compactor) | 2,004 | `Python` | 14-stage Fusion Pipeline for LLM token compression — reversible compression, AST-aware code analysis, intelligent con... |
| [**aimod-cc/Agent2API**](https://github.com/aimod-cc/Agent2API) | 1,995 | `Rust` | Local AI routing gateway with Agent client takeover — reuse existing client logins, call 50+ AI clients through one b... |
| [**TimefoldAI/timefold-solver**](https://github.com/TimefoldAI/timefold-solver) | 1,858 | `Java` | The open source Solver AI for Java and Kotlin to optimize scheduling and routing. Solve the vehicle routing problem, ... |
| [**APIParkLab/APIPark**](https://github.com/APIParkLab/APIPark) | 1,825 | `TypeScript` | Cloud native, ultra-high performance AI&API gateway, LLM API management, distribution system, open platform, supporti... |
| [**vercel-labs/coding-agent-template**](https://github.com/vercel-labs/coding-agent-template) | 1,798 | `TypeScript` | Multi-agent AI coding platform powered by Vercel Sandbox and AI Gateway |
| [**mithun50/openclaw-termux**](https://github.com/mithun50/openclaw-termux) | 1,744 | `Dart` | Run OpenClaw AI Gateway on Android — standalone Flutter app with built-in terminal, web dashboard, and one-tap setup.... |
| [**theopenco/llmgateway**](https://github.com/theopenco/llmgateway) | 1,729 | `TypeScript` | Route, manage, and analyze your LLM requests across multiple providers with a unified API interface. |
| [**Safe3/uusec-waf**](https://github.com/Safe3/uusec-waf) | 1,720 | `Shell` | Industry-leading free, high-performance, AI and semantic technology Web Application Firewall and API Security Gateway... |
| [**NVIDIA/Personal-AI-Router**](https://github.com/NVIDIA/Personal-AI-Router) | 1,720 | `Go` | Router that virtually distributes inference across connected devices in the home. |
| [**awtkns/fastapi-crudrouter**](https://github.com/awtkns/fastapi-crudrouter) | 1,698 | `Python` | A dynamic FastAPI router that automatically creates CRUD routes for your models |
| [**DEEIX-AI/DEEIX-Chat**](https://github.com/DEEIX-AI/DEEIX-Chat) | 1,628 | `Go` | An enterprise AI workspace for model routing, multimodal chat, files, tools, billing, identity, and operations. |
| [**Paritok-official/paritok-4b-v1**](https://github.com/Paritok-official/paritok-4b-v1) | 1,443 | `Python` | Non-destructive compression gateway for AI coding agents. Cuts token bills 25% on turn 1 to past 85% in long or satur... |
| [**astaxie/TokenHub**](https://github.com/astaxie/TokenHub) | 1,427 | `Go` | TokenHub gives enterprises a private gateway to unify AI model access and governance, making every request controllab... |
| [**wouterkool/attention-learn-to-route**](https://github.com/wouterkool/attention-learn-to-route) | 1,389 | `Jupyter Notebook` | Attention based model for learning to solve different routing problems |
| [**ntegrals/10x**](https://github.com/ntegrals/10x) | 1,367 | `TypeScript` | ⚡️ 10x - Up to 20x faster AI coding with multi-step Superpowers. Open-source agent with smart model routing, BYOK, fu... |
| [**LiteLLM-Labs/litellm-agent-control-plane**](https://github.com/LiteLLM-Labs/litellm-agent-control-plane) | 1,328 | `Rust` | 1 place to call all your agents - OpenCode, Hermes, Claude Managed Agents, Cursor Agents API, DeepAgents. |
| [**kerpopule/hermes-jev-skills**](https://github.com/kerpopule/hermes-jev-skills) | 1,317 | `Python` | Jev-powered model routing, memory, compaction, skill selection, computer and browser use for Hermes agents (also Clau... |
| [**chubbyguan/chubbyskills**](https://github.com/chubbyguan/chubbyskills) | 1,313 | `Python` | 把中文全渠道内容（抖音 / B站 / 小红书 / 公众号 / X / 播客）采集进个人知识库的 14 个 AI Skill：图文存图、视频转文字稿、字幕优先免 GPU、RSS/YouTube 订阅调度与每日情报简报，附带知识库 MCP... |
| [**kellyvv/PhoneClaw**](https://github.com/kellyvv/PhoneClaw) | 1,289 | `Swift` | PhoneClaw turns phones into local AI agent runtimes with on-device models, native mobile Skills, LiveLand, and option... |
| [**fatwang2/search2ai**](https://github.com/fatwang2/search2ai) | 1,285 | `TypeScript` | Self-hosted search gateway for AI agents. Unified search, news and page extraction with provider fallback. REST API, ... |
| [**pnoker/iot-dc3**](https://github.com/pnoker/iot-dc3) | 1,266 | `Java` | IoT DC3 — Connect the Physical World to AI. An open-source Industrial IoT Runtime for Physical AI: 36 protocol driver... |
| [**modu-ai/moai-adk**](https://github.com/modu-ai/moai-adk) | 1,252 | `Go` | Agentic development harness for Claude Code — SPEC-driven plan/run/sync, TRUST 5 quality gates, model+effort routing,... |
| [**ASCIT31/Dark-Moon**](https://github.com/ASCIT31/Dark-Moon) | 1,208 | `Python` | Open-source autonomous AI penetration testing. 50 specialist agents across web, API, cloud, Active Directory, Kuberne... |
| [**shadcn-ui/chatbot-template**](https://github.com/shadcn-ui/chatbot-template) | 1,200 | `TypeScript` | A minimal chatbot template built with Next.js, AI SDK, shadcn/ui, shadcn/react, shadcn/typeset. It runs on the Vercel... |
| [**fsbolero/Bolero**](https://github.com/fsbolero/Bolero) | 1,139 | `F#` | Bolero brings Blazor to F# developers with an easy to use Model-View-Update architecture, HTML combinators, hot reloa... |
| [**caozhiyuan/copilot-api**](https://github.com/caozhiyuan/copilot-api) | 1,113 | `TypeScript` | GitHub Copilot, OpenAI Codex, OpenCode Go, and third-party AI provider gateway with OpenAI and Anthropic API compatib... |
| [**kittors/CliRelay**](https://github.com/kittors/CliRelay) | 1,051 | `Go` | Self-hosted AI gateway for coding CLIs — one OpenAI/Claude/Gemini/Codex-compatible endpoint, with a multi-tenant web ... |
| [**w8123/EnterpriseAgentFramework**](https://github.com/w8123/EnterpriseAgentFramework) | 1,044 | `Java` | ReachAI企业级智能体开发平台：快速、安全完成已有业务系统智能化改造，让 AI 在 OA、ERP、CRM 等原系统中查数据、填表单、办业务。ReachAI: Quickly and securely bring AI to exi... |
| [**agentic-community/mcp-gateway-registry**](https://github.com/agentic-community/mcp-gateway-registry) | 1,038 | `Python` | Enterprise-ready MCP Gateway & Registry that centralizes AI development tools with secure OAuth authentication, dynam... |
| [**beizhu-1209/AIHelms**](https://github.com/beizhu-1209/AIHelms) | 1,032 | `Python` | 企业级 AI 资源纳管平台，提供统一 AI网关、Token调度能力，纳管 OpenAI、Azure、Claude、DeepSeek 等主流模型，并支持 MCP 工具与 Skill 的集中注册分发。具备内外双轨定价、成本归因、统一身份认... |
| [**Azure-Samples/AI-Gateway**](https://github.com/Azure-Samples/AI-Gateway) | 1,008 | `Jupyter Notebook` | Labs to explore AI Models, MCP servers, and Agents with the AI Gateway powered by Azure API Management and Microsoft ... |

---

## ⚖️ LLM Proxy & Load Balancing

> Proxy servers and load balancers specifically designed for LLM API traffic management.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**QuantumNous/new-api**](https://github.com/QuantumNous/new-api) | 51,534 | `Go` | Open-source AI gateway. Self-hosted LLM gateway with OpenAI-, Claude- and Gemini-compatible APIs, model routing, acce... |
| [**lidge-jun/opencodex**](https://github.com/lidge-jun/opencodex) | 18,282 | `TypeScript` | Universal provider proxy for OpenAI Codex & Claude Code — use any LLM (Claude, Gemini, Grok, DeepSeek, Ollama…) with ... |
| [**Portkey-AI/gateway**](https://github.com/Portkey-AI/gateway) | 13,339 | `TypeScript` | A blazing fast AI Gateway with integrated guardrails. Route to 1,600+ LLMs, 50+ AI Guardrails with 1 fast & friendly ... |
| [**coaidev/coai**](https://github.com/coaidev/coai) | 9,343 | `TypeScript` | 🚀 Next Gen Multi-tenant AI One-Stop Solution. Builtin Admin & Billing System. Enterprise-Grade Unified LLM Gateway Su... |

---

## ⚡ Inference Serving Engines

> High-performance inference engines that serve LLM models with built-in routing and scheduling capabilities.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**ollama/ollama**](https://github.com/ollama/ollama) | 186,239 | `Go` | Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models. |
| [**vllm-project/vllm**](https://github.com/vllm-project/vllm) | 96,513 | `Python` | A high-throughput and memory-efficient inference and serving engine for LLMs |
| [**sgl-project/sglang**](https://github.com/sgl-project/sglang) | 38,556 | `Python` | SGLang is a high-performance serving framework for large language models and multimodal models. |
| [**GeeeekExplorer/nano-vllm**](https://github.com/GeeeekExplorer/nano-vllm) | 16,337 | `Python` | Nano vLLM |
| [**NVIDIA/TensorRT-LLM**](https://github.com/NVIDIA/TensorRT-LLM) | 15,033 | `Python` | TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and supports state-... |
| [**vllm-project/vllm-omni**](https://github.com/vllm-project/vllm-omni) | 7,603 | `Python` | A framework for efficient model inference with omni-modality models |
| [**vllm-project/semantic-router**](https://github.com/vllm-project/semantic-router) | 6,415 | `Go` | An open, programmable decision layer for models and compute. |
| [**sgl-project/mini-sglang**](https://github.com/sgl-project/mini-sglang) | 5,533 | `Python` | A compact implementation of SGLang, designed to demystify the complexities of modern LLM serving systems. |
| [**vllm-project/aibrix**](https://github.com/vllm-project/aibrix) | 5,182 | `Go` | Cost-efficient and pluggable Infrastructure components for GenAI inference |
| [**vllm-project/llm-compressor**](https://github.com/vllm-project/llm-compressor) | 3,951 | `Python` | State-of-the-art LLM compression, built for production inference with vLLM |
| [**vllm-project/vllm-ascend**](https://github.com/vllm-project/vllm-ascend) | 3,057 | `Python` | Community maintained hardware plugin for vLLM on Huawei Ascend |
| [**vllm-project/guidellm**](https://github.com/vllm-project/guidellm) | 1,760 | `Python` | Evaluate and Enhance Your LLM Deployments for Real-World Inference Needs |
| [**datawhalechina/zero-to-sglang**](https://github.com/datawhalechina/zero-to-sglang) | 1,735 | `Python` | Official SGLang x Datawhale course on LLM inference: understand inference, build a mini-sglang from scratch, then rea... |
| [**sgl-project/sglang-omni**](https://github.com/sgl-project/sglang-omni) | 1,710 | `Python` | High Performance Serving Runtime For Interactive Super Intelligence System |
| [**waybarrios/vllm-mlx**](https://github.com/waybarrios/vllm-mlx) | 1,650 | `Python` | High-performance OpenAI and Anthropic compatible LLM inference server for Apple Silicon. Native MLX, continuous batch... |
| [**1CatAI/1Cat-vLLM**](https://github.com/1CatAI/1Cat-vLLM) | 1,477 | `Python` | V100 / SM70-focused vLLM engineering fork for modern LLM inference. |
| [**Ksuriuri/index-tts-vllm**](https://github.com/Ksuriuri/index-tts-vllm) | 1,245 | `Python` | Added vLLM support to IndexTTS for faster inference. |
| [**weicj/vLLM-2080Ti-Definitive**](https://github.com/weicj/vLLM-2080Ti-Definitive) | 1,206 | `Python` | The definitive vLLM runtime for dual RTX 2080 Ti 22GB + NVLink, delivering Qwen 27B local inference with maximum 200+... |
| [**jmaczan/tiny-vllm**](https://github.com/jmaczan/tiny-vllm) | 1,184 | `C++` | Build your own high performance LLM inference engine in C++ and CUDA - a smaller version of vLLM |

---

## 🎭 LLM Orchestration Frameworks

> Frameworks for orchestrating multiple LLMs with routing, pipeline, and workflow capabilities.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**musistudio/claude-code-router**](https://github.com/musistudio/claude-code-router) | 38,032 | `TypeScript` | One local control plane for every AI agent: route across models, fuse new capabilities, orchestrate tools, and stay f... |
| [**deepset-ai/haystack**](https://github.com/deepset-ai/haystack) | 26,941 | `Python` | Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design mod... |
| [**rocketride-org/rocketride-server**](https://github.com/rocketride-org/rocketride-server) | 20,020 | `Python` | High-performance AI pipeline engine with a C++ core and 50+ Python-extensible nodes. Build, debug, and scale LLM work... |
| [**neuml/txtai**](https://github.com/neuml/txtai) | 13,081 | `Python` | 💡 All-in-one AI framework for semantic search, LLM orchestration and language model workflows |
| [**katanemo/plano**](https://github.com/katanemo/plano) | 7,110 | `Rust` | Plano is an AI-native proxy server and data plane for agentic apps. Smart LLM routing, observability, agent orchestra... |
| [**IBM/mcp-context-forge**](https://github.com/IBM/mcp-context-forge) | 4,767 | `Python` | An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, or REST/gRPC APIs, exposing a unified endpoint... |
| [**archestra-ai/archestra**](https://github.com/archestra-ai/archestra) | 4,434 | `TypeScript` | Enterprise AI Platform with guardrails, MCP registry, gateway & orchestrator |
| [**foryourhealth111-pixel/Vibe-Skills**](https://github.com/foryourhealth111-pixel/Vibe-Skills) | 3,805 | `Python` | Intelligent Skill routing and workflow orchestration for AI agents — +21.12 pp reward, −29.6% tokens on SkillsBench w... |
| [**zhnt/loushang**](https://github.com/zhnt/loushang) | 1,999 | `Python` | AI-native agent harness for coding workflows by python: multi-model LLM orchestration, stateful sessions, tool govern... |
| [**AI-QL/tuui**](https://github.com/AI-QL/tuui) | 1,159 | `TypeScript` | A desktop MCP client designed as a tool unitary utility integration, accelerating AI adoption through the Model Conte... |
| [**proinsight-io/crewmeld**](https://github.com/proinsight-io/crewmeld) | 1,093 | `TypeScript` | CrewMeld — Enterprise AI Digital Workforce Platform. Manage AI employees like real team members. Visual SOP orchestra... |
| [**Zyrexnn/Cybermes**](https://github.com/Zyrexnn/Cybermes) | 1,007 | `Python` | Autonomous Offensive Security, Bug Bounty & Red Teaming Agent Framework powered by Hermes Agent, specialized reasonin... |
| [**DemonDamon/AgenticX**](https://github.com/DemonDamon/AgenticX) | 1,005 | `Python` | AgenticX is a unified, production-ready multi-agent platform — Python SDK + CLI (agx) + Studio server + Machi desktop... |

---

## 📡 API Management & Distribution

> Platforms for managing, distributing, and monitoring LLM API access across teams and applications.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**casdoor/casdoor**](https://github.com/casdoor/casdoor) | 14,779 | `Go` | An open-source Agent-first Identity and Access Management (IAM) /LLM MCP & agent gateway and auth server with web UI ... |
| [**InsForge/InsForge**](https://github.com/InsForge/InsForge) | 13,302 | `TypeScript` | The all-in-one, open-source backend platform for agentic coding. InsForge gives your coding agent database, auth, sto... |

---

## 💰 Cost Optimization & Observability

> Tools focused on reducing LLM costs through smart routing, caching, token optimization, and observability.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**langwatch/langwatch**](https://github.com/langwatch/langwatch) | 5,017 | `TypeScript` | Open-Source Agent Observability & Evals for AI Platform teams. Trace, test, route and govern every agent & coding ass... |
| [**seakee/CPA-Manager-Plus**](https://github.com/seakee/CPA-Manager-Plus) | 4,041 | `Go` | A self-hosted CPA / CLIProxyAPI management panel and AI gateway observability dashboard for requests, usage, cost, qu... |
| [**ascending-llc/jarvis-registry**](https://github.com/ascending-llc/jarvis-registry) | 3,842 | `Python` | Connect any AI copilot or autonomous agent to your enterprise tools — through a single, secure MCP/Agent gateway with... |
| [**aklivity/zilla**](https://github.com/aklivity/zilla) | 1,690 | `Java` | 🦎 A lightweight, streaming-native, multi-protocol gateway for AI, APIs, and real-time data. Route LLM requests across... |
| [**bricks-cloud/BricksLLM**](https://github.com/bricks-cloud/BricksLLM) | 1,232 | `Go` | 🔒 Enterprise-grade API gateway that helps you monitor and impose cost or rate limits per API key. Get fine-grained ac... |
| [**jzyong/game-server**](https://github.com/jzyong/game-server) | 1,228 | `Java` | Distributed Java game server, including cluster management server, gateway server, hall server, game logic server, ba... |

---

## 🔬 Research & Benchmarks

> Academic research papers, frameworks, and benchmarks related to LLM routing strategies.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|

---

## Stats

- **Total repositories**: 129
- **Minimum stars**: 1,000
- **Languages covered**: C, C++, Dart, F#, Go, HTML, Java, JavaScript, Jupyter Notebook, Lua, PowerShell, Python, Rust, Shell, Swift, TypeScript
- **Last updated**: 2026-11-07

### Top 10 by Stars

| Rank | Repository | Stars |
|------|-----------|-------|
| 1 | [ollama/ollama](https://github.com/ollama/ollama) | 186,239 |
| 2 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | 96,513 |
| 3 | [cheaper-inference/OmniRoute](https://github.com/cheaper-inference/OmniRoute) | 85,340 |
| 4 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | 62,868 |
| 5 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | 51,534 |
| 6 | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | 48,680 |
| 7 | [Kong/kong](https://github.com/Kong/kong) | 44,365 |
| 8 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | 44,268 |
| 9 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | 38,556 |
| 10 | [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) | 38,032 |

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
