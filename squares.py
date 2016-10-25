import math

areas = [];

def logic(data):
    aux = math.floor(math.sqrt(data))**2;
    areas.append(aux);
    aux = data - aux;
    
    return aux;

def answer(area):
    aux = logic(area);
    while aux != 0:
        aux = logic(aux);
        
    print (areas);

area = int(input('Choose a number: '));
answer(area);