import os
import re
import yaml

# =========================
# CONFIG
# =========================
MATLAB_SRC = r"C:\Users\Andrea\Documents\GitHub\astra\ASTRA"
DOCS_OUT = r"docs\matlab"

os.makedirs(DOCS_OUT, exist_ok=True)

# =========================
# FUNCTION PARSER (robust)
# =========================
function_pattern = re.compile(
    r"^\s*function\s+(?:\[(.*?)\]|(\w+))?\s*=\s*(\w+)\s*\((.*?)\)",
    re.IGNORECASE
)

section_headers = {
    "DESCRIPTION", "INPUT", "INPUTS", "OUTPUT", "OUTPUTS",
    "EXAMPLES", "PROCESS", "FUNCTION CALLS"
}


def parse_matlab_file(filepath):
    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    func_name, inputs, outputs = None, None, None
    doc_sections = {key: [] for key in section_headers}

    in_section = None

    for line in lines:

        # detect function signature
        match = function_pattern.match(line)
        if match and not func_name:
            outputs = match.group(1) or match.group(2) or ""
            func_name = match.group(3)
            inputs = match.group(4) or ""

        # stop at code section separator
        if line.strip().startswith("% ---"):
            break

        # parse comments
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


# =========================
# MARKDOWN GENERATION
# =========================
def generate_markdown(func_info, outdir, filepath):
    os.makedirs(outdir, exist_ok=True)

    # fallback name for scripts or unparsed functions
    name = func_info["name"]
    if not name:
        name = os.path.splitext(os.path.basename(filepath))[0]

    filename = os.path.join(outdir, f"{name}.md")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# `{name}`\n\n")

        # doc sections
        for section, lines in func_info["doc"].items():
            if lines:
                f.write(f"## {section}\n")
                f.write("\n".join(lines) + "\n\n")

        # signature
        if func_info["inputs"] or func_info["outputs"]:
            f.write("## Function Signature\n")
            signature = f"{name}({func_info['inputs']})"
            if func_info["outputs"]:
                signature = f"[{func_info['outputs']}] = " + signature

            f.write("```matlab\n")
            f.write(signature + "\n")
            f.write("```\n")

    return filename, name


# =========================
# NAV TREE BUILDER
# =========================
nav_tree = {}

for root, _, files in os.walk(MATLAB_SRC):
    rel_dir = os.path.relpath(root, MATLAB_SRC)
    out_dir = os.path.join(DOCS_OUT, rel_dir if rel_dir != "." else "")

    for file in files:
        if not file.endswith(".m"):
            continue

        filepath = os.path.join(root, file)

        func_info = parse_matlab_file(filepath)

        md_file, name = generate_markdown(func_info, out_dir, filepath)

        rel_path = os.path.relpath(md_file, DOCS_OUT).replace("\\", "/")

        parts = rel_path.split("/")

        current = nav_tree
        for p in parts[:-1]:
            current = current.setdefault(p, {})

        current[parts[-1]] = name


# =========================
# INDEX PAGE
# =========================
def write_index(tree, parent_path="", indent=0):
    lines = []

    for key in sorted(tree.keys()):
        val = tree[key]

        if isinstance(val, dict):
            lines.append("  " * indent + f"- {key}/")
            lines.extend(write_index(val, parent_path + "/" + key, indent + 1))
        else:
            path = (parent_path + "/" + key).replace("//", "/")
            lines.append("  " * indent + f"- [{val}](./{path})")

    return lines


with open(os.path.join(DOCS_OUT, "index.md"), "w", encoding="utf-8") as f:
    f.write("# MATLAB Functions\n\n")
    f.write("\n".join(write_index(nav_tree)))


# =========================
# MKDOCS NAV YAML
# =========================
def write_nav_yaml(tree, base="matlab"):
    nav = []

    for key in sorted(tree.keys()):
        val = tree[key]

        if isinstance(val, dict):
            nav.append({
                key: write_nav_yaml(val, base + "/" + key)
            })
        else:
            path = (base + "/" + key).replace("\\", "/")
            nav.append({val: path})

    return nav


with open("mkdocs-nav.yml", "w", encoding="utf-8") as f:
    yaml.dump(
        {"nav": [{"MATLAB API": write_nav_yaml(nav_tree)}]},
        f,
        sort_keys=False
    )

print("Documentation + MkDocs nav generated successfully.")