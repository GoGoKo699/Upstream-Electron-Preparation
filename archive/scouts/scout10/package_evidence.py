"""Package the present fixed-candidate audit and unchanged scout09 evidence."""
from pathlib import Path
import hashlib,json,shutil,zipfile

root=Path(__file__).resolve().parent
out=Path('/mnt/data/fresh_after_singlet_scout10_2026-10-05.zip')
note=Path('/mnt/data/fresh_after_singlet_scout10_2026-10-05.md')
if out.exists() or note.exists():raise FileExistsError('Refuse to overwrite an existing delivered artifact.')
record=json.loads((root/'RUN_RECORD.json').read_text())
for pair in record['exact_comparisons']:
    assert (root/pair['current']).read_bytes()==(root/pair['reference_or_repeat']).read_bytes()
manifest_old=json.loads((root/'prior/MANIFEST.json').read_text())
for name,item in manifest_old.items():
    b=(root/'prior'/name).read_bytes()
    assert len(b)==item['bytes'] and hashlib.sha256(b).hexdigest()==item['sha256']
assert record['new_scientific_failures']==0
files={}
for p in sorted(root.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts:continue
    if p.suffix.lower() in {'.pdf','.pyc','.ttf','.otf','.woff','.woff2'}:continue
    files[p.relative_to(root).as_posix()]=p.read_bytes()
manifest={name:{'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)} for name,data in files.items()}
with zipfile.ZipFile(out,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for name,data in files.items():z.writestr(name,data)
    z.writestr('MANIFEST.json',json.dumps(manifest,indent=2,sort_keys=True)+'\n')
with zipfile.ZipFile(out) as z:
    assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))
    for name,item in manifest.items():
        b=z.read(name)
        assert len(b)==item['bytes'] and hashlib.sha256(b).hexdigest()==item['sha256']
shutil.copyfile(root/'SCOUT_10.md',note)
print(json.dumps(dict(note=str(note),archive=str(out),archive_sha256=hashlib.sha256(out.read_bytes()).hexdigest(),archive_bytes=out.stat().st_size,members=len(files)+1,prior_manifest_entries_unchanged=len(manifest_old),all_hashes_verified=True),indent=2))
