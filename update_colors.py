import os
import re

directory = "/Users/hemanthkancharla/Documents/zewotech/UP/UPTRADERS/src"

replacements = [
    (re.compile(r"#D61A3C", re.IGNORECASE), "#106935"), # main red to green
    (re.compile(r"#D81B24", re.IGNORECASE), "#106935"), # dark red to green
    (re.compile(r"#ff474f", re.IGNORECASE), "#15803d"), # light red to lighter green
    (re.compile(r"brand-red", re.IGNORECASE), "brand-green"), # tailwind class
]

for root, _, files in os.walk(directory):
    for file in files:
        if not (file.endswith(".jsx") or file.endswith(".js") or file.endswith(".css")):
            continue
        filepath = os.path.join(root, file)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            for pattern, repl in replacements:
                new_content = pattern.sub(repl, new_content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated colors in: {filepath}")
        except Exception as e:
            print(f"Error processing {filepath}: {e}")

