//*****************************************************************
// File:   ControlServer.hpp
// Author: Javier Gonzalez Galindo 680566 y Nestor Monzon
// Date:   enero 2019
// Coms:   
//*****************************************************************

#ifndef CONTROL_SERVER
#define CONTROL_SERVER

#include <iostream>
#include <string>
#include <vector>
#include <mutex>
#include <condition_variable>
#include <map>

const int NUM_CONTENEDORES = 3; // Contenedores en cada servidor (Ej: el servidor 1 tendra en el contenedor 2 las tuplas de longitud 2, etc.)

using namespace std;

class ControlServer {
public:
   
    // <NS>: número de surtidores de la gasolinera
    // <logger>: referencia a un objeto de la clase "Logger"
    ControlServer();

    //----------------- Destructor
    ~ControlServer();

    
    // Se bloquea hasta que hay un surtidor libre
    // Devuelve en el <surt> un numero de surtidor, que estaba libre. El surtidor pasa a estar ocupado
    void postnote(vector<string> tupla);
    void postnote(vector<string> tupla, const int contenedor);

    // Libera el surtidor <surt>
    string removeNote(vector<string> tupla, int numtokens);
    string removeNote(vector<string> tupla, int numtokens, const int contenedor);
    // Avisa de que va a empezar un proceso de mantenimiento.
    // Desde este momento, ningún surtidor, aunque esté libre, será concedido
    // Cuando todos los surtidores estén libres, podrá llevar a cabo el mantenimiento
    string readNote(vector<string> tupla, int numtokens);
    string readNote(vector<string> tupla, int numtokens, const int contenedor);

    bool existetupla(vector<string> tupla, int numtokens,multimap<string,vector<string>>::iterator &itEncontrada);
    bool existetupla(vector<string> tupla, int numtokens,multimap<string,vector<string>>::iterator &itEncontrada, const int contenedor);


    void mostrar();

private:
    
    multimap<string,vector<string>> contenedor[NUM_CONTENEDORES]; // 3 contenedores para 3 tamaños
    multimap<string,vector<string>>::iterator it;
    condition_variable esperando_removeNote;
    condition_variable esperando_readNote;
    mutex mtx;
    mutex mtx2;
};
#endif