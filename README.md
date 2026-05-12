<div align="center">
  <h1>Awesome Model Routing</h1>
  <p>A curated list of awesome LLM/AI model routing frameworks, gateways, inference engines, and tools.</p>

  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
  ![GitHub stars](https://img.shields.io/github/stars/yenanjing/awesome-model-routing?style=flat-square)
  ![Last Updated](https://img.shields.io/badge/last%20updated-2026-05-12-blue?style=flat-square)

  <p>Collected <strong>53</strong> repositories with <strong>1,000+</strong> stars across <strong>8</strong> categories.</p>
</div>

---

## 📖 Table of Contents

- [About](#-about)
- [🧠 LLM Routers & Smart Routing](#llm-routers--smart-routing)
- [🚪 AI Gateways & Unified APIs](#ai-gateways--unified-apis)
- [⚖️ LLM Proxy & Load Balancing](#llm-proxy--load-balancing)
- [⚡ Inference Serving Engines](#inference-serving-engines)
- [🎭 LLM Orchestration Frameworks](#llm-orchestration-frameworks)
- [📡 API Management & Distribution](#api-management--distribution)
- [💰 Cost Optimization & Observability](#cost-optimization--observability)
- [🔬 Research & Benchmarks](#research--benchmarks)
- [📊 Stats](#-stats)
- [🤝 Contributing](#-contributing)

---

## 🌟 About

Model routing is a critical infrastructure pattern for modern AI applications. It encompasses intelligent request routing across multiple LLM providers, cost-optimized model selection, load balancing for inference workloads, and unified API gateways that abstract away provider complexity.

This list covers the full spectrum — from smart routers that choose the optimal model per request, to high-performance inference engines, to unified gateways that provide a single endpoint for 100+ LLM APIs.

> **Criteria**: Repositories with 1,000+ stars (with select exceptions for highly relevant routing-specific tools), actively maintained, related to model routing.
> Last updated: 2026-05-12

---

## 🧠 LLM Routers & Smart Routing

> Tools that intelligently route LLM requests to different models based on cost, quality, complexity, or latency.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**BlockRunAI/ClawRouter**](https://github.com/BlockRunAI/ClawRouter) | ⭐ 6,560 | `TypeScript` | The agent-native LLM router for OpenClaw. 41+ models, <1ms routing, USDC payments on Base & Solana via x402. |
| [**mnfst/manifest**](https://github.com/mnfst/manifest) | ⭐ 6,384 | `TypeScript` | Smart Model Routing for Agents. Cut Costs up to 70% 🦚 |
| [**lm-sys/RouteLLM**](https://github.com/lm-sys/RouteLLM) | ⭐ 4,883 | `Python` | A framework for serving and evaluating LLM routers - save LLM costs without compromising quality |
| [**NadirRouter/NadirClaw**](https://github.com/NadirRouter/NadirClaw) | ⭐ 492 | `Python` | Open-source LLM router & AI cost optimizer. Routes simple prompts to cheap/local models, complex ones to premium — au... |

---

## 🚪 AI Gateways & Unified APIs

> Unified API gateways that provide a single interface to access multiple LLM providers with routing, failover, and load balancing.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**BerriAI/litellm**](https://github.com/BerriAI/litellm) | ⭐ 46,671 | `Python` | Python SDK, Proxy Server (AI Gateway) to call 100+ LLM APIs in OpenAI (or native) format, with cost tracking, guardra... |
| [**Kong/kong**](https://github.com/Kong/kong) | ⭐ 43,370 | `Lua` | 🦍 The API and AI Gateway |
| [**apache/apisix**](https://github.com/apache/apisix) | ⭐ 16,582 | `Lua` | The Cloud-Native API Gateway and AI Gateway |
| [**Portkey-AI/gateway**](https://github.com/Portkey-AI/gateway) | ⭐ 11,692 | `TypeScript` | A blazing fast AI Gateway with integrated guardrails. Route to 1,600+ LLMs, 50+ AI Guardrails with 1 fast & friendly ... |
| [**higress-group/higress**](https://github.com/higress-group/higress) | ⭐ 8,363 | `Go` | 🤖 AI Gateway \| AI Native API Gateway |
| [**kgateway-dev/kgateway**](https://github.com/kgateway-dev/kgateway) | ⭐ 5,506 | `Go` | The Cloud-Native API Gateway and AI Gateway |
| [**maximhq/bifrost**](https://github.com/maximhq/bifrost) | ⭐ 4,867 | `Go` | Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ ... |
| [**diegosouzapw/OmniRoute**](https://github.com/diegosouzapw/OmniRoute) | ⭐ 4,410 | `TypeScript` | Never stop coding. Free AI gateway: one endpoint, 160+ providers, RTK+Caveman stacked compression up to ~95% eligible... |
| [**looplj/axonhub**](https://github.com/looplj/axonhub) | ⭐ 3,708 | `Go` | ⚡️ Open-source AI Gateway — Use any SDK to call 100+ LLMs. Built-in failover, load balancing, cost control & end-to-e... |
| [**APIParkLab/APIPark**](https://github.com/APIParkLab/APIPark) | ⭐ 1,706 | `TypeScript` | Cloud native, ultra-high performance AI&API gateway, LLM API management, distribution system, open platform, supporti... |
| [**envoyproxy/ai-gateway**](https://github.com/envoyproxy/ai-gateway) | ⭐ 1,606 | `Go` | Manages Unified Access to Generative AI Services built on Envoy Gateway |
| [**bricks-cloud/BricksLLM**](https://github.com/bricks-cloud/BricksLLM) | ⭐ 1,198 | `Go` | 🔒 Enterprise-grade API gateway that helps you monitor and impose cost or rate limits per API key. Get fine-grained ac... |

---

## ⚖️ LLM Proxy & Load Balancing

> Proxy servers and load balancers specifically designed for LLM API traffic management.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**rtk-ai/rtk**](https://github.com/rtk-ai/rtk) | ⭐ 46,491 | `Rust` | CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies |
| [**songquanpeng/one-api**](https://github.com/songquanpeng/one-api) | ⭐ 33,551 | `JavaScript` | LLM API 管理 & 分发系统，支持 OpenAI、Azure、Anthropic Claude、Google Gemini、DeepSeek、字节豆包、ChatGLM、文心一言、讯飞星火、通义千问、360 智脑、腾讯混元等主流模... |
| [**QuantumNous/new-api**](https://github.com/QuantumNous/new-api) | ⭐ 32,764 | `Go` | A unified AI model hub for aggregation & distribution. It supports cross-converting various LLMs into OpenAI-compatib... |
| [**coaidev/coai**](https://github.com/coaidev/coai) | ⭐ 9,160 | `TypeScript` | 🚀 Next Gen Multi-tenant AI One-Stop Solution. Builtin Admin & Billing System. Enterprise-Grade Unified LLM Gateway Su... |
| [**fruitbars/simple-one-api**](https://github.com/fruitbars/simple-one-api) | ⭐ 2,311 | `Go` | OpenAI 接口接入适配，支持千帆大模型平台、讯飞星火大模型、腾讯混元以及MiniMax、Deep-Seek，等兼容OpenAI接口 |
| [**romgX/openrelay**](https://github.com/romgX/openrelay) | ⭐ 1,903 | `TypeScript` | 几百个免费 AI 模型配额，一键接入本地项目。\| Hundreds of free AI model quotas, one-click access to local projects. |

---

## ⚡ Inference Serving Engines

> High-performance inference engines that serve LLM models with built-in routing and scheduling capabilities.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**ggml-org/llama.cpp**](https://github.com/ggml-org/llama.cpp) | ⭐ 109,706 | `C++` | LLM inference in C/C++ |
| [**vllm-project/vllm**](https://github.com/vllm-project/vllm) | ⭐ 79,771 | `Python` | A high-throughput and memory-efficient inference and serving engine for LLMs |
| [**nomic-ai/gpt4all**](https://github.com/nomic-ai/gpt4all) | ⭐ 77,367 | `C++` | GPT4All: Run Local LLMs on Any Device. Open-source and available for commercial use. |
| [**microsoft/BitNet**](https://github.com/microsoft/BitNet) | ⭐ 38,951 | `Python` | Official inference framework for 1-bit LLMs |
| [**mozilla-ai/llamafile**](https://github.com/mozilla-ai/llamafile) | ⭐ 24,422 | `C++` | Distribute and run LLMs with a single file. |
| [**mlc-ai/web-llm**](https://github.com/mlc-ai/web-llm) | ⭐ 17,960 | `TypeScript` | High-performance In-browser LLM Inference Engine |
| [**kvcache-ai/ktransformers**](https://github.com/kvcache-ai/ktransformers) | ⭐ 17,152 | `Python` | A Flexible Framework for Experiencing Heterogeneous LLM Inference/Fine-tune Optimizations |
| [**alibaba/MNN**](https://github.com/alibaba/MNN) | ⭐ 15,154 | `C++` | MNN: A blazing-fast, lightweight inference engine battle-tested by Alibaba, powering high-performance on-device LLMs ... |
| [**jundot/omlx**](https://github.com/jundot/omlx) | ⭐ 13,728 | `Python` | LLM inference server with continuous batching & SSD caching for Apple Silicon — managed from the macOS menu bar |
| [**NVIDIA/TensorRT-LLM**](https://github.com/NVIDIA/TensorRT-LLM) | ⭐ 13,615 | `Python` | TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and supports state-... |
| [**GeeeekExplorer/nano-vllm**](https://github.com/GeeeekExplorer/nano-vllm) | ⭐ 13,380 | `Python` | Nano vLLM — minimal, educational reimplementation of vLLM for learning LLM serving |
| [**sgl-project/sglang**](https://github.com/sgl-project/sglang) | ⭐ 27,697 | `Python` | SGLang is a high-performance serving framework for large language models and multimodal models. |

---

## 🎭 LLM Orchestration Frameworks

> Frameworks for orchestrating multiple LLMs with routing, pipeline, and workflow capabilities.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**pathwaycom/llm-app**](https://github.com/pathwaycom/llm-app) | ⭐ 59,759 | `Python` | Ready-to-run cloud templates for RAG, AI pipelines, and enterprise search with live data - built with Pathway LLM xpack |
| [**labring/FastGPT**](https://github.com/labring/FastGPT) | ⭐ 28,009 | `TypeScript` | FastGPT is a knowledge-based platform built on the LLMs, offers a comprehensive suite of out-of-the-box capabilities ... |
| [**deepset-ai/haystack**](https://github.com/deepset-ai/haystack) | ⭐ 25,192 | `MDX` | Open-source AI orchestration framework for building context-engineered, production-ready LLM applications. Design mod... |
| [**neuml/txtai**](https://github.com/neuml/txtai) | ⭐ 12,481 | `Python` | 💡 All-in-one AI framework for semantic search, LLM orchestration and language model workflows |
| [**tensorzero/tensorzero**](https://github.com/tensorzero/tensorzero) | ⭐ 11,360 | `Rust` | TensorZero is an open-source LLMOps platform that unifies an LLM gateway, observability, evaluation, optimization, an... |
| [**IBM/mcp-context-forge**](https://github.com/IBM/mcp-context-forge) | ⭐ 3,686 | `Python` | An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, or REST/gRPC APIs, exposing a unified endpoint... |
| [**archestra-ai/archestra**](https://github.com/archestra-ai/archestra) | ⭐ 3,654 | `TypeScript` | Enterprise AI Platform with guardrails, MCP registry, gateway & orchestrator |

---

## 📡 API Management & Distribution

> Platforms for managing, distributing, and monitoring LLM API access across teams and applications.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**cheahjs/free-llm-api-resources**](https://github.com/cheahjs/free-llm-api-resources) | ⭐ 21,309 | `Python` | A list of free LLM inference resources accessible via API. |
| [**casdoor/casdoor**](https://github.com/casdoor/casdoor) | ⭐ 13,592 | `Go` | An open-source Agent-first Identity and Access Management (IAM) /LLM MCP & agent gateway and auth server with web UI ... |
| [**InsForge/InsForge**](https://github.com/InsForge/InsForge) | ⭐ 9,533 | `TypeScript` | The all-in-one, open-source backend platform for agentic coding. InsForge gives your coding agent database, auth, sto... |
| [**mnfst/awesome-free-llm-apis**](https://github.com/mnfst/awesome-free-llm-apis) | ⭐ 4,257 | `JavaScript` | List of Permanent Free LLM API  (API Keys) |

---

## 💰 Cost Optimization & Observability

> Tools focused on reducing LLM costs through smart routing, caching, token optimization, and observability.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**langfuse/langfuse**](https://github.com/langfuse/langfuse) | ⭐ 27,050 | `TypeScript` | 🪢 Open source LLM engineering platform: LLM Observability, metrics, evals, prompt management, playground, datasets. I... |
| [**mlflow/mlflow**](https://github.com/mlflow/mlflow) | ⭐ 25,887 | `Python` | The open source AI engineering platform for agents, LLMs, and ML models. MLflow enables teams of all sizes to debug, ... |
| [**comet-ml/opik**](https://github.com/comet-ml/opik) | ⭐ 19,276 | `Python` | Debug, evaluate, and monitor your LLM applications, RAG systems, and agentic workflows with comprehensive tracing, au... |
| [**raga-ai-hub/RagaAI-Catalyst**](https://github.com/raga-ai-hub/RagaAI-Catalyst) | ⭐ 16,157 | `Python` | Python SDK for Agent AI Observability, Monitoring and Evaluation Framework. Includes features like agent, llm and too... |
| [**vibrantlabsai/ragas**](https://github.com/vibrantlabsai/ragas) | ⭐ 13,882 | `Python` | Supercharge Your LLM Application Evaluations 🚀 |
| [**supercorp-ai/supergateway**](https://github.com/supercorp-ai/supergateway) | ⭐ 2,618 | `TypeScript` | Run MCP stdio servers over SSE and SSE over stdio. AI gateway with routing. |

---

## 🔬 Research & Benchmarks

> Academic research papers, frameworks, and benchmarks related to LLM routing strategies.

| Repository | Stars | Language | Description |
|-----------|-------|----------|-------------|
| [**liguodongiot/llm-action**](https://github.com/liguodongiot/llm-action) | ⭐ 24,264 | `HTML` | 本项目旨在分享大模型相关技术原理以及实战经验（大模型工程化、大模型应用落地） |
| [**humanlayer/12-factor-agents**](https://github.com/humanlayer/12-factor-agents) | ⭐ 19,765 | `TypeScript` | What are the principles we can use to build LLM-powered software that is actually good enough to put in the hands of ... |

---

## 📊 Stats

- **Total repositories**: 53
- **Minimum stars**: 1,000
- **Languages covered**: C++, Go, HTML, JavaScript, Lua, MDX, Python, Rust, TypeScript
- **Last updated**: 2026-05-12

### Top 10 by Stars

| Rank | Repository | Stars |
|------|-----------|-------|
| 1 | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | ⭐ 109,706 |
| 2 | [vllm-project/vllm](https://github.com/vllm-project/vllm) | ⭐ 79,771 |
| 3 | [nomic-ai/gpt4all](https://github.com/nomic-ai/gpt4all) | ⭐ 77,367 |
| 4 | [pathwaycom/llm-app](https://github.com/pathwaycom/llm-app) | ⭐ 59,759 |
| 5 | [BerriAI/litellm](https://github.com/BerriAI/litellm) | ⭐ 46,671 |
| 6 | [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | ⭐ 46,491 |
| 7 | [Kong/kong](https://github.com/Kong/kong) | ⭐ 43,370 |
| 8 | [microsoft/BitNet](https://github.com/microsoft/BitNet) | ⭐ 38,951 |
| 9 | [songquanpeng/one-api](https://github.com/songquanpeng/one-api) | ⭐ 33,551 |
| 10 | [QuantumNous/new-api](https://github.com/QuantumNous/new-api) | ⭐ 32,764 |

---

## 🤝 Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

To add a project:
1. Fork this repository
2. Add your project to the relevant section
3. Ensure it has 1,000+ stars and is actively maintained
4. Submit a Pull Request

---

## 📄 License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

This list is under the [CC0 1.0](LICENSE) license.

---

<div align="center">
  <sub>Generated with ❤️ using <a href="https://claude.ai/claude-code">Claude Code</a></sub>
</div>
