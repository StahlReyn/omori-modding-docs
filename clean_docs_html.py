import re
import subprocess
from pathlib import Path

# --- CONFIGURATION ---
INPUT_HTML = Path("input.html")
OUTPUT_DIR = Path("docs/source")
CHAPTERS_DIR = OUTPUT_DIR / "chapters"
STAGING_HTML = Path("sequential_staging.html")
TEMP_MASTER_RST = Path("temp_master.rst")
# ---------------------


def ensure_output_structure() -> None:
    CHAPTERS_DIR.mkdir(parents=True, exist_ok=True)


def prepare_html_with_placeholders(html_content: str) -> str:
    def replace_img(match: re.Match[str]) -> str:
        return f" RSTMIDDLERIMAGE {match.group(1)} RSTMIDDLEREND "

    return re.sub(r'<img[^>]*?src="([^"]+)"[^>]*>', replace_img, html_content)


def write_staging_file(clean_html: str, staging_path: Path) -> None:
    staging_path.write_text(clean_html, encoding="utf-8")


def run_pandoc(staging_path: Path, output_rst_path: Path) -> None:
    print("Step 2: Running Pandoc HTML-to-RST conversion...")
    subprocess.run(
        ["pandoc", "-f", "html", "-t", "rst", str(staging_path), "-o", str(output_rst_path)],
        check=True,
    )


def restructure_rst_images(rst_content: str) -> str:
    def build_valid_rst_image(match: re.Match[str]) -> str:
        img_path = match.group(1)
        fixed_path = img_path if img_path.startswith("../") else f"../{img_path}"
        return f"\n\n.. image:: {fixed_path}\n   :align: center\n\n"

    pattern = r"RSTMIDDLERIMAGE\s+(\S+)\s+RSTMIDDLEREND"
    return re.sub(pattern, build_valid_rst_image, rst_content)


def move_images_folder(output_dir: Path) -> None:
    source_images = Path("images")
    target_images = output_dir / "images"
    if source_images.exists() and not target_images.exists():
        source_images.rename(target_images)


def split_into_chapters(rst_content: str, chapters_dir: Path) -> tuple[list[str], list[str]]:
    print("Step 4: Splitting document by Top-Level Headings...")
    chapter_blocks = re.split(r"\n(?=[^\n]+\n={3,}\n)", rst_content)

    chapter_paths: list[str] = []
    chapter_titles: list[str] = []

    for idx, block in enumerate(chapter_blocks):
        block_stripped = block.strip()
        if not block_stripped:
            continue

        lines = block_stripped.split("\n")
        heading_text = lines[0].strip()

        safe_name = re.sub(r"[^a-z0-9]+", "_", heading_text.lower()).strip("_")
        if not safe_name:
            safe_name = f"section_{idx}"

        filename = f"{safe_name}.rst"
        filepath = chapters_dir / filename

        filepath.write_text(block_stripped + "\n", encoding="utf-8")

        chapter_paths.append(f"chapters/{safe_name}")
        chapter_titles.append(heading_text)
        print(f" -> Generated: {filepath}")

    return chapter_paths, chapter_titles


def write_index_file(index_path: Path, chapter_paths: list[str], chapter_titles: list[str]) -> None:
    print("Step 5: Compiling master index.rst...")
    if chapter_titles and ("_" in chapter_paths[0] or len(chapter_titles[0]) > 60):
        main_title = "Documentation Workspace"
    else:
        main_title = chapter_titles[0] if chapter_titles else "Documentation Project"

    toctree_links = "\n   ".join(chapter_paths)
    index_template = f"""{main_title}
{"=" * len(main_title)}

.. toctree::
   :maxdepth: 2
   :caption: Table of Contents:

   {toctree_links}
"""

    index_path.write_text(index_template, encoding="utf-8")


def cleanup_temp_files(*paths: Path) -> None:
    for path in paths:
        if path.exists():
            path.unlink()


def main() -> None:
    ensure_output_structure()

    print("Step 1: Embedding image structural placeholders...")
    html_content = INPUT_HTML.read_text(encoding="utf-8")
    clean_html = prepare_html_with_placeholders(html_content)
    write_staging_file(clean_html, STAGING_HTML)

    run_pandoc(STAGING_HTML, TEMP_MASTER_RST)

    print("Step 3: Restructuring images into multi-line RST layout...")
    rst_content = TEMP_MASTER_RST.read_text(encoding="utf-8")
    fixed_rst_content = restructure_rst_images(rst_content)

    move_images_folder(OUTPUT_DIR)

    chapter_paths, chapter_titles = split_into_chapters(fixed_rst_content, CHAPTERS_DIR)
    write_index_file(OUTPUT_DIR / "index.rst", chapter_paths, chapter_titles)

    cleanup_temp_files(STAGING_HTML, TEMP_MASTER_RST)

    print("\nProcessing complete! Your Sphinx documentation tree is ready inside './source/'")


if __name__ == "__main__":
    main()

