from typing import List,Tuple
from Digraph import Digraph

class NFA:
  
  def __init__(self, regex : str):
    # wrap in parens to get parsing started
    regex = '(' + regex + ')'
    self.M : int= len(regex)
    self.regex : List[str] = list(regex)
    self.metaChars : List[str] = ['(','*',')']
    self.G = self.buildNFA()

  def recognizes(self, s : str) -> bool:
    for c in self.metaChars: 
      if c in s:
        raise RuntimeError('Meta Characters in string not supported')
    starts : List[int] = self.G.DFS(0)
    for i,c in enumerate(s):
      
      # collect set of next states to try
      nextStates : List[int] = []
      for vertex in starts:
        if vertex == self.M:
          continue
        if self.regex[vertex] == c or self.regex[vertex] == '.':
          nextStates.append(vertex+1)

      # find all states reachable
      starts = []
      for v in self.G.DFSMultiSource(nextStates).values():
        starts += v 
    # check to see if any state is the last one
    for vertex in starts:
      if vertex == self.M:
        return True
    return False

  def buildNFA(self) -> Digraph:
    NFA : Digraph = Digraph(self.M+1)
    stack : List[Tuple[int,str]] = []
    for i,c in enumerate(self.regex):
      leftParen = i
      if c in ['(','|']:
        stack.append((i,c))
      elif c == ')':
        if stack:
          idx,op = stack.pop()
          if op == '(':
            leftParen = idx
          else: # we have an or |
            
            # naive attempt at multiway or
            # nothing changes in the construction
            # we just need to connect extra things
            ors = [idx]
            while stack and stack[-1][1] == '|':
              ors.append(stack.pop()[0])
            if not stack:
              raise RuntimeError(f'Mismatched Parenthesis')
            #print(stack,ors,i)
            leftParen,_ = stack.pop()
            for orIdx in ors:
              NFA.addEdge(leftParen,orIdx+1)
              NFA.addEdge(orIdx,i)
        else:
          raise RuntimeError(f'Mismatched Parenthesis')
      if i+1 < self.M and self.regex[i+1] == '*':
        NFA.addEdge(leftParen,i+1)
        NFA.addEdge(i+1,leftParen)
      if c in self.metaChars:
        NFA.addEdge(i,i+1)
    if stack:
      raise RuntimeError(f'Mismatched Parenthesis')
    return NFA
        
