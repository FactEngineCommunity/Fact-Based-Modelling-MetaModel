---
title: Model Note
description: Captures documentation notes attached to model elements.
---

## Overview

The **ModelNotes** collection stores textual notes authored for the model. Each **ModelNote** ties the commentary back to a specific model element.

## Attribute definitions – ModelNote element

- **Id** – Unique identifier of the model note.
- **JoinedObjectId** – Identifier of the model element the note describes (role constraint, object type, etc.).
- **IsMDAModelElement** – `true` when the note documents an element from an embedded non-FBM metamodel; otherwise `false`.

As with other elements, the `IsMDAModelElement` flag indicates when the note originates from an MDA model so tools can opt to ignore or present it when focusing solely on FBM content.

## XSD text

```xml
<xs:element minOccurs="0" maxOccurs="unbounded" name="Model Notes">
  <xs:complexType>
    <xs:sequence>
      <xs:element minOccurs="0" maxOccurs="unbounded" name="Model Note">
        <xs:complexType>
          <xs:sequence>
            <xs:element msdata:Ordinal="1" minOccurs="0" name="Note" type="xs:string" />
          </xs:sequence>
          <xs:attribute name="Id" type="xs:string" />
          <xs:attribute name="JoinedObjectId" type="xs:string" />
          <xs:attribute name="IsMDAModelElement" />
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```
