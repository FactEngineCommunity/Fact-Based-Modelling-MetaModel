---
title: Fact Types
description: Details for FactTypes, FactType, Role, FactTypeReading, and PredicatePart elements.
---

## Overview

The **FactTypes** element aggregates the definitions of fact types present in the model. Each fact type captures its roles, readings, and associated sample data.


## Attribute definitions – FactType element

- **Id** – Unique identifier for the fact type.
- **Name** – Name of the fact type.
- **IsSubtypeRelationshipFactType** – `true` when the fact type provides identification for a subtype entity type; otherwise `false`.
- **IsObjectified** – `true` when the fact type is objectified; otherwise `false`.
- **IsPreferredReferenceSchemeFT** – `true` when the fact type supplies the preferred reference scheme for an entity type that does not use a compound scheme; otherwise `false`.
- **IsMDAModelElement** – `true` when the fact type belongs to an embedded non-FBM metamodel; otherwise `false`.
- **DBName** -  May be used to store the name of the related Column/Property/Attribute within the database schema produced by the Model and for the Value Type.
- **IsObjectified** - 'true' if the Fact Type is Objectified/Nested, else 'false'.
- **ObjectifyingEntityTypeId** - The identifier of the Entity Type that effectively 'objectifies' the Fact Type under Terry Halpin's finite model theory interpretation of ORM. See 'IsObjectified' (above).
- **GUID** - Unique GUID/UUID as commonly used to uniquely identify model elements between different modelling tools.
- **IsLinkFactType** - 'true' if the Fact Type is an Implied (Link) Fact Type, else 'false'.
- **LinkFactTypeRoleId** - If 'IsLinkFactType' (above) is 'true', then stores the Role identifier of the Role within the Fact Type that the Implied/Link Fact Type is for.
- **IsDerived** - 'true' if the Entity Type is derived, else 'false'.
- **DerivationText** - If the Entity Type is Derived (see IsDerived, above), then the derivation text of the derivation for the Entity Type in some form of human/machine readable/parseable logical form.
- **IsStored** - <To be confirmed>
- **IsIndependent** - <To be confirmed>
- **IsSubtypeStateControlling** - <To be confirmed>
- **StoreFactCoordinates** - Used in 4-Layer MDA (Model Driven Architecture) use of the metamodel only. 'true' if the X,Y diagramming coordinates for Facts (Sample Populations) are stored in the 'ConceptInstance' element of the XML. See <ORMDiagram>/<FBMDiagram>, <ConceptInstance>.
- **LongDescription** - Informal description of the Entity Type for documentation purposes. Long form.
- **ShortDescription** - Informal description of the Entity Type for documentation purposes. Short form.

> Fact types that deliver reference schemes for entity types (for example single-value reference modes) are marked with `IsPreferredReferenceSchemeFT` so tooling can hide or reveal them appropriately.

## Attribute definitions – Role element

- **Id** – Unique identifier of the role within the model.
- **Name** – Optional role name when provided; otherwise blank.
- **HostingObjectTypeId** – Identifier of the object type that plays the role.

## Attribute definitions – FactTypeReading element

- **Id** – Unique identifier for the reading.
- **FrontText** – Text that precedes the predicate parts (e.g. “in Year”).
- **FollowingText** – Text that follows the predicate parts (e.g. “often”).

The reading contains a `PredicateParts` collection, where each predicate part carries the fragments that surround a referenced role.

### Attribute definitions – PredicatePart element

- **SequenceNr** – Ordinal position of the predicate part within the reading.
- **RoleId** – Identifier of the role associated with this predicate fragment.
- **PreboundText** – Text that appears before the referenced role (e.g. “first” in “Person has first Name”).
- **PostboundText** – Text that appears after the referenced role.
- **PredicatePartText** – Core predicate wording associated with the role.

### Example readings

The document illustrates predicate text with examples such as:

- `in Year Person of note played team-Sport for Country often`
- `tickets for Booking are being mailed to Address`
- `Person has first Name`

## XSD text

```xml
<xs:element minOccurs="0" maxOccurs="unbounded" name="FactType">
  <xs:complexType>
    <xs:sequence>
      <xs:element minOccurs="0" maxOccurs="unbounded" name="RoleGroup">
        <xs:complexType>
          <xs:sequence>
            <xs:element minOccurs="0" maxOccurs="unbounded" name="Role">
              <xs:complexType>
                <xs:sequence>
                  <xs:element minOccurs="0" maxOccurs="unbounded" name="ValueConstraint" />
                </xs:sequence>
                <xs:attribute name="Id" type="xs:string" />
                <xs:attribute name="Name" type="xs:string" />
                <xs:attribute name="SequenceNr" />
                <xs:attribute name="Mandatory" />
                <xs:attribute name="JoinedObjectTypeId" />
              </xs:complexType>
            </xs:element>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element name="FactTypeReadings">
        <xs:complexType>
          <xs:all>
            <xs:element name="FactTypeReading">
              <xs:complexType>
                <xs:sequence>
                  <xs:element name="PredicateParts">
                    <xs:complexType>
                      <xs:all>
                        <xs:element name="PredicatePart">
                          <xs:complexType>
                            <xs:attribute name="SequenceNr" />
                            <xs:attribute name="RoleId" />
                            <xs:attribute name="PreboundText" />
                            <xs:attribute name="PostboundText" />
                            <xs:attribute name="PredicatePartText" />
                          </xs:complexType>
                        </xs:element>
                      </xs:all>
                    </xs:complexType>
                  </xs:element>
                </xs:sequence>
                <xs:attribute name="Id" />
                <xs:attribute name="FrontText" />
                <xs:attribute name="FollowingText" />
              </xs:complexType>
            </xs:element>
          </xs:all>
        </xs:complexType>
      </xs:element>
      <xs:element name="Facts">
        <xs:complexType>
          <xs:all>
            <xs:element minOccurs="0" maxOccurs="1" name="Fact" type="Fact" />
          </xs:all>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
    <xs:attribute name="Id" type="xs:string" />
    <xs:attribute name="Name" type="xs:string" />
    <xs:attribute name="IsSubtypeRelationshipFactType" type="xs:string" />
    <xs:attribute name="IsObjectified" type="xs:string" />
    <xs:attribute name="IsPreferredReferenceSchemeFT" type="xs:string" />
    <xs:attribute name="IsMDAModelElement" />
    <xs:attribute name="DBName" type="xs:string" use="optional" />
    <xs:attribute name="GUID" type="xs:string" use="optional" />
    <xs:attribute name="ObjectifyingEntityTypeId" type="xs:string" />
    <xs:attribute name="IsLinkFactType" type="xs:boolean" />
    <xs:attribute name="LinkFactTypeRoleId" type="xs:string" />
    <xs:attribute name="IsDerived" type="xs:boolean" />
    <xs:attribute name="IsStored" type="xs:boolean" />
    <xs:attribute name="DerivationText" type="xs:string" />
    <xs:attribute name="IsIndependent" type="xs:boolean" />
    <xs:attribute name="IsSubtypeStateControlling" type="xs:boolean" />
    <xs:attribute name="StoreFactCoordinates" type="xs:boolean" />
    <xs:attribute name="LongDescription" type="xs:string" />
    <xs:attribute name="ShortDescription" type="xs:string" />
  </xs:complexType>
</xs:element>
```
