import sounddevice as sd
import wavio
import os
import numpy as np
import scipy
from playsound import playsound
from fuzzywuzzy import fuzz
from watson_developer_cloud import SpeechToTextV1



#TODO: Criptografar e disponibilizar em arquivo de configuração para fácil alteração
speech_to_text = SpeechToTextV1(
    iam_apikey='85dIoj9uglDt40vrSGysIwl1sH1llA9yVvQkEMqG4xTb',
    url='https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/98493ae6-0de0-4eab-8841-4a9ac54b1ab7'
)

# Criando variáveis de uso recorrente
login="Ellen"
audio_filename="output.wav"
dir=" "
usuario_dir=""
palavras_teste =["Vou","ser","um","technee","Safra"] # palavras para testar  a precisão do modelo
fs = 44100  # Taxa de amostragem
segundos = 4  # Duração em segundos do audio
print("[AUDIO_INPUT] Gravando audio")
audio = sd.rec(int(segundos * fs), samplerate=fs, channels=2)
sd.wait()  # Aguarda enquanto o audio está sendo gravado
print("[AUDIO_INPUT] Salvando audio no formato .wav")
wavio.write(audio_filename, audio,fs,sampwidth=2)
print("[AUDIO_INPUT] Tocando audio")
playsound(audio_filename)

# Rotina de integração com a IBM
with open(audio_filename.wav, 'rb') as audio_file:
    palavras_reconhecidas = speech_to_text.recognize(audio_file, content_type='audio/wav').get_result()
palavras_reconhecidas = str(palavras_reconhecidas['results'][0]['alternatives'][0]['transcript'])

print("[WATSON] Transcrição Watson : " + palavras_reconhecidas)

# Métricas para avaliação de performance
print("[FUZZY] Fuzzy Score Parcial: " + str(fuzz.partial_ratio(palavras_teste, palavras_reconhecidas)))
print("[FUZZY] Fuzzy Score : " + str(fuzz.ratio(palavras_teste, palavras_reconhecidas)))


features = np.asarray(())# Alocando array para os atributos do modelo
for file in os.listdir(dir):#Varrendo o diretórios procurando por .wav para extrair features
    filename_wav = os.fsdecode(file)
    if filename_wav.endswith(".wav"):
              print("[FEATURE EXTRACTION] : Reading audio files for processing ...")
                (taxa, sinal) = scipy.io.wavfile.read(usuario_dir + filename_wav)
              #TODO: Criar função para extração de features
              #TODO: Criar função filtro para atenuar ruídos
              #TODO: Definir modelo e treiná-lo com base nos audios adquiridos no momento da inscrição




