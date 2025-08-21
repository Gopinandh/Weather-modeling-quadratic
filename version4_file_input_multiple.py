# Predict temperature by reading multiple sets of inputs from a file
# File format (inputs_multiple.txt):
# each line: a b c t  (space-separated)

def predict_temp(a, b, c, t):
    return a * t**2 + b * t + c

def process_file(path):
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            a, b, c, t = map(float, line.split())
            T = predict_temp(a, b, c, t)
            print(f"a={a}, b={b}, c={c}, t={t} -> T={T:.2f}°C")

if __name__ == "__main__":
    process_file("inputs_multiple.txt")
