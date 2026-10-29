# Nehori

English | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

**An AI skill for clarifying what you want through concrete proposals.**

"I cannot explain well what I want." "I want you to ask me in detail." In such cases, instead of just asking questions and demanding answers, it presents concrete proposals or small samples, and rearranges the next proposal based on your reaction.

## How is it different from dialogue that just asks questions?

When your desires are vague, it can be difficult to answer even if asked to tell your conditions. Nehori does not assume that you already have the answer; instead, it prepares options that can be compared.

For example, if you want a bag that can be used for both work and weekends, but you do not want it to look too rigid for formal work, it does not fixate on a single shape. Instead, it shows a proposal with a soft outline and another that is neat yet light in how it is carried. Reactions like "this part is close," "both are wrong," or "I want to mix these" become clues for the next search.

It is not a system to see through your hidden true feelings. It treats newly emerged desires formed upon seeing examples distinctly from desires you held beforehand.

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

This is an assistant behavior procedure, not a mechanism to technically block communications.

## Installation

This repository contains introduction text and auxiliary files for publishing, in addition to the main skill. **Install the `skills/nehori/` folder.**

### OMP

Download and extract the repository, then run the commands at its root. If a skill with the same name already exists, back it up before replacing it, and do not nest folders.

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

## What it does not do / Limitations

- It does not perform psychological diagnosis, mind reading, measurement of the subconscious, or persuasive tactics aimed at driving purchases.
- What it borrows from high-end customer service is the method of interviewing and proposing. It is not a skill that roleplays sales staff or enforces a specific tone.
- For product names, prices, and specifications, it distinguishes between verified information and imaginary samples. It does not substitute questions about personal preference for verifying expert knowledge.
- It does not send private remarks directly to the outside world as search terms. Nor does it require permanent saving of new personal profiles or conversation logs without consent.
- It does not guarantee effects based on comparative experiments regarding dialogue quality, cultural differences, or long-term burdens. Results vary depending on the model and usage environment.

## Origins

Inspired by the clue-following exploration and dual entry points of [imozuru](https://github.com/MaryCache/imozuru). It is a newly written skill as a method to shift the focus from external information to dialogue with the person themselves, moving back and forth between proposals and corrections. It is not a fork or a required dependency of imozuru.

Active listening, UX interviews, preference concretization through comparison, and consultative sales served as design references. It has not been proven that insights from human interviews or customer service automatically yield the same effects in AI. Please also refer to [Design Rationale and Limitations](skills/nehori/references/research-notes.md).

## License and Publishing

[MIT License](LICENSE). See [CHANGELOG.md](CHANGELOG.md) for changes and [PUBLISHING.md](PUBLISHING.md) for creating the distribution ZIP and uploading to GitHub.
