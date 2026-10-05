"""Verify and package this standalone scout without rewriting earlier artifacts."""
from pathlib import Path
import hashlib,json,os,platform,re,shutil,subprocess,sys,zipfile
import numpy,scipy,sympy

root=Path(__file__).resolve().parent
out=Path('/mnt/data/fresh_after_singlet_scout08_2026-10-05.zip')
note=Path('/mnt/data/fresh_after_singlet_scout08_2026-10-05.md')
if out.exists() or note.exists():raise FileExistsError('Refuse to overwrite a delivered checkpoint.')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
first=json.loads((root/'evidence/first.json').read_text())
repeat=json.loads((root/'evidence/repeat.json').read_text())
assert first['status']==repeat['status']=='PASS' and first['tests_run']==repeat['tests_run']==6
assert (root/'evidence/first.json').read_bytes()==(root/'evidence/repeat.json').read_bytes()
old={}
for name in ('fresh_after_singlet_scout06_2026-10-05.md','fresh_after_singlet_scout06_2026-10-05.zip','fresh_after_singlet_scout07_2026-10-05.md','fresh_after_singlet_scout07_2026-10-05.zip'):
    p=Path('/mnt/data')/name
    old[name]={'sha256':sha(p),'bytes':p.stat().st_size,'role':'Read-only context, not imported scientific code or rerun evidence.'}
report=root/'evidence/repeat.json';before=sha(report)
p=subprocess.run([sys.executable,str(root/'check_pulse_reachability.py'),'--output',str(report)],capture_output=True,text=True,env={**os.environ,'TERM':'dumb','OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','PYTHONDONTWRITEBYTECODE':'1'})
assert p.returncode==2 and sha(report)==before
(root/'evidence/output_refusal.log').write_text(p.stdout+p.stderr)
source_records=[
 {'id':'I19','title':'Quantum percolation of monopole paths and the response of quantum spin ice','authors':'M. Stern, C. Castelnovo, R. Moessner, V. Oganesyan, S. Gopalakrishnan','url':'https://arxiv.org/abs/1911.05742','read':'Primary indexed abstract only.','boundary':'A coherent-diffusion predecessor for the generic screened question; no material or all spin-ice dynamics claim.'},
 {'id':'A25','title':'Tracking Adiabaticity in Non-Equilibrium Many-Body Systems: The Hard Case of the X-ray Photoemission in Metals','authors':'G. Diniz, F. D. Picoli, L. N. Oliveira, I. D’Amico','url':'https://arxiv.org/abs/2502.11313','publisher_url':'https://journals.aps.org/pra/abstract/10.1103/m17z-4g58','read':'Primary abstract and associated publisher abstract describing localized time-dependent scattering.','boundary':'No selected ramp theorem or claim every local adiabaticity problem is solved.'},
 {'id':'A22','title':'Bounds on quantum adiabaticity in driven many-body systems from generalized orthogonality catastrophe and quantum speed limit','authors':'J.-H. Chen and V. Cheianov','url':'https://journals.aps.org/prresearch/abstract/10.1103/PhysRevResearch.4.043055','read':'Primary abstract only.','boundary':'General overlap/adiabaticity context, not used in the pulse proof.'},
 {'id':'K06','title':'Minimal excitation states of electrons in one-dimensional wires','authors':'J. Keeling, I. Klich, L. S. Levitov','url':'https://arxiv.org/pdf/cond-mat/0604017','read':'Parsed author PDF v2, 6 June 2006; minimal excitations, phase construction, one-electron energy profile, equations (1)–(6). Requested page index1 screenshot failed.','boundary':'Minimal voltage-source class is inherited. No unrendered figure values or full source reanalysis.'},
 {'id':'G13','title':'Fractionalization of minimal excitations in integer quantum Hall edge channels','authors':'C. Grenier, J. Dubois, T. Jullien, P. Roulleau, D. C. Glattli, P. Degiovanni','url':'https://arxiv.org/pdf/1301.6777','read':'Parsed author PDF with v1 header: Section II minimality condition, equations (19)–(22) and coherent inputs in III.B, integer fractionalization text in IV.A, Appendix C. Requested page indices6 and8 screenshots failed.','boundary':'Full basic model, outgoing-voltage map, standard even-charge examples and periodic revivals are prior work. No unviewed numerical figure/table reproduction. General arbitrary-input classification is an author-side deduction, not a quoted new result.'},
 {'id':'E13','title':'Minimal-excitation states for electron quantum optics using levitons','authors':'J. Dubois et al.','url':'https://www.nature.com/articles/nature12713','read':'Primary abstract, 23 October 2013 publication record.','boundary':'Experimental context only, not demonstration of the inverse waveform or new threshold.'},
 {'id':'B25','title':'Eigenstate control of plasmon wavepackets with electron-channel blockade','authors':'S. Takada et al.','url':'https://www.nature.com/articles/s41467-025-64876-z','read':'Primary abstract and introductory account, publication12 November2025.','boundary':'Different circuit/mode intervention; not the fixed single-input model. No all-architectures no-go is claimed.'},
 {'id':'R21','title':'Processing Quantum Signals Carried by Electrical Currents','authors':'B. Roussel, C. Cabart, G. Fève, P. Degiovanni','url':'https://journals.aps.org/prxquantum/abstract/10.1103/PRXQuantum.2.020314','read':'Primary abstract only.','boundary':'Relevant control/coherence lead, not a completed construction-level novelty exclusion.'}
]
(root/'SOURCES.json').write_text(json.dumps({'date':'2026-10-05','records':source_records,'scope':'Targeted scout, not exhaustive priority or a completed five-to-ten-per-convention physical audit.','retrieval_limits':['Author HTML requests1301.6777v2 and1806.03897v2 failed; the readable G13 PDF supplied stated passages.','Web PDF screenshots of G13 indices6,8 and K06 index1 failed. Parsed equations/text were used, not unseen figure/table data.','Indexed DIPC author page surfaced Creation and characterization of leviton excitations in tight-binding chains with malformed arXiv2609.0782. Direct page access failed. No full-paper reading, corrected identifier or priority exclusion asserted.','Broad search produced many irrelevant electrical-product pages for the brand Leviton; none was used. Secondary/generated pages and failed searches are not absence evidence.','Other fractional-quantum-Hall leviton abstracts appeared but their different tunneling settings were not imported as coverage of this integer-edge source-control question.'],'exhaustive_priority':False,'independent_review':False,'apparatus_claim':False,'third_party_publications_included':False},indent=2,ensure_ascii=False)+'\n')
record={'date':'2026-10-05','scope':'Fresh scout08 after the Stark-pair checkpoint.','decision':'GO for one bounded finite-energy/finite-accuracy quantum-state test; no dedicated PRL project yet.','prior_mounted_context':old,'charter_scope':'Separation instructions in the current conversation; no absent charter file or prior archive was falsely described as reverified.','selected_model':'One controlled voltage input, two initially equilibrium integer edge channels, equal or near-equal lossless dispersionless collective-mode mixing, finite clean pulse target.','new_groups':6,'complete_scientific_runs':2,'first_and_repeat':'PASS','byte_identical_reports':True,'scientific_failures':0,'formula_or_tolerance_changes':False,'report_sha256':sha(report),'script_sha256':sha(root/'check_pulse_reachability.py'),'exclusive_output_refusal':{'returncode':p.returncode,'existing_bytes_preserved':True},'numerical_scope':'Small coherence kernels, finite coefficient identities and one-dimensional pulse/energy quadrature; no many-body Hilbert-space or cloud simulation.','source_reading_boundary':'Inherited minimal-excitation theorem and exact G13 transfer. Specific arbitrary-input parity/orbit and energy claims are proved author-side; no assertion they are absent from all literature.','not_claimed':['Forbidden odd net charge or charge2e quasiparticles','A no-go with two independently driven inputs','An obstruction for infinite periodic drives or time-gated detection','A finite-error electron-fidelity or hole-count lower bound','A complete dispersive, finite-temperature or implemented-device result','An independent scientific report or exhaustive priority certificate'],'next_decisive_test':'Meaningful finite-input-energy limitation on actual outgoing single-electron fidelity or hole contamination, with a precise closest-literature check. Stop if only an ideal singularity without physical significance or immediately inherited control result.','repositories_accessed':False,'repositories_modified':False,'repository_created':False,'external_contact':False,'manuscript_created':False}
(root/'RUN_RECORD.json').write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
(root/'environment.json').write_text(json.dumps({'python':sys.version,'platform':platform.platform(),'numpy':numpy.__version__,'scipy':scipy.__version__,'sympy':sympy.__version__,'BLAS_threads_for_scientific_runs':1},indent=2)+'\n')
files={}
for p in sorted(root.rglob('*')):
    if not p.is_file() or '__pycache__' in p.parts:continue
    if p.suffix.lower() in {'.pdf','.pyc','.ttf','.otf','.woff','.woff2'}:continue
    files[p.relative_to(root).as_posix()]=p.read_bytes()
manifest={name:{'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)}for name,data in files.items()}
with zipfile.ZipFile(out,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for name,data in files.items():z.writestr(name,data)
    z.writestr('MANIFEST.json',json.dumps(manifest,indent=2,sort_keys=True)+'\n')
with zipfile.ZipFile(out) as z:
    assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))
    for name,item in manifest.items():
        data=z.read(name);assert len(data)==item['bytes'] and hashlib.sha256(data).hexdigest()==item['sha256']
for name,item in old.items():
    p=Path('/mnt/data')/name;assert sha(p)==item['sha256'] and p.stat().st_size==item['bytes']
shutil.copyfile(root/'SCOUT_08.md',note)
print(json.dumps({'note':str(note),'archive':str(out),'sha256':sha(out),'bytes':out.stat().st_size,'manifest_members':len(files),'all_hashes_verified':True,'earlier_context_unchanged':True,'tests':6,'exact_repeat':True},indent=2))
