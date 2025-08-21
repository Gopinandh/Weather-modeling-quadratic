# Predict temperature by reading a single set of inputs from a file
# File format (inputs_single.txt):
# line1: a
# line2: b
# line3: c
# line4: t

def predict_temp(a, b, c, t):
    return a * t**2 + b * t + c

def read_single(path):
    with open(path, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    if len(lines) < 4:
        raise ValueError("inputs_single.txt must contain at least 4 lines (a, b, c, t).")
    a = float(lines[0])
    b = float(lines[1])
    c = float(lines[2])
    t = float(lines[3])
    return a, b, c, t

if __name__ == "__main__":
    a, b, c, t = read_single("inputs_single.txt")
    T = predict_temp(a, b, c, t)
    print(f"Predicted temperature at t={t}: {T:.2f}°C")
