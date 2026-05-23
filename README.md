<div align="center">
  <h1>Awesome Model Routing</h1>
  <p>A curated list of awesome LLM/AI model routing frameworks, gateways, inference engines, and tools.</p>

  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
  ![GitHub stars](https://img.shields.io/github/stars/yenanjing/awesome-model-routing?style=flat-square)
  ![Last Updated](https://img.shields.io/badge/last%20updated-2026-05-23-blue?style=flat-square)

  <p>Collected <strong>75</strong> repositories with <strong>1,000+</strong> stars across <strong>8</strong> categories.</p>
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
> Last updated: 2026-05-23

---

## 🧠 LLM Routers & Smart Routing

> Tools that intelligently route LLM requests to different models based on cost, quality, complexity, or latency.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**mnfst/manifest**](https://github.com/mnfst/manifest) | 6,588 | `TypeScript` | Smart Model Routing for Agents. Cut Costs up to 70% 🦚 |
| [**BlockRunAI/ClawRouter**](https://github.com/BlockRunAI/ClawRouter) | 6,503 | `TypeScript` | The agent-native LLM router for OpenClaw. 41+ models, <1ms routing, USDC payments on Base & Solana via x402. |
| [**lm-sys/RouteLLM**](https://github.com/lm-sys/RouteLLM) | 4,931 | `Python` | A framework for serving and evaluating LLM routers - save LLM costs without compromising quality |

---

## 🚪 AI Gateways & Unified APIs

> Unified API gateways that provide a single interface to access multiple LLM providers with routing, failover, and load balancing.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**Kong/kong**](https://github.com/Kong/kong) | 43,427 | `Lua` | 🦍 The API and AI Gateway |
| [**apache/apisix**](https://github.com/apache/apisix) | 16,630 | `Lua` | The Cloud-Native API Gateway and AI Gateway |
| [**decolua/9router**](https://github.com/decolua/9router) | 13,646 | `JavaScript` | Unlimited FREE AI coding. Connect Claude Code, Codex, Cursor, Cline, Copilot, Antigravity to FREE Claude/GPT/Gemini v... |
| [**higress-group/higress**](https://github.com/higress-group/higress) | 8,452 | `Go` | 🤖 AI Gateway \| AI Native API Gateway |
| [**kgateway-dev/kgateway**](https://github.com/kgateway-dev/kgateway) | 5,527 | `Go` | The Cloud-Native API Gateway and AI Gateway |
| [**diegosouzapw/OmniRoute**](https://github.com/diegosouzapw/OmniRoute) | 5,180 | `TypeScript` | Never stop coding. Free AI gateway: one endpoint, 160+ providers (50+ free), connect Claude Code, Codex, Cursor, Clin... |
| [**maximhq/bifrost**](https://github.com/maximhq/bifrost) | 5,161 | `Go` | Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ ... |
| [**looplj/axonhub**](https://github.com/looplj/axonhub) | 3,934 | `Go` | ⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, cost control & end-to-e... |
| [**octelium/octelium**](https://github.com/octelium/octelium) | 3,822 | `Go` | A next-gen FOSS self-hosted unified zero trust secure access platform that can operate as a remote access VPN, a ZTNA... |
| [**apache/incubator-kie-optaplanner**](https://github.com/apache/incubator-kie-optaplanner) | 3,496 | `Java` | AI constraint solver in Java to optimize the vehicle routing problem, employee rostering, task assignment, maintenanc... |
| [**NateBJones-Projects/OB1**](https://github.com/NateBJones-Projects/OB1) | 3,307 | `TypeScript` | Open Brain — The infrastructure layer for your thinking. One database, one AI gateway, one chat channel — any AI plug... |
| [**nextlevelbuilder/goclaw**](https://github.com/nextlevelbuilder/goclaw) | 3,145 | `Go` | GoClaw - GoClaw is OpenClaw rebuilt in Go — with multi-tenant isolation, 5-layer security, and native concurrency. De... |
| [**cirosantilli/china-dictatorship**](https://github.com/cirosantilli/china-dictatorship) | 3,004 | `HTML` | 反中共政治宣传库。Anti Chinese government propaganda. 住在中国真名用户的网友请别给星星，不然你要被警察请喝茶。常见问答集，新闻集和饭店和音乐建议。卐习万岁卐。冠状病毒审查郝海东新疆改造中心六四事件法... |
| [**agentgateway/agentgateway**](https://github.com/agentgateway/agentgateway) | 2,840 | `Rust` | Next Generation Agentic Proxy for AI Agents and MCP servers |
| [**motiful/cc-gateway**](https://github.com/motiful/cc-gateway) | 2,804 | `TypeScript` | AI API identity gateway — reverse proxy that normalizes device fingerprints and telemetry for privacy-preserving API ... |
| [**supercorp-ai/supergateway**](https://github.com/supercorp-ai/supergateway) | 2,643 | `TypeScript` | Run MCP stdio servers over SSE and SSE over stdio. AI gateway. |
| [**krakend/krakend-ce**](https://github.com/krakend/krakend-ce) | 2,621 | `Go` | KrakenD Community Edition: High-performance, stateless, declarative, API Gateway written in Go. |
| [**dwgx/WindsurfAPI**](https://github.com/dwgx/WindsurfAPI) | 2,570 | `JavaScript` | Windsurf-to-OpenAI compatible API proxy |
| [**raullenchai/Rapid-MLX**](https://github.com/raullenchai/Rapid-MLX) | 2,411 | `Python` | The fastest local AI engine for Apple Silicon. 4.2x faster than Ollama, 0.08s cached TTFT, 100% tool calling. 17 tool... |
| [**kaitranntt/ccs**](https://github.com/kaitranntt/ccs) | 2,394 | `TypeScript` | Switch between Claude accounts, Gemini, Copilot, OpenRouter (300+ models) via CLIProxyAPI OAuth proxy. Visual dashboa... |
| [**techa03/goodsKill**](https://github.com/techa03/goodsKill) | 2,376 | `Java` | 🐎基于SpringCloud 2025.x + Dubbo 3.x + AI构建的模拟秒杀微服务项目，集成了Elasticsearch🔍、Gateway、Mybatis-Plus、Sharding-JDBC等常用开源组件 |
| [**open-compress/claw-compactor**](https://github.com/open-compress/claw-compactor) | 2,207 | `Python` | 14-stage Fusion Pipeline for LLM token compression — reversible compression, AST-aware code analysis, intelligent con... |
| [**bestruirui/octopus**](https://github.com/bestruirui/octopus) | 2,154 | `TypeScript` | One Hub All LLMs For You \| 为个人打造的 LLM API 聚合网关 |
| [**crshdn/mission-control**](https://github.com/crshdn/mission-control) | 2,051 | `TypeScript` | The world's first Autonomous Product Engine (APE): AI agents research your market, generate features, and ship code a... |
| [**martin-ger/esp32_nat_router**](https://github.com/martin-ger/esp32_nat_router) | 1,966 | `C` | An AI-enabled NAT Router/Firewall for the ESP32 |
| [**gege-circle/.github**](https://github.com/gege-circle/.github) | 1,888 | `N/A` | 这里是GitHub的草场，也是戈戈圈爱好者的交流地，主要讨论动漫、游戏、科技、人文、生活等所有话题，欢迎各位小伙伴们在此讨论趣事。This is GitHub grassland, and the community place fo... |
| [**ulab-uiuc/LLMRouter**](https://github.com/ulab-uiuc/LLMRouter) | 1,850 | `Python` | LLMRouter: An Open-Source Library for LLM Routing |
| [**APIParkLab/APIPark**](https://github.com/APIParkLab/APIPark) | 1,723 | `TypeScript` | Cloud native, ultra-high performance AI&API gateway, LLM API management, distribution system, open platform, supporti... |
| [**vercel-labs/coding-agent-template**](https://github.com/vercel-labs/coding-agent-template) | 1,712 | `TypeScript` | Multi-agent AI coding platform powered by Vercel Sandbox and AI Gateway |
| [**awtkns/fastapi-crudrouter**](https://github.com/awtkns/fastapi-crudrouter) | 1,691 | `Python` | A dynamic FastAPI router that automatically creates CRUD routes for your models |
| [**envoyproxy/ai-gateway**](https://github.com/envoyproxy/ai-gateway) | 1,676 | `Go` | Manages Unified Access to Generative AI Services built on Envoy Gateway |
| [**TimefoldAI/timefold-solver**](https://github.com/TimefoldAI/timefold-solver) | 1,661 | `Java` | The open source Solver AI for Java and Kotlin to optimize scheduling and routing. Solve the vehicle routing problem, ... |
| [**Safe3/uusec-waf**](https://github.com/Safe3/uusec-waf) | 1,654 | `Shell` | Industry-leading free, high-performance, AI and semantic technology Web Application Firewall and API Security Gateway... |
| [**mithun50/openclaw-termux**](https://github.com/mithun50/openclaw-termux) | 1,526 | `Dart` | Run OpenClaw AI Gateway on Android — standalone Flutter app with built-in terminal, web dashboard, and one-tap setup.... |
| [**wouterkool/attention-learn-to-route**](https://github.com/wouterkool/attention-learn-to-route) | 1,358 | `Jupyter Notebook` | Attention based model for learning to solve different routing problems |
| [**ntegrals/10x**](https://github.com/ntegrals/10x) | 1,351 | `TypeScript` | ⚡️ 10x - Up to 20x faster AI coding with multi-step Superpowers. Open-source agent with smart model routing, BYOK, fu... |
| [**theopenco/llmgateway**](https://github.com/theopenco/llmgateway) | 1,231 | `TypeScript` | Route, manage, and analyze your LLM requests across multiple providers with a unified API interface. |
| [**fsbolero/Bolero**](https://github.com/fsbolero/Bolero) | 1,127 | `F#` | Bolero brings Blazor to F# developers with an easy to use Model-View-Update architecture, HTML combinators, hot reloa... |
| [**future-agi/future-agi**](https://github.com/future-agi/future-agi) | 1,024 | `Python` | Open-source, end-to-end platform for evaluating, observing, and improving LLM and AI agent applications. Tracing · Ev... |

---

## ⚖️ LLM Proxy & Load Balancing

> Proxy servers and load balancers specifically designed for LLM API traffic management.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**BerriAI/litellm**](https://github.com/BerriAI/litellm) | 48,000 | `Python` | Python SDK, Proxy Server (AI Gateway) to call 100+ LLM APIs in OpenAI (or native) format, with cost tracking, guardra... |
| [**QuantumNous/new-api**](https://github.com/QuantumNous/new-api) | 34,992 | `Go` | A unified AI model hub for aggregation & distribution. It supports cross-converting various LLMs into OpenAI-compatib... |
| [**Portkey-AI/gateway**](https://github.com/Portkey-AI/gateway) | 11,826 | `TypeScript` | A blazing fast AI Gateway with integrated guardrails. Route to 1,600+ LLMs, 50+ AI Guardrails with 1 fast & friendly ... |
| [**coaidev/coai**](https://github.com/coaidev/coai) | 9,177 | `TypeScript` | 🚀 Next Gen Multi-tenant AI One-Stop Solution. Builtin Admin & Billing System. Enterprise-Grade Unified LLM Gateway Su... |
| [**romgX/openrelay**](https://github.com/romgX/openrelay) | 2,050 | `TypeScript` | 几百个免费 AI 模型配额，一键接入本地项目。\| Hundreds of free AI model quotas, one-click access to local projects. |

---

## ⚡ Inference Serving Engines

> High-performance inference engines that serve LLM models with built-in routing and scheduling capabilities.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**ollama/ollama**](https://github.com/ollama/ollama) | 172,090 | `Go` | Get up and running with Kimi-K2.5, GLM-5, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models. |
| [**vllm-project/vllm**](https://github.com/vllm-project/vllm) | 80,782 | `Python` | A high-throughput and memory-efficient inference and serving engine for LLMs |
| [**sgl-project/sglang**](https://github.com/sgl-project/sglang) | 28,142 | `Python` | SGLang is a high-performance serving framework for large language models and multimodal models. |
| [**NVIDIA/TensorRT-LLM**](https://github.com/NVIDIA/TensorRT-LLM) | 13,700 | `Python` | TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and supports state-... |
| [**GeeeekExplorer/nano-vllm**](https://github.com/GeeeekExplorer/nano-vllm) | 13,556 | `Python` | Nano vLLM |
| [**vllm-project/vllm-omni**](https://github.com/vllm-project/vllm-omni) | 4,861 | `Python` | A framework for efficient model inference with omni-modality models |
| [**vllm-project/aibrix**](https://github.com/vllm-project/aibrix) | 4,826 | `Go` | Cost-efficient and pluggable Infrastructure components for GenAI inference |
| [**sgl-project/mini-sglang**](https://github.com/sgl-project/mini-sglang) | 4,232 | `Python` | A compact implementation of SGLang, designed to demystify the complexities of modern LLM serving systems. |
| [**vllm-project/semantic-router**](https://github.com/vllm-project/semantic-router) | 4,210 | `Go` | System Level Intelligent Router for Mixture-of-Models at Cloud, Data Center and Edge |
| [**vllm-project/vllm-ascend**](https://github.com/vllm-project/vllm-ascend) | 2,128 | `C++` | Community maintained hardware plugin for vLLM on Ascend |
| [**waybarrios/vllm-mlx**](https://github.com/waybarrios/vllm-mlx) | 1,244 | `Python` | OpenAI and Anthropic compatible server for Apple Silicon. Run LLMs and vision-language models (Llama, Qwen-VL, LLaVA)... |
| [**Ksuriuri/index-tts-vllm**](https://github.com/Ksuriuri/index-tts-vllm) | 1,157 | `Python` | Added vLLM support to IndexTTS for faster inference. |
| [**vllm-project/guidellm**](https://github.com/vllm-project/guidellm) | 1,157 | `Python` | Evaluate and Enhance Your LLM Deployments for Real-World Inference Needs |

---

## 🎭 LLM Orchestration Frameworks

> Frameworks for orchestrating multiple LLMs with routing, pipeline, and workflow capabilities.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**deepset-ai/haystack**](https://github.com/deepset-ai/haystack) | 25,348 | `MDX` | Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design mod... |
| [**neuml/txtai**](https://github.com/neuml/txtai) | 12,605 | `Python` | 💡 All-in-one AI framework for semantic search, LLM orchestration and language model workflows |
| [**tensorzero/tensorzero**](https://github.com/tensorzero/tensorzero) | 11,392 | `Rust` | TensorZero is an open-source LLMOps platform that unifies an LLM gateway, observability, evaluation, optimization, an... |
| [**katanemo/plano**](https://github.com/katanemo/plano) | 6,503 | `Rust` | Plano is an AI-native proxy and data plane for agentic apps — with built-in orchestration, safety, observability, and... |
| [**abhi1693/openclaw-mission-control**](https://github.com/abhi1693/openclaw-mission-control) | 3,980 | `TypeScript` | AI Agent Orchestration Dashboard - Manage AI agents, assign tasks, and coordinate multi-agent collaboration via OpenC... |
| [**IBM/mcp-context-forge**](https://github.com/IBM/mcp-context-forge) | 3,759 | `Python` | An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, or REST/gRPC APIs, exposing a unified endpoint... |
| [**archestra-ai/archestra**](https://github.com/archestra-ai/archestra) | 3,730 | `TypeScript` | Enterprise AI Platform with guardrails, MCP registry, gateway & orchestrator |
| [**rocketride-org/rocketride-server**](https://github.com/rocketride-org/rocketride-server) | 3,278 | `C++` | High-performance AI pipeline engine with a C++ core and 50+ Python-extensible nodes. Build, debug, and scale LLM work... |
| [**AI-QL/tuui**](https://github.com/AI-QL/tuui) | 1,147 | `TypeScript` | A desktop MCP client designed as a tool unitary utility integration, accelerating AI adoption through the Model Conte... |

---

## 📡 API Management & Distribution

> Platforms for managing, distributing, and monitoring LLM API access across teams and applications.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**casdoor/casdoor**](https://github.com/casdoor/casdoor) | 13,654 | `Go` | An open-source Agent-first Identity and Access Management (IAM) /LLM MCP & agent gateway and auth server with web UI ... |
| [**InsForge/InsForge**](https://github.com/InsForge/InsForge) | 10,507 | `TypeScript` | The all-in-one, open-source backend platform for agentic coding. InsForge gives your coding agent database, auth, sto... |
| [**mnfst/awesome-free-llm-apis**](https://github.com/mnfst/awesome-free-llm-apis) | 4,490 | `JavaScript` | List of Permanent Free LLM API  (API Keys) |

---

## 💰 Cost Optimization & Observability

> Tools focused on reducing LLM costs through smart routing, caching, token optimization, and observability.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**jzyong/game-server**](https://github.com/jzyong/game-server) | 1,228 | `Java` | Distributed Java game server, including cluster management server, gateway server, hall server, game logic server, ba... |
| [**bricks-cloud/BricksLLM**](https://github.com/bricks-cloud/BricksLLM) | 1,205 | `Go` | 🔒 Enterprise-grade API gateway that helps you monitor and impose cost or rate limits per API key. Get fine-grained ac... |
| [**ascending-llc/jarvis-registry**](https://github.com/ascending-llc/jarvis-registry) | 1,012 | `Python` | Connect any AI copilot or autonomous agent to your enterprise tools — through a single, secure MCP/Agent gateway with... |

---

## 🔬 Research & Benchmarks

> Academic research papers, frameworks, and benchmarks related to LLM routing strategies.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|

---

## Stats

- **Total repositories**: 75
- **Minimum stars**: 1,000
- **Languages covered**: C, C++, Dart, F#, Go, HTML, Java, JavaScript, Jupyter Notebook, Lua, MDX, Python, Rust, Shell, TypeScript
- **Last updated**: 2026-05-23

### Top 10 by Stars

| Rank | Repository | Stars |
|------|-----------|-------|
| 1 | [ollama/ollama](https://github.com/ollama/ollama) | 172,090 |
| 2 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | 80,782 |
| 3 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | 48,000 |
| 4 | [Kong/kong](https://github.com/Kong/kong) | 43,427 |
| 5 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | 34,992 |
| 6 | [sgl-project/sglang](https://github.com/sgl-project/sglang) | 28,142 |
| 7 | [deepset-ai/haystack](https://github.com/deepset-ai/haystack) | 25,348 |
| 8 | [apache/apisix](https://github.com/apache/apisix) | 16,630 |
| 9 | [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | 13,700 |
| 10 | [casdoor/casdoor](https://github.com/casdoor/casdoor) | 13,654 |

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
