# Prepare and upload Nehori

This repository is ready for a manual GitHub upload after review. Nothing in the packaging tool creates a remote repository, authenticates to GitHub, commits, pushes, or publishes a release.

For an existing GitHub repository, replace files at their current paths rather than creating a new repository or wrapper folder. When updating from 0.2.0 to 0.2.1, the changed files are `skills/nehori/SKILL.md`, `skills/nehori/references/dialogue-patterns.md`, `skills/nehori/references/conversation-map.md`, `CHANGELOG.md` and `PUBLISHING.md`. From an earlier version, use the full updated package contents. Review any edits made on GitHub before replacing them.

## 1. Review the public contents

- `README.md` is the English landing page; its links open `README.ja.md` and `README.zh-CN.md`.
- The installable unit is `skills/nehori/`, not the entire repository.
- The skill instructions are maintained in Japanese. The README language is not a fixed conversation-language or persona setting.
- The license is MIT, with the notice in `LICENSE`.
- Keep private conversations, development evaluations, full research source texts, screenshots, credentials and machine-specific settings outside this repository.

The small packaging checker catches the listed file/link/path/token problems; it is not a comprehensive secret scanner or a proof of conversational quality. Review every file before making it public.

## 2. Validate and create the archive

Python 3.10 or later is required only for this optional packaging step. Nehori itself is a Markdown skill and does not require Python.

From the repository root:

```sh
python scripts/package.py --output ../dist/nehori-v0.2.1.zip
```

On Windows, `py -3` can replace `python`. To invoke from another directory, pass the script's path; the repository root is resolved from the script, not the current directory:

```sh
python /path/to/nehori/scripts/package.py --output /path/to/releases/nehori-v0.2.1.zip
```

The archive destination must be outside the repository and must not already exist. After making a new revision, choose a new archive name or deliberately remove your old generated archive first. The script prints a JSON manifest containing the archive hash and every packaged member hash.

The checker rejects missing/unexpected files, symlinks, broken or escaping local Markdown links, accidental absolute local paths, private session identifiers and common API-token shapes. Git metadata and Python bytecode caches are excluded. Failed archive writes remove only the partial file created by that invocation.

## 3. Create an empty GitHub repository

1. Sign in to the GitHub account that should own Nehori.
2. Create a repository named `nehori` (or a name you prefer). Start private if you want one more review before publication.
3. Leave GitHub's generated README, license and gitignore options unchecked: this package already supplies them.

Suggested About text:

> A proposal-led AI skill for exploring and clarifying what you want, with explicit approval before external research.

Suggested topics: `agent-skills`, `ai-assistant`, `intent-elicitation`, `conversation-design`, `user-preferences`.

## 4. Upload the extracted contents, not the ZIP

1. Extract the ZIP. It contains one top-level `nehori/` folder.
2. In the new GitHub repository, choose **uploading an existing file** / **Add file → Upload files**.
3. Open the extracted `nehori/` folder and upload its **contents**. Do not upload the ZIP as the only repository file, and do not add another `nehori/` directory above `README.md`.
4. Include `skills/`, `scripts/`, and all top-level files. `.gitignore` is hidden on some systems; show hidden files and confirm it is included.
5. Use an initial commit message such as `Prepare Nehori public package`, then commit the uploaded files.
6. Confirm that `README.md` renders at the repository root, both language links work, and the skill/reference links resolve.

For a local Git workflow instead, use the repository URL GitHub shows for your account. No account, remote URL, commit identity, or access token is embedded in this package.

## 5. Publish only after review

Check the public file list and MIT notice one last time. If the repository is private, change visibility only when you intend it to become public. A tagged release and release ZIP are optional separate actions; this preparation does not claim a release has already happened.

For updates, edit the appropriate source files, keep the three README pages aligned, update `CHANGELOG.md`, and create a new checked archive. Translation assistance is not a substitute for reviewing commands, links and behavioral boundaries.

## Verification scope of this preparation

For the initial 0.1.0 preparation, the packaging CLI was exercised on Windows with Python 3.13. Rejection checks were exercised with Python 3.14 for missing/private files, broken/escaping links, local paths, token-shaped strings, unsafe destinations and a Windows junction. PowerShell installation and native OMP 18.13.3 discovery and reading were checked, as was project-local installation.

For the 0.1.1 revision, the Windows PowerShell commands for Codex, Claude Code and OMP were executed in separate temporary profiles. All four installed skill files, including references, matched the source, without nested folders. Native OMP skill discovery and reading were checked again without modifying the real user profile. All three revised README pages were rendered in a local Markdown preview and their language links were exercised.

All three initial README pages were rendered in a local Markdown preview and their language links were exercised. The initial English and Simplified Chinese translations used Nani. The 0.1.1 revision was translated and copyedited directly in OMP from the maintainer's revised Japanese draft, without operating the Nani UI. Installation commands and links were checked across languages. Codex and Claude Code locations and invocation syntax are based on their linked official documentation; their actual clients and the AI-assisted installer prompt were not executed.

For 0.2.0, skill frontmatter was validated for the installed body, the portable body and the existing OMP entry. The installed entry/body/new reference were read through native OMP. The documented Windows commands copied all five skill files into isolated Codex, Claude Code and OMP profiles; native OMP also read the new reference from an unrelated working directory. Codex and Claude Code clients were not launched.

The three revised README pages were rendered locally; language links, the new reference link and its relative backlink were opened. Packaging rejected an unregistered new reference before its allowlist update and included it afterward. Current checks also rejected an unexpected private file, an absolute local path, a missing new reference, an escaping Markdown link and an existing output archive. The 0.2.0 text and translations were prepared in OMP. Dialogue scenarios were rehearsed by the authoring assistant within the same conversation, not through independent model runs or a controlled old/new comparison.

For 0.2.1, the installed and portable skill frontmatter were validated and the installed entry, body and changed references were read through native OMP. Parent-authored same-conversation rehearsals covered a new subject, a reference experience, an explicit topic change, a non-pet example and unchanged research-consent handling. These checks clarify the intended behavior; they do not prove which opening question a model will choose in a new conversation. Public dialogue examples are fictional, not copies of the user's conversation.

Live GitHub rendering, macOS/Linux installation, other hosts, and independent conversational-quality comparisons were not tested. These checks are not a comprehensive security audit or an effectiveness study.
