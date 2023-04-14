import heapq


# 定义节点类，包括字符、权值和左右子节点
class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # 运算符重载，用于堆排序
    def __lt__(self, other):
        return self.freq < other.freq


# 统计字符出现次数
def count_chars(data):
    freq = {}
    for char in data:
        freq[char] = freq.get(char, 0) + 1
    return freq


# 构建哈夫曼树
def build_huffman_tree(freq):
    # 将字符和出现次数转化为节点列表
    nodes = [Node(char, f) for char, f in freq.items()]
    # 通过堆排序构建哈夫曼树
    heapq.heapify(nodes)
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        parent = Node(freq=left.freq + right.freq)
        parent.left, parent.right = left, right
        heapq.heappush(nodes, parent)
    return nodes[0]


# 遍历哈夫曼树，生成字符编码
def generate_codes(root):
    def dfs(node, code, codes):
        if node.char:
            codes[node.char] = code
            return
        dfs(node.left, code + '0', codes)
        dfs(node.right, code + '1', codes)

    codes = {}
    dfs(root, '', codes)
    return codes


# 将原始数据编码为二进制数据
def encode_data(data, codes):
    encoded_data = ''
    for char in data:
        encoded_data += codes[char]
    return encoded_data


# 将二进制数据解码为原始数据
def decode_data(encoded_data, root):
    decoded_data = ''
    node = root
    for bit in encoded_data:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        if node.char:
            decoded_data += node.char
            node = root
    return decoded_data


# 测试代码
if __name__ == '__main__':
    data = 'hello world'
    freq = count_chars(data)
    root = build_huffman_tree(freq)
    codes = generate_codes(root)
    encoded_data = encode_data(data, codes)
    decoded_data = decode_data(encoded_data, root)
    print('Original data:', data)
    print('Encoded data:', encoded_data)
    print('Decoded data:', decoded_data)
