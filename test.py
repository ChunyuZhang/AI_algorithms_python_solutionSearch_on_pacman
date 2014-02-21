import search
class TestVerySimpleGraph(search.SearchProblem):
    """Gamestate is a list of tuples [('X', 'Y', z), ('A', 'B', c),...]
A tuple ('X', 'Y', z) represents an edge in a graph between X and Y, costing z amount to traverse between them. Edges are assumed to be non-directed.
Goal is the node label for the goal, and start is the node label for the start.
Thus, to initialize a search problem, use TestVerySimpleSearch(Gamestate,goal,start) with appropriate values for all three."""
    def __init__(self, gameState, goal, start):
        self.startState = start
        self.goal = goal
        self.gameState = gameState

    def getStartState(self):
        return self.startState

    def isGoalState(self,state):
        return state == self.goal

    def getSuccessors(self, state):
        successorList = []
        for edge in self.gameState:
            if edge[0]==state:
                successorList.append((edge[1],edge[0]+edge[1],edge[2]))
            if edge[1]==state:
                successorList.append((edge[0],edge[1]+edge[0],edge[2]))
        return successorList

    def getCostOfActions(self,actions):
        cost=0
        for action in actions:
            for edge in self.gameState:
                if edge[0]==action[0] and edge[1]==action[1]:
                    cost+=edge[2]
                if edge[1]==action[0] and edge[0]==action[1]:
                    cost+=edge[2]
        return cost

    def runTest(self):
        print "Path result for DFS:",search.depthFirstSearch(self)
        print "Path result for BFS:",search.breadthFirstSearch(self)
        print "Path result for UCS:",search.uniformCostSearch(self)
        print "Path result for A*:",search.aStarSearch(self,search.nullHeuristic)
        print "Path result for A* with letter heuristic:",search.aStarSearch(self,letterHeuristic)


"""THIS CODE YOU CAN CHANGE"""

def letterHeuristic(position, problem):
    return ord(position)-ord(problem.goal)
"""agraph is a graph with edges AB, AD, BC and CD, goal node D, start node A,  and appropriate node costs."""
agraph = TestVerySimpleGraph([('A','B',1),('A','D',10),('B','C',1),('C','D',1)],'D','A')
agraph.runTest()
