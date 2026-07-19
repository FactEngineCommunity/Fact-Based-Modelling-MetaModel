---
title: Model
description: Describes the highest level container for a Fact-Based Model exchange document.
---

## Overview

The **Model** element is the top-level container for a Fact-Based Model. It aggregates the FBM-specific structures described in subsequent sections of the reference.

<pre>
Model  
  |--FBMModel  
  |--FBMDiagram
</pre>

## Model element

```xml
<?xml version="1.0" encoding="utf-8"?>
<Model xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" XSDVersionNr="1.7">
  <FBMModel ModelId="729bef8f-d78a-4936-a9a2-fe468ca4c7fa" Name="CinemaBookings-SemanticLayerTest" CoreVersionNumber="2.6">
...
  </FBMModel>
  <FBMDiagram>
    <Page Id="a2dbde51-35fe-4ef1-b2d7-f18509a9cf7b" Name="Cinema" Language="ORMModel" IsCoreModelPage="false">
      <ConceptInstance>
```

### Attribute definitions

- **XSDVersionNr** – Identifies the schema version used to generate the exchange document.

### FBMModel element

### Attribute definitions

- **ModelId** – Unique identifier for the model instance.
- **Name** – Display name of the model.
- **CoreVersionNumber** – Is the version number of the Core metamodel, if using this FBM Exchange Schema in a 4-Layer architecture with injected metamodels as Core MDAModelElements (Model Driven Architecture Elements).

### FBMDiagram element

- Contains the set of FBM diagrams (Pages) that are used to present the FBM Model diagramatically.

## Additional details

The XSD definition for the `Model` and `FBMModel` elements appears in [Appendix A](../appendix-a/), where the full complex type is documented.