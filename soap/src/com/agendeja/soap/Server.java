package com.agendeja.soap;

import javax.xml.ws.Endpoint;

public class Server {
    public static void main(String[] args) {
        System.out.println("SOAP rodando...");
        String host = System.getenv().getOrDefault("SOAP_HOST", "0.0.0.0");
        String port = System.getenv().getOrDefault("SOAP_PORT", "8088");
        String endpoint = "http://" + host + ":" + port + "/soap/agendamento";
        
        try {
            Database.ensureSchema();
            System.out.println("Banco inicializado - tabela agendamento criada.");
        } catch (Exception e) {
            System.err.println("Erro ao inicializar banco: " + e.getMessage());
            e.printStackTrace();
        }
        
        System.out.println("Endpoint publicado em: " + endpoint);
        Endpoint.publish(endpoint, new AgendamentoServiceImpl());
    }
}
