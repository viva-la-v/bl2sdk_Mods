'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GLES2 import _types as _cs
# End users want this...
from OpenGL.raw.GLES2._types import *
from OpenGL.raw.GLES2 import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GLES2_EXT_texture_cube_map_array'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GLES2,'GLES2_EXT_texture_cube_map_array',error_checker=_errors._error_checker)
GL_IMAGE_CUBE_MAP_ARRAY_EXT=_C('GL_IMAGE_CUBE_MAP_ARRAY_EXT',0x9054)
GL_INT_IMAGE_CUBE_MAP_ARRAY_EXT=_C('GL_INT_IMAGE_CUBE_MAP_ARRAY_EXT',0x905F)
GL_INT_SAMPLER_CUBE_MAP_ARRAY_EXT=_C('GL_INT_SAMPLER_CUBE_MAP_ARRAY_EXT',0x900E)
GL_SAMPLER_CUBE_MAP_ARRAY_EXT=_C('GL_SAMPLER_CUBE_MAP_ARRAY_EXT',0x900C)
GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW_EXT=_C('GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW_EXT',0x900D)
GL_TEXTURE_BINDING_CUBE_MAP_ARRAY_EXT=_C('GL_TEXTURE_BINDING_CUBE_MAP_ARRAY_EXT',0x900A)
GL_TEXTURE_CUBE_MAP_ARRAY_EXT=_C('GL_TEXTURE_CUBE_MAP_ARRAY_EXT',0x9009)
GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY_EXT=_C('GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY_EXT',0x906A)
GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY_EXT=_C('GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY_EXT',0x900F)
