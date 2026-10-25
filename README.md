# Poigno-VPN

Poigno-VPN est un projet d'apprentissage visant à créer une solution VPN personnelle, avec une attention particulière portée à la confidentialité, à la transparence de la configuration et aux tests.

## État du projet

Le dépôt est au début de son développement. Il ne fournit **pas encore** de tunnel VPN fonctionnel, de serveur VPN ni de rotation automatique de l'adresse IP publique.

La première étape consiste à créer et valider les outils du projet. Un véritable tunnel nécessitera un hébergeur compatible avec le trafic UDP de WireGuard. Les services Web gratuits de Render sont conçus pour exposer des services HTTP et ne proposent pas de port UDP public général : ils ne conviennent donc pas comme point d'entrée WireGuard classique. Voir la [documentation Render sur les services Web](https://render.com/docs/web-services).

## Principes du projet

- Utiliser une technologie VPN éprouvée comme WireGuard, sans réinventer la cryptographie.
- Ne jamais publier de clés privées, de fichiers de configuration client ou d'identifiants.
- Développer et tester gratuitement autant que possible.
- Indiquer clairement ce qui fonctionne et ce qui ne fonctionne pas encore.
- Traiter la rotation d'IP comme une fonctionnalité séparée : se reconnecter au même serveur VPN ne change pas automatiquement son IP publique de sortie.

## Développement

Les premiers outils sont de simples diagnostics exécutables localement ou dans une tâche d'intégration continue. Ils ne créent pas de tunnel VPN.

Consultez [les notes d'architecture](docs/ARCHITECTURE.md) pour connaître le plan actuel et les contraintes d'hébergement.
