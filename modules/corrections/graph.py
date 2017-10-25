#!/usr/bin/env python3

class Node:
    def __init__(self, content):
        self.content = content
        self.neighbours = set()
        self._mark = None

class Graph:
    """
    
    """
    def __init__(self):
        self.nodes = set()
        self.vertices = set()

    def add_vertex(self, n1, n2):
        self.vertices.add( (n1, n2,) )
        self.n1.neighbours.add(n2)

    def parse_file(self, filename):
        
