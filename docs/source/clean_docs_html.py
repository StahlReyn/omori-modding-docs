import re
import subprocess

# --- CONFIGURATION ---
input_html = "input.html"
output_rst = "raw_output.rst"
# ---------------------

# STEP 1: Pre-process HTML with structural string anchors
with open(input_html, "r", encoding="utf-8") as f:
    html_content = f.read()

def replace_img(match):
    img_path = match.group(1)
    # Use a unique text flag that Pandoc will convert as plain text safely
    return f" RSTMIDDLERIMAGE {img_path} RSTMIDDLEREND "

clean_html = re.sub(r'<img[^>]*?src="([^"]+)"[^>]*>', replace_img, html_content)

staging_html = "sequential_staging.html"
with open(staging_html, "w", encoding="utf-8") as f:
    f.write(clean_html)

print("1. HTML structural placeholders created.")

# STEP 2: Execute Pandoc programmatically
print("2. Running Pandoc conversion...")
subprocess.run([
    "pandoc", "-f", "html", "-t", "rst", 
    staging_html, "-o", output_rst
], check=True)

# STEP 3: Post-process the RST file to build the valid multi-line syntax
with open(output_rst, "r", encoding="utf-8") as f:
    rst_content = f.read()

# Pattern matches our custom text block and its internal image path
pattern = r"RSTMIDDLERIMAGE\s+(\S+)\s+RSTMIDDLEREND"

def build_valid_rst_image(match):
    img_path = match.group(1)
    # This explicitly generates the strict multi-line formatting needed for RST
    return f"\n.. image:: {img_path}\n   :align: center\n"

final_rst_content = re.sub(pattern, build_valid_rst_image, rst_content)

with open(output_rst, "w", encoding="utf-8") as f:
    f.write(final_rst_content)

print(f"3. Success! Valid multi-line layout written to '{output_rst}'")
