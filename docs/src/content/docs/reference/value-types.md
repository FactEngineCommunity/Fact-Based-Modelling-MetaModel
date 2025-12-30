---
title: Value Types
description: Covers the ValueTypes collection, ValueType entries, and ValueConstraint usage.
---

## Overview

- **ValueTypes** – Provides the collection of value types defined for the model.
- **ValueType** – Describes an individual value type.
- **ValueConstraint** – Carries the set of permissible values for a value type.

## Attribute definitions – ValueType element

- **Id** – Unique identifier of the value type.
- **Name** – Name assigned to the value type.
- **DataType** – Data type associated with the value type.
- **DataTypePrecision** – Precision qualifier when required by the chosen data type.
- **DataTypeLength** – Length qualifier when required by the chosen data type (for example fixed-length text).
- **IsMDAModelElement** – `true` when the value type belongs to a non-FBM metamodel packaged within the same exchange document; otherwise `false`.
- **GUID** – Unique GUID/UUID as commonly used to uniquely identify model elements between different modelling tools.
- **DBName** – May be used to store the name of the related Column/Property/Attribute within the database schema produced by the Model and for the Value Type.
- **IsIndependent** – 'true' if the Value Type represents a single Entity/Table/Node Type within the database schema produced by the Model and for the Value Type (E.g. A table called 'CountryCode' that has one attribute called 'CountryCode').
- **LongDescription** – Informal description of the Value Type for documentation purposes. Long form.
- **ShortDescription** – Informal description of the Value Type for documentation purposes. Short form.

> Fact-Based Modeling exchange documents may embed Model Driven Architecture (MDA) definitions for languages other than FBM. Elements originating from these auxiliary models are flagged with `IsMDAModelElement`. Diagramming tools that do not employ MDA MetaModels injected into the FBM MetaModel can ignore the IsMDAModelElement attribute.

## XSD text

```xml
<xs:element minOccurs="0" maxOccurs="unbounded" name="ValueTypes">
  <xs:complexType>
    <xs:sequence>
      <xs:element minOccurs="0" maxOccurs="unbounded" name="ValueType">
        <xs:complexType>
          <xs:sequence>
            <xs:element minOccurs="0" maxOccurs="unbounded" ref="Instance" />
            <xs:element minOccurs="0" maxOccurs="1" ref="ValueConstraint" />
          </xs:sequence>
          <xs:attribute name="Id" type="xs:string" />
          <xs:attribute name="Name" />
          <xs:attribute name="DataType" type="xs:string" />
          <xs:attribute name="DataTypePrecision" type="xs:string" />
          <xs:attribute name="DataTypeLength" type="xs:string" />
          <xs:attribute name="IsMDAModelElement" />
          <xs:attribute name="GUID" type="xs:string" use="optional" />
          <xs:attribute name="DBName" type="xs:string" use="optional" />
          <xs:attribute name="IsIndependent" type="xs:boolean" use="required" />
          <xs:attribute name="LongDescription" type="xs:string" use="optional" />
          <xs:attribute name="ShortDescription" type="xs:string" use="optional" />
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```

## Sample XML

Not supplied in the source document.
