import os
import re

directory = "/Users/hemanthkancharla/Documents/zewotech/UP/UPTRADERS/src"

# Regex to match <span></span> or <p></p> with any class names, optionally surrounded by whitespace
replacements = [
    (re.compile(r"^\s*<span[^>]*>\s*</span>\s*$\n", re.MULTILINE), ""),
    (re.compile(r"^\s*<p[^>]*>\s*</p>\s*$\n", re.MULTILINE), ""),
]

for root, _, files in os.walk(directory):
    for file in files:
        if not file.endswith(".jsx"):
            continue
        filepath = os.path.join(root, file)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            for pattern, repl in replacements:
                new_content = pattern.sub(repl, new_content)
            
            # also remove literal string "SUPER MARKET" without tags just in case
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Cleaned empty tags: {filepath}")
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

