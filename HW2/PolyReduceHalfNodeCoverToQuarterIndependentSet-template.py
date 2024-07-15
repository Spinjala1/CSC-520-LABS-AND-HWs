# On our honor, as SFSU students, we, Sripranav Pinjala, Annison Van,
# John King, and Subhan Khan, did not give or receive inappropriate help
# with this assignment. All group members contributed to this work, and
# all concur with the submission. We understand that we will be asked to
# redo the assignment in person if this work presents any question of an
# honor code violation.

from graph import Graph
from VfyQuarterIndependentSet import VfyQuarterIndependentSet

HNC2QISv = 'VERBOSE: PolyReduceHalfNodeCoverToQuarterIndpenedentSet() - '
VERBOSE = True

def printV(text):
    if VERBOSE: print(f'{HNC2QISv}{text}')

HNC2QISd = 'DEV:PolyReduceHalfNodeCoverToQuarterIndpenedentSet() - '
DEV = False

def printD(text):
    if DEV: print(f'{HNC2QISd}{text}')

def make_new_node(nodes, new_nodes):
    '''
    Arguments:
      nodes -- list of nodes in the halfNodeCover instance
      new_nodes -- new nodes

    Returns a node name consisting of Z's, which is not in either
    nodes or new_nodes
    '''
    new_node = 'Z'
    names = nodes + new_nodes
    while new_node in names:
        new_node += 'Z'
    return new_node

def PolyReduceHalfNodeCoverToQuarterIndependentSet(halfNodeCover_instance):
    graph_str = halfNodeCover_instance

    g = Graph(graph_str, weighted=False, directed=False)
    nodes = list(g.nodes.keys())

    new_nodes = []
    for _ in nodes:
        new_nodes.append(make_new_node(nodes, new_nodes))

    nodes.extend(new_nodes)

    new_edges = []
    for new_node in new_nodes:
        for old_node in g.nodes.keys():
            new_edges.append(f'{new_node},{old_node}')


    existing_edges = [f'{edge[0]},{edge[1]}' for edge in g.edges()]

    quarterIndependentSet_instance = ' '.join(existing_edges + new_edges)

    printV(f'quarterIndependentSet_instance = "{quarterIndependentSet_instance}"')

    return quarterIndependentSet_instance

def vfyHalfNodeCoverViaVfyQuarterIndepedentSet(halfNodeCover_instance, S, H):
    quarterIndependentSet_instance = PolyReduceHalfNodeCoverToQuarterIndependentSet(halfNodeCover_instance)
    graph_str = halfNodeCover_instance

    g = Graph(graph_str, weighted=False, directed=False)
    nodes = list(g.nodes.keys())

    printD(f'nodes = {nodes}, H = {H.split()}')
    H_independent_set = ' '.join([node for node in nodes if node not in H.split()])

    printD('Hint for Quarter Independent Set verifier to use on converted' + \
           f' instance: "{H_independent_set}":\n ' + \
           f'        (nodes in node cover graph instance, but not in H = "{H}")')
    result = VfyQuarterIndependentSet(quarterIndependentSet_instance, S, H_independent_set)
    return result

if __name__ == '__main__':
    def test_case(F, I, S, H, expected, num, comment=''):
        err = '** '
        result = F(I, S, H)
        func_name = str(F).split()[1]
        func_call = f'''{func_name}("{I}","{S}","{H}")'''
        if result == expected: err = ''
        e = expected
        print(f'{err}test #{num} {func_call}: expected "{e}", received "{result}"')
        print(f'test #{num} Explanation: {comment}\n')
        return num + 1

    F = vfyHalfNodeCoverViaVfyQuarterIndepedentSet

    num = 1
    I = 'a,b a,c a,d'
    exp = '{a} covers all 4 nodes'
    num = test_case(F, I, 'yes', 'a', 'correct', num, exp)

    I = 'a,b a,c c,d'
    exp = '{a,c} covers all 4 nodes'
    num = test_case(F, I, 'yes', 'a c', 'correct', num, exp)

    I = 'a,b b,c c,d e,f'
    exp = '{a,c,e} is half of 6 nodes'
    num = test_case(F, I, 'yes', 'a c e', 'correct', num, exp)

    I = 'a,b a,c b,d'
    exp = '{a,c} does not cover nodes'
    num = test_case(F, I, 'yes', 'a c', 'unsure', num, exp)

    I = 'a,b a,c a,d b,c c,e'
    exp = '{a,b,c} is over half of 5 nodes'
    num = test_case(F, I, 'yes', ' a b c', 'unsure', num, exp)
