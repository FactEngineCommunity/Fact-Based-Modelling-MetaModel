---
title: Appendix A – Model XSD
description: Complete XSD excerpt for the Model artefact.
---

Appendix A contains the generated XSD fragment for the `Model` artefact. The listing below is reproduced from the source document and summarises how value types, entity types, fact types, role constraints, and model notes are grouped under the `ORMModel` element.

```xml
<xs:element name="FBMModel">
  <xs:complexType>
    <xs:sequence>
      <xs:element minOccurs="0" maxOccurs="unbounded" name="ValueTypes">
        <xs:complexType>
          <xs:sequence>
            <xs:element minOccurs="0" maxOccurs="unbounded" name="ValueType">
              <xs:complexType>
                <xs:sequence>
                  <xs:element minOccurs="0" maxOccurs="unbounded" ref="Instance" />
                  <xs:element minOccurs="0" maxOccurs="unbounded" name="ValueConstraint" />
                </xs:sequence>
                <xs:attribute name="Id" type="xs:string" />
                <xs:attribute name="Name" />
                <xs:attribute name="DataType" type="xs:string" />
                <xs:attribute name="DataTypePrecision" type="xs:string" />
                <xs:attribute name="DataTypeLength" type="xs:string" />
                <xs:attribute name="IsMDAModelElement" />
              </xs:complexType>
            </xs:element>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
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
                <xs:attribute name="ReferenceSchemeRoleConstraintId" type="xs:string" />
                <xs:attribute name="IsMDAModelElement" />
              </xs:complexType>
            </xs:element>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element minOccurs="0" maxOccurs="unbounded" name="FactTypes">
        <xs:complexType>
          <xs:sequence>
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
                            <xs:attribute name="JoinedObjectTypeId" type="xs:string" />
                          </xs:complexType>
                        </xs:element>
                      </xs:sequence>
                    </xs:complexType>
                  </xs:element>
                  <xs:element minOccurs="0" maxOccurs="unbounded" ref="Fact" />
                </xs:sequence>
                <xs:attribute name="Id" type="xs:string" />
                <xs:attribute name="Name" type="xs:string" />
                <xs:attribute name="IsSubtypeRelationshipFactType" type="xs:string" />
                <xs:attribute name="IsObjectified" type="xs:string" />
                <xs:attribute name="IsPreferredReferenceSchemeFT" type="xs:string" />
                <xs:attribute name="IsMDAModelElement" />
              </xs:complexType>
            </xs:element>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
      <xs:element minOccurs="0" maxOccurs="unbounded" name="RoleConstraints">
        <xs:complexType>
          <xs:sequence>
            <xs:element minOccurs="0" maxOccurs="unbounded" name="RoleConstraint">
              <xs:complexType>
                <xs:sequence>
                  <xs:element minOccurs="0" maxOccurs="unbounded" ref="RoleConstraintRole" />
                  <xs:element name="SetComparisonConstraint">
                    <xs:complexType>
                      <xs:sequence>
                        <xs:element name="SetComparisonArgument">
                          <xs:complexType>
                            <xs:sequence>
                              <xs:element name="RolePosition">
                                <xs:complexType>
                                  <xs:sequence>
                                    <xs:element name="CompatibleRole">
                                      <xs:complexType>
                                        <xs:attribute name="RoleId" />
                                      </xs:complexType>
                                    </xs:element>
                                    <xs:element name="ComparableRole">
                                      <xs:complexType>
                                        <xs:attribute name="RoleId" />
                                      </xs:complexType>
                                    </xs:element>
                                  </xs:sequence>
                                  <xs:attribute name="RoleId" />
                                  <xs:attribute name="PositionId" />
                                </xs:complexType>
                              </xs:element>
                            </xs:sequence>
                            <xs:attribute name="Arity" />
                          </xs:complexType>
                        </xs:element>
                      </xs:sequence>
                      <xs:attribute name="ArgumentLength" />
                      <xs:attribute name="NrArguments" />
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
      <xs:element minOccurs="0" maxOccurs="unbounded" name="ModelNotes">
        <xs:complexType>
          <xs:sequence>
            <xs:element minOccurs="0" maxOccurs="unbounded" name="ModelNote">
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
    </xs:sequence>
    <xs:attribute name="ModelId" type="xs:string" />
    <xs:attribute name="Name" type="xs:string" />
  </xs:complexType>
</xs:element>
```
