from ftb_snbt_lib.tag import Byte, Short, Integer, Long, Float, Double, String, List, Array, Compound, Bool
import ftb_snbt_lib as slib
from typing import Any, Dict, List as ListType, Union
from pyhocon import ConfigFactory, HOCONConverter
import json

def parse_snbt(file):
    return slib.load(open(file, "r", encoding="utf-8"))

def snbt_to_dict(snbt_obj: Any) -> Union[Dict[str, Any], ListType[Any], int, float, str, bool]:
    #Yes, this is vibe coded, but it works and it isn't incomprehensible.
    if isinstance(snbt_obj, Compound):
        return {str(key): snbt_to_dict(value) for key, value in snbt_obj.items()}
    if isinstance(snbt_obj, (List, Array)):
        return [snbt_to_dict(item) for item in snbt_obj]
    if isinstance(snbt_obj, (Byte, Short, Integer, Long)):
        return int(snbt_obj)
    if isinstance(snbt_obj, (Float, Double)):
        return float(snbt_obj)
    if isinstance(snbt_obj, String):
        return str(snbt_obj)
    if isinstance(snbt_obj, Bool):
        return bool(snbt_obj)
    return snbt_obj

def snbt_file_to_dict(f):
    return snbt_to_dict(parse_snbt(f))

def conf_file_to_dict(f):
    with open("world.conf", "r", encoding="utf-8") as f:
        return json.loads(HOCONConverter.to_json(ConfigFactory.parse_string(f.read())))

#print(snbt_file_to_dict("./uploads/25d68b12-f38b-42ff-8adc-0afc7ffe85b6.snbt"))
print(conf_file_to_dict("world.conf"))