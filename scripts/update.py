#!/usr/bin/env python3
"""
Auto-update script for awesome-model-routing.
Searches GitHub API for model routing related projects, deduplicates, classifies, and regenerates README.md.
"""

import json
import os
import subprocess
import time
from datetime import date

MIN_STARS = 1000

# Search queries to cover the model routing ecosystem
SEARCH_QUERIES = [
    "model-routing+in:name,description",
    "llm-router+OR+llm-routing+in:name,description",
    "ai-gateway+OR+llm-gateway+in:name,description",
    "inference-routing+OR+model-router+OR+ai-router+in:name,description",
    "topic:llm-router",
    "topic:ai-gateway",
    "topic:model-router",
    "topic:llm-gateway",
    "openai+proxy+gateway+in:name,description",
    "RouteLLM+in:name",
    "one-api+in:name+language:go",
    "vllm+OR+sglang+OR+ollama+in:name",
    "model+orchestration+llm+in:name,description",
    "llm+load+balancing+OR+llm+proxy+in:name,description",
]


def gh_search(query, page=1):
    """Search GitHub API via gh CLI."""
    cmd = [
        "gh", "api",
        f"search/repositories?q={query}&sort=stars&order=desc&per_page=100&page={page}",
        "--jq", '.items[] | {name: .full_name, stars: .stargazers_count, description: .description, url: .html_url, language: .language, topics: (.topics | join(",")), updated: .updated_at, archived: .archived}'
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        projects = []
        for line in result.stdout.strip().split('\n'):
            if line.strip():
                try:
                    projects.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
        return projects
    except Exception as e:
        print(f"  Error searching '{query}': {e}")
        return []


def collect_projects():
    """Run all search strategies and collect projects."""
    all_projects = {}

    for query in SEARCH_QUERIES:
        print(f"Searching: {query}")
        for page in range(1, 4):  # Up to 3 pages per query
            results = gh_search(query, page)
            if not results:
                break

            below_threshold = False
            for p in results:
                if p.get('archived', False):
                    continue
                if p.get('stars', 0) < MIN_STARS:
                    below_threshold = True
                    continue
                name = p.get('name', '')
                if name and name not in all_projects:
                    all_projects[name] = p

            if below_threshold:
                break
            time.sleep(2)  # Rate limit: 30 req/min for search API

        time.sleep(2)

    return all_projects


def is_relevant(p):
    """Check if project is relevant to model routing."""
    routing_keywords = [
        'routing', 'router', 'gateway', 'proxy', 'llm-gateway', 'ai-gateway',
        'model-router', 'llm-router', 'load-balancing', 'loadbalancing',
        'inference', 'serving', 'orchestration', 'llm-proxy', 'openai-proxy',
        'model-selection', 'cost-optimization', 'multi-model', 'multi-provider',
        'llmops', 'model-serving', 'llm-serving', 'ai-router'
    ]

    name = p.get('name', '').lower()
    desc = (p.get('description') or '').lower()
    topics = (p.get('topics') or '').lower()

    for kw in routing_keywords:
        if kw in name or kw in desc or kw in topics:
            return True

    # Known relevant projects
    known = {
        'BerriAI/litellm', 'Kong/kong', 'apache/apisix', 'Portkey-AI/gateway',
        'lm-sys/RouteLLM', 'vllm-project/vllm', 'sgl-project/sglang',
        'NVIDIA/TensorRT-LLM', 'ollama/ollama', 'deepset-ai/haystack',
        'QuantumNous/new-api', 'coaidev/coai', 'tensorzero/tensorzero',
        'higress-group/higress', 'kgateway-dev/kgateway', 'maximhq/bifrost',
        'BlockRunAI/ClawRouter', 'mnfst/manifest', 'envoyproxy/ai-gateway',
        'neuml/txtai', 'songquanpeng/one-api', 'labring/FastGPT',
        'langfuse/langfuse', 'ggml-org/llama.cpp', 'nomic-ai/gpt4all',
        'mozilla-ai/llamafile', 'mlc-ai/web-llm', 'microsoft/BitNet',
    }
    return p.get('name') in known


def classify_project(p):
    """Classify a project into a category."""
    name = p.get('name', '').lower()
    desc = (p.get('description') or '').lower()
    topics = (p.get('topics') or '').lower()

    # Smart routers
    router_names = ['routellm', 'clawrouter', 'manifest', 'nadirrouter', 'nadir']
    if any(r in name for r in router_names):
        return "LLM Routers & Smart Routing"
    if 'smart routing' in desc or 'intelligent routing' in desc or 'llm router' in desc:
        return "LLM Routers & Smart Routing"

    # Inference engines
    inference_names = ['vllm', 'sglang', 'llama.cpp', 'llamafile', 'tensorrt', 'ollama',
                       'gpt4all', 'web-llm', 'bitnet', 'ktransformers', 'mnn', 'omlx', 'nano-vllm']
    if any(i in name for i in inference_names):
        return "Inference Serving Engines"
    if 'inference engine' in desc or 'inference server' in desc:
        return "Inference Serving Engines"

    # Orchestration
    orchestration_names = ['haystack', 'txtai', 'tensorzero', 'fastgpt', 'mcp-context-forge', 'archestra', 'llm-app']
    if any(o in name for o in orchestration_names):
        return "LLM Orchestration Frameworks"
    if 'orchestrat' in desc:
        return "LLM Orchestration Frameworks"

    # Observability
    obs_names = ['langfuse', 'opik', 'mlflow', 'ragaai', 'ragas']
    if any(o in name for o in obs_names):
        return "Cost Optimization & Observability"
    if 'observability' in desc or 'monitoring' in desc or 'evaluation' in desc:
        return "Cost Optimization & Observability"

    # Proxy & Load Balancing
    proxy_names = ['one-api', 'new-api', 'coai', 'simple-one-api', 'rtk', 'openrelay']
    if any(px in name for px in proxy_names):
        return "LLM Proxy & Load Balancing"
    if 'proxy' in desc and 'llm' in desc:
        return "LLM Proxy & Load Balancing"

    # API Management
    api_names = ['free-llm-api', 'casdoor', 'insforge']
    if any(a in name for a in api_names):
        return "API Management & Distribution"

    # Research
    research_names = ['llm-action', '12-factor']
    if any(r in name for r in research_names):
        return "Research & Benchmarks"

    # Default: gateway
    if 'gateway' in desc or 'gateway' in topics or 'gateway' in name:
        return "AI Gateways & Unified APIs"

    return "AI Gateways & Unified APIs"


def truncate_desc(desc, max_len=120):
    if not desc:
        return ""
    desc = desc.replace("|", "\\|").replace("\n", " ").strip()
    if len(desc) > max_len:
        return desc[:max_len - 3] + "..."
    return desc


def format_stars(stars):
    return f"{stars:,}"


def generate_readme(categories):
    """Generate the README.md content."""
    today_str = date.today().strftime("%Y-%m-%d")
    total_projects = sum(len(cat["projects"]) for cat in categories.values())
    languages = set()
    for cat in categories.values():
        for p in cat["projects"]:
            if p.get('language'):
                languages.add(p['language'])

    readme = f'''<div align="center">
  <h1>Awesome Model Routing</h1>
  <p>A curated list of awesome LLM/AI model routing frameworks, gateways, inference engines, and tools.</p>

  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
  ![GitHub stars](https://img.shields.io/github/stars/yenanjing/awesome-model-routing?style=flat-square)
  ![Last Updated](https://img.shields.io/badge/last%20updated-{today_str}-blue?style=flat-square)

  <p>Collected <strong>{total_projects}</strong> repositories with <strong>1,000+</strong> stars across <strong>{len(categories)}</strong> categories.</p>
</div>

---

## Table of Contents

- [About](#-about)
'''

    for cat_name, cat_data in categories.items():
        slug = cat_name.lower().replace(" ", "-").replace("&", "").replace("  ", "-")
        readme += f"- [{cat_data['emoji']} {cat_name}](#{slug})\n"

    readme += """- [Stats](#-stats)
- [Contributing](#-contributing)

---

## About

Model routing is a critical infrastructure pattern for modern AI applications. It encompasses intelligent request routing across multiple LLM providers, cost-optimized model selection, load balancing for inference workloads, and unified API gateways that abstract away provider complexity.

This list covers the full spectrum: from smart routers that choose the optimal model per request, to high-performance inference engines, to unified gateways that provide a single endpoint for 100+ LLM APIs.

> **Criteria**: Repositories with 1,000+ stars, actively maintained, related to model routing.
> Last updated: """ + today_str + """

---

"""

    for cat_name, cat_data in categories.items():
        readme += f"## {cat_data['emoji']} {cat_name}\n\n"
        readme += f"> {cat_data['desc']}\n\n"
        readme += "| Repository | Stars | Language | Description |\n"
        readme += "|-----------|-------|----------|-------------|\n"

        for p in cat_data["projects"]:
            name = p['name']
            url = p['url']
            stars = format_stars(p.get('stars', 0))
            lang = p.get('language') or 'N/A'
            desc = truncate_desc(p.get('description', ''))
            readme += f"| [**{name}**]({url}) | {stars} | `{lang}` | {desc} |\n"

        readme += "\n---\n\n"

    # Stats
    all_sorted = []
    for cat in categories.values():
        all_sorted.extend(cat["projects"])
    all_sorted.sort(key=lambda x: x.get('stars', 0), reverse=True)

    readme += f"""## Stats

- **Total repositories**: {total_projects}
- **Minimum stars**: {MIN_STARS:,}
- **Languages covered**: {', '.join(sorted(languages))}
- **Last updated**: {today_str}

### Top 10 by Stars

| Rank | Repository | Stars |
|------|-----------|-------|
"""

    for i, p in enumerate(all_sorted[:10], 1):
        readme += f"| {i} | [{p['name']}]({p['url']}) | {format_stars(p.get('stars', 0))} |\n"

    readme += f"""
---

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

To add a project:
1. Fork this repository
2. Add your project to the relevant section
3. Ensure it has {MIN_STARS:,}+ stars and is actively maintained
4. Submit a Pull Request

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

This list is under the [CC0 1.0](LICENSE) license.

---

<div align="center">
  <sub>Generated with love using <a href="https://claude.ai/claude-code">Claude Code</a> | Auto-updated daily via GitHub Actions</sub>
</div>
"""
    return readme


def main():
    print("=== Awesome Model Routing Updater ===")
    print(f"Date: {date.today()}")
    print(f"Min stars: {MIN_STARS}")
    print()

    # Step 1: Collect projects
    print("Step 1: Collecting projects from GitHub...")
    all_projects = collect_projects()
    print(f"  Found {len(all_projects)} unique projects with {MIN_STARS}+ stars")

    # Step 2: Filter for relevance
    print("Step 2: Filtering for relevance...")
    relevant = {k: v for k, v in all_projects.items() if is_relevant(v)}
    print(f"  {len(relevant)} projects are relevant to model routing")

    # Step 3: Classify
    print("Step 3: Classifying projects...")
    categories = {
        "LLM Routers & Smart Routing": {
            "emoji": "\U0001f9e0",
            "desc": "Tools that intelligently route LLM requests to different models based on cost, quality, complexity, or latency.",
            "projects": []
        },
        "AI Gateways & Unified APIs": {
            "emoji": "\U0001f6aa",
            "desc": "Unified API gateways that provide a single interface to access multiple LLM providers with routing, failover, and load balancing.",
            "projects": []
        },
        "LLM Proxy & Load Balancing": {
            "emoji": "⚖️",
            "desc": "Proxy servers and load balancers specifically designed for LLM API traffic management.",
            "projects": []
        },
        "Inference Serving Engines": {
            "emoji": "⚡",
            "desc": "High-performance inference engines that serve LLM models with built-in routing and scheduling capabilities.",
            "projects": []
        },
        "LLM Orchestration Frameworks": {
            "emoji": "\U0001f3ad",
            "desc": "Frameworks for orchestrating multiple LLMs with routing, pipeline, and workflow capabilities.",
            "projects": []
        },
        "API Management & Distribution": {
            "emoji": "\U0001f4e1",
            "desc": "Platforms for managing, distributing, and monitoring LLM API access across teams and applications.",
            "projects": []
        },
        "Cost Optimization & Observability": {
            "emoji": "\U0001f4b0",
            "desc": "Tools focused on reducing LLM costs through smart routing, caching, token optimization, and observability.",
            "projects": []
        },
        "Research & Benchmarks": {
            "emoji": "\U0001f52c",
            "desc": "Academic research papers, frameworks, and benchmarks related to LLM routing strategies.",
            "projects": []
        },
    }

    for name, p in relevant.items():
        cat = classify_project(p)
        categories[cat]["projects"].append(p)

    # Sort each category by stars
    for cat in categories.values():
        cat["projects"].sort(key=lambda x: x.get('stars', 0), reverse=True)

    for cat_name, cat_data in categories.items():
        print(f"  {cat_data['emoji']} {cat_name}: {len(cat_data['projects'])} projects")

    # Step 4: Generate README
    print("Step 4: Generating README.md...")
    readme = generate_readme(categories)

    with open("README.md", "w") as f:
        f.write(readme)

    total = sum(len(c["projects"]) for c in categories.values())
    print(f"\nDone! README.md updated with {total} projects across {len(categories)} categories.")


if __name__ == "__main__":
    main()
