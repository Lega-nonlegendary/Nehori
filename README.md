# Nehori(根堀り)

English | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

**An AI skill for clarifying what you want through concrete proposals.**

"I can't quite explain what I want." "I want something, but I don't know what kind to choose." Nehori is designed for moments like these. Once installed, it helps your AI guide the conversation and narrow down your wishes, much like a dedicated personal aide.

Instead of only asking questions and expecting you to supply the answers, it offers concrete proposals or small examples, then reshapes the next proposal based on your response.

## How is it different from dialogue that just asks questions?

When your desires are vague, it can be difficult to answer even if asked to tell your conditions. Nehori does not assume that you already have the answer; instead, it prepares options that can be compared.

For example, if you want a bag that works for both work and weekends without looking like a formal business bag, Nehori shows two options rather than fixing on a single shape. Reactions such as "this part is close," "neither is right," or "I'd like to combine the two" become clues for what to explore next.

It distinguishes preferences that emerge only after seeing an example from preferences you held beforehand, aiming to make its suggestions more relevant.

## How to use

```text
Use Nehori and ask me thoroughly about my needs.
I want a bag to use on weekends, but I cannot picture a specific shape yet.
```

```text
I feel something is off with this proposal, so please ask me in detail.
I want to organize what is bothering me while looking at proposals.
```

```text
I want to think together about the atmosphere of the screen I want to build, while showing examples I can compare.
```

You do not need to answer all questions. "None of these are right," "I only like this part," "I don't know yet," "I want to leave this to you," or "This is enough" can all be communicated as they are.

## How Nehori proceeds

1. Grasp the starting point. Using the current purpose, context of use, and already known conditions, it asks only for missing details that would significantly alter the proposals.
2. Think through two paths. It combines a path that develops the preferences you have explicitly stated with a path that explores alternative interpretations and adjacent possibilities.
3. Offer concrete proposals. It communicates not just names, but also the context of use, reasons why it fits, and points that depend on conditions. You do not have to choose a full proposal; adopting parts or rejecting everything is perfectly fine.
4. Rearrange based on reactions. Receiving not only choices, but also reasons, hesitations, feelings of discomfort, and additional conditions, it decides whether to broaden or narrow down options.
5. Wrap up where it becomes useful. Once words expressing your desires or criteria for choosing are established, it returns them including undecided points. Continuing questions for the sake of it is not the goal.

The two paths do not mean launching two sub-agents every time. Delegation occurs only when environment permissions, models, and cost conditions are met; otherwise, a single assistant considers both paths. Only one assistant speaks with the user.

## Confirming content before searching

When looking up external real-world examples or products, it indicates the purpose, example search terms, targets and sources, and the boundary for the initial investigation, waiting for approval before searching. The same allowed scope is passed on to the explorer role.

There is no need to re-confirm every time for rephrasings of search terms within the same plan. If expanding the scope to reviews or videos, it shows the additional details and waits for approval again. This applies not only to search tools, but also to retrievals via browsers or URLs. Reading provided local materials does not require this search permission.

## Installation

This repository contains introduction text and auxiliary files for publishing, in addition to the main skill. **Install the `skills/nehori/` folder.**

### Ask your AI to install it (recommended)

Give an AI with file access the URL of this README or the location of the extracted repository, then ask:

```text
Install this repository's skills/nehori/ so I can use it in my current AI environment.
Read the README and SKILL.md first, then copy the entire folder, including its references, into the user-level skills directory appropriate for this AI product and operating system.
If a skill with the same name already exists, ask before overwriting it.
Do not change unrelated skills or authentication settings. After installation, verify and report the location and how to invoke the skill.
```

A regular chat without filesystem permissions cannot install files on your PC. In that case, use the manual instructions below.

For manual installation, download and extract the repository and run the following commands from its root. Back up an existing same-named skill before replacing it, and avoid nesting one `nehori/` folder inside another. If you run the AI in WSL, use the macOS / Linux commands inside WSL and its Linux home directory, not your Windows home.

### Codex

For a user-level skill in Codex CLI or the IDE extension, place `skills/nehori/` in `~/.agents/skills/nehori/`.

macOS / Linux:

```sh
mkdir -p ~/.agents/skills
cp -R skills/nehori ~/.agents/skills/nehori
```

Windows (PowerShell):

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills" | Out-Null
Copy-Item -LiteralPath ".\skills\nehori" -Destination "$env:USERPROFILE\.agents\skills\nehori" -Recurse
```

Check `/skills` after installation, then include `$nehori` in your request. Restart Codex if the skill does not appear.

```text
$nehori Ask me in detail about what I want.
```

For this project only, use `.agents/skills/nehori/`. You can also ask the built-in `$skill-installer` to install it by supplying this repository's URL and the `skills/nehori/` path.

Reference: [Official OpenAI skill installation documentation](https://learn.chatgpt.com/docs/build-skills).

### Claude Code

For a user-level skill in local Claude Code sessions, place `skills/nehori/` in `~/.claude/skills/nehori/`.

macOS / Linux:

```sh
mkdir -p ~/.claude/skills
cp -R skills/nehori ~/.claude/skills/nehori
```

Windows (PowerShell):

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -LiteralPath ".\skills\nehori" -Destination "$env:USERPROFILE\.claude\skills\nehori" -Recurse
```

Invoke it in Claude Code with `/nehori`.

```text
/nehori Ask me in detail about what I want.
```

For this project only, use `.claude/skills/nehori/`. If it does not appear, check the location and start a new Claude Code session.

Reference: [Official Claude Code skill installation documentation](https://code.claude.com/docs/en/skills).

### OMP

macOS / Linux:

```sh
mkdir -p ~/.omp/agent/skills
cp -R skills/nehori ~/.omp/agent/skills/nehori
```

Windows (PowerShell):

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.omp\agent\skills" | Out-Null
Copy-Item -LiteralPath ".\skills\nehori" -Destination "$env:USERPROFILE\.omp\agent\skills\nehori" -Recurse
```

In a new conversation, ask: "Use Nehori and ask me in detail." If OMP skill commands are enabled, you can also invoke it with `/skill:nehori`.

To use it only within a specific project, place `skills/nehori/` into that project's `.omp/skills/nehori/`.

### Other Agent Skills compatible environments

Place `skills/nehori/` into the directory designated for skills by your environment. Supporting the skill format is distinct from auto-triggering or tool permissions working in the same way. Follow the installation steps specific to your environment.

The core instructions are currently managed in Japanese. Please inform the assistant of your preferred conversation language. Nehori does not fix the conversation language, tone, or persona.

## Skill structure

The main instructions cover principles and reasons, the dialogue flow, approval before external research, and trust boundaries. Supporting references are read only when needed.

| File | Purpose |
|---|---|
| [SKILL.md](skills/nehori/SKILL.md) | Shared dialogue steps and decision criteria |
| [exploration.md](skills/nehori/references/exploration.md) | Inputs, outputs and integration for the two exploration roles |
| [dialogue-patterns.md](skills/nehori/references/dialogue-patterns.md) | Questioning approaches and sample replies for different kinds of consultation |
| [conversation-map.md](skills/nehori/references/conversation-map.md) | Distinguishing statements, preferences, interpretations and open choices, then choosing the next step |
| [research-notes.md](skills/nehori/references/research-notes.md) | Design rationale, origins and limits of adaptation |

The conversation map is an aid within the conversation, not an automatically saved personal profile. When the user wants concrete candidates and there is enough information to distinguish them, Nehori moves to candidates or a research plan rather than continuing to ask questions.

## What it does not do / Limitations

- It does not perform psychological diagnosis, mind reading, measurement of the subconscious, or persuasive tactics aimed at driving purchases.
- It does not require roleplay or enforce a particular tone.
- For product names, prices, and specifications, it distinguishes between verified information and imaginary samples. It does not substitute questions about personal preference for verifying expert knowledge.
- It does not send private remarks directly to the outside world as search terms. Nor does it require permanent saving of new personal profiles or conversation logs without consent.
- It does not guarantee effects based on comparative experiments regarding dialogue quality, cultural differences, or long-term burdens. Results vary depending on the model and usage environment.

## Origins

Inspired by the clue-following exploration and dual entry points of [imozuru](https://github.com/MaryCache/imozuru). Nehori is newly written, shifting the focus from external information to dialogue with the user and moving between proposals and corrections. It is not a fork or a required dependency of imozuru. imozuru is also an excellent skill in its own right.

Active listening, UX interviews, preference concretization through comparison, and consultative sales served as design references. It has not been proven that insights from human interviews or customer service automatically yield the same effects in AI. Please also refer to [Design Rationale and Limitations](skills/nehori/references/research-notes.md).

## License and Publishing

[MIT License](LICENSE). See [CHANGELOG.md](CHANGELOG.md) for changes and [PUBLISHING.md](PUBLISHING.md) for creating the distribution ZIP and uploading to GitHub.
