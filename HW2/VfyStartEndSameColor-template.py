# On our honor, as SFSU students, we, Sripranav Pinjala, Annison Van,
# John King, and Subhan Khan, did not give or receive inappropriate help
# with this assignment. All group members contributed to this work, and
# all concur with the submission. We understand that we will be asked to
# redo the assignment in person if this work presents any question of an
# honor code violation.

from graph import Graph

# identifier for verbose output
VSESCv = 'VERBOSE: VfyStartEndSameColor() '
VERBOSE = True
def printV(text):
    if VERBOSE: print(f'{VSESCv}{text}')

VSESCd = 'DEV: VfyStartEndSameColor() '
DEV = False
def printD(text):
    if DEV: print(f'{VSESCd}{text}')

def VfyStartEndSameColor(I, S, H):
    if len(S) > 3 or len(H) > 5 * len(I):
        printV('unreasonable length hint or solution')
        return 'unsure'

    if S != 'yes':
        printV('solution != "yes"')
        return 'unsure'

    cycle = H.split(',')  # Hint is a comma delimited list of nodes
    if len(cycle) < 2:
        printV('Cycles must have at least 2 nodes.')
        return 'unsure'

    instance_graph, instance_colorings = I.split(';')


    g = Graph(instance_graph, directed=True, weighted=False)

    node_color_kv = {}  # node->color key/value pairs
    color_count_kv = {} # color->count key/value pairs
    colorings_list = instance_colorings.split()
    for node_color in colorings_list:
        node, color = node_color.split(':')
        node_color_kv[node] = color
        if color not in color_count_kv:
            color_count_kv[color] = 0

    s_node = cycle[0]
    try:
        s_color = node_color_kv[s_node]
    except KeyError:
        printV(f'"{s_node}" in hint but not graph')
        return 'unsure'

    e_node = cycle[-1]
    try:
        e_color = node_color_kv[e_node]
    except KeyError:
        printV(f'"{e_node}" in hint but not graph')
        return 'unsure'

    if s_color != e_color:
        printV(f'{s_color} starts cycle and {e_color} ends it.')
        return 'unsure'

    # makes sure there are no duplicate colors except for the start/end node
    seen_colors = set()
    for i in range(1, len(cycle) - 1):
        color = node_color_kv[cycle[i]]
        if color in seen_colors:
            printV(f'duplicate color {color} found in cycle')
            return 'unsure'
        seen_colors.add(color)

        #  Makes sure all nodes in cycle exist in the graph
    for node in node_color_kv:
        if node not in cycle:
            printV(f'"{node_color_kv[node]}" not in cycle')
            return 'unsure'

    # Makes sure the cycle contains each color exactly once, except the start/end color
    cycle_colors = [node_color_kv[node] for node in cycle[1:-1]]
    if len(cycle_colors) != len(set(cycle_colors)):
        printV('Cycle does not contain each color exactly once except start/end color')
        return 'unsure'

    # makes sure all edges in the cycle exist in the graph
    for i in range(len(cycle)):
        newedges = str(list(g.edges()))

        if i == len(cycle) - 1:
            templist = [cycle[i], ',', cycle[0]]
            temp = ''.join(templist)
            if temp not in newedges:
                printV(f'Edge ({cycle[i]},{cycle[0]}) not in graph')
                return 'unsure'
        else:
            templist = [cycle[i], ',', cycle[i+1]]
            temp = ''.join(templist)
            if temp not in newedges:
                printV(f'Edge ({cycle[i]},{cycle[i+1]}) not in graph')
                return 'unsure'


    printV(f'"{I}" is a positive instance, all verifications succeeded')
    return 'correct'

if __name__ == '__main__':
    def test_case(F, I, S, H, expected, num, comment=''):

        # Evaluate test case to see whether or not it meets expectations.
        err = '** '   # Error flag is on by default
        result = F(I, S, H) # Call the verifier and store the result.

        # Get the function name as a string
        func_name = str(F).split()[1]
        call = f'''{func_name}("{I}","{S}","{H}")'''
        if result == expected:
            err = ''  # turn off error flag when results meet expectations

        e = expected
        print(f'{err}test #{num} {call}: expected "{e}", received "{result}"')
        print(f'test #{num} Explanation: {comment}\n')
        return num + 1

    F = VfyStartEndSameColor
    num = 1

    I = 'a,b  b,c  c,d  d,a; a:red b:blue c:yellow d:blue'
    exp = 'solution too long'
    num = test_case(F, I, 'maybe', 'a,b,c,d', 'unsure', num, exp)

    I = 'a,b  b,c  c,d  d,a; a:red b:blue c:yellow d:blue'
    exp = "can't verify negative instance"
    num = test_case(F, I, 'no', 'a,b,c,d', 'unsure', num, exp)

    I = 'a,a; a:red'
    exp = 'One node does not a cycle make'
    num = test_case(F, I, 'yes', 'a', 'unsure', num, exp)

    I = 'a,b  b,c  c,d  d,a ; a:red b:blue c:yellow d:red'
    exp = 'e not in graph'
    num = test_case(F, I, 'yes', 'e,a,b,c,d', 'unsure', num, exp)

    I = 'a,b  b,a  c,d  d,a ; a:red b:blue c:yellow d:red'
    exp = '"a" occurs twice'
    num = test_case(F, I, 'yes', 'a,b,a,d', 'unsure', num, exp)

    I = 'a,b  b,d  c,d  d,a; a:red b:blue c:yellow d:red'
    exp = 'No b-c edge'
    num = test_case(F, I, 'yes', 'a,b,c,d', 'unsure', num, exp)

    I = 'a,b  b,c  c,d  d,a; a:red b:blue c:blue d:red'
    exp = 'duplicate blues in interior of cycle'
    num = test_case(F, I, 'yes', 'a,b,c,d', 'unsure', num, exp)

    I = 'a,b  b,c  c,a  d,a; a:red b:blue c:red d:yellow'
    exp = 'no yellow in cycle'
    num = test_case(F, I, 'yes', 'a,b,c', 'unsure', num, exp)

    I = 'a,b  b,c  c,d  d,e e,f f,a; a:red b:blue c:yellow d:blue e:red f:red'
    exp = '3 reds'
    num = test_case(F, I, 'yes', 'a,b,c,d,e,f', 'unsure', num, exp)

    I = 'a,b  b,c  c,d  d,a; a:red b:blue c:white d:yellow'
    exp = 'start/end color not same'
    num = test_case(F, I, 'yes', 'a,b,c,d', 'unsure', num, exp)

    I = 'a,b  b,c  c,d  d,a; a:blue b:red c:yellow d:blue'
    exp = 'a-b-c-d traverses every color; only first and last have same color'
    num = test_case(F, I, 'yes', 'a,b,c,d', 'correct', num, exp)