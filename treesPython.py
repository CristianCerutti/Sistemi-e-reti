class Node:
    def __init__ (self,data) :  #costruttore
        self.left = None
        self.right = None
        self.data = data

    # metodo di inserimento dei nodi
    def insert (self, data) : # confronta il valore del nodo da aggiungere con il nodo corrente
        if self.data :
            if data < self.data : # caso di nodi sulla sinistra
                if self.left is None : 
                    self.left = Node(data)
                else :
                    self.left.insert(data)

            elif data > self.data : # caso di nodi sulla destra
                if self.right is None : 
                    self.right = Node(data)
                else :
                    self.right.insert(data)
            
            else :
                self.data = data

    def printTree (self) : # stampa l'intero albero
        if self.left :
            self.left.PrintTree()

        print(self.data)

        if self.right :
            self.right.PrintTree()

    def inorderTraversal(self, root):
        res = []
        if root: 
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
            
        return res

    def preorder(self, root):
        res = []
        if root: 
            res.append(root.data)
            res = res + self.preorder(root.left)
            res = res + self.preorder(root.right)
        return res

    def postorderTraversal(self, root):
        res  = []
        if root: 
            res = self.postorderTraversal(root.left)
            res = res + self.postorderTraversal(root.right)
            res.append(root.data)
        return res 

def main():
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    print(root.postorderTraversal(root))

if __name__ == "__main__":
    main()
