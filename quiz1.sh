Jordan Shore
JordanShore
gunzip -c ~/Code/MCB185/data/dictionary.gz | grep -E -v "[^ozniacr]" | grep -E "r+"  | grep -E ".{4,}"
