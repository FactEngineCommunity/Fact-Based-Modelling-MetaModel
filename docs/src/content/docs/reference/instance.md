---
title: Instance
description: Details for the Instance element that captures identified object instances.
---

## Overview

An **Instance** element lists the string values that uniquely identify an instance of an object type within a Fact-Based Model. Instances for entity and value types use this structure, while objectified fact types rely on their corresponding objectifying entity types to define their instance set.

> Only Entity Types and Value Types carry Instance elements within the exchange metamodel. Subtype instances are derived from their value type reference schemes unless the entity type has a compound reference scheme.

### Usage notes

* An entity type may identify each instance with a GUID value.
* When a fact type is objectified, the objectifying entity type holds the unique instances for that fact.

## XSD text

```xml
<xs:element name="Instance">
  <xs:complexType>
    <xs:sequence>
      <xs:element minOccurs="0" maxOccurs="unbounded" ref="String" />
    </xs:sequence>
  </xs:complexType>
</xs:element>
```
