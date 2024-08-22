import time
import os
import shutil
from botcity.core import DesktopBot
from botcity.maestro import *
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def mover_primeiro_arquivo_mp4(origem, destino):
    arquivos = os.listdir(origem)

    arquivos_mp4 = [
        arquivo for arquivo in arquivos if arquivo.endswith('.mp4')]

    arquivos_mp4.sort()
    if len(arquivos_mp4) == 0:
        print("Não há arquivos .mp4 na pasta de origem.")
        return

    primeiro_arquivo_mp4 = arquivos_mp4[0]

    caminho_origem = os.path.join(origem, primeiro_arquivo_mp4)
    caminho_destino = os.path.join(destino, primeiro_arquivo_mp4)

    shutil.move(caminho_origem, caminho_destino)
    print(f'Arquivo "{primeiro_arquivo_mp4}" movido para "{destino}".')


pasta_origem = r"C:\Users\noturno\Documents\videos"
pasta_destino = r"C:\Users\noturno\Documents\videos\videos_usados"


def importar_video(bot):
    if not bot.find("add_projeto", matching=0.97, waiting_time=10000):
        not_found("add_projeto")
    bot.click()

    bot.sleep(3000)

    if bot.find("cancelar_capcut_pro", matching=0.97, waiting_time=10000):
        bot.click_relative(499, 21)

    if bot.find("btn_importar", matching=0.97, waiting_time=10000):
        bot.click()

    if not bot.find("caminho_pasta", matching=0.97, waiting_time=10000):
        not_found("caminho_pasta")
    bot.click()
    bot.control_a()
    bot.delete()
    bot.kb_type("C:/Users/noturno/Documents/videos")
    bot.enter()


def selecionar_video(bot):
    if not bot.find("selecionar_video", matching=0.97, waiting_time=10000):
        not_found("selecionar_video")
    bot.click()

    bot.sleep(2000)

    if not bot.find("abrir", matching=0.97, waiting_time=10000):
        not_found("abrir")
    bot.click()

    # chamar notificação
    noticacao(bot, "Upload de vídeo concluído")

    bot.mouse_move(375, 382)

    if bot.find("add_timeline", matching=0.97, waiting_time=10000):
        print("Foi adicionado a timeline")
        bot.click()


def gerar_legenda(bot):
    if not bot.find("legendas", matching=0.97, waiting_time=10000):
        not_found("legendas")
    bot.click()

    if not bot.find("gerar_legenda", matching=0.97, waiting_time=10000):
        not_found("gerar_legenda")
    bot.click()
    bot.sleep(15000)

    if not bot.find("exportar", matching=0.97, waiting_time=10000):
        not_found("exportar")
    bot.click()

    if not bot.find("gratis", matching=0.97, waiting_time=10000):
        not_found("gratis")
    bot.click()


def gerar_nome(bot):
    if not bot.find("nome_video", matching=0.97, waiting_time=10000):
        not_found("nome_video")
    bot.click_relative(167, 11)
    bot.control_a()
    bot.delete()
    horario = time.localtime()
    nome = "video"
    nome_video = f"{nome}-{horario[3]}-{horario[4]}-{horario[5]}"
    bot.paste(nome_video)

    # exportar o arquivo
    bot.enter()


def fechar_capcut(bot):
    bot.alt_f4()
    bot.alt_f4()
    bot.sleep(2000)
    bot.alt_f4()
    bot.sleep(3000)


def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()
    app_path = r"C:/Users/noturno/AppData/Local/CapCut/Apps/CapCut.exe"
    bot.execute(app_path)
    bot.maximize_window()

    importar_video(bot)

    bot.sleep(3000)

    selecionar_video(bot)

    bot.sleep(3000)

    # gerar_legenda(bot)

    if bot.find("exportar", matching=0.97, waiting_time=10000):
        print("Clicou no exportar")
        bot.click()

    bot.wait(5000)

    gerar_nome(bot)

    fechar_capcut(bot)

    mover_primeiro_arquivo_mp4(pasta_origem, pasta_destino)

    bot.wait(3000)

    bot.execute(r'C:\Users\noturno\Documents\videos')

    """
    Uncomment to mark this task as finished on BotMaestro
    maestro.finish_task(
         task_id=execution.task_id,
         status=AutomationTaskFinishStatus.SUCCESS,
         message="Task Finished OK."
    )
    """


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
