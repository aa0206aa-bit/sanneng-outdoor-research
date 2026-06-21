#!/usr/bin/env python3
"""報告品質驗證腳本 — 對應 CLAUDE.md 規則"""

import re
import sys

REPORT = "2026-06-18-三能戶外市場研究報告.md"

def load(path):
    with open(path, encoding="utf-8") as f:
        return f.readlines()

def check_unmarked_numbers(lines):
    """數字聲明必須標 ✅ 或 ⚠️"""
    pattern = re.compile(r"(?<![`\\])(NT\$[\d,]+|[\d,]+\s*(?:億|萬|%|元|人|處|倍))")
    skip = re.compile(r"^\s*[|#>\-`]|✅|⚠️|❌|來源|附錄|validate")
    errors = []
    for i, line in enumerate(lines, 1):
        if skip.search(line):
            continue
        matches = pattern.findall(line)
        if matches and "✅" not in line and "⚠️" not in line and "❌" not in line:
            errors.append((i, line.rstrip(), matches))
    return errors

def check_chapter_format(lines):
    """主章節（##）格式：## N｜標題（English）"""
    pattern = re.compile(r"^## \d+")
    valid = re.compile(r"^## [\d.]+[｜|].*（[A-Za-z &/,\-]+）")
    errors = []
    for i, line in enumerate(lines, 1):
        if pattern.match(line) and not valid.match(line):
            errors.append((i, line.rstrip()))
    return errors

def check_source_refs(lines):
    """附錄來源表的編號必須與正文引用一致"""
    ref_defined = set(re.findall(r"^\|\s*(\d+)\s*\|", "".join(lines), re.MULTILINE))
    ref_cited = set(re.findall(r"\[來源\s*(\d+)\]", "".join(lines)))
    missing = ref_cited - ref_defined
    return sorted(missing)

def run():
    try:
        lines = load(REPORT)
    except FileNotFoundError:
        print(f"❌ 找不到檔案：{REPORT}")
        sys.exit(1)

    total_errors = 0

    # 1. 未標記數字
    unmarked = check_unmarked_numbers(lines)
    if unmarked:
        print(f"\n⚠️  未標記數字聲明（{len(unmarked)} 處）：")
        for ln, text, matches in unmarked[:5]:
            print(f"  行 {ln:>4}｜{', '.join(matches)} → {text[:60]}")
        if len(unmarked) > 5:
            print(f"  … 還有 {len(unmarked)-5} 處")
        total_errors += len(unmarked)
    else:
        print("✅ 數字標記：全部合規")

    # 2. 章節格式
    bad_chapters = check_chapter_format(lines)
    if bad_chapters:
        print(f"\n⚠️  章節格式不符（{len(bad_chapters)} 處）：")
        for ln, text in bad_chapters:
            print(f"  行 {ln:>4}｜{text}")
        total_errors += len(bad_chapters)
    else:
        print("✅ 章節格式：全部合規")

    # 3. 來源引用
    missing_refs = check_source_refs(lines)
    if missing_refs:
        print(f"\n⚠️  引用了未定義的來源編號：{missing_refs}")
        total_errors += len(missing_refs)
    else:
        print("✅ 來源引用：全部合規")

    print(f"\n{'❌ 發現 '+str(total_errors)+' 個問題，需修正' if total_errors else '✅ 全部通過，報告符合 CLAUDE.md 規範'}")
    sys.exit(1 if total_errors else 0)

if __name__ == "__main__":
    run()
