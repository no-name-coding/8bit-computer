def assemble_to_bin(input_file="code.txt", output_file="rom.bin"):
    output_bytes = []
    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("//"):
                continue
            parts = line.split()
            if len(parts) != 4:
                continue
            try:
                numbers = [int(x) for x in parts]
            except ValueError:
                continue
            if any(n < 0 or n > 255 for n in numbers):
                continue
            output_bytes.extend(numbers)
    with open(output_file, "wb") as f:
        f.write(bytearray(output_bytes))
    print(f"Fertig! {len(output_bytes)} Bytes geschrieben in {output_file}")
if __name__ == "__main__":
    assemble_to_bin()
