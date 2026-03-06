import builtins

# Python2 compatibility layer for PyCrypto
if not hasattr(builtins, "xrange"):
    builtins.xrange = range

if not hasattr(builtins, "long"):
    builtins.long = int

if not hasattr(builtins, "basestring"):
    builtins.basestring = str

try:
    from Crypto.Cipher import ARC4, XOR
except ImportError:
    try:
        from Crypto.Cipher import ARC4
        XOR = None
    except ImportError:
        ARC4 = None
        XOR = None

__all__ = ["AES","python_AES","python_DES","python_DES3","DES","DES3","Blowfish","python_Blowfish","python_Twofish","python_Serpent","python_Rijndael","ARC4","ARC2","CAST","XOR","python_PRESENT"]

try:
        import Crypto.Cipher.IDEA
        __all__.append("IDEA")
        __all__.append("RC5")
except ImportError:
        pass
