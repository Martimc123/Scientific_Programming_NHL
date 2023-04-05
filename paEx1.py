from typing import Set,Tuple,List

def id_to_fruit(fruit_id: int, fruits: List[str]) -> str:
    idx = 0
    for fruit in fruits:
        if fruit_id == idx:
            return fruit
        idx += 1
    raise RuntimeError(f"Fruit with id {fruit_id} does not exist")

name1 = id_to_fruit(1, ["apple", "orange", "melon", "kiwi", "strawberry"])
name3 = id_to_fruit(3, ["apple", "orange", "melon", "kiwi", "strawberry"])
name4 = id_to_fruit(4, ["apple", "orange", "melon", "kiwi", "strawberry"])    

""" | 1 - It does not print the fruit at the correct index, why is the returned result wrong?
    | Ans: It returns a result that is wrong and doesn't print the fruit at correct index because the id_to_fruit expects a set, the elements of sets in python don't have a specific order
    | as such, anytime the funtion runs we get a totally different set, hence why we get the wrong string result instead of getting the one at the correct position of the input.
    |
    | 2 - How could this be fixed?
    | Ans: To fix this problem, what we must do is change the input we give, that is, the set to one where the order of the elements doesn't change, as such we need to pass to the
    | function as argument the index and a list or tuple of the elements we have, we can do this by replacing the curly brackets {} to regular brackets [] or parenthisis () and we need
    | to go to the function signature and change the expected type of the fruits to a list or tuple, in order to match the input we passed to the functions. 
"""