# FactEngine FBM metamodel for Python

Typed [Pydantic v2](https://docs.pydantic.dev/) classes for the FactEngine
Fact-Based Modelling (FBM) exchange metamodel, distributed as a pure-Python
wheel.

The public Python API uses conventional `snake_case` field names. Pydantic
aliases preserve the names used by the VB.NET classes and XML vocabulary, so
`model_dump(by_alias=True)` produces familiar `PascalCase` keys.

```python
from fbm_metamodel import FBMModel, Model, ValueType

document = Model(
    fbm_model=FBMModel(
        model_id="example",
        name="Example",
        value_types=[ValueType(id="Name", name="Name")],
    )
)
```

Read and write `.fbm` XML with the standard-library codec:

```python
from fbm_metamodel import load_fbm, save_fbm

document = load_fbm("Examples/CinemaBookings.fbm")
save_fbm(document, "roundtrip.fbm")
```

Version 1.8 uses `FBMModel` and `FBMDiagram` exclusively. The Python reader and
writer deliberately do not accept or emit the version 1.7 `ORMModel` and
`ORMDiagram` vocabulary.

## Development

```text
python -m build
```

This creates both a source distribution and a reusable wheel in `dist/`.
