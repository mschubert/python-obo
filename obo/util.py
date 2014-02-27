import numpy as np
import networkx as nx

def getAllSuccessors(G, nodeId):
    successors = dfs_successors(G, source=nodeId).values()
    return set(it.chain.from_iterable(it.repeat(x,1) if
        isinstance(x,str) else x for x in successors))

def getAllPredecessors(G, nodeId):
    return getAllSuccessors(G.reverse(), nodeId)

def coarsenIdentifiers(G, nodes, identifiers):
    def plength(G, source, targets):
        target = None
        length = np.Inf
        for t in targets:
            try:
                current = len(nx.shortest_path(G, source, t))
                if current < length:
                    length = current
                    target = t
            except nx.NetworkXNoPath:
                pass
        return target

    return [plength(G,i,nodes) for i in identifiers]

#def coarsenLabels(G, nodes, labels, synonyms=False, exact=True):
#    # map labels to identifiers
#
##    coarsenIdentifiers(...)
#    pass
#
#def writeSIF(G, None):
#    pass
#
##typedefs, terms, G = loadAndParseFile("BrendaTissueOBO.txt")
##try: is_a, if no nonnection otherwise then part_of, then develops_from (or similar)
##connected = nx.compose(G['part_of'], G['develops_from'])
#gg = nx.compose_all(G.values())
#gg = gg.reverse()
#
##TODO: function for BTO:id->label, label(+/-synonyms)->BTO:id
## graph cutting with ID list
## ? other ontoCAT functions
#
#coarsenIdentifiers(gg, ['BTO:0000000'], ['BTO:0000042'])
#

