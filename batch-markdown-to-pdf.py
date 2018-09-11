work_dir_str = "~/Downloads/测试目录/"

from pathlib import Path
import os

work_dir = Path(work_dir_str)
work_dir = work_dir.expanduser()

export_pdf_dir = work_dir / 'pdf'
# print(export_pdf_dir)
if not export_pdf_dir.exists():
    export_pdf_dir.mkdir()

for md_file in list(work_dir.glob('*.md')):
    # print(md_file)
    # print(type(md_file))
    md_file_name = md_file.name
    # print(md_file_name)
    pdf_file_name = md_file_name.replace('.md', '.pdf')
    # print(pdf_file_name)
    pdf_file = export_pdf_dir / pdf_file_name
    # print(pdf_file)
    # cmd = "pandoc '{}' -o '{}' --pdf-engine=xelatex -V mainfont='PingFang SC'".format(md_file, pdf_file)
    # cmd = "pandoc '{}' -o '{}' --pdf-engine=xelatex -V mainfont='PingFang SC' --template=pm-template.latex".format(md_file, pdf_file)
    cmd = "pandoc '{}' -o '{}' --pdf-engine=xelatex -V mainfont='PingFang SC' --template=template.tex".format(md_file, pdf_file)
    os.system(cmd)