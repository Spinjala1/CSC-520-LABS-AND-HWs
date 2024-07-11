from graph import Graph

#identifier for verbose output
VSESCv = 'VERBOSE: VfyStartEndSameColor() '
VERBOSE = True
def printV(text):
    if VERBOSE: print(f'{VSESCv}{text}')

VSESCd = 'DEV: VfyStartEndSameColor() '
DEV = False
def printD(text):
    if DEV: print(f'{VSESCd}{text}')


def VfyStartEndSameColor(I,S,H):
    if len(S) > 3 or len(H) > 5 * len(I): 
        printV(f'unreasonable length hint or solution')
        return 'unsure'

    if S != 'yes':
        printV(f'solution != "yes"')
        return 'unsure'
        
    cycle = H.split(',')  # Hint is a comma delimited list of nodes
    if len(cycle) < 2:
        printV(f'Cycles must have at least 2 nodes.')
        return 'unsure'

    instance_graph, instance_colorings = I.split(';')

    #Use WCBC library function to create a directed, unweighted graph
    g = Graph(instance_graph,directed=True, weighted=False)

    nodes = list(g.nodes)
    nodes_sav = nodes[:]  # clone node list for future reference
    edges = list(g.edges())
    
    for idx in range(len(edges)):
        #convert edges from a list of graph edges to a list of strings
        edges[idx] = str(edges[idx])    
    
    colors = []         # colors 
    node_color_kv = {}  # node->color key/value pairs
    color_count_kv = {} # color->count key/value pairs
    colorings_list = instance_colorings.split()
    for node_color in colorings_list:
        node,color = node_color.split(':')
        node_color_kv[node] = color
        if color not in colors:
            colors.append(color)

        color_count_kv[color] = 0
    s_node = cycle[0]
    s_color = None
    try:
        s_color = node_color_kv[s_node]
    except:
         printV(f'"{s_node}" in hint but not graph')
         return 'unsure'

    e_node = cycle[-1]
    e_color = None
    try:
        e_color = node_color_kv[e_node]
    except:
         printV(f'"{e_node}" in hint but not graph')
         return 'unsure'
     
    e_color = node_color_kv[cycle[-1]]
    if s_color != e_color:
        printV(f'{s_color} starts cycle and {e_color} ends it.')
        return 'unsure'

    ### ** HW #2 Add any and all checks needed for verification failues

    
    printV(f'"{I}" is a positive instance, all verifications succeeded')
    return 'correct'

if __name__ == '__main__':
    
    def test_case(F,I,S,H,expected,num,comment=''):
        # Evaluate test case to see whether or not it meets expectations.
        #
        err = '** '   # Error flag is on by default
        result = F(I,S,H) # Call the verifier and store the result.

        # Get the function name as a string
        func_name = str(F).split()[1]
        call = f'''{func_name}("{I}","{S}","{H}")'''
        if result == expected:
            err = ''  # turn off error flag when results meet expectations

        e = expected
        print (f'{err}test #{num} {call}: expected "{e}", received "{result}"')
        print (f'test #{num} Explanation: {comment}\n')
        return num + 1

    
    
    F = VfyStartEndSameColor
    num = 1

    I = 'a,b  b,c  c,d  d,a; a:red b:blue c:yellow d:blue'
    exp = 'solution too long'
    num = test_case(F,I,'maybe','a,b,c,d','unsure',num,exp)

    I = 'a,b  b,c  c,d  d,a; a:red b:blue c:yellow d:blue'
    exp = "can't verify negative instance"
    num = test_case(F,I,'no','a,b,c,d','unsure',num,exp)

    I = 'a,a; a:red'
    exp = 'One node does not a cycle make'
    num = test_case(F,I,'yes','a','unsure',num,exp)

    I = 'a,b  b,c  c,d  d,a ; a:red b:blue c:yellow d:red'
    exp = 'e not in graph'
    num = test_case(F,I,'yes','e,a,b,c,d','unsure',num,exp)

    I = 'a,b  b,a  c,d  d,a ; a:red b:blue c:yellow d:red'
    exp = '"a" occurs twice'
    num = test_case(F,I,'yes','a,b,a,d','unsure',num,exp)

    I = 'a,b  b,d  c,d  d,a; a:red b:blue c:yellow d:red'
    exp = 'No b-c edge'
    num = test_case(F,I,'yes','a,b,c,d','unsure',num,exp)    

    I = 'a,b  b,c  c,d  d,a; a:red b:blue c:blue d:red'
    exp = 'duplicate blues in interior of cycle'
    num = test_case(F,I,'yes','a,b,c,d','unsure',num,exp)

    I = 'a,b  b,c  c,a  d,a; a:red b:blue c:red d:yellow'
    exp = 'no yellow in cycle'
    num = test_case(F,I,'yes','a,b,c','unsure',num,exp)
    
    I = 'a,b  b,c  c,d  d,e e,f f,a; a:red b:blue c:yellow d:blue e:red f:red'
    exp = '3 reds'
    num = test_case(F,I,'yes','a,b,c,d,e,f','unsure',num,exp)
    
    I = 'a,b  b,c  c,d  d,a; a:red b:blue c:white d:yellow'
    exp = 'start/end color not same'
    num = test_case(F,I,'yes','a,b,c,d','unsure',num,exp)    

    I = 'a,b  b,c  c,d  d,a; a:blue b:red c:yellow d:blue'
    exp = 'a-b-c-d traverses every color; only first and last have same color'
    num = test_case(F,I,'yes','a,b,c,d','correct',num,exp)    
    

