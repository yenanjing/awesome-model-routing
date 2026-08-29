<div align="center">
  <h1>Awesome Model Routing</h1>
  <p>A curated list of awesome LLM/AI model routing frameworks, gateways, inference engines, and tools.</p>

  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
  ![GitHub stars](https://img.shields.io/github/stars/yenanjing/awesome-model-routing?style=flat-square)
  ![Last Updated](https://img.shields.io/badge/last%20updated-2026-08-29-blue?style=flat-square)

  <p>Collected <strong>98</strong> repositories with <strong>1,000+</strong> stars across <strong>8</strong> categories.</p>
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
> Last updated: 2026-08-29

---

## 🧠 LLM Routers & Smart Routing

> Tools that intelligently route LLM requests to different models based on cost, quality, complexity, or latency.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**tashfeenahmed/freellmapi**](https://github.com/tashfeenahmed/freellmapi) | 21,972 | `TypeScript` | 7.4 billion tokens per month. 34 free LLM providers. 635 free model endpoints. All behind one /v1 endpoint, plus any ... |
| [**justlovemaki/AIClient2API**](https://github.com/justlovemaki/AIClient2API) | 8,702 | `JavaScript` | Self-hosted multi-protocol AI API proxy for Antigravity, Codex, Grok, Kiro, OpenAI, Claude, and custom providers. Sup... |
| [**mnfst/manifest**](https://github.com/mnfst/manifest) | 7,484 | `TypeScript` | Connect Your Agents And Harnesses With Any Provider 🦚 |
| [**BlockRunAI/ClawRouter**](https://github.com/BlockRunAI/ClawRouter) | 6,575 | `TypeScript` | The agent-native LLM router for autonomous agents. Every frontier model behind one wallet, <1ms local routing, USDC p... |
| [**lm-sys/RouteLLM**](https://github.com/lm-sys/RouteLLM) | 5,414 | `Python` | A framework for serving and evaluating LLM routers - save LLM costs without compromising quality |
| [**ENTERPILOT/GoModel**](https://github.com/ENTERPILOT/GoModel) | 1,096 | `Go` | AI gateway / AI control plane / AI proxy written in Go. Unified OpenAI-compatible and Anthropic-compatible API for Op... |

---

## 🚪 AI Gateways & Unified APIs

> Unified API gateways that provide a single interface to access multiple LLM providers with routing, failover, and load balancing.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**diegosouzapw/OmniRoute**](https://github.com/diegosouzapw/OmniRoute) | 57,857 | `TypeScript` | Never stop coding. Free MIT AI gateway: one endpoint, 350 providers (90+ free), 1200+ models Kimi, Claude, GPT, Gemin... |
| [**BerriAI/litellm**](https://github.com/BerriAI/litellm) | 57,527 | `Python` | The fastest, litest AI Gateway. Rust core with Python SDK. Call 100+ LLM APIs in OpenAI (or native) format with cost ... |
| [**Kong/kong**](https://github.com/Kong/kong) | 44,057 | `Lua` | 🦍 The API and AI Gateway |
| [**zhaoxuya520/reverse-skill**](https://github.com/zhaoxuya520/reverse-skill) | 30,308 | `PowerShell` | Reverse Engineering / Authorized Penetration Testing / Security Research Skill Router Pack AI-powered routing + On-de... |
| [**decolua/9router**](https://github.com/decolua/9router) | 26,605 | `JavaScript` | Unlimited FREE AI coding. Connect Claude Code, Codex, Cursor, Cline, Copilot, Antigravity to FREE Claude/GPT/Gemini v... |
| [**mksglu/context-mode**](https://github.com/mksglu/context-mode) | 20,241 | `TypeScript` | Context window optimization for AI coding agents. Sandboxes tool output (98% reduction), persists session memory, and... |
| [**apache/apisix**](https://github.com/apache/apisix) | 17,050 | `Lua` | The Cloud-Native API Gateway and AI Gateway |
| [**higress-group/higress**](https://github.com/higress-group/higress) | 9,236 | `Go` | 🤖 AI Gateway \| AI Native API Gateway |
| [**maximhq/bifrost**](https://github.com/maximhq/bifrost) | 7,639 | `Go` | Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ ... |
| [**kgateway-dev/kgateway**](https://github.com/kgateway-dev/kgateway) | 5,676 | `Go` | The Cloud-Native API Gateway and AI Gateway |
| [**oomol-lab/open-connector**](https://github.com/oomol-lab/open-connector) | 5,400 | `TypeScript` | Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI. |
| [**looplj/axonhub**](https://github.com/looplj/axonhub) | 5,122 | `Go` | ⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, cost control & end-to-e... |
| [**AgnesAI-Labs/AgnesAI-Models**](https://github.com/AgnesAI-Labs/AgnesAI-Models) | 5,016 | `N/A` | Official Agnes AI gateway and model catalog for OpenAI-compatible text, image, video, and agent workflows. |
| [**agentgateway/agentgateway**](https://github.com/agentgateway/agentgateway) | 4,633 | `Rust` | Next Generation Agentic Proxy for AI Agents and MCP servers |
| [**NateBJones-Projects/OB1**](https://github.com/NateBJones-Projects/OB1) | 4,522 | `TypeScript` | Open Brain — The infrastructure layer for your thinking. One database, one AI gateway, one chat channel — any AI plug... |
| [**octelium/octelium**](https://github.com/octelium/octelium) | 4,029 | `Go` | A next-gen FOSS self-hosted unified zero trust secure access platform that can operate as a remote access VPN, a ZTNA... |
| [**nextlevelbuilder/goclaw**](https://github.com/nextlevelbuilder/goclaw) | 3,578 | `Go` | GoClaw - GoClaw is OpenClaw rebuilt in Go — with multi-tenant isolation, 5-layer security, and native concurrency. De... |
| [**raullenchai/Rapid-MLX**](https://github.com/raullenchai/Rapid-MLX) | 3,564 | `Python` | The fastest local AI engine for Apple Silicon. 4.2x faster than Ollama, 0.08s cached TTFT, 100% tool calling. 17 tool... |
| [**butterbase-ai/butterbase**](https://github.com/butterbase-ai/butterbase) | 3,310 | `TypeScript` | Open-source backend-as-a-service. Postgres, auth, storage, functions, AI gateway, MCP. |
| [**cirosantilli/china-dictatorship**](https://github.com/cirosantilli/china-dictatorship) | 3,172 | `HTML` | 反中共政治宣传库。Anti Chinese government propaganda. 住在中国真名用户的网友请别给星星，不然你要被警察请喝茶。常见问答集，新闻集和饭店和音乐建议。卐习万岁卐。冠状病毒审查郝海东新疆改造中心六四事件法... |
| [**motiful/cc-gateway**](https://github.com/motiful/cc-gateway) | 3,016 | `TypeScript` | AI API identity gateway — reverse proxy that normalizes device fingerprints and telemetry for privacy-preserving API ... |
| [**duolahypercho/codex-router**](https://github.com/duolahypercho/codex-router) | 2,973 | `JavaScript` | External-model router for Codex with guided Kimi OAuth/API, DeepSeek, safe migration, and rollback. |
| [**kaitranntt/ccs**](https://github.com/kaitranntt/ccs) | 2,832 | `TypeScript` | Switch between Claude accounts, Gemini, Copilot, OpenRouter (300+ models) via CLIProxyAPI OAuth proxy. Visual dashboa... |
| [**supercorp-ai/supergateway**](https://github.com/supercorp-ai/supergateway) | 2,823 | `TypeScript` | Run MCP stdio servers over SSE and SSE over stdio. AI gateway. |
| [**fuxicodex/Fuxi**](https://github.com/fuxicodex/Fuxi) | 2,688 | `Python` | FuXi is a fast, self-contained AI coding agent that lives in your terminal — edit code, run commands, and drive tools... |
| [**krakend/krakend-ce**](https://github.com/krakend/krakend-ce) | 2,668 | `Go` | KrakenD Community Edition: High-performance, stateless, declarative, API Gateway written in Go. |
| [**ulab-uiuc/LLMRouter**](https://github.com/ulab-uiuc/LLMRouter) | 2,633 | `Python` | LLMRouter: An Open-Source Library for LLM Routing |
| [**wang2122/sprix-sage-router**](https://github.com/wang2122/sprix-sage-router) | 2,624 | `Python` | Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks. |
| [**NVIDIA-NeMo/Switchyard**](https://github.com/NVIDIA-NeMo/Switchyard) | 2,563 | `Python` | Switchyard lets LLM applications route traffic across models and providers while preserving native OpenAI and Anthrop... |
| [**bestruirui/octopus**](https://github.com/bestruirui/octopus) | 2,558 | `TypeScript` | One Hub All LLMs For You \| 为个人打造的 LLM API 聚合网关 |
| [**workweave/router**](https://github.com/workweave/router) | 2,532 | `Go` | Model router for agentic systems. Routes every prompt to the right model in <50ms. Cut costs 40-70% with just an endp... |
| [**techa03/goodsKill**](https://github.com/techa03/goodsKill) | 2,426 | `Java` | 🐎基于SpringCloud 2025.x + Dubbo 3.x + AI构建的模拟秒杀微服务项目，集成了Elasticsearch🔍、Gateway、Mybatis-Plus、Sharding-JDBC等常用开源组件 |
| [**crshdn/mission-control**](https://github.com/crshdn/mission-control) | 2,136 | `TypeScript` | The world's first Autonomous Product Engine (APE): AI agents research your market, generate features, and ship code a... |
| [**martin-ger/esp32_nat_router**](https://github.com/martin-ger/esp32_nat_router) | 2,135 | `C` | An AI-enabled NAT Router/Firewall for the ESP32 |
| [**open-compress/claw-compactor**](https://github.com/open-compress/claw-compactor) | 2,032 | `Python` | 14-stage Fusion Pipeline for LLM token compression — reversible compression, AST-aware code analysis, intelligent con... |
| [**gege-circle/.github**](https://github.com/gege-circle/.github) | 1,987 | `N/A` | 这里是GitHub的草场，也是戈戈圈爱好者的交流地，主要讨论动漫、游戏、科技、人文、生活等所有话题，欢迎各位小伙伴们在此讨论趣事。This is GitHub grassland, and the community place fo... |
| [**envoyproxy/ai-gateway**](https://github.com/envoyproxy/ai-gateway) | 1,974 | `Go` | Manages Unified Access to Generative AI Services built on Envoy Gateway |
| [**future-agi/future-agi**](https://github.com/future-agi/future-agi) | 1,867 | `Python` | Open-source, end-to-end platform for evaluating, observing, and improving LLM and AI agent applications. Tracing · Ev... |
| [**APIParkLab/APIPark**](https://github.com/APIParkLab/APIPark) | 1,804 | `TypeScript` | Cloud native, ultra-high performance AI&API gateway, LLM API management, distribution system, open platform, supporti... |
| [**vercel-labs/coding-agent-template**](https://github.com/vercel-labs/coding-agent-template) | 1,772 | `TypeScript` | Multi-agent AI coding platform powered by Vercel Sandbox and AI Gateway |
| [**TimefoldAI/timefold-solver**](https://github.com/TimefoldAI/timefold-solver) | 1,770 | `Java` | The open source Solver AI for Java and Kotlin to optimize scheduling and routing. Solve the vehicle routing problem, ... |
| [**Safe3/uusec-waf**](https://github.com/Safe3/uusec-waf) | 1,704 | `Shell` | Industry-leading free, high-performance, AI and semantic technology Web Application Firewall and API Security Gateway... |
| [**awtkns/fastapi-crudrouter**](https://github.com/awtkns/fastapi-crudrouter) | 1,696 | `Python` | A dynamic FastAPI router that automatically creates CRUD routes for your models |
| [**mithun50/openclaw-termux**](https://github.com/mithun50/openclaw-termux) | 1,692 | `Dart` | Run OpenClaw AI Gateway on Android — standalone Flutter app with built-in terminal, web dashboard, and one-tap setup.... |
| [**theopenco/llmgateway**](https://github.com/theopenco/llmgateway) | 1,586 | `TypeScript` | Route, manage, and analyze your LLM requests across multiple providers with a unified API interface. |
| [**Paritok-official/paritok-4b-v1**](https://github.com/Paritok-official/paritok-4b-v1) | 1,447 | `Python` | Non-destructive compression gateway for AI coding agents. Cuts token bills 25% on turn 1 to past 85% in long or satur... |
| [**DEEIX-AI/DEEIX-Chat**](https://github.com/DEEIX-AI/DEEIX-Chat) | 1,395 | `Go` | An enterprise AI workspace for model routing, multimodal chat, files, tools, billing, identity, and operations. |
| [**wouterkool/attention-learn-to-route**](https://github.com/wouterkool/attention-learn-to-route) | 1,383 | `Jupyter Notebook` | Attention based model for learning to solve different routing problems |
| [**ntegrals/10x**](https://github.com/ntegrals/10x) | 1,361 | `TypeScript` | ⚡️ 10x - Up to 20x faster AI coding with multi-step Superpowers. Open-source agent with smart model routing, BYOK, fu... |
| [**LiteLLM-Labs/litellm-agent-control-plane**](https://github.com/LiteLLM-Labs/litellm-agent-control-plane) | 1,239 | `Rust` | 1 place to call all your agents - OpenCode, Hermes, Claude Managed Agents, Cursor Agents API, DeepAgents. |
| [**kellyvv/PhoneClaw**](https://github.com/kellyvv/PhoneClaw) | 1,225 | `Swift` | PhoneClaw turns phones into local AI agent runtimes with on-device models, native mobile Skills, LiveLand, and option... |
| [**astaxie/TokenHub**](https://github.com/astaxie/TokenHub) | 1,203 | `Go` | TokenHub gives enterprises a private gateway to unify AI model access and governance, making every request controllab... |
| [**modu-ai/moai-adk**](https://github.com/modu-ai/moai-adk) | 1,191 | `Go` | Agentic development harness for Claude Code — SPEC-driven plan/run/sync, TRUST 5 quality gates, model+effort routing,... |
| [**fsbolero/Bolero**](https://github.com/fsbolero/Bolero) | 1,131 | `F#` | Bolero brings Blazor to F# developers with an easy to use Model-View-Update architecture, HTML combinators, hot reloa... |
| [**beizhu-1209/AIHelms**](https://github.com/beizhu-1209/AIHelms) | 1,023 | `Python` | 企业级 AI 资源纳管平台，提供统一 AI网关、Token调度能力，纳管 OpenAI、Azure、Claude、DeepSeek 等主流模型，并支持 MCP 工具与 Skill 的集中注册分发。具备内外双轨定价、成本归因、统一身份认... |

---

## ⚖️ LLM Proxy & Load Balancing

> Proxy servers and load balancers specifically designed for LLM API traffic management.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**QuantumNous/new-api**](https://github.com/QuantumNous/new-api) | 46,730 | `Go` | A unified AI model hub for aggregation & distribution. It supports cross-converting various LLMs into OpenAI-compatib... |
| [**Portkey-AI/gateway**](https://github.com/Portkey-AI/gateway) | 12,852 | `TypeScript` | A blazing fast AI Gateway with integrated guardrails. Route to 1,600+ LLMs, 50+ AI Guardrails with 1 fast & friendly ... |
| [**lidge-jun/opencodex**](https://github.com/lidge-jun/opencodex) | 12,501 | `TypeScript` | Universal provider proxy for OpenAI Codex & Claude Code — use any LLM (Claude, Gemini, Grok, DeepSeek, Ollama…) with ... |
| [**coaidev/coai**](https://github.com/coaidev/coai) | 9,297 | `TypeScript` | 🚀 Next Gen Multi-tenant AI One-Stop Solution. Builtin Admin & Billing System. Enterprise-Grade Unified LLM Gateway Su... |
| [**romgX/openrelay**](https://github.com/romgX/openrelay) | 2,292 | `TypeScript` | 几百个免费 AI 模型配额，一键接入本地项目。\| Hundreds of free AI model quotas, one-click access to local projects. |

---

## ⚡ Inference Serving Engines

> High-performance inference engines that serve LLM models with built-in routing and scheduling capabilities.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**ollama/ollama**](https://github.com/ollama/ollama) | 179,706 | `Go` | Get up and running with Kimi-K2.6, GLM-5.2, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models. |
| [**vllm-project/vllm**](https://github.com/vllm-project/vllm) | 90,386 | `Python` | A high-throughput and memory-efficient inference and serving engine for LLMs |
| [**sgl-project/sglang**](https://github.com/sgl-project/sglang) | 32,659 | `Python` | SGLang is a high-performance serving framework for large language models and multimodal models. |
| [**GeeeekExplorer/nano-vllm**](https://github.com/GeeeekExplorer/nano-vllm) | 15,213 | `Python` | Nano vLLM |
| [**NVIDIA/TensorRT-LLM**](https://github.com/NVIDIA/TensorRT-LLM) | 14,498 | `Python` | TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and supports state-... |
| [**vllm-project/vllm-omni**](https://github.com/vllm-project/vllm-omni) | 6,453 | `Python` | A framework for efficient model inference with omni-modality models |
| [**vllm-project/semantic-router**](https://github.com/vllm-project/semantic-router) | 5,399 | `Go` | A programmable Mixture-of-Models router for heterogeneous LLM inference |
| [**vllm-project/aibrix**](https://github.com/vllm-project/aibrix) | 5,043 | `Go` | Cost-efficient and pluggable Infrastructure components for GenAI inference |
| [**sgl-project/mini-sglang**](https://github.com/sgl-project/mini-sglang) | 4,898 | `Python` | A compact implementation of SGLang, designed to demystify the complexities of modern LLM serving systems. |
| [**vllm-project/vllm-ascend**](https://github.com/vllm-project/vllm-ascend) | 2,730 | `C++` | Community maintained hardware plugin for vLLM on Ascend |
| [**vllm-project/guidellm**](https://github.com/vllm-project/guidellm) | 1,553 | `Python` | Evaluate and Enhance Your LLM Deployments for Real-World Inference Needs |
| [**waybarrios/vllm-mlx**](https://github.com/waybarrios/vllm-mlx) | 1,551 | `Python` | High-performance OpenAI and Anthropic compatible LLM inference server for Apple Silicon. Native MLX, continuous batch... |
| [**Ksuriuri/index-tts-vllm**](https://github.com/Ksuriuri/index-tts-vllm) | 1,235 | `Python` | Added vLLM support to IndexTTS for faster inference. |
| [**jmaczan/tiny-vllm**](https://github.com/jmaczan/tiny-vllm) | 1,079 | `C++` | Build your own high performance LLM inference engine in C++ and CUDA - a smaller version of vLLM |

---

## 🎭 LLM Orchestration Frameworks

> Frameworks for orchestrating multiple LLMs with routing, pipeline, and workflow capabilities.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**musistudio/claude-code-router**](https://github.com/musistudio/claude-code-router) | 36,959 | `TypeScript` | One local control plane for every AI agent: route across models, fuse new capabilities, orchestrate tools, and stay f... |
| [**deepset-ai/haystack**](https://github.com/deepset-ai/haystack) | 26,354 | `Python` | Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design mod... |
| [**neuml/txtai**](https://github.com/neuml/txtai) | 12,912 | `Python` | 💡 All-in-one AI framework for semantic search, LLM orchestration and language model workflows |
| [**rocketride-org/rocketride-server**](https://github.com/rocketride-org/rocketride-server) | 7,370 | `Python` | High-performance AI pipeline engine with a C++ core and 50+ Python-extensible nodes. Build, debug, and scale LLM work... |
| [**katanemo/plano**](https://github.com/katanemo/plano) | 7,021 | `Rust` | Plano is an AI-native proxy server and data plane for agentic apps. Smart LLM routing, observability, agent orchestra... |
| [**open-multi-agent/open-multi-agent**](https://github.com/open-multi-agent/open-multi-agent) | 6,839 | `TypeScript` | TypeScript AI agent orchestration framework with dynamic workflows. Describe the goal, not the graph: a coordinator p... |
| [**IBM/mcp-context-forge**](https://github.com/IBM/mcp-context-forge) | 4,386 | `Python` | An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, or REST/gRPC APIs, exposing a unified endpoint... |
| [**archestra-ai/archestra**](https://github.com/archestra-ai/archestra) | 4,235 | `TypeScript` | Enterprise AI Platform with guardrails, MCP registry, gateway & orchestrator |
| [**zhnt/loushang**](https://github.com/zhnt/loushang) | 1,277 | `Python` | AI-native agent harness for coding workflows by python: multi-model LLM orchestration, stateful sessions, tool govern... |
| [**AI-QL/tuui**](https://github.com/AI-QL/tuui) | 1,152 | `TypeScript` | A desktop MCP client designed as a tool unitary utility integration, accelerating AI adoption through the Model Conte... |

---

## 📡 API Management & Distribution

> Platforms for managing, distributing, and monitoring LLM API access across teams and applications.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**casdoor/casdoor**](https://github.com/casdoor/casdoor) | 14,290 | `Go` | An open-source Agent-first Identity and Access Management (IAM) /LLM MCP & agent gateway and auth server with web UI ... |
| [**InsForge/InsForge**](https://github.com/InsForge/InsForge) | 12,811 | `TypeScript` | The all-in-one, open-source backend platform for agentic coding. InsForge gives your coding agent database, auth, sto... |
| [**mnfst/awesome-free-llm-apis**](https://github.com/mnfst/awesome-free-llm-apis) | 7,183 | `JavaScript` | List of Permanent Free LLM API  (API Keys) |

---

## 💰 Cost Optimization & Observability

> Tools focused on reducing LLM costs through smart routing, caching, token optimization, and observability.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**seakee/CPA-Manager-Plus**](https://github.com/seakee/CPA-Manager-Plus) | 2,942 | `Go` | A self-hosted CPA / CLIProxyAPI management panel and AI gateway observability dashboard for requests, usage, cost, qu... |
| [**ascending-llc/jarvis-registry**](https://github.com/ascending-llc/jarvis-registry) | 2,769 | `Python` | Connect any AI copilot or autonomous agent to your enterprise tools — through a single, secure MCP/Agent gateway with... |
| [**aklivity/zilla**](https://github.com/aklivity/zilla) | 1,716 | `Java` | 🦎 A lightweight, multi-protocol gateway for event-driven applications and AI agents. Expose and govern Kafka, MQTT, A... |
| [**bricks-cloud/BricksLLM**](https://github.com/bricks-cloud/BricksLLM) | 1,229 | `Go` | 🔒 Enterprise-grade API gateway that helps you monitor and impose cost or rate limits per API key. Get fine-grained ac... |
| [**jzyong/game-server**](https://github.com/jzyong/game-server) | 1,228 | `Java` | Distributed Java game server, including cluster management server, gateway server, hall server, game logic server, ba... |

---

## 🔬 Research & Benchmarks

> Academic research papers, frameworks, and benchmarks related to LLM routing strategies.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|

---

## Stats

- **Total repositories**: 98
- **Minimum stars**: 1,000
- **Languages covered**: C, C++, Dart, F#, Go, HTML, Java, JavaScript, Jupyter Notebook, Lua, PowerShell, Python, Rust, Shell, Swift, TypeScript
- **Last updated**: 2026-08-29

### Top 10 by Stars

| Rank | Repository | Stars |
|------|-----------|-------|
| 1 | [ollama/ollama](https://github.com/ollama/ollama) | 179,706 |
| 2 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | 90,386 |
| 3 | [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 57,857 |
| 4 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | 57,527 |
| 5 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | 46,730 |
| 6 | [Kong/kong](https://github.com/Kong/kong) | 44,057 |
| 7 | [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) | 36,959 |
| 8 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | 32,659 |
| 9 | [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | 30,308 |
| 10 | [decolua/9router](https://github.com/decolua/9router) | 26,605 |

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
