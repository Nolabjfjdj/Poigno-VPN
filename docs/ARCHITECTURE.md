# Architecture et plan de développement

## Étape actuelle : base du dépôt

La première étape porte sur la documentation et les diagnostics de base. Il ne s'agit pas encore d'une implémentation VPN.

## Composants prévus

1. **Configuration cliente** — utiliser le format et les outils éprouvés de WireGuard, sans développer notre propre cryptographie.
2. **Point d'entrée serveur** — utiliser un hébergeur qui accepte le trafic UDP public et autorise l'usage d'un VPN.
3. **Vérification de l'IP** — comparer l'adresse IP publique de sortie avant et après la connexion au tunnel.
4. **Politique de rotation** — choisir entre plusieurs points de sortie légitimes, ou utiliser un hébergeur proposant une rotation d'adresse documentée. Une reconnexion au même point d'entrée ne garantit pas une nouvelle IP publique.
5. **Gestion des secrets** — garder les clés privées et les configurations client complètes hors de Git. Utiliser un stockage local sécurisé ou des secrets CI si nécessaire.

## Contraintes d'hébergement gratuit

- Les services Web Render transmettent le trafic public vers un port HTTP. Ce fonctionnement ne fournit pas un point d'écoute UDP public général pour WireGuard.
- Les services Render gratuits peuvent se mettre en veille lorsqu'ils sont inactifs et peuvent redémarrer. Ils peuvent convenir à un tableau de bord Web ou à une API de développement, mais pas à un serveur VPN permanent fiable.
- GitHub Actions sert à automatiser les tâches de compilation et de test, pas à héberger un serveur VPN permanent.

## Liste de validation

- [ ] Vérifier que l'hébergeur prend explicitement en charge le trafic UDP WireGuard.
- [ ] Générer les clés avec les outils WireGuard sur le client et le serveur.
- [ ] Ne pas publier les clés privées dans le dépôt, les journaux, les captures d'écran ou les rapports de problème.
- [ ] Confirmer que la négociation du tunnel fonctionne.
- [ ] Vérifier l'adresse IP publique et le comportement DNS une fois connecté.
- [ ] Tester le comportement lorsque le serveur est indisponible.
- [ ] Documenter les limites de l'offre gratuite et préciser si l'IP de sortie est fixe ou peut changer.

## Transparence sur l'état réel

Une compilation réussie, un déploiement, une vérification de disponibilité ou une requête de contrôle d'IP ne prouvent pas qu'un tunnel VPN fonctionne. Le projet doit présenter ces états séparément.
