class RouteTrieNode:
    def __init__(self, handler = None):
       
        self.handler = handler
        self.children = {}

    def insert(self, path_part):
        
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode()

    def find(self, path_part):
       
        if path_part in self.children:
            return True
        return False

    def __str__(self):
        
        trie_children = self.children
        count_children = len(trie_children)
        desc = ""
        for key,value in trie_children.items():
            if count_children > 1 or count_children == 0:
                desc += str(key) + "=>" + str(value) + "\n"
            else:
                desc += str(key) + "=>" + str(value)

        return desc


class RouteTrie:
    def __init__(self, root_handler):
     
        self.root = RouteTrieNode(root_handler)

    def insert(self, path_parts, handler):
      
        current_node = self.root

        for path_part in path_parts:
            current_node.insert(path_part)
            current_node = current_node.children[path_part]
   
        current_node.handler = handler

    def find(self, path_parts):

        current_node = self.root

        if path_parts is None:
            return None

       
        if len(path_parts) == 0:
            return self.root.handler

      
        for path_part in path_parts:
           
            if not current_node.find(path_part):
                return None
           
            current_node = current_node.children[path_part]

        
        return current_node.handler



class Router:
    def __init__(self, root_handler, not_found_handler = None):
        
        self.root_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, url_path, handler):
       
        path_parts = self._split_path(url_path)

        if path_parts != None:
            self.root_trie.insert(path_parts, handler)

    def lookup(self, url_path):
        
        path_parts = self._split_path(url_path)
        url_handler = self.root_trie.find(path_parts)
        if url_handler is None:
            return self.not_found_handler
        return url_handler


    def _split_path(self, url_path):

        if url_path is None or type(url_path) != str:
            return None

       
        if url_path == '/' or url_path == '':
            return []

        path_parts = url_path.split(sep='/')

        
        return [path_part for path_part in path_parts if path_part != '']



def test_function(test_case):
    url_handler = test_case[0].lookup(test_case[1])
    solution = test_case[2]
    if url_handler == solution:
        return "Pass"
    else:
        return "Fail"


router = Router("root handler", "not found handler")
print('\nCreate:\t router = Router("root handler", "not found handler")\n')


print('---- \t Testing Not valid inputs \t -----')
solution = "not found handler"

url = None
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup({}): {} \t{}'.format(url, solution, test))

url = 3
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup({}):    {} \t{}'.format(str(url), solution, test))

url = " "
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup("{}"):  {} \t{}'.format(str(url), solution, test))

# Testing Edge cases:
print('\n---- \t Testing Edge cases \t -----')
solution = "root handler"

url = "/"
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup("{}"): {} \t{}'.format(str(url), solution, test))

url = ""
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup("{}"):  {} \t{}'.format(str(url), solution, test))


# Add route
router.add_handler("/home/about", "about handler")  # add a route

print('\nRoute:\t router.add_handler("/home/about", "about handler")')


# some lookups with the expected output
print('\n---- \t Testing lookups search miss \t -----')
solution = "not found handler"

url = "/home"
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup("{}"): \t {} \t{}'.format(url, solution, test))

url = "home"
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup("{}"):  \t {} \t{}'.format(url, solution, test))

url = "/home/about/me"
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup("{}"): {} \t{}'.format(url, solution, test))

print('\n---- \t Testing lookups search hit \t -----')
solution = "about handler"

url = "/home/about"
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup("{}"):  {} \t{}'.format(url, solution, test))

url = "/home/about/"
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup("{}"): {} \t{}'.format(url, solution, test))

# Add route
router.add_handler("/home/about/me", "about me handler")
print('\nRoute:\t router.add_handler("/home/about/me", "about me handler")\n')

solution = "about me handler"
url = "/home/about/me"
test_case = [router, url, solution]
test = test_function(test_case)
print('router.lookup("{}"):  {} \t{}'.format(url, solution, test))
