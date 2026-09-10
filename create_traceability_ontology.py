import tomllib
from rdflib import (
    DCTERMS,
    OWL,
    RDF,
    RDFS,
    XSD,
    BNode,
    Graph,
    Literal,
    Namespace,
    URIRef,
)
from rdflib.collection import Collection


def create_union(classes):
    union_node = BNode()
    members_node = BNode()
    g.add((union_node, RDF.type, OWL.Class))
    g.add((union_node, OWL.unionOf, members_node))
    Collection(g, members_node, classes)
    return union_node


with open("pyproject.toml", "rb") as f:
    pyproject_data = tomllib.load(f)


KEY = "traceability"

NS = Namespace(f"http://frittenburger.de/ontology/{KEY}#")

g = Graph()
g.namespace_manager.bind("trc", NS)

ontology = URIRef(f"https://gitlab.hpi.de/dfriedenberger/{KEY}")
g.add((ontology, RDF.type, OWL.Ontology))
g.add((ontology, DCTERMS.title, Literal("Traceability Ontology")))
g.add((ontology, DCTERMS.description, Literal("An RDF ontology for object-level traceability.", lang="en")))
g.add((ontology, OWL.versionInfo, Literal(pyproject_data["tool"]["poetry"]["version"])))
g.add((ontology, DCTERMS.creator, Literal("Dirk Friedenberger")))
g.add((ontology, DCTERMS.creator, URIRef("https://www.researchgate.net/profile/Dirk_Friedenberger")))
g.add((ontology, DCTERMS.identifier, Literal(NS)))

# concepts

# Model Taxonomy
g.add((NS.IdentifiableObject, RDF.type, OWL.Class))
g.add((NS.IdentifiableObject, RDFS.label, Literal("Identifiable Object", lang='en')))
g.add((NS.IdentifiableObject, RDFS.comment, Literal("Abstract base class for entities with identifier and title metadata.", lang='en')))

g.add((NS.TraceableObject, RDF.type, OWL.Class))
g.add((NS.TraceableObject, RDFS.label, Literal("Traceable Object", lang='en')))
g.add((NS.TraceableObject, RDFS.comment, Literal("Abstract base class for all traceable entities in the model.", lang='en')))
g.add((NS.TraceableObject, RDFS.subClassOf, NS.IdentifiableObject))


g.add((NS.Requirement, RDF.type, OWL.Class))
g.add((NS.Requirement, RDFS.label, Literal("Requirement", lang='en')))
g.add((NS.Requirement, RDFS.comment, Literal("A requirement that defines a goal, constraint, or expected system behavior.", lang='en')))
g.add((NS.Requirement, RDFS.subClassOf, NS.TraceableObject))

g.add((NS.DesignElement, RDF.type, OWL.Class))
g.add((NS.DesignElement, RDFS.label, Literal("Design Element", lang='en')))
g.add((NS.DesignElement, RDFS.comment, Literal("A design artifact that realizes requirements.", lang='en')))
g.add((NS.DesignElement, RDFS.subClassOf, NS.TraceableObject))


g.add((NS.Implementation, RDF.type, OWL.Class))
g.add((NS.Implementation, RDFS.label, Literal("Implementation", lang='en')))
g.add((NS.Implementation, RDFS.comment, Literal("A software implementation artifact such as a module, class, or function.", lang='en')))
g.add((NS.Implementation, RDFS.subClassOf, NS.TraceableObject))


g.add((NS.TestCase, RDF.type, OWL.Class))
g.add((NS.TestCase, RDFS.label, Literal("Test Case", lang='en')))
g.add((NS.TestCase, RDFS.comment, Literal("A verification artifact used to validate requirements or implementation.", lang='en')))
g.add((NS.TestCase, RDFS.subClassOf, NS.TraceableObject))


g.add((NS.Decision, RDF.type, OWL.Class))
g.add((NS.Decision, RDFS.label, Literal("Decision", lang='en')))
g.add((NS.Decision, RDFS.comment, Literal("A decision made during development or change management.", lang='en')))
g.add((NS.Decision, RDFS.subClassOf, NS.TraceableObject))

g.add((NS.Source, RDF.type, OWL.Class))
g.add((NS.Source, RDFS.label, Literal("Source", lang='en')))
g.add((NS.Source, RDFS.comment, Literal("A source artifact such as a document, note, ticket, or standard.", lang='en')))
g.add((NS.Source, RDFS.subClassOf, NS.TraceableObject))

g.add((NS.Stakeholder, RDF.type, OWL.Class))
g.add((NS.Stakeholder, RDFS.label, Literal("Stakeholder", lang='en')))
g.add((NS.Stakeholder, RDFS.comment, Literal("A person, role, or organization responsible for creating or changing artifacts.", lang='en')))
g.add((NS.Stakeholder, RDFS.subClassOf, NS.IdentifiableObject))

# Datatype properties
g.add((NS.identifier, RDF.type, OWL.DatatypeProperty))
g.add((NS.identifier, RDFS.domain, NS.IdentifiableObject))
g.add((NS.identifier, RDFS.range, XSD.string))
g.add((NS.identifier, RDFS.label, Literal("Identifier", lang='en')))
g.add((NS.identifier, RDFS.comment, Literal("Stable unique key of a traceable object.", lang='en')))

g.add((NS.title, RDF.type, OWL.DatatypeProperty))
g.add((NS.title, RDFS.domain, NS.IdentifiableObject))
g.add((NS.title, RDFS.range, XSD.string))
g.add((NS.title, RDFS.label, Literal("Title", lang='en')))
g.add((NS.title, RDFS.comment, Literal("Human-readable title of a traceable object.", lang='en')))

g.add((NS.createdAt, RDF.type, OWL.DatatypeProperty))
g.add((NS.createdAt, RDFS.domain, NS.TraceableObject))
g.add((NS.createdAt, RDFS.range, XSD.dateTime))
g.add((NS.createdAt, RDFS.label, Literal("Created At", lang='en')))
g.add((NS.createdAt, RDFS.comment, Literal("Timestamp when the object was initially created.", lang='en')))

g.add((NS.modifiedAt, RDF.type, OWL.DatatypeProperty))
g.add((NS.modifiedAt, RDFS.domain, NS.TraceableObject))
g.add((NS.modifiedAt, RDFS.range, XSD.dateTime))
g.add((NS.modifiedAt, RDFS.label, Literal("Modified At", lang='en')))
g.add((NS.modifiedAt, RDFS.comment, Literal("Timestamp of the latest modification.", lang='en')))

g.add((NS.modality, RDF.type, OWL.DatatypeProperty))
g.add((NS.modality, RDFS.domain, NS.Requirement))
g.add((NS.modality, RDFS.range, XSD.string))
g.add((NS.modality, RDFS.label, Literal("Modality", lang='en')))
g.add((NS.modality, RDFS.comment, Literal("Binding level of the requirement, for example must, should, or may.", lang='en')))

g.add((NS.condition, RDF.type, OWL.DatatypeProperty))
g.add((NS.condition, RDFS.domain, NS.Requirement))
g.add((NS.condition, RDFS.range, XSD.string))
g.add((NS.condition, RDFS.label, Literal("Condition", lang='en')))
g.add((NS.condition, RDFS.comment, Literal("Optional condition under which the requirement applies.", lang='en')))

g.add((NS.designType, RDF.type, OWL.DatatypeProperty))
g.add((NS.designType, RDFS.domain, NS.DesignElement))
g.add((NS.designType, RDFS.range, XSD.string))
g.add((NS.designType, RDFS.label, Literal("Design Type", lang='en')))
g.add((NS.designType, RDFS.comment, Literal("Design element kind, for example architecture block, interface, or SysML element.", lang='en')))

g.add((NS.implementationType, RDF.type, OWL.DatatypeProperty))
g.add((NS.implementationType, RDFS.domain, NS.Implementation))
g.add((NS.implementationType, RDFS.range, XSD.string))
g.add((NS.implementationType, RDFS.label, Literal("Implementation Type", lang='en')))
g.add((NS.implementationType, RDFS.comment, Literal("Technology or realization type of the implementation artifact, for example software, firmware, or hardware.", lang='en')))

g.add((NS.version, RDF.type, OWL.DatatypeProperty))
g.add((NS.version, RDFS.domain, NS.Implementation))
g.add((NS.version, RDFS.range, XSD.string))
g.add((NS.version, RDFS.label, Literal("Version", lang='en')))
g.add((NS.version, RDFS.comment, Literal("Version or revision identifier of the implementation artifact.", lang='en')))

g.add((NS.testType, RDF.type, OWL.DatatypeProperty))
g.add((NS.testType, RDFS.domain, NS.TestCase))
g.add((NS.testType, RDFS.range, XSD.string))
g.add((NS.testType, RDFS.label, Literal("Test Type", lang='en')))
g.add((NS.testType, RDFS.comment, Literal("Type of test case, for example unit, integration, or acceptance.", lang='en')))

g.add((NS.verificationStatus, RDF.type, OWL.DatatypeProperty))
g.add((NS.verificationStatus, RDFS.domain, NS.TestCase))
g.add((NS.verificationStatus, RDFS.range, XSD.string))
g.add((NS.verificationStatus, RDFS.label, Literal("Verification Status", lang='en')))
g.add((NS.verificationStatus, RDFS.comment, Literal("Verification result state, for example planned, passed, failed, or blocked.", lang='en')))

g.add((NS.decisionStatus, RDF.type, OWL.DatatypeProperty))
g.add((NS.decisionStatus, RDFS.domain, NS.Decision))
g.add((NS.decisionStatus, RDFS.range, XSD.string))
g.add((NS.decisionStatus, RDFS.label, Literal("Decision Status", lang='en')))
g.add((NS.decisionStatus, RDFS.comment, Literal("Decision state, for example proposed, accepted, rejected, or deprecated.", lang='en')))

g.add((NS.sourceType, RDF.type, OWL.DatatypeProperty))
g.add((NS.sourceType, RDFS.domain, NS.Source))
g.add((NS.sourceType, RDFS.range, XSD.string))
g.add((NS.sourceType, RDFS.label, Literal("Source Type", lang='en')))
g.add((NS.sourceType, RDFS.comment, Literal("Source type, for example document, standard, ticket, or meeting note.", lang='en')))

g.add((NS.sourceReference, RDF.type, OWL.DatatypeProperty))
g.add((NS.sourceReference, RDFS.domain, NS.Source))
g.add((NS.sourceReference, RDFS.range, XSD.anyURI))
g.add((NS.sourceReference, RDFS.label, Literal("Source Reference", lang='en')))
g.add((NS.sourceReference, RDFS.comment, Literal("Resolvable URI or external reference to the source artifact.", lang='en')))

g.add((NS.stakeholderRole, RDF.type, OWL.DatatypeProperty))
g.add((NS.stakeholderRole, RDFS.domain, NS.Stakeholder))
g.add((NS.stakeholderRole, RDFS.range, XSD.string))
g.add((NS.stakeholderRole, RDFS.label, Literal("Stakeholder Role", lang='en')))
g.add((NS.stakeholderRole, RDFS.comment, Literal("Primary role of the stakeholder in lifecycle activities.", lang='en')))

g.add((NS.organization, RDF.type, OWL.DatatypeProperty))
g.add((NS.organization, RDFS.domain, NS.Stakeholder))
g.add((NS.organization, RDFS.range, XSD.string))
g.add((NS.organization, RDFS.label, Literal("Organization", lang='en')))
g.add((NS.organization, RDFS.comment, Literal("Organization or team affiliation of the stakeholder.", lang='en')))


# Relations

# Four categories (Satisfaction, Dependency, Evolution, Rationale) by Ramesh & Jarke (2001)
# Abstract evolution relation
g.add((NS.EvolutionRelation, RDF.type, OWL.ObjectProperty))
g.add((NS.EvolutionRelation, RDFS.label, Literal("Evolution Relation", lang='en')))
g.add((NS.EvolutionRelation, RDFS.comment, Literal("Abstract relation category for evolution links.", lang='en')))

# Abstract satisfaction relation
g.add((NS.SatisfactionRelation, RDF.type, OWL.ObjectProperty))
g.add((NS.SatisfactionRelation, RDFS.label, Literal("Satisfaction Relation", lang='en')))
g.add((NS.SatisfactionRelation, RDFS.comment, Literal("Abstract relation category for satisfaction and verification links.", lang='en')))

# Abstract dependency relation
g.add((NS.DependencyRelation, RDF.type, OWL.ObjectProperty))
g.add((NS.DependencyRelation, RDFS.label, Literal("Dependency Relation", lang='en')))
g.add((NS.DependencyRelation, RDFS.comment, Literal("Abstract relation category for dependency and decomposition links.", lang='en')))

# Abstract rationale relation
g.add((NS.RationaleRelation, RDF.type, OWL.ObjectProperty))
g.add((NS.RationaleRelation, RDFS.label, Literal("Rationale Relation", lang='en')))
g.add((NS.RationaleRelation, RDFS.comment, Literal("Abstract relation category for justification-related links.", lang='en')))

# Explicit relation definition for links

# Satisfaction
g.add((NS.satisfies, RDF.type, OWL.ObjectProperty))
g.add((NS.satisfies, RDFS.subPropertyOf, NS.SatisfactionRelation))
g.add((NS.satisfies, RDFS.domain, NS.DesignElement))
g.add((NS.satisfies, RDFS.range, NS.Requirement))
g.add((NS.satisfies, RDFS.label, Literal("satisfies", lang='en')))
g.add((NS.satisfies, RDFS.comment, Literal("Links a design element to a requirement it satisfies.", lang='en')))

g.add((NS.verifies, RDF.type, OWL.ObjectProperty))
g.add((NS.verifies, RDFS.subPropertyOf, NS.SatisfactionRelation))
g.add((NS.verifies, RDFS.domain, NS.TestCase))
g.add((NS.verifies, RDFS.range, NS.Requirement))
g.add((NS.verifies, RDFS.label, Literal("verifies", lang='en')))
g.add((NS.verifies, RDFS.comment, Literal("Links a test case to a requirement it verifies.", lang='en')))

g.add((NS.covers, RDF.type, OWL.ObjectProperty))
g.add((NS.covers, RDFS.subPropertyOf, NS.SatisfactionRelation))
g.add((NS.covers, RDFS.domain, NS.TestCase))
g.add((NS.covers, RDFS.range, NS.Implementation))
g.add((NS.covers, RDFS.label, Literal("covers", lang='en')))
g.add((NS.covers, RDFS.comment, Literal("Links a test case to an implementation artifact it covers.", lang='en')))

g.add((NS.realizes, RDF.type, OWL.ObjectProperty))
g.add((NS.realizes, RDFS.subPropertyOf, NS.DependencyRelation))
g.add((NS.realizes, RDFS.domain, NS.Implementation))
g.add((NS.realizes, RDFS.range, NS.DesignElement))
g.add((NS.realizes, RDFS.label, Literal("realizes", lang='en')))
g.add((NS.realizes, RDFS.comment, Literal("Links an implementation artifact to the design element it realizes.", lang='en')))

# Dependency
g.add((NS.contains, RDF.type, OWL.ObjectProperty))
g.add((NS.contains, RDFS.subPropertyOf, NS.DependencyRelation))
g.add((NS.contains, RDFS.domain, NS.Requirement))
g.add((NS.contains, RDFS.range, NS.Requirement))
g.add((NS.contains, RDFS.label, Literal("contains", lang='en')))
g.add((NS.contains, RDFS.comment, Literal("Represents hierarchical containment between requirements.", lang='en')))

# Rationale
g.add((NS.justifies, RDF.type, OWL.ObjectProperty))
g.add((NS.justifies, RDFS.subPropertyOf, NS.RationaleRelation))
g.add((NS.justifies, RDFS.domain, NS.Source))
g.add((NS.justifies, RDFS.range, NS.Requirement))
g.add((NS.justifies, RDFS.label, Literal("justifies", lang='en')))
g.add((NS.justifies, RDFS.comment, Literal("Links a source to a requirement it justifies.", lang='en')))

g.add((NS.references, RDF.type, OWL.ObjectProperty))
g.add((NS.references, RDFS.subPropertyOf, NS.RationaleRelation))
g.add((NS.references, RDFS.domain, NS.Decision))
g.add((NS.references, RDFS.range, NS.TraceableObject))
g.add((NS.references, RDFS.label, Literal("references", lang='en')))
g.add((NS.references, RDFS.comment, Literal("Links a decision to a traceable object it references.", lang='en')))

g.add((NS.involves, RDF.type, OWL.ObjectProperty))
g.add((NS.involves, RDFS.subPropertyOf, NS.DependencyRelation))
g.add((NS.involves, RDFS.domain, NS.TraceableObject))
g.add((NS.involves, RDFS.range, NS.Stakeholder))
g.add((NS.involves, RDFS.label, Literal("involves", lang='en')))
g.add((NS.involves, RDFS.comment, Literal("Links a traceable object to a stakeholder involved in it.", lang='en')))

g.serialize(destination="py_traceability_rdf/traceability.ttl", format="turtle")
