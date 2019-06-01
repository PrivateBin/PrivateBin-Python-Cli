import json, ntpath, os, zlib
from base64 import b64encode, b64decode

class PBinCLIException(Exception):
    pass


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def check_readable(f):
    # Checks if path exists and readable
    if not os.path.exists(f) or not os.access(f, os.R_OK):
        raise PBinCLIException("Error accessing path: {}".format(f))


def check_writable(f):
    # Checks if path is writable
    if not os.access(os.path.dirname(f) or ".", os.W_OK):
        raise PBinCLIException("Path is not writable: {}".format(f))


def decompress(s):
     return zlib.decompress(s, -zlib.MAX_WBITS)


def compress(s):
     # using compressobj as compress doesn't let us specify wbits
     # needed to get the raw stream without headers
     co = zlib.compressobj(wbits=-zlib.MAX_WBITS)
     return co.compress(s) + co.flush()



def json_encode(d):
    return json.dumps(d, separators=(',',':')).encode()
