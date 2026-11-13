import lzma, os
_d = os.path.dirname(os.path.abspath(__file__))
_p = os.path.join(_d, 'p.bin')
if not os.path.exists(_p):
    _p = 'p.bin'
exec(lzma.decompress(open(_p, 'rb').read()))
