from pathlib import Path
from html import escape

def render_html(markdown_text):
    body=[]
    for line in markdown_text.splitlines():
        if line.startswith("# "): body.append(f"<h1>{escape(line[2:])}</h1>")
        elif line.startswith("## "): body.append(f"<h2>{escape(line[3:])}</h2>")
        elif line.startswith("**") and line.endswith("**"): body.append(f"<p><strong>{escape(line.strip("*"))}</strong></p>")
        elif line.strip(): body.append(f"<p>{escape(line)}</p>")
    return "<!doctype html><html><head><meta charset='utf-8'><title>Master AI Business Playbook</title><style>body{font-family:system-ui;max-width:900px;margin:40px auto;padding:0 20px;line-height:1.6}h1,h2{line-height:1.2}</style></head><body>"+''.join(body)+"</body></html>"

def write_html(markdown_text, path):
    Path(path).write_text(render_html(markdown_text),encoding="utf-8")
