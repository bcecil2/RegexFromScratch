from typing import Union,Dict,Iterable,List,Set
class Digraph:
  
  def __init__(self,nodes : Union[int,Dict[int,List[int]]]) -> None:
    if isinstance(nodes,int):
      self.V : int = nodes
      self.E : int = 0
      self.adj : Dict[int,List[int]] = {i:[] for i in range(nodes)}
    else:
      self.V  = len(nodes)
      self.E  = sum([len(nodes[v]) for v in nodes])
      self.adj  = nodes
  
  def __getitem__(self,idx : int) -> List[int]:
    return self.adj[idx]

  def addEdge(self, v : int , w : int) -> None:
    # assumes both exist
    self.adj[v].append(w)
    self.E += 1

  def removeEdge(self,v :int, w : int) -> None:
    # assumes both exist and slow
    self.adj[v].remove(w)
    self.E -= 1

  def _DFS(self, source : int, seen : Set[int])-> List[int]:
    l = []
    for x in self.adj[source]:
      if not x in seen:
        l.append(x)
        seen.add(x)
        l += self._DFS(x,seen)
    return l
  
  def DFS(self,source : int) -> List[int]:
    # cheesy wrapper to keep us from 
    # including source in reachable nodes
    return [source] + self._DFS(source,set())

  def DFSMultiSource(self, source : Iterable[int]) -> Dict[int,List[int]]:
    return {s:self.DFS(s) for s in source}
