---
title: Revision History
description: Summary of changes applied to the FBM Exchange MetaModel XSD documentation.
---

## V1.1

- Corrected errata describing the `EntityType` structure: the `ReferenceSchemeRoleConstraintId` is recorded as an attribute rather than a sub-element.
- Normalised element names (`ModelNotes`, `ModelNote`) throughout the document.
- Removed unnecessary `name="New_ComplexType"` annotations introduced by an XSD editor.

## V1.0

- Initial public release of the specification.

## V0.83

- Replaced the term “Compound Reference Mode” with “Compound Reference Scheme”.
- Renamed `ReferenceMode` to `ReferenceScheme` where required.
- Added the `IsMDAModelElement` attribute to the `ValueType`, `EntityType`, `FactType`, `RoleConstraint`, and `ModelNote` elements.
- Closed several issue items dated 2015-05-10 through 2015-05-12.

## V0.82

- Updated the issues register in preparation for the following release.

## V0.81

- Renamed the `JoinedObjectId` attribute to `JoinedObjectTypeId` on the `Role` element.
- Added the `ValueConstraint` sub-element to the `Role` element definition.

## V0.8

- Introduced the `DataTypePrecision` and `DataTypeLength` attributes on the `ValueType` element.

## V0.7

- Added the `SubtypeRelationship` element definition.
- Renamed the `IsSubtypeConstraintFactType` attribute to `IsSubtypeRelationshipFactType` on the `FactType` element.
