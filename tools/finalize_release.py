#!/usr/bin/env python3
from pathlib import Path
import hashlib, sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT/"KAZF55_T1w.nii.gz",
    ROOT/"KAZF55_brainmask.nii.gz",
    ROOT/"KAZF55_MPM.nii.gz",
    ROOT/"KAZF55_labels.tsv",
    ROOT/"README.md",
    ROOT/"transforms"/"KAZF55_to_MNI152_0GenericAffine.mat",
    ROOT/"transforms"/"KAZF55_to_MNI152_1Warp.nii.gz",
    ROOT/"transforms"/"KAZF55_to_MNI152_1InverseWarp.nii.gz",
]
missing=[p for p in required if not p.exists()]
probs=sorted((ROOT/"probability_maps").glob("KAZF55_prob_*.nii.gz"))

if missing:
    print("ERROR: missing required files:")
    for p in missing: print(" -", p.relative_to(ROOT))
    sys.exit(1)
if len(probs)!=18:
    print(f"ERROR: expected 18 probability maps, found {len(probs)}")
    sys.exit(1)

for p in ROOT.rglob("*"):
    if p.is_file() and "AKZ" in p.name.upper():
        print("ERROR: possible participant-ID file:", p.relative_to(ROOT))
        sys.exit(1)

def sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024), b""): h.update(b)
    return h.hexdigest()

files=[]
for p in ROOT.rglob("*"):
    if not p.is_file(): continue
    rel=p.relative_to(ROOT)
    if rel.parts[0] in {".git","tools"}: continue
    if p.name in {".gitkeep","LICENSE_NOTICE.md","SHA256SUMS.txt"}: continue
    files.append(p)

with (ROOT/"SHA256SUMS.txt").open("w",encoding="utf-8") as f:
    for p in sorted(files,key=lambda x:str(x.relative_to(ROOT))):
        f.write(f"{sha(p)}  {p.relative_to(ROOT)}\n")

print("Release validation passed.")
print("18 probability maps found.")
print("Required template/mask/MPM/transforms found.")
print("SHA256SUMS.txt generated.")
print("Reminder: add final LICENSE only after author/PI approval.")
