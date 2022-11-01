from random import randint
from flask import Flask, jsonify, request


app=Flask(__name__)
Usuarios=[]

Estampas=[]



@app.route('/')
def home():
    print('PANINI QATAR 2022')
    return 'PANINI QATAR 2022'

#___________________________________________________crear Usuario____________________
@app.route('/user', methods = ['POST'])
def crear_usuario():
    User= request.get_json()
      
    Usuarios.append(User)
    return jsonify({"Mensaje:":"Usuario Creado","Status:":200})  
    
  #_____________________________________________ver USsuario__________________________  

@app.route('/users', methods = ['GET'])
def mostrar_usuario():
    return jsonify(Usuarios)
#_________________________________________________EDITAR USUARIO______________________

@app.route('/user<id>', methods = ['PUT'])
def editar_usuario(id):
    body_usuario= request.get_json
    for usuario in Usuarios:
      if usuario["id"]== id:
          usuario["Nombre"]= body_usuario.get("Nombre")
          usuario["Nickname"]=body_usuario.get("Nickname")
          usuario["Password"]=body_usuario.get("Password")
          
          return({"Mensaje:":"Usuario Modificado con Exito","Status:":200})
    

    return jsonify({"Mensaje:":"Usuario no Existe","Status:":404})
#____________________________________________Eliminar usuario_____________________________
@app.route('/user<id>', methods = ['DELETE'])
def eliminar_usuario(id):
    for i in range(len(Usuarios)):
        usuario=Usuarios[i]
        if usuario["id"]== id:
            return jsonify({"Mensaje:":"Usuario Eliminado","Satutos:":200})
        
        return jsonify({"Mensaje:":"Usuario No Encontrado","Satutos:":404})
#_______________________________________________________________________________
#_____________________________Cargar Estampas________________________
@app.route('/sticker', methods = ['POST'])
def cargar_estampas():
    Sticker= request.get_json()
    
    for sticker in Sticker:
        
        Estampas.append(sticker)
          
    print(len(Estampas))
       
    return jsonify({"Mensaje:":"Estampas cargadas","Status:":200})
   
#______________________________________________________

  


#_______________________________________Sobre___________________________
@app.route('/box:user', methods = ['GET'])
def mostrar_estampa():
    nick_Usuario=request.get_json
    indice0 = randint(0,len(Estampas))
    indice1 = randint(0,len(Estampas))
    indice2 = randint(0,len(Estampas))
    indice3 = randint(0,len(Estampas))
    indice4 = randint(0,len(Estampas))

    sobre=[Estampas[indice0],Estampas[indice1],Estampas[indice2],
           Estampas[indice3],Estampas[indice4]]
    
    return jsonify(sobre)
#______________________________________________________________
#______________________________Cargar Sobre___________________

#_____________________________________________________________
#_______________________________Buscar Jugador______________
@app.route('/sticker/find', methods = ['GET'])
def buscar_jugador():
    Name_Player=request.args.get("Name_Player")
    Last_Name_Player=request.args.get("Last_Name_Player")
    return jsonify(Estampas)
#________________________________
#____________________________________________________________
if __name__== '__main__':
    app.run(port=3004,debug=True)