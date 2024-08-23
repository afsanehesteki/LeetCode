# class FileSystem:

#     def __init__(self):
#         self.m = collections.defaultdict()

# # Approah 1: Using HashMap to save various paths 
# # Time Complexity: O(M) -->  where M is the length of path
# # path.rfind('/') --> O(M), worst case needs to examine every character to find last '/'
# # path[:path. --> Slice operation is  also O(M)

# # Space Complexity: O(K) where K represents the number of unique paths that we add

#     def createPath(self, path: str, value: int) -> bool:
#         #basic path validations
#         if path in self.m or len(path)==0 or path=="/":
#             return False

#         #if the parent doesn't exist. Note that "/" is a valid parent.
#         parent = path[:path.rfind('/')] 
#         if len(parent)>1 and parent not in self.m:
#             return False
        
#         #add this new path and return true.
#         self.m[path] = value    
#         return True
            
#     def get(self, path: str) -> int:
#         # if path in self.m: 
#         #     return self.m[path]
#         # else:
#         #     return -1   

#         return self.m.get(path, -1) 


# Approach 2: Trie based approach
# Time Complexity:
#create ~ It takes O(T) to add a path to the trie if it contains T components.
#get ~ It takes O(T) to find a path in the trie if it contains T components.

# Space Complexity:
# create ~ Lets look at the worst case space complexity. In the worst case, none of the paths will have any common prefixes. We are not considering the ancestors of a larger path here. In such a case, each unique path will end up taking a different branch in the trie. Also, for a path containing T components, there will be T nodes in the trie.
# get ~ O(1).
class TrieNode(object):
    def __init__(self, name):
        self.map = defaultdict(TrieNode)
        self.name= name
        self.value = -1

class FileSystem:

    def __init__(self):
        self.root = TrieNode("")

    def createPath(self, path: str, value: int) -> bool:
        components = path.split("/")
        if len(path)==0 or path=="/":
            return False
        cur = self.root
        for i in range(1, len(components)):
            sub_path = components[i]
            # For each component, we check if it exists in the current node's dictionary.
            if sub_path not in cur.map:
                 # If it doesn't and it is the last node, add it to the Trie.
                if i == len(components) -1: 
                    cur.map[sub_path] = TrieNode(sub_path)
                else: 
                    return False
            cur = cur.map[sub_path]
        
        # Value not equal to -1 means the path already exists in the trie.
        if cur.value !=-1:
            return False
        cur.value = value        
        return True
              
    def get(self, path: str) -> int:
        components = path.split("/")
        cur = self.root
        for i in range(1,len(components)):
            # For each component, we check if it exists in the current node's dictionary.
            sub_path =  components[i]
            if sub_path not in cur.map:
                return -1
            cur = cur.map[sub_path]
        return cur.value


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
