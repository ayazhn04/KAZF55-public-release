# KAZF55

KAZF55 is a female-specific T1-weighted structural MRI template developed from 55 cognitively healthy Kazakh women. This repository is intended to distribute the group-level KAZF55 atlas resources described in the accompanying manuscript. It does **not** contain individual participant MRI data.

## Release contents

### Atlas images
- `KAZF55_T1w.nii.gz` — final 1 mm isotropic KAZF55 T1-weighted template.
- `KAZF55_brainmask.nii.gz` — binary brain mask in KAZF55 template space.
- `KAZF55_MPM.nii.gz` — maximum-probability anatomical label map.
- `probability_maps/KAZF55_prob_<Structure>.nii.gz` — 18 structure-wise probability maps.

### KAZF55 ↔ MNI152 transforms
- `transforms/KAZF55_to_MNI152_0GenericAffine.mat`
- `transforms/KAZF55_to_MNI152_1Warp.nii.gz`
- `transforms/KAZF55_to_MNI152_1InverseWarp.nii.gz`

These transforms correspond to the brain-restricted KAZF55–MNI152 registration used in the manuscript's standard-space compatibility analyses and are intended for use within brain support.

### Documentation
- `KAZF55_labels.tsv` — label identifier to anatomical structure mapping.
- `SHA256SUMS.txt` — SHA-256 checksums generated after all final release files are staged.
- `LICENSE` — to be added only after the project authors/PI confirm the final license.

## Spaces and image format
The KAZF55 template and atlas products are distributed as NIfTI files at 1 mm isotropic resolution. `KAZF55_MPM.nii.gz`, the probability maps, and `KAZF55_brainmask.nii.gz` are defined in KAZF55 space. The MNI152 transform files correspond to the MNI152 ICBM 2009c reference used in the manuscript.

## Typical use
Register a T1-weighted MRI to `KAZF55_T1w.nii.gz` using a volumetric registration workflow. Use nearest-neighbor interpolation for anatomical labels. The provided KAZF55↔MNI152 transforms can move group-level images or label maps between KAZF55 and MNI152 space.

## Integrity verification
After the complete release is assembled:

```bash
sha256sum -c SHA256SUMS.txt
```

On macOS:

```bash
shasum -a 256 -c SHA256SUMS.txt
```

## Data availability
Only group-level atlas resources are distributed here. Individual participant T1-weighted MRI data are not included.

## Citation
A formal citation will be added after the KAZF55 manuscript is accepted/published.

Working manuscript title:

> KAZF55: A Female-Specific Structural MRI Template Correcting Registration Bias from Population and Sex Mismatch in the Kazakh Population

## Contact
Srinivasa Rao Bolla, PhD  
Nazarbayev University  
`srinivasa.bolla@nu.edu.kz`

## License
CC BY 4.0 has been proposed for the public atlas release, but the final license should be added only after author/PI approval.
