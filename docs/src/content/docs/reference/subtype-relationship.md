---
title: SubtypeRelationship
description: Captures subtype/supertype relationships within the FBM exchange metamodel.
---

## Overview

A **SubtypeRelationship** element links a subtype entity type to its parent entity type through the fact type that defines their identification relationship. Although subtype identification facts are often hidden in diagrams, they are explicitly captured in the exchange schema.

## Attribute definitions

- **ParentEntityTypeId** – Identifier of the supertype entity within whose scope the relationship is defined. This may reference an objectifying entity type for an objectified fact type.
- **SubtypingFactTypeId** – Identifier of the fact type that realises the subtype/supertype relationship. These subtyping fact types commonly remain invisible on ORM diagrams even though the connection is rendered as a directed arrow.

## XSD text

```xml
<xs:element name="SubtypeRelationship">
  <xs:complexType>
    <xs:sequence />
    <xs:attribute name="ParentEntityTypeId" type="xs:string" />
    <xs:attribute name="SubtypingFactTypeId" type="xs:string" />
  </xs:complexType>
</xs:element>
```
