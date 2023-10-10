# Un semnal este digitizat cu o frecventa de esantionare de 2000 Hz

# (a) Care este intervalul de timp intre doua esantioane?
freq = 2000 # Hz
interval = 1 / freq
print(f"Intervalul de timp dintre 2 esantioane, avand frecventa de 2000 Hz: {interval}")

# (b) Daca un esantion este memorat pe 4 biti, cati bytes vor ocupa 1 ora de achizitie?
num_bits = 4
# 1 h = 3600 s si 1 byte = 8 bits
num_bytes = num_bits * freq * 3600 / 8
print(f"bytes per ora: {num_bytes}")
