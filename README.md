# 🧰 文化回應課程協作 v2.4.22 (CRT-Architect)

結合臺灣 108 課綱、Banks 多元文化理論、TSEL 與花蓮/台灣在地文化之高互動備課、健檢、實踐教練與教育心理學 Word (.docx) 匯出技能。

## 📦 安裝與使用說明 (OpenAI Codex / Agent Skills Standard)

本技能完全符合 OpenAI Codex CLI 與 Agent Skills Open Standard 規範。
# 🧰 文化回應課程協作 v2.4.22 (CRT-Architect)

結合臺灣 108 課綱、Banks 多元文化理論、TSEL 與花蓮/台灣在地文化之高互動備課、健檢、實踐教練與教育心理學 Word (.docx) 匯出技能。

## 📦 安裝與使用說明 (Installation & Usage Guides)

本技能完全符合 Agent Skills Open Standard 規範，支援 **Claude Code**、**OpenCode** 與 **OpenAI Codex CLI**。

---

### 1. Claude Code 安裝、配置與呼叫指南

#### 安裝路徑 (Installation Paths)
- **全域技能路徑**：`~/.claude/skills/crt-architect`
- **專案區域技能路徑**：`.claude/skills/crt-architect`

#### Git Clone 命令：
```bash
# 全域安裝
mkdir -p ~/.claude/skills
git clone <repository_url> ~/.claude/skills/crt-architect

# 專案區域安裝
mkdir -p .claude/skills
git clone <repository_url> .claude/skills/crt-architect
```

#### 呼叫指南 (Invocation)
在 Claude Code 對話介面或 CLI 中，可使用斜線指令或對話進行呼叫：
```bash
/crt-architect
```
或直接在對話中提示 Claude Code 載入並執行 `crt-architect` 技能進行課程設計與健檢。

---

### 2. OpenCode 安裝、配置與呼叫指南

#### 安裝路徑 (Installation Paths)
- **全域技能路徑**：`~/.config/opencode/skills/crt-architect`
- **專案區域技能路徑**：`.opencode/skills/crt-architect`

#### Git Clone 命令：
```bash
# 全域安裝
mkdir -p ~/.config/opencode/skills
git clone <repository_url> ~/.config/opencode/skills/crt-architect

# 專案區域安裝
mkdir -p .opencode/skills
git clone <repository_url> .opencode/skills/crt-architect
```

#### 呼叫指南 (Invocation)
在 OpenCode 中，技能會自動被環境識別與載入。可於對話中提示 OpenCode 使用 CRT-Architect 技能，或直接調用技能進行備課與診斷。

---

### 3. OpenAI Codex CLI 安裝、配置與呼叫指南

#### 安裝路徑 (Installation Paths)
- **全域技能路徑**：`~/.agents/skills/crt-architect`
- **專案區域技能路徑**：`.agents/skills/crt-architect` 或 `.codex/skills/crt-architect`

#### Git Clone 命令：
```bash
# 全域安裝
mkdir -p ~/.agents/skills
git clone <repository_url> ~/.agents/skills/crt-architect

# 專案區域安裝
mkdir -p .agents/skills
git clone <repository_url> .agents/skills/crt-architect
```

#### 呼叫指南 (Invocation)
安裝完成後，可直接於 OpenAI Codex CLI 對話中透過前綴 `$` 符號呼叫：
```bash
$crt-architect
```
或在對話中提示 Codex CLI 使用 CRT-Architect 技能進行互動式備課、教案檢驗與 Word 文件匯出。

### 1. 安裝路徑 (Installation Paths)

請將本技能儲存庫選定放置於以下任一相容路徑：

- **全域技能路徑**：
  `~/.agents/skills/crt-architect`
- **專案區域技能路徑 (推薦)**：
  `.agents/skills/crt-architect` 或 `.codex/skills/crt-architect`

#### Git Clone 命令：
```bash
# 安裝至專案區域技能目錄
mkdir -p .agents/skills
git clone <repository_url> .agents/skills/crt-architect

# 或安裝至全域技能目錄
mkdir -p ~/.agents/skills
git clone <repository_url> ~/.agents/skills/crt-architect
```

### 2. 在 OpenAI Codex CLI 呼叫技能 (Invocation)

安裝完成後，可直接於 OpenAI Codex / CLI 對話中透過前綴 `$` 符號呼叫：

```bash
$crt-architect
```

#### 預設 Prompt 範例：
> "呼叫文化回應課程協作，請協助我設計結合臺灣 108 課綱與花蓮在地文化的互動教案與學習單，並於確認後匯出為符合教育心理學與純正數學排版的 Word (.docx) 文件。"

### 3. Word (.docx) 7合1教學包自動化匯出 (Exporter Script)

Codex CLI 可直接透過以下 Python 腳本產出包含 OpenXML 原生數學公式 (`m:oMath`)、直式分數與教育心理學排版的 Word 7合1教學包：

```bash
# 透過示範資料產出 demo 7合1教學包
python3 scripts/export_crt_docx.py --demo --output demo_lesson.docx

# 透過自訂 JSON 教案檔產體
python3 scripts/export_crt_docx.py --input lesson.json --output lesson.docx
```

## 📂 檔案結構 (Repository Structure)

- `SKILL.md`：核心技能規範與工作流指南（符合 OpenAI Codex Frontmatter 規範）
- `agents/openai.yaml`：OpenAI Codex 專屬 UI metadata 與觸發策略設定
- `scripts/export_crt_docx.py`：Python 7合1 Word 匯出工具
- `references/`
  - `lookup_scoring_matrices.md`：免代碼三步查表計分矩陣
  - `taiwan_curriculum_and_urls.md`：108 課綱條目與相關資源連結
  - `hualien_crt_and_strategies.md`：花蓮在地文化資源與教學策略
  - `word_export_edpsych_guide.md`：Word 匯出與教育心理學視覺規範 (.docx) 匯出之 AI 備課與實踐教練技能
