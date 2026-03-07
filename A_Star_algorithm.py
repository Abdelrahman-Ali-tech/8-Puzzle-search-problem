from Node import Node
import heapq
def A_star(initial_state,type_huristic="manhattan"):
    root=Node(initial_state,parent=None,action=None,cost=0,huristic=True,type_huristic=type_huristic)
    frontier=[]
    heapq.heappush(frontier,(root.huristic+root.cost,root))
    frontier_states={root._state:root.huristic+root.cost}
    explored=set()
    while frontier:
        _,current_node=heapq.heappop(frontier)
        if current_node._state not in explored:
            frontier_states.pop(current_node._state)
            explored.add(current_node._state)
            if current_node.goal_test():
                return Success(current_node.get_path_actions(),current_node.depth(),len(explored),current_node._state)
            for neighbor in current_node.get_neighbors():
                if neighbor._state not in explored and (neighbor._state not in frontier_states or neighbor.huristic+neighbor.cost<frontier_states[neighbor._state]):
                    heapq.heappush(frontier,(neighbor.huristic+neighbor.cost,neighbor))
                    frontier_states[neighbor._state]=neighbor.huristic+neighbor.cost
    return Failure()

        



def Success(path_actions,depth,explored,state):
    print("Path to solution:",path_actions)
    print("Depth of solution:",depth)  
    print("state of solution:",state)
    return path_actions,depth,explored      
def    Failure():
    print("No solution found")