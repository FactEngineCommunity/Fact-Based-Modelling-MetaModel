---
title: Model
description: Describes the highest level container for a Fact-Based Model exchange document.
---

## Overview

The **Model** element is the top-level container for a Fact-Based Model. It aggregates the FBM-specific structures described in subsequent sections of the reference.

<pre>
Model  
  |--FBMModel  
  |--FBMDiagrams  
</pre>

## Model element

### Attribute definitions

- **XSDVersionNr** – Identifies the schema version used to generate the exchange document.

### FBMModel element

### Attribute definitions

- **ModelId** – Unique identifier for the model instance.
- **Name** – Display name of the model.

### FBMDiagrams element

- Contains the set of FBM diagrams (Pages) that are used to present the FBM Model diagramatically.

## Additional details

The XSD definition for the `Model` and `FBMModel` elements appears in [Appendix A](../appendix-a/), where the full complex type is documented.