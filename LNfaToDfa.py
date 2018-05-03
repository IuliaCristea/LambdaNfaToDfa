def getLambdaClosure(transitions,state):
    if '#' not in transitions[state].keys():
        return [state]
    toReturn = transitions[state]['#']
    toReturn.append(state)
    for stateAux in toReturn:
        if '#' not in transitions[stateAux].keys():
            continue
        for st in transitions[stateAux]['#']:
            if st not in toReturn:
                toReturn.append(st)
    return list(set(toReturn))

def getTable1(states, transitions, symbols):
    #print(states)
    #print (symbols)
    closure = {}
    for state in states:
        closure[state] = getLambdaClosure(transitions,state)

    table1 = {}
    for state in states:
        for sym in symbols:
            aux = []
            for st in closure[state]:
                if sym not in transitions[st].keys():
                    continue
                aux = aux + transitions[st][sym]
                #print(aux)
            aux = list(set(aux))
            lambdaFinal = []
            for st in aux:
                lambdaFinal = lambdaFinal + closure[st]
            lambdaFinal = list(set(lambdaFinal))
            if state in table1.keys():
                table1[state][sym] = lambdaFinal
            else:
                table1[state] = {}
                table1[state][sym] = lambdaFinal
    return table1

def getTransitions(listTrans, sym, transitions):
    toReturn = []
    for i in listTrans:
        if sym in transitions[i].keys():
            toReturn.append(i)
    return toReturn

def getTable2(table1, initialState, symbols, transitions):

    table2 = {}
    newInitialState = tuple(getLambdaClosure(transitions,initialState))
    queue = [newInitialState]
    for newState in queue:
        table2[newState] = {}
        for sym in symbols:
            aux = []
            for st in newState:
                if sym in table1[st]:
                    aux = aux + table1[st][sym]
            aux = list(set(aux))
            table2[newState][sym] = aux
            auxT = tuple(aux)
            if auxT not in queue:
                queue.append(auxT)
    return table2



def readFile(fileName):
    f = open(fileName,"r")
    lines = f.readlines()
    lines = [line.strip("\n") for line in lines]
    #print(lines)
    nrOfStates = lines[0]
    #print(nrOfStates)
    states = lines[1]
    states = states.split(" ")
    #print(states)
    nrOfSymbols = lines[2]
    symbols = lines[3]
    symbols = symbols.split(" ")
    #print(symbols)
    initialState = lines[4]
    nrOfFinalStates = lines[5]
    finalStates = lines[6]
    nrOfTransitions = lines[7]
    #print (nrOfTransitions)
    transitions = {}
    linesTrans = [line.split() for line in lines[8:]]
    #print(linesTrans)
    for line in linesTrans:
        if line[0] not in transitions.keys():
            transitions[line[0]] = {}
            transitions[line[0]][line[1]] = [line[2]]
        else:
            if line[1] not in transitions[line[0]]:
                transitions[line[0]][line[1]] = [line[2]]
            else:
                transitions[line[0]][line[1]].append(line[2])
    #print(transitions)
    table1 = getTable1(states,transitions,symbols)
    table2 = getTable2(table1, initialState, symbols, transitions)
    print(table2)
    #print(table1)

def main():
    readFile("date.in")


if __name__ == "__main__":
    main()