from math import sqrt

class Node:
    def __init__(self,state,parent=None,action=None,cost=0,huristic=False,type_huristic="manhattan"):
        self._state=state
        self._action=action
        self._parent=parent
        self.cost=cost
        self.huristic=False
        self.type_huristic=type_huristic
        if huristic:
            self.huristic=self.get_huristic(self.type_huristic)
   

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

        return self.cost
    
    def get_huristic(self,type_huristic):
        distance=0
        for inx,value in  enumerate(self._state):
            if value != '0':
                curent_row=inx//3
                curent_col=inx%3
                goal_row=int(value)//3
                goal_col=int(value)%3
                if(type_huristic=="manhattan"):
                    distance+=abs(curent_row-goal_row)+abs(curent_col-goal_col)
                elif(type_huristic=="euclidean"): 
                    distance+=sqrt(((curent_row-goal_row)**2+(curent_col-goal_col)**2))  
        return distance            

    def goal_test(self):
        return self._state=="012345678"        
    
    
    def get_possible_actions(self,zero_row,zero_col):
        possible_actions=[]
        if zero_row>0:
            possible_actions.append((zero_row-1,zero_col,"Up"))
        if zero_row<2:    
              possible_actions.append((zero_row+1,zero_col,"Down"))
        if zero_col>0:
            possible_actions.append((zero_row,zero_col-1,"Left"))
        if zero_col<2:    
              possible_actions.append((zero_row,zero_col+1,"Right"))     
        return possible_actions
           

        

    def get_neighbors(self):
        neighbors=[]
        zero_inx=self._state.find('0')
        zero_row=zero_inx//3
        zero_col=zero_inx%3
        possible_actions=self.get_possible_actions(zero_row,zero_col)
        for action in possible_actions:
            new_inx=action[0]*3+action[1]
            new_state=list(self._state)
            new_state[zero_inx],new_state[new_inx]=new_state[new_inx],new_state[zero_inx]
            neighbors.append(Node("".join(new_state),self,action[2],self.cost+1,self.huristic,self.type_huristic))
        return neighbors      



    def __lt__(self,other):
        return self.huristic+self.cost<other.huristic+other.cost    
       
