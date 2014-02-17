#!/usr/bin/env python2

from parser import Parser
import networkx as nx

# parse file and populate obo data and graph object
terms = dict()
typedefs = dict()

# extract relationships from data
with open("BrendaTissueOBO.txt") as fp:
    parser = Parser(fp)
    for stanza in parser:
        if stanza.name == 'Term':
            terms[stanza.tags["id"][0]] = stanza.tags
        if stanza.name == 'Typedef':
            typedefs[stanza.tags["id"][0]] = stanza.tags

# add appropriate edges in graph
G = nx.Graph()
for key,value in terms.iteritems():
    for td in typedefs.keys():
        if value.has_key(td):
            for edge in value[td]:
                G.add_edge(key, edge) #TODO: add edge type // OR: add graph per edge type


