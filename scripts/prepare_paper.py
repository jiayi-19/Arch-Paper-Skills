#!/usr/bin/env python3
"""Copy an author-provided template into a new independent writing workspace."""
import argparse
from pathlib import Path
import shutil


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--template',required=True,type=Path);p.add_argument('--out',required=True,type=Path)
    a=p.parse_args();source=a.template.resolve();target=a.out.absolute()
    if not source.is_dir():p.error('Template must be a directory')
    if target.exists() or target.is_symlink():p.error('Output must not already exist')
    if target.resolve().is_relative_to(source):p.error('Output must be outside the source template')
    if any(x.is_symlink() for x in source.rglob('*')):p.error('Resolve source symlinks explicitly before copying the template')
    shutil.copytree(source,target,ignore=shutil.ignore_patterns('.git','.env','__pycache__','*.pyc','.venv','node_modules','*.aux','*.log','*.out','*.fls','*.fdb_latexmk'))
    print(target)

if __name__=='__main__':main()
