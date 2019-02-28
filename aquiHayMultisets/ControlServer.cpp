//*****************************************************************
// File:   ControlServer.cpp
// Author: Javier Gonzalez Galindo 680566 y Nestor Monzon
// Date:   enero 2019
// Coms:   
//*****************************************************************

#include "ControlServer.hpp"
#include <cassert>
#include <mutex>
#include <regex>
using namespace std;


ControlServer::ControlServer() {
    for (int i = 0; i<NUM_CONTENEDORES; i++) {
        contenedor[i].clear();   
    }
};

int elegirContenedor (const int numTokens) {
    int contenedor;
    if (numTokens == 1 || numTokens == 4 || numTokens == 6) { 
        contenedor = 0; // Primer contenedor
    }
    else if (numTokens == 2 || numTokens == 5) {
        contenedor = 1; // Segundo contenedor
    }
    else { // numTokens == 3 
        contenedor = 2;
    }
    return contenedor;
}

bool ControlServer::existetupla(vector<string> tupla,int numtokens,multimap<string,vector<string>>::iterator &itEncontrada){
    return this->existetupla(tupla, numtokens, itEncontrada, elegirContenedor(numtokens));
}

bool ControlServer::existetupla(vector<string> tupla,int numtokens,multimap<string,vector<string>>::iterator &itEncontrada, const int nContenedor){
    bool encontrada=false;
    pair<multimap<string,vector<string>>::iterator,multimap<string,vector<string>>::iterator> result;
    if(!regex_match (tupla[0], regex("(^\\?+[A-Z]$)"))){
        result = contenedor[nContenedor].equal_range(tupla[0]);
    }else{
        result = make_pair(contenedor[nContenedor].begin(),contenedor[nContenedor].end());
    }
    if(result.first != result.second){
        // HE encontrado posibles candidatos
        int numaciertos;
        for (multimap<string,vector<string>>::iterator it1 = result.first; it1 != result.second && !encontrada; it1++){
            // comparar si es la misma nota
            numaciertos=0;
            if(it1->second.size()==numtokens){
                // tamaño de la tupla coincide con la buscada
                for(int i =0 ; i< numtokens; i++){
                    
                    if((it1->second[i] == tupla[i]) || (regex_match (tupla[i], regex("(^\\?+[A-Z]$)")))){
                        numaciertos++;
                    }else{
                        if(it1->second[i]=="" && (tupla[i]=="" || (regex_match (tupla[i], regex("(^\\?+[A-Z]$)"))))){
                            numaciertos++;
                        }
                    }
                }
                if(numaciertos == numtokens){
                    itEncontrada = it1;
                    encontrada=true;
                }else {
                    encontrada=false;
                }
            }
        }
    }
    return encontrada;
}

void ControlServer::postnote(vector<string> tupla){
    this->postnote(tupla, elegirContenedor(tupla.size()));
}

// Se bloquea hasta que hay un surtidor libre
// Devuelve en el <surt> un numero de surtidor, que estaba libre. El surtidor pasa a estar ocupado
void ControlServer::postnote(vector<string> tupla, const int nContenedor){
    unique_lock<mutex> lck( mtx);
    contenedor[nContenedor].insert (pair<string,vector<string>>(tupla[0],tupla));
    esperando_readNote.notify_all();
    esperando_removeNote.notify_all();
};

string ControlServer::removeNote(vector<string> tupla, int numtokens){
    return this->removeNote(tupla, numtokens, elegirContenedor(numtokens));
}

    // Libera el surtidor <surt>
string ControlServer::removeNote(vector<string> tupla, int numtokens, const int nContenedor){
    unique_lock<mutex> lck(mtx);
    string resultado="";
    multimap<string,vector<string>>::iterator itEncontrada;
    //busco la tupla por la clave
    while(!existetupla(tupla,numtokens,itEncontrada,nContenedor)){
        esperando_removeNote.wait(lck);
    }
    for(int i =0 ; i< numtokens; i++){
        resultado+=itEncontrada->second[i];
        if(i!=numtokens-1){
            resultado+=",";
        } 
    }
    contenedor[nContenedor].erase(itEncontrada);
    return resultado;
};

string ControlServer::readNote(vector<string> tupla, int numtokens){
    return this->readNote(tupla, numtokens, elegirContenedor(numtokens));
}

// Avisa de que va a empezar un proceso de mantenimiento.
// Desde este momento, ningún surtidor, aunque esté libre, será concedido
// Cuando todos los surtidores estén libres, podrá llevar a cabo el mantenimiento
string ControlServer::readNote(vector<string> tupla, int numtokens, const int nContenedor){
    unique_lock<mutex> lck(mtx);
    string resultado="";
    multimap<string,vector<string>>::iterator itEncontrada;
    //busco la tupla por la clave
    while(!existetupla(tupla,numtokens,itEncontrada,nContenedor)){
        esperando_readNote.wait(lck);
    }
    for(int i =0 ; i< numtokens; i++){
        resultado+=itEncontrada->second[i];
        if(i!=numtokens-1){
            resultado+=",";
        } 
    }  
    return resultado;
};

void ControlServer::mostrar(){
    cout << "mymultimap contains:\n";
    for (int j = 0; j<NUM_CONTENEDORES; j++) {
          for (it=contenedor[j].begin(); it!=contenedor[j].end(); ++it){
              cout << (*it).first << " => ";
              for (int i=0 ; i < (*it).second.size(); i++){
                  cout << (*it).second[i];
              }
              cout<< "\n";
  }
    }

    
};
ControlServer:: ~ControlServer() {
};

