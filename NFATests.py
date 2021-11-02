import unittest
import time

from NFA import NFA
class NFATests(unittest.TestCase):
  
  def test_build(self):
    nfa = NFA('((A*B|AC)D)')
    G = {0:[1],
          1: [2],
          2:[3,7],
          3:[4],
          4:[3,5],
          5:[],
          6:[9],
          7:[],
          8:[],
          9:[10],
          10:[],
          11:[12],
          12:[13],
          13:[]}
    self.assertEqual(nfa.G.adj,G)
  def test_recognize(self):
    nfa = NFA('((A*B|AC)D)')
    falses = ['AC','BACD','ACCD']
    trues = ['ACD','AAAAAAAABD','BD', 'ABD']
    for f in falses:
      self.assertFalse(nfa.recognizes(f))
    for t in trues:
      self.assertTrue(nfa.recognizes(t))

  def test_multiWayOr(self):
    nfa = NFA('A|B|C')
    falses = ['ABC','AB', 'AC','X']
    trues = ['A','B','C']
    for f in falses:
      self.assertFalse(nfa.recognizes(f))
    for t in trues:
      self.assertTrue(nfa.recognizes(t))
  def test_complicated(self):
    nfa = NFA('GCG(CGG|AGG)*CTG')
    false = 'GCGGCGTGTGTGCGAGAG' 
    true = 'GCGCGGAGGCGGCTG'
    self.assertFalse(nfa.recognizes(false))
    self.assertTrue(nfa.recognizes(true))

  def test_speed(self):
    one = NFA('(a|aa)*b')
    two = NFA('(a*)*|b*')
    longFalse = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaac'
    longTrue = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
    t0 = time.time()
    self.assertFalse(one.recognizes(longFalse))
    self.assertTrue(one.recognizes(longTrue))
    self.assertFalse(two.recognizes(longFalse))
    self.assertTrue(two.recognizes(longTrue[:-1]))
    t1 = time.time()
    print(t1-t0)

if __name__ == '__main__':
  unittest.main()
