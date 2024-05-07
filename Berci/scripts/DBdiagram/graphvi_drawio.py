from graphviz2drawio import graphviz2drawio

path = "C:/Users/bertalan.pasztor/Documents/drawio_diagrams/graphviz/"
xml = graphviz2drawio.convert(path + "tariff.dot")
with open(path + "tariff.drawio", 'w') as f:
    f.write(xml)