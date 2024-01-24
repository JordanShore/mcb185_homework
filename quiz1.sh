Jordan Shore
JordanShore
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep -E -v "[^ozniacr]" | grep -E "r+"  | grep -E ".{4,}"
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep -E -v "[^tairnlb]" | grep -E "b+"  | grep -E ".{4,}"
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep -E -v "[^maodinc]" | grep -E "c+"  | grep -E ".{4,}"
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep -E -v "[^anoigrz]" | grep -E "z+"  | grep -E ".{4,}"
gunzip -c jaspar2024_core.transfac.gz | grep tax | cut -d ":" -f 2 | sort | uniq -c 
