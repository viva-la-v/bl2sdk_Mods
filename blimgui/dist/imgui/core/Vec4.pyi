# encoding: utf-8
# module imgui.core
# from C:\Users\justi\AppData\Local\Programs\Python\Python37-32\lib\site-packages\imgui\core.cp37-win32.pyd
# by generator 1.147
"""
.. todo:: consider inlining every occurence of ``_cast_args_ImVecX`` (profile)
.. todo: verify mem safety of char* variables and check for leaks
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # C:\Users\justi\AppData\Local\Programs\Python\Python37-32\lib\warnings.py
from itertools import izip_longest


from .tuple import tuple

class Vec4(tuple):
    """ Vec4(x, y, z, w) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new OrderedDict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new Vec4 object from a sequence or iterable """
        pass

    def _replace(_self, **kwds): # reliably restored by inspect
        """ Return a new Vec4 object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, x, y, z, w): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, x, y, z, w): # reliably restored by inspect
        """ Create new instance of Vec4(x, y, z, w) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    w = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 3"""

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 0"""

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 1"""

    z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 2"""


    _fields = (
        'x',
        'y',
        'z',
        'w',
    )
    _fields_defaults = {}
    _field_defaults = {}
    __slots__ = ()

