# Predict temperature using hardcoded coefficients
# T(t) = a*t^2 + b*t + c

def predict_temp(a, b, c, t):
    return a * t**2 + b * t + c

if __name__ == "__main__":
    a = 0.5
    b = -3
    c = 28
    t = 5  # e.g., 5th hour or 5th day
    T = predict_temp(a, b, c, t)
    print(f"Predicted temperature at t={t}: {T:.2f}°C")
