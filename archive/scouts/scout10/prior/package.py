"""Verify and package scout09 without replacing any earlier delivered artifact."""
from pathlib import Path
import hashlib,json,shutil,zipfile
root=Path(__file__).resolve().parent
out=Path('/mnt/data/fresh_after_singlet_scout09_2026-10-05.zip')
note=Path('/mnt/data/fresh_after_singlet_scout09_2026-10-05.md')
if out.exists() or note.exists():raise FileExistsError('Choose new delivery paths; do not overwrite artifacts.')
sha=lambda b:hashlib.sha256(b).hexdigest()
record=json.loads((root/'RUN_RECORD.json').read_text())
for item in record['exact_report_comparisons']:
 assert (root/item['current']).read_bytes()==(root/item['reference_or_repeat']).read_bytes()
prior=json.loads((root/'prior/MANIFEST.json').read_text())
for name,item in prior.items():
 data=(root/'prior'/name).read_bytes();assert len(data)==item['bytes'] and sha(data)==item['sha256']
for name,item in record['inputs_pinned_read_only'].items():
 data=(Path('/mnt/data')/name).read_bytes();assert len(data)==item['bytes'] and sha(data)==item['sha256']
files={}
for p in sorted(root.rglob('*')):
 if not p.is_file() or '__pycache__' in p.parts:continue
 if p.suffix.lower() in {'.pdf','.pyc','.ttf','.otf','.woff','.woff2'}:raise ValueError(f'Unexpected publication/font/bytecode file: {p}')
 files[p.relative_to(root).as_posix()]=p.read_bytes()
manifest={n:{'sha256':sha(b),'bytes':len(b)} for n,b in files.items()}
with zipfile.ZipFile(out,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for n,b in files.items():z.writestr(n,b)
 z.writestr('MANIFEST.json',json.dumps(manifest,indent=2,sort_keys=True)+'\n')
with zipfile.ZipFile(out) as z:
 assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))
 for n,item in manifest.items():
  b=z.read(n);assert len(b)==item['bytes'] and sha(b)==item['sha256']
shutil.copyfile(root/'SCOUT_09.md',note)
print(json.dumps(dict(note=str(note),archive=str(out),archive_sha256=sha(out.read_bytes()),archive_bytes=out.stat().st_size,manifest_files=len(manifest),all_hashes_verified=True,prior_files_unchanged=len(prior)),indent=2))
