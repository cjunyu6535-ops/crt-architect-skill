#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CRT-Architect 7-in-1 Word (.docx) Exporter Script
OpenAI Codex CLI Skill Integration script for exporting CRT lesson plans.

Usage:
    python3 scripts/export_crt_docx.py --input lesson.json --output output.docx
    python3 scripts/export_crt_docx.py --demo
"""

import argparse
import json
import os
import sys

try:
    import docx
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Inches, Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
except ImportError:
    pass


def create_omath_fraction(num_text, den_text):
    """
    Creates an OpenXML Math (m:oMath) vertical fraction element.
    """
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


def add_math_paragraph(doc, text_before, num, den, text_after=""):
    """
    Adds a paragraph with standard inline math formatting and vertical fraction.
    """
    p = doc.add_paragraph()
    if text_before:
        p.add_run(text_before)
    
    fraction_xml = create_omath_fraction(num, den)
    p._p.append(fraction_xml)
    
    if text_after:
        p.add_run(text_after)
    return p


def generate_crt_docx(data, output_path):
    """
    Generates a 7-in-1 Word (.docx) teaching package based on CRT & EdPsych standards.
    """
    doc = docx.Document()
    
    # Document Title
    title = doc.add_heading(data.get("unit_title", "文化回應課程協作 (CRT-Architect) 7合1教學包"), level=0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # 1. 單元基本資訊與 CRT 理念
    h1 = doc.add_heading("1. 單元基本資訊與 CRT 理念", level=1)
    p1 = doc.add_paragraph()
    p1.add_run("【科目領域】").bold = True
    p1.add_run(f" {data.get('subject', '跨領域 / 數學與多元文化')}\n")
    p1.add_run("【適用年級】").bold = True
    p1.add_run(f" {data.get('grade', '國小高年級 / 國中七年級')}\n")
    p1.add_run("【文化脈絡】").bold = True
    p1.add_run(f" {data.get('cultural_context', '花蓮在地文化與臺灣多元族群實踐')}\n")
    p1.add_run("【CRT核心理念】").bold = True
    p1.add_run(f" {data.get('crt_concept', '融合 Banks 多元文化教育理念與高期望支持學習環境')}")
    
    # 2. 三面九項素養與 108 課綱條目
    h2 = doc.add_heading("2. 三面九項素養與 108 課綱條目", level=1)
    p2 = doc.add_paragraph()
    p2.add_run("• 核心素養：A2 系統思考與解決問題、B1 符號運用與溝通表達、C2 團隊合作與多元理解\n")
    p2.add_run("• 學習表現 / 內容條目：數-E-A1, 社-E-C2, 原住民族文化回應教學指標")

    # 3. 教學目標與 TSEL 情意指標
    h3 = doc.add_heading("3. 教學目標與 TSEL 情意指標", level=1)
    p3 = doc.add_paragraph()
    p3.add_run("• 認知目標：理解比例與垂直分數 (例如：")
    add_math_paragraph(doc, "代表比例：", "3", "4", " 意涵)\n")
    p3.add_run("• 情意指標 (TSEL)：發展社會情緒學習與文化認同感\n")
    p3.add_run("• 技能目標：能運用 Unicode 數學符號 (×, ÷, ±, ≠, ≤, ≥, π, √) 進行精確運算與圖表說明")

    # 4. 教案設計與黃金時間分配 (Prime-Time 1 & 2)
    h4 = doc.add_heading("4. 教案設計與黃金時間分配 (Prime-Time 1 & 2)", level=1)
    p4 = doc.add_paragraph()
    p4.add_run("• Prime-Time 1 (前10-15分鐘)：引起動機與高注意力學習 (文化情境導入)\n")
    p4.add_run("• Down-Time (中間15-20分鐘)：探究與小組互動實作\n")
    p4.add_run("• Prime-Time 2 (後10分鐘)：總結、反思與後設認知整合")

    # 5. 高互動探究策略與防微歧視檢核
    h5 = doc.add_heading("5. 高互動探究策略與防微歧視檢核", level=1)
    p5 = doc.add_paragraph()
    p5.add_run("• 探究策略：鷹架提問、同儕協作與文化回應對話\n")
    p5.add_run("• 防微歧視檢核：避免單一文化偏見與刻板印象，確保多元視角平等呈現")

    # 6. 多元評量與表現性任務量規
    h6 = doc.add_heading("6. 多元評量與表現性任務量規", level=1)
    table = doc.add_table(rows=3, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = '評量面向'
    hdr_cells[1].text = '優良 (4分)'
    hdr_cells[2].text = '基礎 (2分)'
    
    row1 = table.rows[1].cells
    row1[0].text = '文化理解'
    row1[1].text = '能深入剖析在地文化並提出創新觀點'
    row1[2].text = '能描述文化基本概念'
    
    row2 = table.rows[2].cells
    row2[0].text = '數學溝通'
    row2[1].text = '正確運用分數與符號表達概念'
    row2[2].text = '基本數學運算表達'

    # 7. 學習單、教師引導與修復觸發機制
    h7 = doc.add_heading("7. 學習單、教師引導與修復觸發機制", level=1)
    p7 = doc.add_paragraph()
    p7.add_run("• 學生學習單：包含問題探究、運算區與學習歷程記錄\n")
    p7.add_run("• 教師引導卡：針對不同學習風格提供彈性鷹架\n")
    p7.add_run("• 修復觸發機制：當同儕溝通出現文化誤解時，引導修復式對話與情緒支持")

    doc.save(output_path)
    print(f"Successfully exported 7-in-1 CRT Word document to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="CRT-Architect 7-in-1 Word Exporter")
    parser.add_argument("--input", "-i", type=str, help="Path to input JSON file containing lesson plan data")
    parser.add_argument("--output", "-o", type=str, default="output.docx", help="Path to output .docx file")
    parser.add_argument("--demo", action="store_true", help="Generate a demo CRT 7-in-1 .docx document")
    
    args = parser.parse_args()
    
    if args.demo or not args.input:
        demo_data = {
            "unit_title": "【CRT-Architect】花蓮部落傳統建築與數學比例 7合1教學包",
            "subject": "數學與原住民族文化回應教學",
            "grade": "國小六年級 / 國中七年級",
            "cultural_context": "花蓮太魯閣族與阿美族傳統建築家屋與竹編幾何結構",
            "crt_concept": "結合 Banks 多元文化理論 (Content Integration, Equity Pedagogy) 與 TSEL 社會情緒學習"
        }
        generate_crt_docx(demo_data, args.output)
    else:
        if os.path.exists(args.input):
            with open(args.input, "r", encoding="utf-8") as f:
                data = json.load(f)
            generate_crt_docx(data, args.output)
        else:
            print(f"Error: Input file '{args.input}' not found.", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
