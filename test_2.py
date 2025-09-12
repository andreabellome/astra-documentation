import os
import re

# Input: folder containing your MATLAB .m files
MATLAB_SRC = "C:/Users/andre/Documents/GitHub/astra/ASTRA"
# Output: where to put the markdown docs (inside your mkdocs project)
DOCS_OUT = "docs/matlab"

os.makedirs(DOCS_OUT, exist_ok=True)

function_pattern = re.compile(
    r"^\s*function\s+(?:\[(.*?)\]|(\w+))?\s*=\s*(\w+)\((.*?)\)", re.IGNORECASE
)
section_headers = ["DESCRIPTION", "DESCRIPTION:", "INPUT", "INPUT:", "INPUTS:", "INPUTS", "OUTPUTS:", "OUTPUT", "OUTPUT:", "PROCESS", "FUNCTION CALLS", "FUNCTION CALLS:"]

def parse_matlab_file(filepath):
    """Parse a MATLAB .m file to extract function signature and structured docstring."""
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    func_name, inputs, outputs = None, None, None
    doc_sections = {key: [] for key in section_headers}

    in_section = None
    for line in lines:
        # Match function signature
        match = function_pattern.match(line)
        if match and not func_name:
            outputs = match.group(1) or match.group(2) or ""
            func_name = match.group(3)
            inputs = match.group(4) or ""

        # Stop reading comments at the separator
        if line.strip().startswith("% ---"):
            break

        # Process docstring
        if line.strip().startswith("%"):
            content = line.strip("%").strip()
            if not content:
                continue

            upper = content.split()[0].upper()
            if upper in section_headers:
                in_section = upper
                continue

            if in_section:
                doc_sections[in_section].append(content)

    return {
        "name": func_name,
        "inputs": inputs,
        "outputs": outputs,
        "doc": doc_sections,
    }

def generate_markdown(func_info, outdir):
    """Generate a Markdown file for one function."""
    if not func_info["name"]:
        return None

    os.makedirs(outdir, exist_ok=True)
    filename = os.path.join(outdir, f"{func_info['name']}.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# `{func_info['name']}`\n\n")

        # Add structured doc sections
        for section, lines in func_info["doc"].items():
            if lines:
                f.write(f"## {section}\n")
                f.write("\n".join(lines))
                f.write("\n\n")

        # Add function signature
        f.write("## Function Signature\n")
        signature = f"{func_info['name']}({func_info['inputs']})"
        if func_info["outputs"]:
            signature = f"[{func_info['outputs']}] = " + signature
        f.write(f"```matlab\n{signature}\n```\n")

    return filename

# --- Main script ---
nav_tree = {}

for root, _, files in os.walk(MATLAB_SRC):
    rel_dir = os.path.relpath(root, MATLAB_SRC)
    out_dir = os.path.join(DOCS_OUT, rel_dir if rel_dir != "." else "")
    for file in files:
        if file.endswith(".m"):
            func_info = parse_matlab_file(os.path.join(root, file))
            md_file = generate_markdown(func_info, out_dir)
            if md_file:
                rel_path = os.path.relpath(md_file, DOCS_OUT)
                parts = rel_path.split(os.sep)
                current = nav_tree
                for p in parts[:-1]:
                    current = current.setdefault(p, {})
                current[parts[-1]] = func_info["name"]

def write_index(tree, parent_path="", indent=0):
    """Recursively write index entries for nav tree with correct relative paths."""
    lines = []
    for key in sorted(tree.keys()):
        val = tree[key]
        if isinstance(val, dict):
            lines.append("  " * indent + f"- {key}/")
            sub_path = os.path.join(parent_path, key)
            lines.extend(write_index(val, sub_path, indent + 1))
        else:
            rel_path = os.path.join(parent_path, key).replace("\\", "/")
            lines.append("  " * indent + f"- [{val}](./{rel_path})")
    return lines

with open(os.path.join(DOCS_OUT, "index.md"), "w", encoding="utf-8") as f:
    f.write("# MATLAB Functions\n\n")
    f.write("Browse the automatically generated documentation:\n\n")
    f.write("\n".join(write_index(nav_tree)))
    f.write("\n")

def write_nav_yaml(tree, parent_path="matlab"):
    """Recursively generate MkDocs nav YAML structure."""
    nav = []
    for key in sorted(tree.keys()):
        val = tree[key]
        if isinstance(val, dict):
            nav.append({key: write_nav_yaml(val, os.path.join(parent_path, key).replace("\\", "/"))})
        else:
            rel_path = os.path.join(parent_path, key).replace("\\", "/")
            nav.append({val: rel_path})
    return nav

import yaml

with open("mkdocs-nav.yml", "w", encoding="utf-8") as f:
    yaml.dump([{"MATLAB API": write_nav_yaml(nav_tree)}], f, sort_keys=False)