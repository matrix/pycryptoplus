import importlib.util
import pathlib

path = pathlib.Path(__file__).parents[2] / "Crypto/Util/number.py"
code = path.read_text()

# patch
code = code.replace("L", "")
code = code.replace("from _number_new import *", "")
code = code.replace("from _number import *", "")

module = {}
exec(code, module)

globals().update(module)
