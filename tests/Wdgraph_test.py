import unittest
import sys
sys.path.append("../Wdgraph")
from Wdgraph import Wdgraph

class WdgraphTestCase(unittest.TestCase):
    def testLen(self):
        graph = Wdgraph()
        self.assertEqual(len(graph), 0)
        graph.set_edge(0, 1, 1)
        self.assertEqual(len(graph), 2)
        graph.set_edge(0, 1, 0)
        self.assertEqual(len(graph), 2)
        graph.set_edge(2, 3, 12)
        self.assertEqual(len(graph), 4)

    def testSetGetEdge(self):
        graph = Wdgraph()

        graph.set_edge("hi", "hello", 1.5)
        self.assertEqual(graph.get_edge("hi", "hello"), 1.5)
        with self.assertRaises(Exception):
            graph.get_edge("hello", "hi")

        graph.set_edge("hi", "hello", 15)
        self.assertEqual(graph.get_edge("hi", "hello"), 15)

        graph.set_edge("no", "hi", -2.3)
        self.assertEqual(graph.get_edge("no", "hi"), -2.3)
        with self.assertRaises(Exception):
            graph.get_edge("hi", "no")


    def testOutDegree(self):
        graph = Wdgraph()

        graph.set_edge(1, 2, 3)
        graph.set_edge(2, 1, 4)

        self.assertEqual(graph.get_outdegree(1), 1)
        self.assertEqual(graph.get_outdegree(2), 1)

        graph.set_edge(1, 3, 4)
        self.assertEqual(graph.get_outdegree(1), 2)
        self.assertEqual(graph.get_outdegree(2), 1)
        self.assertEqual(graph.get_outdegree(3), 0)

    def testTacos(self):
        graph = Wdgraph()
        "I really like eating tacos. Tacos are my favorite food."

        graph.set_edge("I", "really", 1)
        graph.set_edge("really", "like", 1)
        graph.set_edge("like", "eating", 1)
        graph.set_edge("eating", "tacos", 1)
        graph.set_edge("tacos", "tacos", 1)
        graph.set_edge("tacos", "are", 1)
        graph.set_edge("are", "my", 1)
        graph.set_edge("my", "favorite", 1)
        graph.set_edge("favorite", "food", 1)

        tacos = [   graph.get_edge("I", "really"),
                    graph.get_edge("really", "like"),
                    graph.get_edge("like", "eating"),
                    graph.get_edge("eating", "tacos"),
                    graph.get_edge("tacos", "tacos"),
                    graph.get_edge("tacos", "are"),
                    graph.get_edge("are", "my"),
                    graph.get_edge("my", "favorite"),
                    graph.get_edge("favorite", "food")   ]

        for taco in tacos:
            self.assertEqual(1, taco)

        self.assertEqual(graph.get_outdegree("I"), 1)
        self.assertEqual(graph.get_outdegree("tacos"), 2)

    def testCreateProbabilityGraph(self):
        graph = Wdgraph()
        "1 5 2 3 4 5 2 4 3 5 4 1 5 2 3 2 4 1 5 3 5 2 3 4 2 3 5 1"

        graph.set_edge(1, 5, 3)
        graph.set_edge(5, 2, 4)
        graph.set_edge(2, 3, 4)
        graph.set_edge(3, 4, 2)
        graph.set_edge(4, 5, 1)
        graph.set_edge(2, 4, 2)
        graph.set_edge(4, 3, 1)
        graph.set_edge(3, 5, 3)
        graph.set_edge(5, 4, 1)
        graph.set_edge(4, 1, 2)
        graph.set_edge(3, 2, 1)
        graph.set_edge(5, 3, 1)
        graph.set_edge(4, 2, 1)
        graph.set_edge(5, 1, 1)

        graph.create_probability_graph()

        self.assertEqual(graph.get_edge(1, 5), 1)
        self.assertEqual(graph.get_edge(5, 2), 4 / 7)
        self.assertEqual(graph.get_edge(2, 3), 2 / 3)
        self.assertEqual(graph.get_edge(3, 4), 1 / 3)

        with self.assertRaises(Exception):
            graph.get_edge(5, 5)
            graph.get_edge(1, 4)

    def testGetOutneighbors(self):
        graph = Wdgraph()

        graph.set_edge("h", "g", 3.5)
        graph.set_edge("g", "h", 2.5)

        self.assertEqual(graph.get_outneighbors("h"), [["g", 3.5]])
        self.assertEqual(graph.get_outneighbors("g"), [["h", 2.5]])

        graph.set_edge("h", "y", 2.4)

        self.assertEqual(graph.get_outneighbors("h"), [["g", 3.5], ["y", 2.4]])


if __name__ == "__main__":
    unittest.main()
