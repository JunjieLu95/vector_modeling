# -*- coding: utf-8 -*-
"""
Create two Vector class for modeling vectors.

@author: jlu
"""

import math

class Vector:
    """Vector with an arbitrary number of coordinates.
    
    Parameters
    ----------
    *coords : int, float
        One or more values representing the coordinates of the vector.
    """
    
    def __init__(self, *coords):
        for coord in coords:
            if not isinstance(coord, (int, float)):
                raise TypeError("Input coordinate must be int or float")
                
        self._coords = tuple(coords)
    
    @property
    def coords(self):
        """Coordinates of the vector.
        
        Returns
        -------
        tuple
        """
        return self._coords
    
    @property
    def norm(self):
        """Magnitude of the vector.
        
        Returns
        -------
        float
        """
        squared = (x ** 2 for x in self.coords)
        return math.sqrt(sum(squared))
    
    def __repr__(self):
        return f"Vector{self._coords}"
    
    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            raise ValueError('Vectors should have same dimension for addition')
        new_coords = (a + b for a, b in zip(self.coords, other.coords))
        return Vector(*new_coords)
        
    def __sub__(self, other):
        if len(self.coords) != len(other.coords):
            raise ValueError('Vectors should have same dimension for substraction')
        new_coords = (a - b for a, b in zip(self.coords, other.coords))
        return Vector(*new_coords)
    
    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number")
        scaled = (x * scalar for x in self.coords)
        return Vector(*scaled)
        
    def dot(self, other):
        """Compute the dot product of two vectors.
        
        Both vectors must have the same dimension.
        
        Parameters
        ----------
        other : Vector
            The other vector to compute the dot product with.

        Returns
        -------
        float
            The dot product of the two vectors.

        """
        if len(self.coords) != len(other.coords):
            raise ValueError('Vectors should have same dimension for dot product')
        return sum(a * b for a, b in zip(self.coords, other.coords))


class Vector3(Vector):
    """3D vector subclass.

    Parameters
    ----------
    x : int, float
        The x-coordinate of the vector.
    y : int, float
        The y-coordinate of the vector.
    z : int, float
        The z-coordinate of the vector.
    """
    def __init__(self, x, y, z):
        super().__init__(x, y, z)
    
    @property
    def x(self):
        """First coordinate of the vector.
        
        Returns
        -------
        float
        """
        return self.coords[0]
    
    @property
    def y(self):
        """Second coordinate of the vector.
        
        Returns
        -------
        float
        """
        return self.coords[1]
    
    @property
    def z(self):
        """Third coordinate of the vector.
        
        Returns
        -------
        float
        """
        return self.coords[2]
    
    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"

    def cross(self, other):
        """Compute the cross product of two 3D vectors.
        
        Parameters
        ----------
        other : Vector3
            The other 3D vector to compute the cross product.

        Returns
        -------
        Vector3
            The resulting 3D vector from the cross product.

        """
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector3(x, y, z)


















