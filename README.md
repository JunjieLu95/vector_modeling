# Vector_Modeling

## What is Vector_Modeling?

Vector_Modeling is a Python library for computing vector operations. 
It has two classes. 
The first class supports vectors with arbitrary dimensions to perform addition, subtraction, scaling and dot product.
The other class is a subclass for 3D vectors, and provides the cross product.

## Install from PyPI

Vector_Modeling is a small, lightweight library and doesn't require a complex environment.  
You can install it from PyPI with this command:

```sh
pip install vector_modeling
```

## About Vector_Modeling

Vector_Modeling is a simple yet robust Python library for vector operations.

## Example

``` python

    from vector_modeling import Vector, Vector3

    # Create two arbitrary-dimensional vectors
    v1 = Vector(1, 2, 3, 4)
    v2 = Vector(4, 3, 2, 1)
    print("v1 + v2 =", v1 + v2)  # Vector addition
    print("Dot product:", v1.dot(v2))  # Dot product

    # Create two 3D vectors
    v3 = Vector3(1, 0, 0)
    v4 = Vector3(0, 1, 0)
    print("v3 cross v4 =", v3.cross(v4))  # Cross product
```

## License

Vector_Modeling is licensed under the MIT license.
