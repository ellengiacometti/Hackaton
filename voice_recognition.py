
from playsound import playsound
import interface_ibm as ibm
import manipula_audio as ma
import time




if __name__ == "__main__":



    ## Gravar Audios
    nome_audio_entrada=["Intenção01.wav","Intenção02.wav","Intenção03.wav","Intenção04.wav","Intenção05.wav","Intenção06.wav","Intenção07.wav"]
    # gravarAudio(nome_audios)
    ## Teste
    audio_crip=ma.encodeAudio(nome_audio_entrada[0])
    ma.decodeAudio(audio_crip,"TesteCrip.wav")
    # # tipo_modelo ='pt-BR_NarrowbandModel' /'pt-BR_BroadbandModel'
    transcript=ibm.voz2Texto("TesteCrip.wav")

    print("Transcript:",transcript)
    [intencao,confianca]=ibm.texto2Intencao(transcript)
    print("Intenção:",intencao)
    print("Confiança:",confianca)

    # voz_modelo= pt-BR_IsabelaVoice,pt-BR_IsabelaV3Voice,





