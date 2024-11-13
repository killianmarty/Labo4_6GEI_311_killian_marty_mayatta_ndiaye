package client_java;

import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Scanner;

/**
 * @brief Classe principale du client Java de l'API de cours.
 */
public class Main {
    /**
     * @brief Fonction principale du client Java de l'API de cours.
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        HttpClient client = HttpClient.newHttpClient();

        System.out.print("Veuillez entrer l'url et le port: ");
        String url = scanner.nextLine();

        while (true) {
            System.out.print("Quelle action voulez vous acccomplir: ? \n 1- Consulter une ressource \n 2- Ajouter une ressource \n 3- Supprimer une ressource ");
            String action = scanner.nextLine();
            while (!action.equals("1") && !action.equals("2") && !action.equals("3")) {
                System.out.print("Quelle action voulez vous acccomplir: ? \n 1- Consulter une ressource \n 2- Ajouter une ressource \n 3- Supprimer une ressource ");
                action = scanner.nextLine();
            }

            String methode = "";
            if (action.equals("1")) {
                methode = "GET";
            } else if (action.equals("2")) {
                methode = "POST";
            } else if (action.equals("3")) {
                methode = "DELETE";
            }

            try {
                if (methode.equals("GET")) {
                    System.out.print("Quelle ressource voulez vous consulter : \n 1- Tous les cours \n 2- Un cours specifique \n 3- Un fichier spécifique dans un cours \n 4- Un dossier spécifique dans un cours \n 5- Une séance spécifique d'un cours\n 6- Rechercher un cours par tag\n ");
                    String option = scanner.nextLine();
                    while (!option.equals("1") && !option.equals("2") && !option.equals("3") && !option.equals("4") && !option.equals("5") && !option.equals("6")) {
                        System.out.print("Quelle ressource voulez vous consulter : \n 1- Tous les cours \n 2- Un cours specifique \n 3- Un fichier spécifique dans un cours \n 4- Un dossier spécifique dans un cours \n 5- Une séance spécifique d'un cours\n 6- Rechercher un cours par tag\n ");
                        option = scanner.nextLine();
                    }

                    String ressource = "";
                    if (option.equals("1")) {
                        ressource = "/cours";
                    } else if (option.equals("2")) {
                        System.out.print("Veuillez entrer l'id du cours : ");
                        String id = scanner.nextLine();
                        ressource = "/cours/" + id;
                        System.out.print("Sous quel mode voulez vous visualisez: \n 1- Semaine \n 2- Module\n");
                        String mode = scanner.nextLine();
                        while (!mode.equals("1") && !mode.equals("2")) {
                            System.out.println("Veuillez entrer un mode valide ");
                            System.out.print("Sous quel mode voulez vous visualisez: \n 1- Semaine \n 2- Module\n");
                            mode = scanner.nextLine();
                        }
                        String modem = mode.equals("1") ? "semaine" : "module";
                        ressource += "?mode=" + modem;
                    } else if (option.equals("3")) {
                        System.out.print("Veuillez entrer l'id du cours : ");
                        String id = scanner.nextLine();
                        System.out.print("Veuillez entrer l'id du fichiers : ");
                        String id_2 = scanner.nextLine();
                        ressource = "/cours/" + id + "/fichier/" + id_2;
                    } else if (option.equals("4")) {
                        System.out.print("Veuillez entrer l'id du cours : ");
                        String id = scanner.nextLine();
                        System.out.print("Veuillez entrer l'id du dossier : ");
                        String id_2 = scanner.nextLine();
                        ressource = "/cours/" + id + "/dossier/" + id_2;
                    } else if (option.equals("5")) {
                        System.out.print("Veuillez entrer l'id du cours : ");
                        String id = scanner.nextLine();
                        System.out.print("Veuillez entrer l'id de la séance : ");
                        String id_2 = scanner.nextLine();
                        ressource = "/cours/" + id + "/seances/" + id_2;
                    } else if (option.equals("6")) {
                        System.out.print("Veuillez entrer le tag : ");
                        String tag = scanner.nextLine();
                        ressource = "/search?tag=" + tag;
                    }

                    HttpRequest request = HttpRequest.newBuilder()
                            .uri(URI.create(url + ressource))
                            .GET()
                            .build();
                    HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
                    System.out.println(response.body());

                } else if (methode.equals("POST")) {
                    System.out.print("Quelle ressource voulez vous ajouter : \n 1- Un cours  \n 2- Un fichier dans un cours \n 3- Un dossier dans un cours \n 4- Une séance dans un cours\n ");
                    String option = scanner.nextLine();
                    while (!option.equals("1") && !option.equals("2") && !option.equals("3") && !option.equals("4")) {
                        System.out.print("Quelle ressource voulez vous ajouter : \n 1- Un cours  \n 2- Un fichier dans un cours \n 3- Un dossier dans un cours \n 4- Une séance dans un cours\n ");
                        option = scanner.nextLine();
                    }

                    String ressource = "";
                    String json = "";
                    if (option.equals("1")) {
                        System.out.print("Veuillez entrer l'id du cours : ");
                        String id = scanner.nextLine();
                        ressource = "/cours/" + id;
                        System.out.print("Entrez la valeur pour 'discipline': ");
                        String discipline = scanner.nextLine();
                        System.out.print("Entrez la valeur pour 'name': ");
                        String name = scanner.nextLine();
                        System.out.print("Entrez les tags séparés par des espaces: ");
                        String tags = scanner.nextLine();
                        json = String.format("{\"id\": %s, \"discipline\": \"%s\", \"name\": \"%s\", \"tags\": \"%s\"}", id, discipline, name, tags);
                    } else if (option.equals("2")) {
                        System.out.print("Veuillez entrer l'id du cours : ");
                        String id = scanner.nextLine();
                        System.out.print("Veuillez entrer l'id du fichier : ");
                        String id_2 = scanner.nextLine();
                        ressource = "/cours/" + id + "/fichier/" + id_2;
                        System.out.print("Entrez la valeur pour 'titre': ");
                        String titre = scanner.nextLine();
                        System.out.print("Entrez la valeur pour 'type': ");
                        String type = scanner.nextLine();
                        System.out.print("Veuillez entrer l'id du dossier parent (0 si à la racine) : ");
                        String idParent = scanner.nextLine();
                        json = String.format("{\"titre\": \"%s\", \"type\": \"%s\", \"idParent\": %s}", titre, type, idParent);
                    } else if (option.equals("3")) {
                        System.out.print("Veuillez entrer l'id du cours : ");
                        String idCours = scanner.nextLine();
                        System.out.print("Veuillez entrer l'id du nouveau dossier : ");
                        String idDossier = scanner.nextLine();
                        System.out.print("Veuillez entrer l'id du dossier parent (0 si à la racine) : ");
                        String idParent = scanner.nextLine();
                        System.out.print("Veuillez entrer le titre du dossier : ");
                        String titre = scanner.nextLine();
                        ressource = "/cours/" + idCours + "/dossier/" + idDossier;
                        json = String.format("{\"idParent\": %s, \"titre\": \"%s\"}", idParent, titre);
                    } else if (option.equals("4")) {
                        System.out.print("Veuillez entrer l'id du cours : ");
                        String id = scanner.nextLine();
                        System.out.print("Veuillez entrer l'id de la séance : ");
                        String id_2 = scanner.nextLine();
                        ressource = "/cours/" + id + "/seances/" + id_2;
                        System.out.print("Entrez la valeur pour 'titre': ");
                        String titre = scanner.nextLine();
                        System.out.print("Entrez la valeur pour 'semaine': ");
                        String semaine = scanner.nextLine();
                        System.out.print("Entrez la valeur pour 'thematique': ");
                        String thematique = scanner.nextLine();
                        System.out.print("Entrez les id des fichiers séparés par des espaces: ");
                        String fichiers = scanner.nextLine();
                        json = String.format("{\"id\": %s, \"titre\": \"%s\", \"semaine\": %s, \"thematique\": \"%s\", \"fichiers\": \"%s\"}", id_2, titre, semaine, thematique, fichiers);
                    }

                    HttpRequest request = HttpRequest.newBuilder()
                            .uri(URI.create(url + ressource))
                            .header("Content-Type", "application/json")
                            .POST(HttpRequest.BodyPublishers.ofString(json))
                            .build();
                    HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
                    System.out.println(response.body());

                } else if (methode.equals("DELETE")) {
                    System.out.print("Quelle ressource voulez vous supprimer : \n 1- Un cours  \n 2- Un fichier dans un cours \n 3- Un dossier dans un cours \n 4- Une séance dans un cours ");
                    String option = scanner.nextLine();
                    while (!option.equals("1") && !option.equals("2") && !option.equals("3") && !option.equals("4")) {
                        System.out.print("Quelle ressource voulez vous supprimer : \n 1- Un cours  \n 2- Un fichier dans un cours \n 3- Un dossier dans un cours \n 4- Une séance dans un cours ");
                        option = scanner.nextLine();
                    }

                    String ressource = "";
                    if (option.equals("1")) {
                        System.out.print("Veuillez entrer l'id du cours : ");
                        String id = scanner.nextLine();
                        ressource = "/cours/" + id;
                    } else if (option.equals("2")) {
                        System.out.print("Veuillez entrer l'id du cours : ");
                        String id = scanner.nextLine();
                        System.out.print("Veuillez entrer l'id du fichier : ");
                        String id_2 = scanner.nextLine();
                        ressource = "/cours/" + id + "/fichier/" + id_2;
                    } else if (option.equals("3")) {
                        System.out.print("Veuillez entrer l'id du cours : ");
                        String id = scanner.nextLine();
                        System.out.print("Veuillez entrer l'id du dossier : ");
                        String id_2 = scanner.nextLine();
                        ressource = "/cours/" + id + "/dossier/" + id_2;
                    } else if (option.equals("4")) {
                        System.out.print("Veuillez entrer l'id du cours : ");
                        String id = scanner.nextLine();
                        System.out.print("Veuillez entrer l'id de la séance : ");
                        String id_2 = scanner.nextLine();
                        ressource = "/cours/" + id + "/seances/" + id_2;
                    }

                    HttpRequest request = HttpRequest.newBuilder()
                            .uri(URI.create(url + ressource))
                            .DELETE()
                            .build();
                    HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
                    System.out.println(response.body());
                }

                System.out.print("Voulez-vous faire une autre opération ? (oui/non) : ");
                String refaire = scanner.nextLine().trim().toLowerCase();
                if (!refaire.equals("oui")) {
                    System.out.println("Merci d'avoir utilisé le programme. Au revoir !");
                    break;
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        scanner.close();
    }
}