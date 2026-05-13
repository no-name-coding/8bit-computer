CODES = {
    #ALU
    "NOOP": 0,
    "ADD": 1,
    "SUB": 2,
    "AND": 3,
    "OR": 4,
    "XOR": 5,
    "NOT": 6,
    "SHL": 7,
    "SHR": 8,
    #Num°
    "SET": 16,
    "SETR": 17,
    "SETRA": 18,
    #Reg°
    "SAVR": 32,
    "SAVRA": 33,
    #°Reg
    "RAM1": 48,
    "RAM2": 49,
    "key": 56,
    #control
    "JMP": 64,
    "JMPI": 65,
    #vgl
    "EQ": 80,
    "NEQ": 81,
    "SMAL": 82,
    "BIG": 83,
    "keyp": 88,
    #display
    #audio
    #IO
    "nxkey": 128,
    #logic
    "fNOT": 144,
    "fAND": 145,
    "fOR": 146,
    "fXOR": 147
}


def parse_value(value):
    if value in CODES:
        return CODES[value]
    return int(value)
def assemble_to_bin(input_file, output_file):
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
                numbers = [parse_value(x) for x in parts]
            except (ValueError, KeyError):
                continue
            if any(n < 0 or n > 255 for n in numbers):
                continue
            output_bytes.extend(numbers)
    with open(output_file, "wb") as f:
        f.write(bytearray(output_bytes))
    print(f"Fertig! {len(output_bytes)} Bytes geschrieben in {output_file}")
if __name__ == "__main__":
    FILEfrom = input("von") + ".txt"
    FILEto = input("nach") + ".bin"
    assemble_to_bin(FILEfrom,FILEto)
