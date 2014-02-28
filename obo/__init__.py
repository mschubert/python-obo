#!/usr/bin/env python2

import itertools as it
from parser import Parser
import networkx as nx
from networkx.algorithms.traversal.depth_first_search import dfs_successors
import numpy as np

class OBO(nx.DiGraph):
    def __init__(self, fname):
        super(nx.DiGraph, self)
        nx.DiGraph.__init__(self)
        self.typedefs = dict()

        with open(fname) as fp:
            parser = Parser(fp)
            for stanza in parser:
                if stanza.name == 'Term':
                    self.add_node(stanza.tags["id"][0], stanza.tags)
                if stanza.name == 'Typedef':
                    self.typedefs[stanza.tags["id"][0]] = stanza.tags

        self._edges = {key:[] for key in self.typedefs.keys()}

        for key,value in self.node.iteritems():
            if value.has_key('is_a'):
                for val in value['is_a']:
                    self._edges['is_a'].append((key, val))

            if value.has_key('relationship'):
                for rs in value['relationship']:
                    rel,to = rs.split()
                    self._edges[rel].append((key, to))

        self.active_edges = ['is_a']

    @property
    def active_edges(self):
        return self._active_edges

    @active_edges.setter
    def active_edges(self, ebunch):
        self.remove_edges_from(self.edges())
        for arg in ebunch:
            self.add_edges_from(self._edges[arg])
        self._active_edges = ebunch

    @property
    def edge_types(self):
        return self._edges.keys()

    def add_edge_type(self):
        raise NotImplementedError()

    def remove_edge_type(self):
        raise NotImplementedError()

