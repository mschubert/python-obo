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
G = {td:nx.Graph() for td in typedefs.keys()}

for key,value in terms.iteritems():
    if value.has_key('is_a'):
        G['is_a'].add_edge(key, value['is_a'][0])

    if value.has_key('relationship'):
        for rs in value['relationship']:
            rel,to = rs.split()
            G[rel].add_edge(key, to)


