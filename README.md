# Pipeline X-Ray

AI-assisted diagnostics for CI/CD pipelines: DORA-style metrics, bottleneck detection and actionable recommendations.

> **Status:** early development (Phase 0 — Foundation). Not ready for use yet.

## Why

CI/CD pipelines tend to degrade silently. Builds get slower, flaky tests pile up, and failures take longer to recover from — but since nobody owns "pipeline health", these problems are rarely measured, let alone fixed.

Pipeline X-Ray analyzes the execution history of your pipelines, measures how your delivery process is actually performing, and tells you what to improve first — with concrete, evidence-based recommendations.

## How it works

1. **Collect** — fetches workflow runs, jobs and steps from the GitHub Actions API.
2. **Measure** — computes DORA-style metrics such as build duration, success rate, run frequency and time to recover from failures.
3. **Detect** — a rule engine flags objective issues, like missing dependency caching, unpinned actions, slow builds and flaky tests.
4. **Explain** — an LLM turns the metrics and findings into a readable report with prioritized recommendations.

The rules find the problems; the AI only explains them. Every recommendation in the report is backed by a metric or a rule finding.

## Principles

- **Read-only access** — GitHub tokens only need minimal, read-only permissions.
- **No source code sent to AI** — only pipeline metadata and logs are used, never your repository's code.
- **Evidence over guesses** — the AI report is grounded on deterministic metrics and rules, so it does not invent issues.
- **Practice what it preaches** — this project applies the same DevOps practices it recommends: CI, containers, quality and security checks.

## Roadmap

- [ ] **Phase 0 — Foundation:** repository, tooling and first test
- [ ] **Phase 1 — Collector:** fetch pipeline data from the GitHub API
- [ ] **Phase 2 — Storage & metrics:** data model and DORA-style metrics
- [ ] **Phase 3 — Rule engine:** automated detection of pipeline issues
- [ ] **Phase 4 — AI report:** readable diagnostics generated from findings
- [ ] **Phase 5 — Open source validation:** analyze real projects and contribute fixes
- [ ] **Phase 6 — DevOps on itself:** Docker, CI pipeline, quality gates and releases
- [ ] **Phase 7 — Interface:** installable CLI, API and dashboard
- [ ] **Phase 8 — Portfolio & content:** case studies, architecture diagram and demo

## Development

### Prerequisites

- [uv](https://docs.astral.sh/uv/)
- Git

### Setup

```bash
git clone https://github.com/pedrorubacow/pipeline-xray.git
cd pipeline-xray
uv sync
uv run pre-commit install
```

### Common commands

```bash
uv run pytest              # run tests
uv run ruff check .        # lint
uv run ruff format .       # format
```

## License

MIT — see [LICENSE](LICENSE).
