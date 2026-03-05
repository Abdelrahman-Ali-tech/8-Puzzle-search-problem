class Node:
    def __init__(self,state,parent=None,action=None):
        self._state=state
        self._action=action
        self._parent=parent

    def get_path(self):
        path=[]
        goal_node=self
        while goal_node._parent != None :
            path.append(goal_node._parent)
            goal_node=goal_node._parent
        path.reverse()
        return path 
    
    # return sequence of actions that agent took it to reach the goal
    def get_path_actions(self):
        path_actions=[]
        goal_node=self
        while goal_node._parent != None :
            path_actions.append(goal_node._action)
            goal_node=goal_node._parent
        path_actions.reverse()
        return path_actions 
    
    # depth & cost are equal in BFS,DFS,DIS 
    def depth(self):
        path=self.get_path()
        return len(path)
