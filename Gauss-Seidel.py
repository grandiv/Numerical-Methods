def f1(x, y, z):
    return (7.85 + 0.1 * y + 0.2 * z) / 3

def f2(x, y, z):
    return (-19.3 - 0.1 * x + 0.3 * z) / 7

def f3(x, y, z):
    return (71.4 - 0.3 * x + 0.2 * y) / 10

x0, y0, z0 = 0, 0, 0
e1, e2, e3 = 1, 1, 1  # Inisialisasi e1, e2, e3 dengan nilai yang lebih besar dari e (tolerable error)
count = 1

e = float(input("Enter tolerable error:\n"))

print("\nCount\tx\ty\tz")
while e1 > e or e2 > e or e3 > e:
    # Calculation
    x1 = f1(x0, y0, z0)
    y1 = f2(x1, y0, z0)
    z1 = f3(x1, y1, z0)
    

    # Error
    e1 = abs(x0 - x1)
    e2 = abs(y0 - y1)
    e3 = abs(z0 - z1)

    if count > 1 and e1 <= e and e2 <= e and e3 <= e:
        break  # Hentikan loop jika hasil sudah konvergen

    # Set value for next iteration
    x0 = x1
    y0 = y1
    z0 = z1
    print(f"{count}\t{x1:.4f}\t{y1:.4f}\t{z1:.4f}")
    count += 1

print(f"\nSolution: x={x1:.3f}, y={y1:.3f}, and z={z1:.3f}")