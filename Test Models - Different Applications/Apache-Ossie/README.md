# Apache Ossie generated reference results

These 30 YAML files were generated from the sibling `Boston` FBM
fixtures by the pure-Python Ossie Fact-Based Modelling converter.

They are a **current conversion baseline**, not hand-authored golden files.
`manifest.json` records all 57 structured conversion warnings by
source file. Known warnings include FBM constraints and objectification not yet
representable in Ossie. Every FBM fact type reading is emitted in `verbalizes`,
including multiple readings with the same role order and readings that use any
other role order. The current Apache Python relationship parser may reject some
of those valid document readings, so structural validation uses the public
Ossie specification DTO.

Refresh this folder after Ossie `requires` constraint parsing and mapping is
implemented. Do not silently remove warnings when refreshing it.

The source fixture for each YAML file has the same relative name under the
adjacent `Boston` directory, with `.fbm` replacing `.yaml`.
