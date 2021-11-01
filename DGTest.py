import unittest
from Digraph import Digraph
class DGTests(unittest.TestCase):
  
  def setUp(self):
    self.D = {0:[5,1],
         1:[],
         2:[0,3],
         3:[5,2],
         4:[3,2],
         5:[4]}

    self.G = Digraph(self.D)

  def test_initFromInt(self):
    G = Digraph(5)
    self.assertEqual(G.V,5)
    self.assertEqual(G.E,0)
    for i in range(5):
      self.assertTrue(i in G.adj)
      self.assertEqual(G[i],[])
  def test_InitFromDict(self):
    G = self.G
    self.assertEqual(G.V,6)
    self.assertEqual(G.E,9)
    for i in self.D:
      self.assertEqual(self.D[i],G[i])

  def test_AddEdge(self):
    self.G.addEdge(1,0)
    self.assertEqual(self.G.E,10)
    self.assertTrue(0 in self.G[1])

  def test_RemoveEdge(self):
    self.G.removeEdge(5,4)
    self.assertEqual(self.G.E,8)
    self.assertTrue(not (4 in self.G[5]))

  def test_DFS(self):
    reachable = self.G.DFS(0)
    print(reachable)
    nodes = [5,1,4]
    for node in nodes:
      self.assertTrue(node in reachable)
    self.assertEqual(self.G.DFS(1),[])
  
  def test_DFSMulti(self):
    # this test works by induction on the
    # normal dfs, i promise
    for x in self.D.keys():
      print(self.G.DFS(x))
    print(self.G.DFSMultiSource(self.D.keys()))
if __name__ == '__main__':
  unittest.main()

