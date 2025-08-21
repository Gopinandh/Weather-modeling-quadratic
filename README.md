# Weather Modeling (Quadratic) — Stage-wise Implementations

This project demonstrates weather (temperature) prediction using a simple quadratic model:

	T(t) = a * t^2 + b * t + c

## Files
- `version1_hardcoded.py` — Hardcoded inputs.
- `version2_keyboard_input.py` — Keyboard input with validation.
- `version3_file_input_single.py` — Reads one set of inputs from `inputs_single.txt`.
- `version4_file_input_multiple.py` — Reads multiple sets from `inputs_multiple.txt`.
- `inputs_single.txt` — Example single input file (a, b, c, t on separate lines).
- `inputs_multiple.txt` — Example multi-input file (a b c t per line).

## Run (Windows / PowerShell)
```powershell
# Hardcoded
python version1_hardcoded.py

# Keyboard input
python version2_keyboard_input.py

# Single-file input
python version3_file_input_single.py

# Multi-file input
python version4_file_input_multiple.py
```

## Git Quick Start
1. Create repo on GitHub (do NOT initialize with README).
2. In this folder run:
   ```powershell
   git init
   git branch -M main
   git add .
   git commit -m "Initial commit - Weather Modeling Experiment"
   git remote add origin https://github.com/<YourUsername>/weather-model-quadratic.git
   git push -u origin main
   ```

If you have 2FA enabled on GitHub, use a **Personal Access Token** as the password when pushing via HTTPS.
