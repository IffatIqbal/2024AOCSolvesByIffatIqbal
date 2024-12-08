from collections import defaultdict, deque

def parse_input(data):
    sections = data.strip().split("\n\n")
    rules = [tuple(map(int, rule.split("|"))) for rule in sections[0].splitlines()]
    updates = [list(map(int, update.split(","))) for update in sections[1].splitlines()]
    return rules, updates

def build_graph(rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    for x, y in rules:
        graph[x].append(y)
        in_degree[y] += 1
        in_degree[x]
    return graph, in_degree


def is_valid_update(update, graph, in_degree):
    filtered_graph = defaultdict(list)
    filtered_in_degree = defaultdict(int)
    
    update_set = set(update)
    for x in update_set:
        filtered_in_degree[x] = 0  
    
    for x in update_set:
        for y in graph[x]:
            if y in update_set:
                filtered_graph[x].append(y)
                filtered_in_degree[y] += 1

    queue = deque([node for node in update if filtered_in_degree[node] == 0])
    topo_sorted = []
    
    while queue:
        node = queue.popleft()
        topo_sorted.append(node)
        for neighbor in filtered_graph[node]:
            filtered_in_degree[neighbor] -= 1
            if filtered_in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return topo_sorted == update

def process_updates(rules, updates):
    graph, in_degree = build_graph(rules)
    middle_sum = 0
    
    for update in updates:
        if is_valid_update(update, graph, in_degree):
            middle_page = update[len(update) // 2]
            middle_sum += middle_page
    
    return middle_sum

# Input data (replace with actual input)
data = """<INPUT GOES HERE>"""  # Replace with the given input
rules, updates = parse_input(data)
result = process_updates(rules, updates)
print("Sum of middle pages:", result)
