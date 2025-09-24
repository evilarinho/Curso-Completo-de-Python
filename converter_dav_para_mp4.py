import subprocess
import os # Importar para verificar a existência de ficheiros

def converter_dav_para_mp4(input_file, output_file):
    # Comandos do FFmpeg para copiar os streams de vídeo e áudio
    # -c:v copy e -c:a copy evitam a recodificação desnecessária, sendo mais rápido.
    # Se isto der erros, remova -c:v copy e -c:a copy, e o ffmpeg tentará recodificar.
    ffmpeg_command = f'ffmpeg -i "{input_file}" -c:v copy -c:a copy "{output_file}"'
    try:
        subprocess.run(ffmpeg_command, shell=True, check=True) # check=True para verificar erros
        print(f"Ficheiro convertido com sucesso: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao converter o ficheiro {input_file}: {e}")
    except FileNotFoundError:
        print("FFmpeg não encontrado. Verifique se está instalado e no PATH ou na mesma pasta do script.")

# Exemplo de uso:
if __name__ == "__main__":
    ficheiro_dav_entrada = "video_original.dav"
    ficheiro_mp4_saida = "video_convertido.mp4"

    # Verifique se o ficheiro de entrada existe antes de tentar converter
    if os.path.exists(ficheiro_dav_entrada):
        converter_dav_para_mp4(ficheiro_dav_entrada, ficheiro_mp4_saida)
    else:
        print(f"Erro: O ficheiro de entrada '{ficheiro_dav_entrada}' não foi encontrado.")
