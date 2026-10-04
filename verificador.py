import subprocess


def ler_hosts(caminho):
    with open(caminho, "r") as arquivo:
        return [linha.strip() for linha in arquivo if linha.strip()]


def host_responde(host):
    resultado = subprocess.run(
        ["ping", "-n", "1", host],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return resultado.returncode == 0


for host in ler_hosts("hosts.txt"):
    if host_responde(host):
        print(f"[ONLINE]  {host}")
    else:
        print(f"[OFFLINE] {host}")