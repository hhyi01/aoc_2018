with open("p_08_input.txt") as f:
    nodes = f.readlines()

nodes = [int(x.strip()) for x in nodes[0].split(" ")]
print(nodes)


meta_data = []
parent_nodes = []


# recursive approach, exceeds call stack
def get_meta_data(node_list):
    get_meta_data_helper(node_list)


def get_meta_data_helper(nodes_list):
    if len(nodes_list) == 0:
        return

    first_node_header = nodes_list[0:2]
    print("Node header: " + str(first_node_header))
    children = int(first_node_header[0])
    print("Children: " + str(children))
    metadata_entries = int(first_node_header[1])
    print("Meta data entries: " + str(metadata_entries))

    if children == 0:
        print(nodes_list)
        meta_data.append(nodes_list[2:2+metadata_entries])
        last_parent = parent_nodes.pop() if len(parent_nodes) > 0 else []
        print("Last parent: " + str(last_parent))
        nodes_list = last_parent + nodes_list[2+metadata_entries:]
        print("Current nodes list: " + str(nodes_list))
        get_meta_data_helper(nodes_list)
    else:
        parent_nodes.append([children-1, metadata_entries])
        get_meta_data_helper(nodes_list[2:])


# iterative approach
def get_meta_data_iter(node_list):
    while len(node_list) > 0:
        curr_node_header = node_list[0:2]
        print("Node header: " + str(curr_node_header))
        children = int(curr_node_header[0])
        print("Children: " + str(children))
        metadata_entries = int(curr_node_header[1])
        print("Meta data entries: " + str(metadata_entries))

        if children == 0:
            print(node_list)
            meta_data.append(node_list[2:2+metadata_entries])
            last_parent = parent_nodes.pop() if len(parent_nodes) > 0 else []
            print("Last parent: " + str(last_parent))
            node_list = last_parent + node_list[2+metadata_entries:]
            print("Current nodes list: " + str(node_list))
        else:
            parent_nodes.append([children-1, metadata_entries])
            node_list = node_list[2:]


def sum_meta_data(metadata_list):
    total = 0
    for m in metadata_list:
        total += sum(m)
    return total


get_meta_data_iter(nodes)
print("Meta data final: " + str(meta_data))
print("Parent nodes: " + str(parent_nodes))
print("Meta data total: " + str(sum_meta_data(meta_data)))

