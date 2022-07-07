
# clothing super class, then other smaller ones (instead of just string type)
class Clothing:
    def __init__(self, id, type) -> None:
        self.id = id
        self.type = type 

def foo():
    return "foo"
    
def main():
    item = Clothing(1, "tank top")
    print(item.type)


main()