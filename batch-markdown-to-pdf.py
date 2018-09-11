work_dir_str = "~/Downloads/测试目录/"

from pathlib import Path
import os

work_dir = Path(work_dir_str)
work_dir = work_dir.expanduser()

export_pdf_dir = work_dir / 'pdf'
if not export_pdf_dir.exists():
    export_pdf_dir.mkdir()

for md_file in list(work_dir.glob('*.md')):
    md_file_name = md_file.name
    pdf_file_name = md_file_name.replace('.md', '.pdf')
    pdf_file = export_pdf_dir / pdf_file_name
    cmd = "pandoc '{}' -o '{}' --pdf-engine=xelatex -V mainfont='PingFang SC' --template=template.tex".format(md_file, pdf_file)
    os.system(cmd)