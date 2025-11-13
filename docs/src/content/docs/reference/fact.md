---
title: Fact
description: Describes the Fact element that records sample data for a fact type.
---

## Overview

A **Fact** element stores the data population for a fact type. Each fact groups one or more **FactData** entries that record the role values that participate in the fact instance.

## Attribute definitions

### Fact element

- **Id** – Unique identifier for the fact instance captured by this element.

### FactData element

- **RoleId** – Identifier of the role whose value is supplied by the surrounding FactData entry.

## XSD text

```xml
<xs:element name="Fact">
  <xs:complexType>
    <xs:sequence>
      <xs:element minOccurs="0" maxOccurs="unbounded" name="Data">
        <xs:complexType>
          <xs:sequence>
            <xs:element minOccurs="0" maxOccurs="unbounded" name="FactData">
              <xs:complexType>
                <xs:sequence>
                  <xs:element msdata:Ordinal="1" minOccurs="0" name="Value" type="xs:string" />
                </xs:sequence>
                <xs:attribute name="RoleId" type="xs:string" />
              </xs:complexType>
            </xs:element>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
    <xs:attribute name="Id" type="xs:string" />
  </xs:complexType>
</xs:element>
```
