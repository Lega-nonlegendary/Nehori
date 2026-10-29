# Nehori

[English](README.md) | 日本語 | [简体中文](README.zh-CN.md)

**まだ言葉になっていない希望を、提案を見ながら具体的にするAIスキル。**

「何が欲しいのか、うまく説明できない」「何かが欲しいけど、具体的にどういうものを選べばいいのか分からない」。そんなときに、Nehoriは有効です。これを導入することで、AIがまるで専属の付き人のように、貴方の願いを絞り込む話術を修得してくれます。

質問だけで答えを求めず、具体案や小さな見本を見せ、その反応から次の提案を組み替えます。

## 質問するだけの対話と、何が違う？

希望が曖昧な段階では、「条件を教えて」と聞かれても答えにくいことがあります。Nehoriは、答えを持っていることを前提にせず、比べられる案を用意します。

たとえば、「仕事にも休日にも使える鞄が欲しい。でも堅い仕事用にはしたくない」という希望なら、形を一つに決めつけず、二つの案を見せます。その案への「この部分は近い」「両方とも違う」「その二つを混ぜたい」という反応が、次に探す手がかりになります。

例を見て初めて生まれた希望も、以前から持っていた希望と区別しながら扱い、より的確な提案を目指します。

## 使い方

```text
Nehoriを使って、根掘り葉掘り聞いてほしい。
休日に使う鞄が欲しいけれど、まだ具体的な形が浮かばない。
```

```text
この案に違和感があるので、私に詳しく聞いてほしい。
何が引っ掛かっているのか、提案を見ながら整理したい。
```

```text
作りたい画面の雰囲気を、比較できる例を出しながら一緒に考えてほしい。
```

全部の質問に答える必要はありません。「どれも違う」「ここだけ好き」「まだ分からない」「ここは任せたい」「ここで十分」も、そのまま伝えられます。

## Nehoriの進め方

1. **起点をつかむ。** 今回の目的、使う場面、既に分かっている条件を使い、提案を大きく変える不足だけを聞きます。
2. **二つの経路で考える。** 明示された希望を具体化する経路と、別の解釈や隣接する可能性を探す経路を組み合わせます。
3. **具体案を渡す。** 名前だけでなく、使う場面、合う理由、条件次第の点を伝えます。案を選ばず、部分的に採用したり、全部断ったりしても構いません。
4. **反応から組み替える。** 選択だけでなく、理由、迷い、違和感、追加条件を受け取り、広げるか絞るかを決めます。
5. **役に立つところで区切る。** 希望を表す言葉や選ぶ基準ができたら、未決定も含めて返します。質問の継続そのものを目的にしません。

二つの経路は、毎回二つのサブエージェントを起動するという意味ではありません。環境の権限・モデル・費用の条件を満たす場合だけ委任し、それ以外は一人のアシスタントが二経路を検討します。ユーザーと話す聞き手は一人です。

## 検索する前に、内容を確認します

外部の実例や商品を調べる場合は、**目的、検索語の例、対象と情報源、最初の調査の区切り**を示し、了承を待ってから検索します。探索役にも同じ許可範囲を引き継ぎます。

同じ計画内の検索語の言い換えまで、毎回確認し直す必要はありません。口コミや動画などへ範囲を広げる場合は、追加内容を示して再び了承を待ちます。検索ツールだけでなく、ブラウザやURLからの取得も対象です。提供済みのローカル資料を読むことには、この検索許可は不要です。

## 入れ方

このリポジトリには、スキル本体のほかに紹介文と公開用の補助ファイルが入っています。**インストールするのは `skills/nehori/` フォルダーです。**

### AIに導入を依頼する（おすすめ）

ファイル操作ができるAIに、このREADMEのページURL、または解凍したリポジトリの場所を渡し、次のように依頼します。

```text
このリポジトリの skills/nehori/ を、今使っているAI環境で使えるように導入してください。
最初にREADMEとSKILL.mdを読み、AI製品とOSに合ったユーザー用スキルディレクトリへ、参照資料を含むフォルダー全体を配置してください。
既に同名のスキルがあれば、上書きせずに確認してください。
無関係なスキルや認証設定は変更せず、導入後に配置先と呼び出し方を確認して報告してください。
```

ファイル操作の権限がない通常のチャットだけでは、PCへの自動導入はできません。その場合は、以下の手動導入を使ってください。

手動で導入する場合は、リポジトリをダウンロードして展開し、そのルートで以下のコマンドを実行します。既に同名のスキルがある場合は、置き換える前にバックアップし、フォルダーを二重に入れないでください。WSLでAIを動かす場合は、Windows側ではなくWSL側のホームに、macOS / Linuxの手順で配置します。

### Codex

Codex CLIやIDE拡張のユーザー用スキルとして使う場合は、`skills/nehori/` を `~/.agents/skills/nehori/` に配置します。

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

導入後は `/skills` で確認し、`$nehori` を付けて依頼できます。検出されない場合はCodexを再起動してください。

```text
$nehori 私が望んでいるものについて、詳しく聞いてください。
```

このプロジェクト内だけで使う場合は `.agents/skills/nehori/` に置きます。組み込みの `$skill-installer` に、このリポジトリのURLと対象の `skills/nehori/` を伝えて導入を依頼する方法もあります。

参照：[OpenAI公式のスキル導入手順](https://learn.chatgpt.com/docs/build-skills)。

### Claude Code

ユーザー用スキルとして使う場合は、`skills/nehori/` を `~/.claude/skills/nehori/` に配置します。

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

Claude Codeで `/nehori` を使って呼び出せます。

```text
/nehori 私が望んでいるものについて、詳しく聞いてください。
```

このプロジェクト内だけで使う場合は `.claude/skills/nehori/` に置きます。見つからない場合は、配置先を確認してClaude Codeのセッションを開き直してください。

参照：[Claude Code公式のスキル導入手順](https://code.claude.com/docs/en/skills)。

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

新しい会話で、`Nehoriを使って、私に詳しく聞いてほしい` と頼みます。OMPのスキルコマンドが有効なら、`/skill:nehori` でも呼び出せます。

プロジェクト内だけで使う場合は、`skills/nehori/` を、そのプロジェクトの `.omp/skills/nehori/` に置きます。

### その他のAgent Skills対応環境

`skills/nehori/` を、利用する環境が指定するスキル用ディレクトリに配置してください。スキル形式を受け付けることと、自動発動やツールの権限が同じように動くことは別です。環境固有の導入手順に従ってください。

指示本文は現在、日本語で管理しています。希望する会話の言語はアシスタントに伝えてください。Nehoriは会話の言語・口調・人物像を固定しません。

## しないこと・限界

- 心理診断、読心、潜在意識の測定、購入へ誘導する説得は行いません。
- 役を演じたり、特定の口調を強制したりするスキルではありません。
- 商品名・価格・性能は、確認した情報と想像上の見本を区別します。専門知識の確認を、本人の好みへの質問で代用しません。
- 私的な発言をそのまま検索語として外部へ送りません。新しい個人プロファイルや会話記録を、了承なく永続保存することも求めません。
- 対話品質、文化差、長期的な負担について、比較実験による効果を保証するものではありません。モデルや利用環境で結果は変わります。

## 来歴

[imozuru](https://github.com/MaryCache/imozuru)の、手がかりをたどる探索手段と二つの入口から着想を得ています。対象を外部情報から本人との対話へ移し、提案と訂正を往復する方法として、新しく記述したスキルです。imozuruのフォークや必須依存ではありませんが、こちらも素晴らしいスキルです。

傾聴、UX面接、比較による選好の具体化、提案型の接客などを設計の参考にしています。人間の面接や接客の知見が、そのままAIで同じ効果を持つと実証されたわけではありません。[設計の根拠と限界](skills/nehori/references/research-notes.md)も参照してください。

## ライセンスと公開

[MIT License](LICENSE)。変更履歴は [CHANGELOG.md](CHANGELOG.md)、配布ZIPの作成とGitHubへのアップロード手順は [PUBLISHING.md](PUBLISHING.md) にあります。
