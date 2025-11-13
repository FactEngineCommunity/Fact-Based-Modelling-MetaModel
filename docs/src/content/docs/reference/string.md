---
title: String
description: Definition of the String element used to persist scalar values within FBM instances.
---

## Overview

A **String** element stores a scalar string value. These values often provide identifiers that support Instance elements elsewhere in the exchange document.

See also: [Instance](./instance).

## XSD text

```xml
<xs:element name="String" nillable="true">
  <xs:complexType>
    <xs:simpleContent msdata:ColumnName="string_Text" msdata:Ordinal="0">
      <xs:extension base="xs:string" />
    </xs:simpleContent>
  </xs:complexType>
</xs:element>
```

## Sample XML

```xml
<String>c69ea3a6-6d73-47aa-abf6-c52311f4c3a5</String>
```
