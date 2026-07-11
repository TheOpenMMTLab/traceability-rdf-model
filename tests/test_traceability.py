from py_traceability_rdf import Traceability
from rdflib import URIRef, Graph, RDF


def test_namespace_exists():
    assert Traceability._NS is not None
    assert str(Traceability._NS).startswith("http://")


def test_classes_exist():
    assert isinstance(Traceability.IdentifiableObject, URIRef)
    assert isinstance(Traceability.Requirement, URIRef)
    assert isinstance(Traceability.DesignElement, URIRef)
    assert isinstance(Traceability.CodeModule, URIRef)
    assert isinstance(Traceability.TestCase, URIRef)
    assert isinstance(Traceability.Stakeholder, URIRef)


def test_object_properties_exist():
    assert isinstance(Traceability.satisfies, URIRef)
    assert isinstance(Traceability.verifies, URIRef)
    assert isinstance(Traceability.implements, URIRef)
    assert isinstance(Traceability.involves, URIRef)
    assert isinstance(Traceability.isJustifiedBy, URIRef)


def test_datatype_properties_exist():
    assert isinstance(Traceability.identifier, URIRef)
    assert isinstance(Traceability.title, URIRef)
    assert isinstance(Traceability.criticality, URIRef)


def test_workflow():
    g = Graph()
    g.bind("trc", Traceability._NS)

    req = URIRef("http://example.org#req_x")
    design = URIRef("http://example.org#design_x")
    module = URIRef("http://example.org#module_x")
    test = URIRef("http://example.org#test_x")
    stakeholder = URIRef("http://example.org#stakeholder_x")

    g.add((req, RDF.type, Traceability.Requirement))
    g.add((design, RDF.type, Traceability.DesignElement))
    g.add((module, RDF.type, Traceability.CodeModule))
    g.add((test, RDF.type, Traceability.TestCase))
    g.add((stakeholder, RDF.type, Traceability.Stakeholder))
    g.add((design, Traceability.satisfies, req))
    g.add((module, Traceability.implements, design))
    g.add((test, Traceability.verifies, module))
    g.add((design, Traceability.involves, stakeholder))

    assert (design, Traceability.satisfies, req) in g
    assert (module, Traceability.implements, design) in g
    assert (test, Traceability.verifies, module) in g
    assert (design, Traceability.involves, stakeholder) in g
