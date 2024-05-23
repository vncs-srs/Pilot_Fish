#!/bin/bash

# Caminho para o seu script Python
SCRIPT_PATH="~/Pilot_Fish/Codigos/Codigo_Principal/Rastreamento_Peixe.py"

# Verifica se o arquivo Python existe
if [ ! -f "$SCRIPT_PATH" ]; then
    echo "Arquivo $SCRIPT_PATH não encontrado!"
    exit 1
fi

# Cria o arquivo de serviço systemd
SERVICE_FILE="/etc/systemd/system/Pilor_Fish.service"
echo "[Unit]
Description=Rastreamento de peixe
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/bin/python3 $SCRIPT_PATH

[Install]
WantedBy=multi-user.target" > $SERVICE_FILE

# Define permissões apropriadas para o arquivo de serviço
chmod 644 $SERVICE_FILE

# Recarrega os serviços do systemd
systemctl daemon-reload

# Habilita o serviço para iniciar automaticamente no boot
systemctl enable Pilor_Fish.service

# Inicia o serviço
systemctl start Pilor_Fish.service

echo "Serviço de rastreamento de peixe configurado e iniciado com sucesso."
