from rdflib import RDF, Graph, URIRef

from py_traceability_rdf import Traceability


def test_namespace_exists():
    assert Traceability._NS is not None
    assert str(Traceability._NS).startswith("http://")


def test_classes_exist():
    assert isinstance(Traceability.IdentifiableObject, URIRef)
    assert isinstance(Traceability.Requirement, URIRef)
    assert isinstance(Traceability.DesignElement, URIRef)
    assert isinstance(Traceability.Implementation, URIRef)
    assert isinstance(Traceability.TestCase, URIRef)
    assert isinstance(Traceability.Stakeholder, URIRef)


def test_object_properties_exist():
    assert isinstance(Traceability.RationaleRelation, URIRef)
    assert isinstance(Traceability.satisfies, URIRef)
    assert isinstance(Traceability.verifies, URIRef)
    assert isinstance(Traceability.covers, URIRef)
    assert isinstance(Traceability.realizes, URIRef)
    assert isinstance(Traceability.justifies, URIRef)
    assert isinstance(Traceability.references, URIRef)
    assert isinstance(Traceability.involves, URIRef)


def test_datatype_properties_exist():
    assert isinstance(Traceability.identifier, URIRef)
    assert isinstance(Traceability.title, URIRef)
    assert isinstance(Traceability.modality, URIRef)
    assert isinstance(Traceability.condition, URIRef)


def test_workflow():
    g = Graph()
    g.bind("trc", Traceability._NS)

    req = URIRef("http://example.org#req_x")
    design = URIRef("http://example.org#design_x")
    module = URIRef("http://example.org#module_x")
    test = URIRef("http://example.org#test_x")
    stakeholder = URIRef("http://example.org#stakeholder_x")
    source = URIRef("http://example.org#source_x")
    decision = URIRef("http://example.org#decision_x")

    g.add((req, RDF.type, Traceability.Requirement))
    g.add((design, RDF.type, Traceability.DesignElement))
    g.add((module, RDF.type, Traceability.Implementation))
    g.add((test, RDF.type, Traceability.TestCase))
    g.add((stakeholder, RDF.type, Traceability.Stakeholder))
    g.add((source, RDF.type, Traceability.Source))
    g.add((decision, RDF.type, Traceability.Decision))
    g.add((design, Traceability.satisfies, req))
    g.add((module, Traceability.realizes, design))
    g.add((test, Traceability.verifies, req))
    g.add((test, Traceability.covers, module))
    g.add((source, Traceability.justifies, req))
    g.add((decision, Traceability.references, req))
    g.add((design, Traceability.involves, stakeholder))

    assert (design, Traceability.satisfies, req) in g
    assert (module, Traceability.realizes, design) in g
    assert (test, Traceability.verifies, req) in g
    assert (test, Traceability.covers, module) in g
    assert (source, Traceability.justifies, req) in g
    assert (decision, Traceability.references, req) in g
    assert (design, Traceability.involves, stakeholder) in g
