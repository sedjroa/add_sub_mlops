# add_sub_mlops
Introduction au monde du mlops. Ceci est une très petite app avec la logique frontend, backend. Elle intègre les bonnes pratiques de codage PEP8 et le suivi.

## Comment lancer l'application
```bash
> pip install -r requirements.txt
> python back.py
> streamlit run front.py
```

## Consulter la documentation et essayez-vous avec l'API
Dans voter navigateur:
```bash
ie `documentation`:  http://127.0.0.1:8000/docs
```
## Consulter la documentation
Pas besoin de podman. Dans votre natigateur [localhost](http://127.0.0.1:8000/)
Effectuez vos premières opérations depuis le navigateur:
```bash
ie `addition`:  http://127.0.0.1:8000/add?a=1&b=3 --> A+B=4
ie `soustraction`:  http://127.0.0.1:8000/sub?a=1&b=3 --> A-B=-2
```

## Suivi interations 

- Télécharger [Prometheus](https://prometheus.io/download/)
- Lancer le .exe depuis votre terminal: `.\chemin\vers\prometheus.exe --config.file="chemin\vers\prometheus.yml"`
- Interface Prometheus : http://localhost:9090/targets
- Visualiser le flux (nombre total d'opérations): http://localhost:9090/graph

![alt text](image.png)