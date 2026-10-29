# Prepare and upload Nehori

This repository is ready for a manual GitHub upload after review. Nothing in the packaging tool creates a remote repository, authenticates to GitHub, commits, pushes, or publishes a release.

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
python scripts/package.py --output ../dist/nehori-v0.1.0.zip
```

On Windows, `py -3` can replace `python`. To invoke from another directory, pass the script's path; the repository root is resolved from the script, not the current directory:

```sh
python /path/to/nehori/scripts/package.py --output /path/to/releases/nehori-v0.1.0.zip
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

The packaging CLI was exercised on Windows with Python 3.13. Rejection checks were exercised with Python 3.14 for missing/private files, broken/escaping links, local paths, token-shaped strings, unsafe destinations and a Windows junction. The documented PowerShell installation commands were run against a temporary profile, followed by native OMP 18.13.3 skill discovery and reading. Project-local installation was also checked without changing the real user profile.

All three README pages were rendered in a local Markdown preview and their language links were exercised. English and Simplified Chinese were translated from the Japanese page using Nani, then copyedited and checked for preserved installation commands and links.

Live GitHub rendering, macOS/Linux installation, other hosts, and independent conversational-quality comparisons were not tested. These checks are not a comprehensive security audit or an effectiveness study.
