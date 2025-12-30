---
title: Entity Types
description: Documents the EntityTypes collection and EntityType attributes within the exchange schema.
---

## Overview

- **EntityTypes** – Holds the collection of entity type definitions for a model.
- **EntityType** – Captures the metadata for an individual entity type, including subtyping information.

## Attribute definitions – EntityType element

- **Id** – Unique identifier of the entity type. It must be unique across value types, entity types, fact types, role constraints, and model notes.
- **Name** – Human-readable name of the entity type. Uniqueness is expected across the same set of elements listed above.
- **IsObjectifyingEntityType** – `true` when the entity type objectifies a fact type; otherwise `false`.
- **ReferenceMode** – Textual reference mode when the entity type uses a simple (non-compound) reference scheme. Empty when no reference mode is yet defined.
- **ReferenceSchemeRoleConstraintId** – Identifier of the role constraint that governs the entity type's reference scheme when one exists.
- **IsMDAModelElement** – `true` when the entity type is part of an embedded non-FBM metamodel; otherwise `false`.
- **GUID** – Unique GUID/UUID as commonly used to uniquely identify model elements between different modelling tools.
- **ReferenceModeValueTypeId** – The Value Type of the Simple Reference Scheme for the Entity Type if the Entity Type has a Simple Reference Scheme (Reference Mode).
- **HideReferenceMode** – 'true' if the Reference Mode in diagrams showing this Entity Type is hidden, else 'false'. Object-Role Modeling Specific.
- **IsIndependent** – <To be completed>.
- **IsPersonal** – 'true' if the verbalisation text for the Entity Type is produced such that the Entity Type is recognised as a Person.
- **IsAbsorbed** – 'true' if the Entity Type is a subtype of another Object Type but is not a stand-alone Table/Node Type in the database schema produced for the Model.
- **IsDerived** – 'true' if the Entity Type is derived, else 'false'.
- **DerivationText** – If the Entity Type is Derived (see IsDerived, above), then the derivation text of the derivation for the Entity Type in some form of human/machine readable/parseable logical form.
- **LongDescription** – Informal description of the Entity Type for documentation purposes. Long form.
- **ShortDescription** – Informal description of the Entity Type for documentation purposes. Short form.

## Attribute definitions – ReferenceSchemeRoleConstraint

- **RoleConstraintId** – Identifier of the role constraint that ranges over the reference scheme for the entity type.

> As with value types, the `IsMDAModelElement` flag highlights elements imported from non-FBM metamodels so consuming tools can include or ignore them as needed.

## XSD text

```xml
<xs:element minOccurs="0" maxOccurs="unbounded" name="EntityTypes">
  <xs:complexType>
    <xs:sequence>
      <xs:element minOccurs="0" maxOccurs="unbounded" name="EntityType">
        <xs:complexType>
          <xs:sequence>
            <xs:element minOccurs="0" maxOccurs="unbounded" ref="Instance" />
            <xs:element minOccurs="0" maxOccurs="unbounded" ref="SubtypeRelationship" />
          </xs:sequence>
          <xs:attribute name="Id" type="xs:string" />
          <xs:attribute name="Name" type="xs:string" />
          <xs:attribute name="IsObjectifyingEntityType" type="xs:string" />
          <xs:attribute name="ReferenceMode" />
          <xs:attribute name="ReferenceModeRoleConstraintId" type="xs:string" />
          <xs:attribute name="IsMDAModelElement" />
          <xs:attribute name="GUID" type="xs:string" use="optional" />
          <xs:attribute name="DBName" type="xs:string" use="optional" />
          <xs:attribute name="ReferenceModeValueTypeId" type="xs:string" use="optional" />
          <xs:attribute name="HideReferenceMode" type="xs:boolean" use="required" />
          <xs:attribute name="IsIndependent" type="xs:boolean" use="required" />
          <xs:attribute name="IsPersonal" type="xs:boolean" use="required" />
          <xs:attribute name="IsAbsorbed" type="xs:boolean" use="required" />
          <xs:attribute name="IsDerived" type="xs:boolean" use="required" />
          <xs:attribute name="DerivationText" type="xs:string" use="optional" />
          <xs:attribute name="LongDescription" type="xs:string" use="optional" />
          <xs:attribute name="ShortDescription" type="xs:string" use="optional" />
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```
