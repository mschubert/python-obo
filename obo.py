#!/usr/bin/env python2

import itertools as it
from parser import Parser
import networkx as nx
from networkx.algorithms.traversal.depth_first_search import dfs_successors, dfs_predecessors

def loadAndParseFile(fname="BrendaTissueOBO.txt"):
    # parse file and populate obo data and graph object
    terms = dict() # TODO: put the term values in tree (nodes are dicts in nx)
    typedefs = dict()

    # extract relationships from data
    with open(fname) as fp:
        parser = Parser(fp)
        for stanza in parser:
            if stanza.name == 'Term':
                terms[stanza.tags["id"][0]] = stanza.tags
            if stanza.name == 'Typedef':
                typedefs[stanza.tags["id"][0]] = stanza.tags

    # add appropriate edges in graph
    G = {td:nx.DiGraph() for td in typedefs.keys()}

    for key,value in terms.iteritems():
        if value.has_key('is_a'):
            for val in value['is_a']:
                G['is_a'].add_edge(key, val)

        if value.has_key('relationship'):
            for rs in value['relationship']:
                rel,to = rs.split()
                G[rel].add_edge(key, to)

    return typedefs, terms, G

def getAllSuccessors(G, nodeId):
    successors = dfs_successors(G, source=nodeId).values()
    return set(it.chain.from_iterable(it.repeat(x,1) if
        isinstance(x,str) else x for x in successors))

def getAllPredecessors(G, nodeId):
    predecessors = dfs_predecessors(G, source=nodeId).values()
    return set(it.chain.from_iterable(it.repeat(x,1) if
        isinstance(x,str) else x for x in predecessors))

def coarsenIdentifiers(G, nodes, identifiers):
    # temporarily remove all edges upstream of node list given
    removedEdges = []
    for node in nodes:
        for child in G.successors(node):
            removedEdges.append((node,child))
            G.remove_edge(node,child)

    # get all children of resulting graph
    lookup = dict()
    for node in nodes:
        for pred in getAllPredecessors(G, node):
            lookup[pred] = node

    # re-add temporarily removed edges
    for src, dest in removedEdges:
        G.add_edge(src, dest)

    return [lookup[i] for i in identifiers]

def coarsenLabels(G, nodes, labels, synonyms=False, exact=True):
    # map labels to identifiers

#    coarsenIdentifiers(...)
    pass



typedefs, terms, G = loadAndParseFile("BrendaTissueOBO.txt")

#try: is_a, if no nonnection otherwise then part_of, then develops_from (or similar)
#connected = nx.compose(G['part_of'], G['develops_from'])
gg = nx.compose_all(G.values())

#TODO: function for BTO:id->label, label(+/-synonyms)->BTO:id
# graph cutting with ID list
# ? other ontoCAT functions

coarsenIdentifiers(gg, ['BTO:0000000'], ['BTO:0000042'])

