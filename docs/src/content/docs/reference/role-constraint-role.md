---
title: RoleConstraintRole
description: Explains the RoleConstraintRole element that links role constraints to individual roles.
---

## Overview

Each **RoleConstraintRole** element records how a role constraint targets specific roles. A single constraint contains one or more of these elements, capturing the ordered roles that participate in the constraint logic.

The `SequenceNr` attribute preserves the ordinal position for each referenced role. For subset constraints, `IsEntry` and `IsExit` distinguish the inbound and outbound role links that make up an entry/exit pair.

## Attribute definitions

- **RoleId** – Identifier of the role linked to the constraint via this entry.
- **SequenceNr** – Ordinal number that orders the role within the constraint's role list.
- **IsEntry** – `true` when the role participates as the entry role in a subset constraint pair; otherwise `false`.
- **IsExit** – `true` when the role is the exit role in a subset constraint pair; otherwise `false`.

## XSD text

```xml
<xs:element name="RoleConstraintRole">
  <xs:complexType>
    <xs:sequence />
    <xs:attribute name="RoleId" type="xs:string" />
    <xs:attribute name="SequenceNr" type="xs:string" />
    <xs:attribute name="IsEntry" type="xs:string" />
    <xs:attribute name="IsExit" type="xs:string" />
  </xs:complexType>
</xs:element>
```
