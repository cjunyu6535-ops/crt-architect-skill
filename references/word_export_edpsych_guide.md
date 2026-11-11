# 教育心理學與純正數學排版 Word .docx 終極匯出規範

## 1. 認知負荷理論視覺分塊與鷹架設計
- **降低外在認知負荷 (Extranous Cognitive Load)**：採用清爽、結構化視覺分塊（標題、醒目提示框、表格）。
- **優化內在認知負荷 (Intrinsic Cognitive Load)**：提供漸進式鷹架 (Scaffolding)，將複雜概念拆解為步驟與小組合作。
- **促進精細認知負荷 (Germane Cognitive Load)**：引導反思與深層概念整合。

## 2. 嚴禁殘留原始 LaTeX 語法與純正 Unicode 數學符號
- 匯出 Word (.docx) 時，嚴禁直接呈現 `\frac{a}{b}`、`\sqrt{x}` 等原始 LaTeX 語法字串。
- 內文數學運算符號統一替換為純正 Unicode 數學符號（如 `×`、`÷`、`±`、`≠`、`≤`、`≥`、`π`、`√`）。

## 3. OpenXML Math `m:oMath` 直式分數 Python 輔助函式
```python
import docx
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def create_omath_fraction(num_text, den_text):
    """建立 OpenXML Math (m:oMath) 直式分數結構"""
    omath = OxmlElement('m:oMath')
    f = OxmlElement('m:f')
    
    num = OxmlElement('m:num')
    r_num = OxmlElement('m:r')
    t_num = OxmlElement('m:t')
    t_num.text = str(num_text)
    r_num.append(t_num)
    num.append(r_num)
    
    den = OxmlElement('m:den')
    r_den = OxmlElement('m:r')
    t_den = OxmlElement('m:t')
    t_den.text = str(den_text)
    r_den.append(t_den)
    den.append(r_den)
    
    f.append(num)
    f.append(den)
    omath.append(f)
    return omath
```

## 4. 7 合 1 完整 Word 教學包標準章節結構
1. **單元基本資訊與 CRT 理念**
2. **三面九項素養與 108 課綱條目**
3. **教學目標與 TSEL 情意指標**
4. **教案設計與黃金時間分配 (Prime-Time 1 & 2)**
5. **高互動探究策略與防微歧視檢核**
6. **多元評量與表現性任務量規**
7. **學習單、教師導引與修復觸發機制**
