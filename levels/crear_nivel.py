"""
lee un archivo txt que tiene dibujado el nivel de mario y lo guarda en un archivo json para que funcione
"""
import json

def crear_nivel(file_dir):
    """
    param:
    file_dir: la ubicacion del archivo
    
    return --> (ancho, alto, nivel)
    ancho: es cuantos bloques tiene de largo el nivel
    alto:  es cuantos bloques tiene de largo el nivel
    nivel: es una lista de listas de los caracteres para crear el nivel
    """
    
    
def is_str_equal(a: str, b:str):
    return a.lower() == b.lower()

def to_json(filename: str, id: str, json_name:str):
    ancho, alto, nivel = crear_nivel(filename)
    objects = {
            "bush":[], 
            "sky":[],
            "cloud":[],
            "ground":[], 
            "pipe":[]
        } ## bushes, sky, cloud, ground
    layers = {
                "sky":{
                    "x":[0,ancho],
                    "y":[0,13]
                },
                "ground":{
                    "x":[0,ancho],
                    "y":[14, 16]
                }
            }
    entities = {
            "CoinBox":[], 
            "coinBrick":[],
            "coin":[],
            "Goomba":[],
            "Koopa":[],
            "RandomBox":[]
            
        } ## boxes, goombas, turtles, etc
    
    i = 0 
    while i < alto:
        j = 0
        while j < len(nivel[i]):
            elem = nivel[i][j]
            if is_str_equal(elem, "c"):
                objects["sky"].append([j, i])
            elif is_str_equal(elem, "#"):
                objects["ground"].append([j,i])          
            elif is_str_equal(elem, "n"):
                objects["cloud"].append([j,i])
            elif is_str_equal(elem, "a"):
                objects["bush"].append([j,i])
            elif is_str_equal(elem, "m"):
                entities["coin"].append([j,i])
            elif is_str_equal(elem, "x"):
                entities["CoinBox"].append([j,i])
            elif is_str_equal(elem, "r"):
                entities["RandomBox"].append([j,i, "RedMushroom"])
            elif is_str_equal(elem, "p"):
                entities["coinBrick"].append([j,i])
            elif is_str_equal(elem, "g"):
                entities["Goomba"].append([j,i])
            elif is_str_equal(elem, "k"):
                entities["Koopa"].append([j,i])
         
            j += 1
        i += 1
    
    level = {"id": id, "length": ancho, "level": {"objects": objects, "layers": layers, "entities": entities}}
    
    with open(json_name, "w") as f:
        json.dump( level, f,)
    
        
to_json("nivel1-3.txt", 3, "Level1-3.json")