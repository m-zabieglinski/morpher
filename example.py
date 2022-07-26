import morpher 

x = ['kot', 2, 10, 'pies', 'ryba']

a = morpher.Morpher(10)
print(a.state)
a.morph(x, "katamari")
print(a.state)