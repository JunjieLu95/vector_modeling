# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:55:47 2025

@author: Junjie
"""

import math
import pytest
from vector_modeling.vector import Vector, Vector3

def test_vector_add():
    v1 = Vector(1, 2, 3)
    v2 = Vector(13, 14, 15)
    result = v1 + v2
    assert result.coords == (14, 16, 18)

def test_vector_norm():
    v = Vector(3, 4)
    assert math.isclose(v.norm, 5)

def test_vector_dot():
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    assert v1.dot(v2) == 32

def test_vector3_cross():
    v3 = Vector3(1, 0, 0)
    v4 = Vector3(0, 1, 0)
    cross = v3.cross(v4)
    assert cross.coords == (0, 0, 1)

def test_is_vector_invalid_coordinate():
    with pytest.raises(TypeError):
        Vector('1', 'a', 3)
