"""Namespace-tolerant XML reader and canonical FBM XML writer."""

from __future__ import annotations

from enum import Enum
from os import PathLike
from pathlib import Path
from typing import Any, Iterable
from xml.etree import ElementTree as ET

from .models import (
    ConceptInstance,
    ConceptInstanceFlag,
    EntityType,
    Fact,
    FactData,
    FactType,
    FactTypeReading,
    FBMModel,
    JoinPath,
    Model,
    ModelNote,
    Page,
    PredicatePart,
    Role,
    RoleConstraint,
    RoleConstraintArgument,
    RoleConstraintRole,
    RoleReference,
    SubtypeRelationship,
    Synonym,
    ValueType,
)

Pathish = str | PathLike[str]


def _local_name(name: str) -> str:
    return name.rsplit("}", 1)[-1]


def _child(element: ET.Element, *names: str) -> ET.Element | None:
    accepted = set(names)
    return next((item for item in element if _local_name(item.tag) in accepted), None)


def _children(element: ET.Element | None, name: str) -> list[ET.Element]:
    if element is None:
        return []
    return [item for item in element if _local_name(item.tag) == name]


def _attributes(element: ET.Element) -> dict[str, str]:
    return {_local_name(key): value for key, value in element.attrib.items()}


def _text(element: ET.Element | None) -> str:
    return "" if element is None or element.text is None else element.text


def _string_values(element: ET.Element, wrapper_name: str) -> list[str]:
    values: list[str] = []
    for wrapper in _children(element, wrapper_name):
        strings = _children(wrapper, "string")
        if strings:
            values.extend(_text(item) for item in strings)
        elif wrapper.text and wrapper.text.strip():
            values.append(wrapper.text)
    return values


def _subtype_relationships(element: ET.Element) -> list[SubtypeRelationship]:
    wrapper = _child(element, "SubtypeRelationships")
    return [SubtypeRelationship.model_validate(_attributes(item)) for item in _children(wrapper, "SubtypeRelationship")]


def _value_type(element: ET.Element) -> ValueType:
    data: dict[str, Any] = _attributes(element)
    data["Instance"] = _string_values(element, "Instance")
    data["ValueConstraint"] = _string_values(element, "ValueConstraint")
    data["SubtypeRelationships"] = _subtype_relationships(element)
    return ValueType.model_validate(data)


def _entity_type(element: ET.Element) -> EntityType:
    data: dict[str, Any] = _attributes(element)
    graph_label = _child(element, "GraphLabel")
    data["GraphLabel"] = [_text(item) for item in _children(graph_label, "string")]
    data["Instance"] = _string_values(element, "Instance")
    data["SubtypeRelationships"] = _subtype_relationships(element)
    return EntityType.model_validate(data)


def _fact_data(element: ET.Element) -> FactData:
    data = _attributes(element)
    value = _child(element, "Value", "Data")
    data["Data"] = _text(value) if value is not None else _text(element)
    return FactData.model_validate(data)


def _fact(element: ET.Element) -> Fact:
    data: dict[str, Any] = _attributes(element)
    data_items: list[FactData] = []
    for wrapper in _children(element, "Data"):
        items = _children(wrapper, "FactData")
        data_items.extend(_fact_data(item) for item in items)
    data["Data"] = data_items
    return Fact.model_validate(data)


def _role(element: ET.Element) -> Role:
    data: dict[str, Any] = _attributes(element)
    data["ValueConstraint"] = _string_values(element, "ValueConstraint")
    return Role.model_validate(data)


def _predicate_part(element: ET.Element) -> PredicatePart:
    data = _attributes(element)
    data["PredicatePartText"] = _text(_child(element, "PredicatePartText"))
    return PredicatePart.model_validate(data)


def _fact_type_reading(element: ET.Element) -> FactTypeReading:
    data: dict[str, Any] = _attributes(element)
    wrapper = _child(element, "PredicateParts")
    data["PredicateParts"] = [_predicate_part(item) for item in _children(wrapper, "PredicatePart")]
    return FactTypeReading.model_validate(data)


def _fact_type(element: ET.Element) -> FactType:
    data: dict[str, Any] = _attributes(element)
    graph_label = _child(element, "GraphLabel")
    data["GraphLabel"] = [_text(item) for item in _children(graph_label, "string")]
    data["RoleGroup"] = [
        _role(item)
        for wrapper in _children(element, "RoleGroup")
        for item in _children(wrapper, "Role")
    ]
    data["Facts"] = [
        _fact(item)
        for wrapper in _children(element, "Facts")
        for item in _children(wrapper, "Fact")
    ]
    data["FactTypeReadings"] = [
        _fact_type_reading(item)
        for wrapper in _children(element, "FactTypeReadings")
        for item in _children(wrapper, "FactTypeReading")
    ]
    data["SubtypeRelationships"] = _subtype_relationships(element)
    return FactType.model_validate(data)


def _role_reference(element: ET.Element) -> RoleReference:
    return RoleReference.model_validate(_attributes(element))


def _argument(element: ET.Element) -> RoleConstraintArgument:
    data: dict[str, Any] = _attributes(element)
    role_wrapper = _child(element, "Role")
    data["Role"] = [_role_reference(item) for item in _children(role_wrapper, "RoleReference")]
    join_element = _child(element, "JoinPath")
    if join_element is None:
        data["JoinPath"] = JoinPath()
    else:
        path_wrapper = _child(join_element, "RolePath")
        data["JoinPath"] = JoinPath(
            role_path=[_role_reference(item) for item in _children(path_wrapper, "RoleReference")],
            join_path_error=_attributes(join_element).get("JoinPathError"),
        )
    return RoleConstraintArgument.model_validate(data)


def _role_constraint(element: ET.Element) -> RoleConstraint:
    data: dict[str, Any] = _attributes(element)
    roles_wrapper = _child(element, "RoleConstraintRoles")
    data["RoleConstraintRoles"] = [
        RoleConstraintRole.model_validate(_attributes(item))
        for item in _children(roles_wrapper, "RoleConstraintRole")
    ]
    data["Argument"] = [
        _argument(item)
        for wrapper in _children(element, "Argument")
        for item in _children(wrapper, "RoleConstraintArgument")
    ]
    data["ValueConstraint"] = _string_values(element, "ValueConstraint")
    return RoleConstraint.model_validate(data)


def _model_note(element: ET.Element) -> ModelNote:
    data = _attributes(element)
    data["Note"] = _text(_child(element, "Note"))
    return ModelNote.model_validate(data)


def _fbm_model(element: ET.Element) -> FBMModel:
    data: dict[str, Any] = _attributes(element)
    mappings = (
        ("ValueTypes", "ValueType", _value_type),
        ("EntityTypes", "EntityType", _entity_type),
        ("FactTypes", "FactType", _fact_type),
        ("RoleConstraints", "RoleConstraint", _role_constraint),
        ("ModelNotes", "ModelNote", _model_note),
        ("Synonyms", "Synonym", lambda item: Synonym.model_validate(_attributes(item))),
    )
    for wrapper_name, item_name, parser in mappings:
        data[wrapper_name] = [
            parser(item)
            for wrapper in _children(element, wrapper_name)
            for item in _children(wrapper, item_name)
        ]
    return FBMModel.model_validate(data)


def _concept_instance_flag(element: ET.Element) -> ConceptInstanceFlag:
    data = _attributes(element)
    data["isDirty"] = _text(_child(element, "isDirty")) or False
    return ConceptInstanceFlag.model_validate(data)


def _concept_instance(element: ET.Element) -> ConceptInstance:
    data: dict[str, Any] = _attributes(element)
    data["isDirty"] = _text(_child(element, "isDirty")) or False
    data["ConceptInstanceFlag"] = [
        _concept_instance_flag(item) for item in _children(element, "ConceptInstanceFlag")
    ]
    return ConceptInstance.model_validate(data)


def _page(element: ET.Element) -> Page:
    data: dict[str, Any] = _attributes(element)
    data["ConceptInstance"] = [
        _concept_instance(item)
        for wrapper in _children(element, "ConceptInstance")
        for item in _children(wrapper, "ConceptInstance")
    ]
    return Page.model_validate(data)


def from_xml(source: str | bytes | ET.Element) -> Model:
    """Parse XML text or an Element into a validated :class:`Model`."""
    root = source if isinstance(source, ET.Element) else ET.fromstring(source)
    if _local_name(root.tag) != "Model":
        raise ValueError(f"Expected Model root element, found {_local_name(root.tag)!r}")
    fbm_element = _child(root, "FBMModel")
    if fbm_element is None:
        raise ValueError("The document has no FBMModel element")
    diagram_element = _child(root, "FBMDiagram")
    data: dict[str, Any] = _attributes(root)
    data["FBMModel"] = _fbm_model(fbm_element)
    data["FBMDiagram"] = [_page(item) for item in _children(diagram_element, "Page")]
    return Model.model_validate(data)


def load_fbm(path: Pathish) -> Model:
    """Read a `.fbm` XML document from *path*."""
    return from_xml(Path(path).read_bytes())


def _set_attributes(element: ET.Element, model: Any, names: Iterable[str]) -> None:
    for name in names:
        value = getattr(model, name)
        if value is None:
            continue
        alias = model.__class__.model_fields[name].serialization_alias or name
        if isinstance(value, Enum):
            value = value.value
        elif isinstance(value, bool):
            value = str(value).lower()
        element.set(alias, str(value))


def _append_strings(parent: ET.Element, wrapper_name: str, values: list[str]) -> None:
    wrapper = ET.SubElement(parent, wrapper_name)
    for value in values:
        ET.SubElement(wrapper, "string").text = value


def _append_subtypes(parent: ET.Element, values: list[SubtypeRelationship]) -> None:
    wrapper = ET.SubElement(parent, "SubtypeRelationships")
    for value in values:
        item = ET.SubElement(wrapper, "SubtypeRelationship")
        _set_attributes(item, value, value.__class__.model_fields)


def _write_value_type(parent: ET.Element, value: ValueType) -> None:
    item = ET.SubElement(parent, "ValueType")
    attribute_names = [name for name in value.__class__.model_fields if name not in {"instances", "value_constraints", "subtype_relationships"}]
    _set_attributes(item, value, attribute_names)
    _append_strings(item, "Instance", value.instances)
    _append_strings(item, "ValueConstraint", value.value_constraints)
    _append_subtypes(item, value.subtype_relationships)


def _write_entity_type(parent: ET.Element, value: EntityType) -> None:
    item = ET.SubElement(parent, "EntityType")
    excluded = {"graph_labels", "instances", "subtype_relationships"}
    _set_attributes(item, value, [name for name in value.__class__.model_fields if name not in excluded])
    _append_strings(item, "GraphLabel", value.graph_labels)
    _append_strings(item, "Instance", value.instances)
    _append_subtypes(item, value.subtype_relationships)


def _write_role(parent: ET.Element, value: Role) -> None:
    item = ET.SubElement(parent, "Role")
    _set_attributes(item, value, [name for name in value.__class__.model_fields if name != "value_constraints"])
    _append_strings(item, "ValueConstraint", value.value_constraints)


def _write_fact(parent: ET.Element, value: Fact) -> None:
    item = ET.SubElement(parent, "Fact")
    _set_attributes(item, value, ["id"])
    data_wrapper = ET.SubElement(item, "Data")
    for fact_data in value.data:
        data_item = ET.SubElement(data_wrapper, "FactData")
        _set_attributes(data_item, fact_data, ["role_id"])
        ET.SubElement(data_item, "Value").text = fact_data.data


def _write_reading(parent: ET.Element, value: FactTypeReading) -> None:
    item = ET.SubElement(parent, "FactTypeReading")
    _set_attributes(item, value, ["id", "front_reading_text", "following_reading_text"])
    parts = ET.SubElement(item, "PredicateParts")
    for part in value.predicate_parts:
        part_element = ET.SubElement(parts, "PredicatePart")
        _set_attributes(part_element, part, ["sequence_nr", "role_id", "prebound_reading_text", "postbound_reading_text"])
        ET.SubElement(part_element, "PredicatePartText").text = part.predicate_part_text


def _write_fact_type(parent: ET.Element, value: FactType) -> None:
    item = ET.SubElement(parent, "FactType")
    excluded = {"graph_labels", "roles", "facts", "fact_type_readings", "subtype_relationships"}
    _set_attributes(item, value, [name for name in value.__class__.model_fields if name not in excluded])
    _append_strings(item, "GraphLabel", value.graph_labels)
    roles = ET.SubElement(item, "RoleGroup")
    for role in value.roles:
        _write_role(roles, role)
    facts = ET.SubElement(item, "Facts")
    for fact in value.facts:
        _write_fact(facts, fact)
    readings = ET.SubElement(item, "FactTypeReadings")
    for reading in value.fact_type_readings:
        _write_reading(readings, reading)
    _append_subtypes(item, value.subtype_relationships)


def _write_role_constraint(parent: ET.Element, value: RoleConstraint) -> None:
    item = ET.SubElement(parent, "RoleConstraint")
    excluded = {"roles", "arguments", "value_constraints"}
    _set_attributes(item, value, [name for name in value.__class__.model_fields if name not in excluded])
    roles = ET.SubElement(item, "RoleConstraintRoles")
    for role in value.roles:
        role_element = ET.SubElement(roles, "RoleConstraintRole")
        _set_attributes(role_element, role, role.__class__.model_fields)
    arguments = ET.SubElement(item, "Argument")
    for argument in value.arguments:
        argument_element = ET.SubElement(arguments, "RoleConstraintArgument")
        _set_attributes(argument_element, argument, ["id", "sequence_nr"])
        role_wrapper = ET.SubElement(argument_element, "Role")
        for reference in argument.roles:
            reference_element = ET.SubElement(role_wrapper, "RoleReference")
            _set_attributes(reference_element, reference, ["role_id"])
        join_element = ET.SubElement(argument_element, "JoinPath")
        _set_attributes(join_element, argument.join_path, ["join_path_error"])
        path_wrapper = ET.SubElement(join_element, "RolePath")
        for reference in argument.join_path.role_path:
            reference_element = ET.SubElement(path_wrapper, "RoleReference")
            _set_attributes(reference_element, reference, ["role_id"])
    _append_strings(item, "ValueConstraint", value.value_constraints)


def _write_model_note(parent: ET.Element, value: ModelNote) -> None:
    item = ET.SubElement(parent, "ModelNote")
    _set_attributes(item, value, ["id", "guid", "joined_object_type_id", "is_mda_model_element"])
    ET.SubElement(item, "Note").text = value.note


def _write_fbm_model(parent: ET.Element, value: FBMModel) -> None:
    item = ET.SubElement(parent, "FBMModel")
    _set_attributes(item, value, ["model_id", "name", "core_version_number"])
    containers = (
        ("ValueTypes", value.value_types, _write_value_type),
        ("EntityTypes", value.entity_types, _write_entity_type),
        ("FactTypes", value.fact_types, _write_fact_type),
        ("RoleConstraints", value.role_constraints, _write_role_constraint),
        ("ModelNotes", value.model_notes, _write_model_note),
    )
    for container_name, values, writer in containers:
        container = ET.SubElement(item, container_name)
        for child in values:
            writer(container, child)
    synonyms = ET.SubElement(item, "Synonyms")
    for value_item in value.synonyms:
        synonym = ET.SubElement(synonyms, "Synonym")
        _set_attributes(synonym, value_item, value_item.__class__.model_fields)


def _write_flag(parent: ET.Element, value: ConceptInstanceFlag) -> None:
    item = ET.SubElement(parent, "ConceptInstanceFlag")
    _set_attributes(item, value, [name for name in value.__class__.model_fields if name != "is_dirty"])
    ET.SubElement(item, "isDirty").text = str(value.is_dirty).lower()


def _write_concept_instance(parent: ET.Element, value: ConceptInstance) -> None:
    item = ET.SubElement(parent, "ConceptInstance")
    _set_attributes(item, value, [name for name in value.__class__.model_fields if name not in {"is_dirty", "flags"}])
    ET.SubElement(item, "isDirty").text = str(value.is_dirty).lower()
    for flag in value.flags:
        _write_flag(item, flag)


def to_xml(
    model: Model,
    *,
    encoding: str = "utf-8",
    xml_declaration: bool = True,
    namespace: str | None = None,
    schema_location: str | None = None,
) -> bytes:
    """Serialize a model using canonical `FBMModel`/`FBMDiagram` names."""
    root = ET.Element("Model")
    _set_attributes(root, model, ["xsd_version_nr"])
    if namespace:
        root.set("xmlns", namespace)
    if schema_location:
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        root.set("xsi:schemaLocation", schema_location)
    _write_fbm_model(root, model.fbm_model)
    diagrams = ET.SubElement(root, "FBMDiagram")
    for page in model.fbm_diagram:
        page_element = ET.SubElement(diagrams, "Page")
        _set_attributes(page_element, page, ["id", "name", "language", "is_core_model_page"])
        instances = ET.SubElement(page_element, "ConceptInstance")
        for instance in page.concept_instances:
            _write_concept_instance(instances, instance)
    ET.indent(root, space="  ")
    return ET.tostring(root, encoding=encoding, xml_declaration=xml_declaration)


def save_fbm(model: Model, path: Pathish, **kwargs: Any) -> None:
    """Serialize *model* and write it to *path*."""
    Path(path).write_bytes(to_xml(model, **kwargs))
