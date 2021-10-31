from pprint import pprint


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        pprint(self.graph_dict)

    def paths(self, start, end, path=[]):
        path = path + [start]

        if start is end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def shortest_path(self, start, end, path=[]):

        path = path + [start]

        if start is end:
            return path

        if start not in self.graph_dict:
            return None

        smallpath = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.shortest_path(node, end, path)
                if sp:
                    if smallpath is None or len(sp) < len(smallpath):
                        smallpath = sp

        return smallpath


routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
]

routes_graph = Graph(routes)

start = "Mumbai"
end = "Toronto"
print(f"Paths between {start} and {end}: ")
pprint(routes_graph.paths(start, end))
print(f"Shortest paths between {start} and {end}: ")
pprint(routes_graph.shortest_path(start, end))
