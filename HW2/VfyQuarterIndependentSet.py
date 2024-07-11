from graph import Graph
from math import ceil

#identifier for verbose output
VQISv = 'VERBOSE: VfyQuarterIndependentSet() '
VERBOSE = True
def printV(text):
    if VERBOSE: print(f'{VQISv}{text}')

VQISd = 'DEV: VfyQuarterIndependentSet() '
DEV = False
def printD(text):
    if DEV: print(f'{VQISd}{text}')


def  VfyQuarterIndependentSet(I,S,H):
    edges = I.split()
    g = Graph(I,directed=False,weighted=False)

    nodes = list(g.nodes.keys())
    printD(f'graph nodes "{nodes}"')    
    hint_nodes = H.split()
    printD(f'hint nodes "{hint_nodes}"')    
    
    needed = ceil(len(nodes)/4)
    set_size = len(hint_nodes)
    
    if set_size < needed:
        nodes = 'nodes'
        if set_size == 1: nodes = 'node'
        printV(f'{set_size} {nodes} in hint, {needed} needed')
        return 'unsure'
        
    for idx,node_1 in enumerate(hint_nodes[:-1]):
        for node_2 in hint_nodes[idx+1:]:
            if f'{node_1},{node_2}' in edges or f'{node_2},{node_1}' in edges:
                if VERBOSE:
                    e =  f'{node_1},{node_2}'
                    msg = f'"{H}" not independent set, edge "{e}" exists'
                    printV(f'{msg}')
                    return 'unsure'
  
    return 'correct'

if __name__ == '__main__':
    def test_case(F, I, S, H, expected, num, comment=''):
        err = '** '
        result = F(I, S, H)
        func_name = str(F).split()[1]
        func_call = f'{func_name}("{I}", "{S}", "{H}")'
        if result == expected:
            err = ''
        e = expected
        print(f'{err}test #{num} {func_call}: expected "{e}", received "{result}"')
        print(f'test #{num} Explanation: {comment}\n')
        return num + 1

    F =  VfyQuarterIndependentSet
    num = 1

    I = 'a,b a,c a,d a,e a,f a,g g,h g,i'
    exp = '{b d} is independent set'
    num = test_case(F, I, 'yes', 'b d', 'correct', num, exp)

    I = 'a,b a,c a,d a,e a,f'
    exp = '{b is less than quarter of the nodes'
    num = test_case(F, I, 'yes', 'b', 'unsure', num, exp)

    I = 'a,b a,c a,d a,e a,f d,f b,d'
    exp = '{b d f } is not an independent set'
    num = test_case(F, I, 'yes', 'b d', 'unsure', num, exp)


    
    
