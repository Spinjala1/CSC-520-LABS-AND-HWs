from graph import Graph
from VfyQuarterIndependentSet import VfyQuarterIndependentSet

HNC2QISv =  'VERBOSE: PolyReduceHalfNodeCoverToQuarterIndpenedentSet() - '
VERBOSE = True
def printV(text):
    if VERBOSE: print(f'{HNC2QISv}{text}')

HNC2QISd =  'DEV:PolyReduceHalfNodeCoverToQuarterIndpenedentSet() - '
DEV = False
def printD(text):
    if DEV: print(f'{HNC2QISd}{text}')


def make_new_node(nodes,new_nodes):
    '''
    Arguments:
      nodes -- list of nodes in the halfNodeCover instance
      new_nodes -- new nodes

    Returns a node name consisting of Z's, which is not in either
    nodes or new_nodes
    '''
    
    new_node = 'Z'
    names = nodes + new_nodes
    for n in names:
        if n == new_node: new_node += 'Z'
        
    return new_node

    
def PolyReduceHalfNodeCoverToQuarterIndependentSet(halfNodeCover_instance):
    graph_str = halfNodeCover_instance

    g = Graph(graph_str, weighted=False, directed=False)
    nodes = list(g.nodes.keys())

    new_nodes = []
    
    ### HW #2: Create the correct number of new node names,
    ###             making sure that they're unique
    #
    nodes.extend(new_nodes) ## Add the new nodes to the old ones

    ### HW #2: Create new edges to connect the new nodes
    ###             to the graph in the correct way. Remember,
    ###             in an undirected graph, the edge 'a,b' is
    ###             the same as the edge 'b,a', and including
    ###             both in a graph would incur a WCBC error from
    ###             graph.py
    #
    new_edges = []

    ### HW #2: Use your work above to make the needed transformation
    ###            of halfNodeCover_instance into quarterIndependentSet_instance,
    ###            such that quarterIndependentSet_instance will be a positive
    ###            instance of QuarterIndependentSet iff halfNodeCover_instance
    ###            is a positive instance of HalfNodeCover.  Making no change, as
    ###            in the code below that you are asked to change, could result in
    ###            mapping a negative instance of HalfNodeCover onto a positive
    ###            instance of QuarterIndependent set.
    #
    quarterIndependentSet_instance = halfNodeCover_instance ## ** CHANGE THIS **
    
    printV(f'quarterIndependentSet_instance = "{quarterIndependentSet_instance}"')
    
    return quarterIndependentSet_instance
C =  PolyReduceHalfNodeCoverToQuarterIndependentSet


def vfyHalfNodeCoverViaVfyQuarterIndepedentSet(halfNodeCover_instance,S,H):
    quarterIndependentSet_instance = C(halfNodeCover_instance)
    graph_str = halfNodeCover_instance

    g = Graph(graph_str, weighted=False, directed=False)
    nodes = list(g.nodes.keys()) #Convert to list
    
    # The hint for quarterIndependentSet consists of whatever nodes are not
    # in the hint for halfnodeCover
    # 
    printD(f'nodes = {nodes}, H = {H.split()}')
    H_independent_set = ' '.join([node for node in nodes if node not in H.split()])

    printD('Hint for Quarter Independent Set verifier to use on converted' + \
           f' instance: "{H_independent_set}":\n ' + \
           f'        (nodes in node cover graph instance, but not in H = "{H}")')
    result = \
        VfyQuarterIndependentSet(quarterIndependentSet_instance,S,H_independent_set)
    return result


if __name__ == '__main__':

    def test_case(F,I,S,H,expected,num,comment=''):
        err = '** '
        result = F(I,S,H)
        func_name = str(F).split()[1]
        func_call = f'''{func_name}("{I}","{S}","{H}")'''
        if result == expected: err = ''
        e = expected
        print (f'{err}test #{num} {func_call}: expected "{e}", received "{result}"')
        print (f'test #{num} Explanation: {comment}\n')
        return num + 1

    F = vfyHalfNodeCoverViaVfyQuarterIndepedentSet


    num = 1
    I = 'a,b  a,c a,d'                    
    exp = '{a} covers all 4 nodes'
    num = test_case(F,I,'yes','a','correct',num,exp)

    I = 'a,b  a,c c,d'                    
    exp = '{a,c} covers all 4 nodes'
    num = test_case(F,I,'yes','a c','correct',num,exp)

    I = 'a,b  b,c c,d e,f'                    
    Exp = '{a,c,e} is half of 6 nodes'
    num = test_case(F,I,'yes','a c e','correct',num,exp)

    I = 'a,b  a,c b,d'                    
    exp = '{a,c} does not cover nodes'
    num = test_case(F,I,'yes','a c','unsure',num,exp)

    I = 'a,b a,c a,d b,c c,e'                    
    exp = '{a,b,c} is over half of 5 nodes'
    num = test_case(F,I,'yes',' a b c','unsure',num,exp)

