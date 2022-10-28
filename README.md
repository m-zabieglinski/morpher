# Morpher
An excercise in function dictionaries. Instance of Morpher class holds an object that can be later morphed using one of the available functions and some other object.

**morpher.py** contains the class itself

**morpher_functions.py** contains the dictionary of all morphing functions available. It was designed as easily appendable.

**example.py** is an example of morphing 10 using the _katamari_ morphing function and a list. Katamari operates on lists of strings: it takes the current state of Morpher (in this example, initialized as number 10) and then iterates through the given list. For each word in the list, if the word is shorter than the current state of the Morpher, it replaces the current state of the Morpher with a concatenation of the current state of the Morpher and the word. It's like rolling a katamari ball of strings, if you know that game.

```
import morpher 

x = ['kot', 2, 10, 'pies', 'ryba']

a = morpher.Morpher(10)
print(a.state)
10
a.morph(x, "katamari")
print(a.state)
10210piesryba
```
