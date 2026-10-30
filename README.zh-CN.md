# Nehori

[English](README.md) | [日本語](README.ja.md) | 简体中文

**一款通过具体提案，帮助你厘清尚未说清的愿望的 AI 技能。**

“说不清自己想要什么。”“想买点什么，却不知道具体该选哪一种。”Nehori 适合这样的时刻。安装后，AI 会像专属助理一样，通过对话帮助你逐步明确自己的愿望。

它不会只提问并要求你给出答案，而是会展示具体方案或小示例，再根据你的反应调整下一次提案。

## 与仅进行提问的对话有什么不同？

在期望尚处于模糊的阶段，即使被问到“请告诉我条件”，有时也很难回答。Nehori 不会以你心中已有答案为前提，而是会提供可以用来比较的方案。

例如，如果你“想要一个工作和休息日都能用的包，但不想要过于正式的商务款”，Nehori 不会直接定下一种外形，而是先展示两个方案。“这部分比较接近”“两个都不合适”“想把这两个结合起来”等反应，会成为下一步探索的线索。

它会区分看过示例后才产生的偏好与原本就有的偏好，以提供更贴合需求的建议为目标。

## 使用方法

```text
请使用Nehori，寻根究底地问我吧。
想要一个在休息日用的包，但还没有浮现出具体的形状。
```

```text
我对这个方案感到有些违和，请详细问问我。
想一边看提案，一边整理究竟是什么地方让人感到卡壳。
```

```text
想制作的画面氛围，希望能一边展示可以比较的例子一边和我一起思考。
```

没有必要回答所有的提问。“都不对”、“只喜欢这里”、“还不清楚”、“这里想交给你”、“到这里就足够了”等反馈，也都可以直接传达。

## Nehori 的推进方式

1. 把握起点。 利用本次的目的、使用场景以及已知条件，仅询问会对提案产生重大改变的缺失信息。
2. 沿两条路径思考。 将把明确提出的期望具体化的路径，与探索其他解读或相邻可能性路径相结合。
3. 提供具体方案。 不仅告知名称，还会传达使用场景、契合的理由以及取决于条件的要点。你可以不选择任何方案，也可以仅部分采纳，或者全部拒绝。
4. 根据反应重新调整。 不仅接收选择，还接收理由、犹豫、违和感及追加条件，以此决定是扩展还是收窄。
5. 在有用的地方及时打住。 一旦形成了表达期望的词语或选择标准，就会连同未决定的事项一并呈交。不以持续提问本身为目的。

两条路径并不意味着每次都要启动两个子 Agent。仅在满足环境权限、模型及成本条件时进行委派，除此之外将由一名助手共同考量两条路径。与用户交流的倾听者始终只有一人。

## 在搜索之前，会先确认内容

在检索外部的实例或商品时，会提示目的、搜索词示例、对象与信息源以及首次调查的阶段节点，获得同意后再进行搜索。探索角色也会继承相同的授权范围。

在同一计划内对搜索词进行同义改写，无需每次都重新确认。如果将范围扩大到口碑或视频等，则会展示追加内容并再次等待同意。这不仅包含搜索工具，从浏览器或 URL 获取信息也属于受控对象。读取已提供的本地资料不需要此搜索许可。

## 安装方法

本仓库除了技能主体外，还包含介绍文本和用于公开的辅助文件。要安装的是 `skills/nehori/` 文件夹。

### 请 AI 帮你安装（推荐）

把本 README 的页面 URL 或解压后的仓库位置交给具有文件操作权限的 AI，再提出以下请求：

```text
请安装本仓库的 skills/nehori/，使我能在当前 AI 环境中使用它。
先阅读 README 和 SKILL.md，再根据 AI 产品和操作系统，将包含参考资料的整个文件夹放入相应的用户级技能目录。
如果已有同名技能，请先确认，不要直接覆盖。
不要更改无关技能或身份验证设置。安装后，请确认并报告安装位置和调用方法。
```

没有文件操作权限的普通聊天无法自动在你的电脑上安装文件。这种情况下，请使用下面的手动安装方法。

手动安装前，请先下载并解压仓库，在仓库根目录运行以下命令。如果已有同名技能，请在替换前备份，不要把一个 `nehori/` 文件夹嵌套在另一个里面。如果你在 WSL 中运行 AI，请在 WSL 内使用 macOS / Linux 命令，安装到 Linux 的主目录，而不是 Windows 的主目录。

### Codex

在 Codex CLI 或 IDE 扩展中使用用户级技能时，请将 `skills/nehori/` 放到 `~/.agents/skills/nehori/`。

macOS / Linux:

```sh
mkdir -p ~/.agents/skills
cp -R skills/nehori ~/.agents/skills/nehori
```

Windows（PowerShell）:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.agents\skills" | Out-Null
Copy-Item -LiteralPath ".\skills\nehori" -Destination "$env:USERPROFILE\.agents\skills\nehori" -Recurse
```

安装后可通过 `/skills` 确认，并在请求中加入 `$nehori`。如果没有检测到技能，请重启 Codex。

```text
$nehori 请详细询问我想要什么。
```

仅在本项目中使用时，请放到 `.agents/skills/nehori/`。也可以向内置的 `$skill-installer` 提供本仓库的 URL 和 `skills/nehori/` 路径，请它代为安装。

参考：[OpenAI 官方技能安装文档](https://learn.chatgpt.com/docs/build-skills)。

### Claude Code

在本地 Claude Code 会话中使用用户级技能时，请将 `skills/nehori/` 放到 `~/.claude/skills/nehori/`。

macOS / Linux:

```sh
mkdir -p ~/.claude/skills
cp -R skills/nehori ~/.claude/skills/nehori
```

Windows（PowerShell）:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -LiteralPath ".\skills\nehori" -Destination "$env:USERPROFILE\.claude\skills\nehori" -Recurse
```

在 Claude Code 中使用 `/nehori` 调用。

```text
/nehori 请详细询问我想要什么。
```

仅在本项目中使用时，请放到 `.claude/skills/nehori/`。如果找不到技能，请检查安装位置并重新开启 Claude Code 会话。

参考：[Claude Code 官方技能安装文档](https://code.claude.com/docs/en/skills)。

### OMP

macOS / Linux:

```sh
mkdir -p ~/.omp/agent/skills
cp -R skills/nehori ~/.omp/agent/skills/nehori
```

Windows（PowerShell）:

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.omp\agent\skills" | Out-Null
Copy-Item -LiteralPath ".\skills\nehori" -Destination "$env:USERPROFILE\.omp\agent\skills\nehori" -Recurse
```

在新的对话中，请求 `使用Nehori，请详细询问我`。如果 OMP 的技能命令已启用，也可以通过 `/skill:nehori` 来调用。

如果仅在项目内部使用，请将 `skills/nehori/` 放置在该项目的 `.omp/skills/nehori/` 中。

### 其他支持 Agent Skills 的环境

请将 `skills/nehori/` 放置在所用环境指定的技能目录中。支持技能格式与自动触发或工具权限以同样方式运作是两回事。请遵循具体环境的导入步骤。

技能指令目前以日语维护。请将希望对话使用的语言告知助手。Nehori 不会固定对话的语言、语气或人设。

## 技能结构

主文件负责原则及其理由、对话流程、外部搜索前的许可和信任边界。参考资料只在需要时读取。

| 文件 | 作用 |
|---|---|
| [SKILL.md](skills/nehori/SKILL.md) | 通用对话步骤和判断标准 |
| [exploration.md](skills/nehori/references/exploration.md) | 两个探索角色的输入、返回内容及整合方法 |
| [dialogue-patterns.md](skills/nehori/references/dialogue-patterns.md) | 适合不同咨询类型的提问方式和回复示例 |
| [conversation-map.md](skills/nehori/references/conversation-map.md) | 区分用户发言、意向、解释和未定事项，并确定下一步 |
| [research-notes.md](skills/nehori/references/research-notes.md) | 设计依据、来历和转用的局限 |

对话地图仅用于整理当前对话，并不是自动保存的个人档案。当用户希望寻找具体候选项，而且已有足够条件区分这些选项时，Nehori 会转向候选项或搜索计划，而不是继续追问。

## 不做的事与局限性

- 不会进行心理诊断、读心、潜在意识测量，以及引导购买的劝说。
- 这个技能不会要求角色扮演，也不会强制特定的语气。
- 对于商品名称、价格和性能，会严格区分已确认的信息与想象中的示例。不会用对使用者偏好的提问来替代对专业知识的确认。
- 不会将私人发言直接作为搜索词发送到外部。也不会要求在未获得同意的情况下永久保存新的个人画像或对话记录。
- 关于对话质量、文化差异以及长期负担，并不保证通过对比实验证明的效果。结果会因模型和使用环境而异。

## 来历

灵感来自 [imozuru](https://github.com/MaryCache/imozuru) 顺藤摸瓜式的探索方法以及两个入口的设计。Nehori 是重新编写的技能，将对象从外部信息转向与用户本人的对话，在提案与修正之间往复。它不是 imozuru 的 Fork，也不将 imozuru 作为必需依赖。imozuru 本身也是一款很出色的技能。

设计时参考了倾听、UX 访谈、通过比较使偏好具体化以及提案型服务等内容。但这并不意味着人类在访谈或服务中的经验已被证实能在 AI 上产生完全相同的效果。另请参考[设计的依据与局限性](skills/nehori/references/research-notes.md)。

## 许可证与发布

[MIT License](LICENSE)。变更历史记录位于 [CHANGELOG.md](CHANGELOG.md)，分发 ZIP 包的创建和上传至 GitHub 的步骤位于 [PUBLISHING.md](PUBLISHING.md)。
