---
title: Role Constraint
description: Defines the RoleConstraints collection and the RoleConstraint structure within the schema.
---

## Overview

The **RoleConstraints** collection lists each constraint defined in the model. Every **RoleConstraint** element records its identifying details, participating roles, and optional arguments or join paths.

## Attribute definitions – RoleConstraint element

- **Id** – Unique identifier for the role constraint.
- **Name** – Name assigned to the constraint.
- **RoleConstraintType** – Type of constraint (e.g. uniqueness, frequency, value comparison).
- **RingConstraintType** – Specifies the ring constraint category when the type is `RingConstraint`.
- **Cardinality** – Captures the cardinality range expression when applicable.
- **IsDeontic** – `true` when the constraint is deontic; otherwise `false`.
- **CardinalityRangeType** – Indicates the range style for cardinality or frequency constraints (`LessThanOrEqual`, `Equal`, `GreaterThanOrEqual`, or `Between`).
- **MinimumFrequencyCount** – Minimum bound for frequency constraints.
- **MaximumFrequencyCount** – Maximum bound for frequency constraints.
- **IsPreferredIdentifier** – `true` when the constraint supplies the preferred identification scheme for an entity type.
- **ValueRangeType** – For value comparison constraints, identifies the comparison operator (`LessThan`, `LessThanOrEqual`, `GreaterThan`, `GreaterThanOrEqual`).
- **IsMDAModelElement** – `true` when the constraint is part of an embedded non-FBM metamodel; otherwise `false`.

## Supporting elements

- **RoleConstraintRole** – See [RoleConstraintRole](./role-constraint-role) for the element that links constraints to specific roles.
- **Argument / RoleConstraintArgument** – Each argument lists the roles and join path that participate in the constraint logic.
- **JoinPath** – Captures the ordered sequence of roles traversed between the argument roles.
- **RoleReference** – References individual roles inside the argument or join path. When provided within a join path, the `JoinPathError` attribute conveys validation issues.

## XSD text

```xml
<xs:element minOccurs="0" maxOccurs="unbounded" name="RoleConstraints">
  <xs:complexType>
    <xs:sequence>
      <xs:element minOccurs="0" maxOccurs="unbounded" name="RoleConstraint">
        <xs:complexType>
          <xs:sequence>
            <xs:element minOccurs="0" maxOccurs="unbounded" ref="RoleConstraintRole" />
            <xs:element name="Argument">
              <xs:complexType>
                <xs:sequence>
                  <xs:element name="RoleConstraintArgument">
                    <xs:complexType>
                      <xs:sequence>
                        <xs:element name="Role">
                          <xs:complexType>
                            <xs:sequence>
                              <xs:element name="RoleReference">
                                <xs:complexType>
                                  <xs:attribute name="RoleId" />
                                </xs:complexType>
                              </xs:element>
                            </xs:sequence>
                          </xs:complexType>
                        </xs:element>
                        <xs:element name="JoinPath">
                          <xs:complexType>
                            <xs:sequence>
                              <xs:element name="RolePath">
                                <xs:complexType>
                                  <xs:sequence>
                                    <xs:element name="RoleReference">
                                      <xs:complexType>
                                        <xs:attribute name="RoleId" />
                                      </xs:complexType>
                                    </xs:element>
                                  </xs:sequence>
                                </xs:complexType>
                              </xs:element>
                            </xs:sequence>
                            <xs:attribute name="JoinPathError" />
                          </xs:complexType>
                        </xs:element>
                      </xs:sequence>
                    </xs:complexType>
                  </xs:element>
                </xs:sequence>
              </xs:complexType>
            </xs:element>
          </xs:sequence>
          <xs:attribute name="Id" type="xs:string" />
          <xs:attribute name="Name" type="xs:string" />
          <xs:attribute name="RoleConstraintType" type="xs:string" />
          <xs:attribute name="RingConstraintType" type="xs:string" />
          <xs:attribute name="IsDeontic" type="xs:string" />
          <xs:attribute name="IsPreferredIdentifier" type="xs:string" />
          <xs:attribute name="CardinalityRangeType" type="xs:string" />
          <xs:attribute name="Cardinality" type="xs:string" />
          <xs:attribute name="MinimumFrequencyCount" type="xs:string" />
          <xs:attribute name="MaximumFrequencyCount" type="xs:string" />
          <xs:attribute name="ValueRangeType" />
          <xs:attribute name="IsMDAModelElement" />
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
</xs:element>
```
