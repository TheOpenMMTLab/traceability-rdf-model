from pathlib import Path
from rdflib.namespace import DefinedNamespace
from rdflib import URIRef
from .ontology_reader import OntologyReader

current_dir = Path(__file__).parent
ontology_file = current_dir / "traceability.ttl"
ontology = OntologyReader(str(ontology_file))


class Traceability(DefinedNamespace):

    _NS = ontology.get_namespace()

    TraceableObject: URIRef = ontology.get_class("#TraceableObject")
    Requirement: URIRef = ontology.get_class("#Requirement")
    DesignElement: URIRef = ontology.get_class("#DesignElement")
    CodeModule: URIRef = ontology.get_class("#CodeModule")
    TestCase: URIRef = ontology.get_class("#TestCase")
    Decision: URIRef = ontology.get_class("#Decision")
    Rationale: URIRef = ontology.get_class("#Rationale")
    Source: URIRef = ontology.get_class("#Source")
    Stakeholder: URIRef = ontology.get_class("#Stakeholder")

    EvolutionRelation: URIRef = ontology.get_object_property("#EvolutionRelation")
    SatisfactionRelation: URIRef = ontology.get_object_property("#SatisfactionRelation")
    DependencyRelation: URIRef = ontology.get_object_property("#DependencyRelation")
    RationaleRelation: URIRef = ontology.get_object_property("#RationaleRelation")

    contains: URIRef = ontology.get_object_property("#contains")
    satisfies: URIRef = ontology.get_object_property("#satisfies")
    verifies: URIRef = ontology.get_object_property("#verifies")
    implements: URIRef = ontology.get_object_property("#implements")
    tracesTo: URIRef = ontology.get_object_property("#tracesTo")
    isJustifiedBy: URIRef = ontology.get_object_property("#isJustifiedBy")
    originatesFrom: URIRef = ontology.get_object_property("#originatesFrom")
    createdBy: URIRef = ontology.get_object_property("#createdBy")

    identifier: URIRef = ontology.get_datatype_property("#identifier")
    title: URIRef = ontology.get_datatype_property("#title")
    description: URIRef = ontology.get_datatype_property("#description")
    createdAt: URIRef = ontology.get_datatype_property("#createdAt")
    modifiedAt: URIRef = ontology.get_datatype_property("#modifiedAt")
    criticality: URIRef = ontology.get_datatype_property("#criticality")
    designType: URIRef = ontology.get_datatype_property("#designType")
    programmingLanguage: URIRef = ontology.get_datatype_property("#programmingLanguage")
    modulePath: URIRef = ontology.get_datatype_property("#modulePath")
    testType: URIRef = ontology.get_datatype_property("#testType")
    verificationStatus: URIRef = ontology.get_datatype_property("#verificationStatus")
    decisionStatus: URIRef = ontology.get_datatype_property("#decisionStatus")
    rationaleKind: URIRef = ontology.get_datatype_property("#rationaleKind")
    sourceType: URIRef = ontology.get_datatype_property("#sourceType")
    sourceReference: URIRef = ontology.get_datatype_property("#sourceReference")
    stakeholderRole: URIRef = ontology.get_datatype_property("#stakeholderRole")
    organization: URIRef = ontology.get_datatype_property("#organization")
