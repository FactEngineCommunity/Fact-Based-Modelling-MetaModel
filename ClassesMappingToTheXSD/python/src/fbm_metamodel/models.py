"""Pydantic representation of the FactEngine FBM exchange metamodel."""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import AliasChoices, BaseModel, ConfigDict, Field


def _pascal_case(field_name: str) -> str:
    special = {
        "db_name": "DBName",
        "fbm_diagram": "FBMDiagram",
        "fbm_model": "FBMModel",
        "guid": "GUID",
        "xsd_version_nr": "XSDVersionNr",
    }
    return special.get(field_name, "".join(part.capitalize() for part in field_name.split("_")))


class FBMBaseModel(BaseModel):
    """Shared configuration for all FBM model classes."""

    model_config = ConfigDict(
        alias_generator=_pascal_case,
        populate_by_name=True,
        validate_assignment=True,
        extra="forbid",
    )


class FBMDataType(str, Enum):
    DATA_TYPE_NOT_SET = "DataTypeNotSet"
    BOOLEAN = "Boolean"
    LOGICAL_TRUE_FALSE = "LogicalTrueFalse"
    LOGICAL_YES_NO = "LogicalYesNo"
    NUMERIC_AUTO_COUNTER = "NumericAutoCounter"
    AUTO_UUID = "AutoUUID"
    NUMERIC_DECIMAL = "NumericDecimal"
    NUMERIC_FLOAT_CUSTOM_PRECISION = "NumericFloatCustomPrecision"
    NUMERIC_FLOAT_DOUBLE_PRECISION = "NumericFloatDoublePrecision"
    NUMERIC_FLOAT_SINGLE_PRECISION = "NumericFloatSinglePrecision"
    NUMERIC_MONEY = "NumericMoney"
    NUMERIC_SIGNED_BIG_INTEGER = "NumericSignedBigInteger"
    NUMERIC_SIGNED_INTEGER = "NumericSignedInteger"
    NUMERIC_SIGNED_SMALL_INTEGER = "NumericSignedSmallInteger"
    NUMERIC_UNSIGNED_BIG_INTEGER = "NumericUnsignedBigInteger"
    NUMERIC_UNSIGNED_INTEGER = "NumericUnsignedInteger"
    NUMERIC_UNSIGNED_SMALL_INTEGER = "NumericUnsignedSmallInteger"
    NUMERIC_UNSIGNED_TINY_INTEGER = "NumericUnsignedTinyInteger"
    OTHER_OBJECT_ID = "OtherObjectID"
    OTHER_ROW_ID = "OtherRowID"
    RAW_DATA_FIXED_LENGTH = "RawDataFixedLength"
    RAW_DATA_LARGE_LENGTH = "RawDataLargeLength"
    RAW_DATA_OLE_OBJECT = "RawDataOLEObject"
    RAW_DATA_PICTURE = "RawDataPicture"
    RAW_DATA_VARIABLE_LENGTH = "RawDataVariableLength"
    TEMPORAL_AUTO_TIMESTAMP = "TemporalAutoTimestamp"
    TEMPORAL_DATE = "TemporalDate"
    TEMPORAL_DATE_AND_TIME = "TemporalDateAndTime"
    TEMPORAL_TIME = "TemporalTime"
    TEXT_FIXED_LENGTH = "TextFixedLength"
    TEXT_LARGE_LENGTH = "TextLargeLength"
    TEXT_VARIABLE_LENGTH = "TextVariableLength"


class ConceptType(str, Enum):
    NONE = "None"
    DERIVATION_TEXT = "DerivationText"
    ENTITY_TYPE = "EntityType"
    ENTITY_TYPE_DERIVATION_TEXT = "EntityTypeDerivationText"
    ENTITY_TYPE_NAME = "EntityTypeName"
    FACT_TYPE_READING = "FactTypeReading"
    FACT = "Fact"
    FACT_TYPE = "FactType"
    FACT_TYPE_DERIVATION_TEXT = "FactTypeDerivationText"
    FACT_TYPE_NAME = "FactTypeName"
    FACT_TABLE = "FactTable"
    GENERAL_CONCEPT = "GeneralConcept"
    MODEL_NOTE = "ModelNote"
    MODEL = "Model"
    PAGE = "Page"
    ROLE = "Role"
    RING_CONSTRAINT = "RingConstraint"
    ROLE_DATA = "RoleData"
    ROLE_NAME = "RoleName"
    ROLE_CONSTRAINT = "RoleConstraint"
    ROLE_CONSTRAINT_ROLE = "RoleConstraintRole"
    SUBTYPE_RELATIONSHIP = "SubtypeRelationship"
    VALUE = "Value"
    VALUE_CONSTRAINT = "ValueConstraint"
    VALUE_TYPE = "ValueType"


class SubtypeRelationship(FBMBaseModel):
    parent_entity_type_id: str = ""
    subtyping_fact_type_id: str = ""
    is_primary_subtype_relationship: bool = False


class ValueType(FBMBaseModel):
    id: str
    guid: str | None = None
    name: str
    db_name: str = ""
    data_type: FBMDataType = FBMDataType.DATA_TYPE_NOT_SET
    data_type_precision: int = 0
    data_type_length: int = 0
    instances: list[str] = Field(default_factory=list, alias="Instance")
    value_constraints: list[str] = Field(default_factory=list, alias="ValueConstraint")
    long_description: str = ""
    short_description: str = ""
    is_independent: bool = False
    is_mda_model_element: bool = Field(False, alias="IsMDAModelElement")
    subtype_relationships: list[SubtypeRelationship] = Field(
        default_factory=list, alias="SubtypeRelationships"
    )


class EntityType(FBMBaseModel):
    id: str
    guid: str | None = None
    name: str
    db_name: str = ""
    graph_labels: list[str] = Field(default_factory=list, alias="GraphLabel")
    instances: list[str] = Field(default_factory=list, alias="Instance")
    reference_mode_value_type_id: str | None = None
    reference_scheme_role_constraint_id: str = ""
    is_objectifying_entity_type: bool = False
    reference_mode: str = ""
    hide_reference_mode: bool = False
    subtype_relationships: list[SubtypeRelationship] = Field(
        default_factory=list, alias="SubtypeRelationships"
    )
    is_independent: bool = False
    is_personal: bool = False
    is_absorbed: bool = False
    is_mda_model_element: bool = Field(False, alias="IsMDAModelElement")
    is_derived: bool = False
    derivation_text: str = ""
    long_description: str = ""
    short_description: str = ""


class FactData(FBMBaseModel):
    role_id: str
    data: str = ""


class Fact(FBMBaseModel):
    id: str
    data: list[FactData] = Field(default_factory=list)


class Role(FBMBaseModel):
    id: str
    name: str = ""
    sequence_nr: int = 1
    mandatory: bool = False
    joined_object_type_id: str
    value_constraints: list[str] = Field(default_factory=list, alias="ValueConstraint")


class PredicatePart(FBMBaseModel):
    sequence_nr: int
    role_id: str = Field(
        "",
        validation_alias=AliasChoices("role_id", "RoleId", "Role_Id"),
        serialization_alias="Role_Id",
    )
    prebound_reading_text: str = ""
    postbound_reading_text: str = ""
    predicate_part_text: str = ""


class FactTypeReading(FBMBaseModel):
    id: str
    front_reading_text: str = ""
    following_reading_text: str = ""
    predicate_parts: list[PredicatePart] = Field(default_factory=list, alias="PredicateParts")


class FactType(FBMBaseModel):
    id: str
    guid: str | None = None
    name: str
    db_name: str = ""
    graph_labels: list[str] = Field(default_factory=list, alias="GraphLabel")
    objectifying_entity_type_id: str = ""
    roles: list[Role] = Field(default_factory=list, alias="RoleGroup")
    facts: list[Fact] = Field(default_factory=list, alias="Facts")
    fact_type_readings: list[FactTypeReading] = Field(
        default_factory=list, alias="FactTypeReadings"
    )
    is_link_fact_type: bool = False
    link_fact_type_role_id: str | None = None
    is_mda_model_element: bool = Field(False, alias="IsMDAModelElement")
    is_subtype_relationship_fact_type: bool = False
    is_objectified: bool = False
    is_preferred_reference_scheme_ft: bool = Field(
        False, alias="IsPreferredReferenceSchemeFT"
    )
    is_derived: bool = False
    is_stored: bool = False
    derivation_text: str = ""
    long_description: str = ""
    short_description: str = ""
    is_independent: bool = False
    is_subtype_state_controlling: bool = False
    subtype_relationships: list[SubtypeRelationship] = Field(
        default_factory=list, alias="SubtypeRelationships"
    )
    store_fact_coordinates: bool = False


class RoleReference(FBMBaseModel):
    role_id: str


class JoinPath(FBMBaseModel):
    role_path: list[RoleReference] = Field(default_factory=list)
    join_path_error: str | None = None


class RoleConstraintArgument(FBMBaseModel):
    id: str | None = None
    sequence_nr: int = 1
    roles: list[RoleReference] = Field(default_factory=list, alias="Role")
    join_path: JoinPath = Field(default_factory=JoinPath)


class RoleConstraintRole(FBMBaseModel):
    role_id: str
    sequence_nr: int = 0
    is_entry: bool = False
    is_exit: bool = False
    argument_id: str = ""
    argument_sequence_nr: int = 0


class RoleConstraint(FBMBaseModel):
    id: str
    guid: str | None = None
    name: str = ""
    role_constraint_type: str
    ring_constraint_type: str = ""
    is_preferred_uniqueness: bool = False
    is_deontic: bool = False
    is_mda_model_element: bool = Field(False, alias="IsMDAModelElement")
    minimum_frequency_count: int = 0
    maximum_frequency_count: int = 0
    cardinality: int = 0
    cardinality_range_type: str = ""
    value_range_type: str | None = None
    roles: list[RoleConstraintRole] = Field(
        default_factory=list, alias="RoleConstraintRoles"
    )
    arguments: list[RoleConstraintArgument] = Field(default_factory=list, alias="Argument")
    value_constraints: list[str] = Field(default_factory=list, alias="ValueConstraint")
    long_description: str = ""
    short_description: str = ""


class ModelNote(FBMBaseModel):
    id: str
    guid: str | None = None
    joined_object_type_id: str = Field(
        "",
        validation_alias=AliasChoices(
            "joined_object_type_id", "JoinedObjectTypeId", "JoinedObjectId"
        ),
        serialization_alias="JoinedObjectTypeId",
    )
    note: str = ""
    is_mda_model_element: bool = Field(False, alias="IsMDAModelElement")


class Synonym(FBMBaseModel):
    model_element_id: str
    synonym: str


class FBMModel(FBMBaseModel):
    model_id: str = ""
    name: str = ""
    core_version_number: str | None = None
    value_types: list[ValueType] = Field(default_factory=list, alias="ValueTypes")
    entity_types: list[EntityType] = Field(default_factory=list, alias="EntityTypes")
    fact_types: list[FactType] = Field(default_factory=list, alias="FactTypes")
    role_constraints: list[RoleConstraint] = Field(
        default_factory=list, alias="RoleConstraints"
    )
    model_notes: list[ModelNote] = Field(default_factory=list, alias="ModelNotes")
    synonyms: list[Synonym] = Field(default_factory=list, alias="Synonyms")

    def get_model_element_by_id(self, model_element_id: str) -> Any | None:
        """Return the first top-level model element having the requested ID."""
        collections = (
            self.value_types,
            self.entity_types,
            self.fact_types,
            self.role_constraints,
            self.model_notes,
        )
        return next(
            (item for collection in collections for item in collection if item.id == model_element_id),
            None,
        )


class ConceptInstanceFlag(FBMBaseModel):
    symbol: str = ""
    concept_type: ConceptType = ConceptType.NONE
    role_id: str = "NotUsed"
    x: int = 0
    y: int = 0
    width: int = 0
    height: int = 0
    orientation: int = 0
    visible: bool = False
    instance_number: int = 1
    flag: str = ""
    is_dirty: bool = Field(False, alias="isDirty")


class ConceptInstance(FBMBaseModel):
    symbol: str
    concept_type: ConceptType = ConceptType.NONE
    role_id: str = "NotUsed"
    x: int = 0
    y: int = 0
    width: int = 0
    height: int = 0
    orientation: int = 0
    visible: bool = False
    instance_number: int = 1
    is_dirty: bool = Field(False, alias="isDirty")
    flags: list[ConceptInstanceFlag] = Field(default_factory=list, alias="ConceptInstanceFlag")

    def equals_by_symbol_type(self, other: ConceptInstance) -> bool:
        return self.symbol == other.symbol and self.concept_type == other.concept_type

    def equals_by_symbol_role_id(self, other: ConceptInstance) -> bool:
        return self.symbol == other.symbol and self.role_id == other.role_id


class Page(FBMBaseModel):
    id: str
    name: str = ""
    language: str = ""
    is_core_model_page: bool = False
    concept_instances: list[ConceptInstance] = Field(
        default_factory=list, alias="ConceptInstance"
    )


class Model(FBMBaseModel):
    xsd_version_nr: float = 1.8
    fbm_model: FBMModel = Field(default_factory=FBMModel)
    fbm_diagram: list[Page] = Field(default_factory=list)
