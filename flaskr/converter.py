import ftb_snbt_lib as slib
from ftb_snbt_lib.tag import Compound, ByteArray, IntArray, LongArray, Bool, String, List as TagList

def parse_snbt(file):
    return slib.load(open(file, "r", encoding="utf-8"))

def snbt_to_python(snbt_obj):
    if isinstance(snbt_obj, dict):  # Compound
        return {k: snbt_to_python(v) for k, v in snbt_obj.items()}
    elif isinstance(snbt_obj, list):  # List or Array
        return [snbt_to_python(item) for item in snbt_obj]
    else:  # Primitive types
        if isinstance(snbt_obj, str):
            return 



c = parse_snbt("./uploads/25d68b12-f38b-42ff-8adc-0afc7ffe85b6.snbt")

print(snbt_to_python(c))