from typing import Dict


def write_report(path: str, config: Dict, metrics_values) -> None:
    """ escreve o arquivo de relatorio do experimento """
    relatorio = open(path, 'w')
    relatorio.write(f'Tipo de dado: {config["type"]}\n'
                    f'Diretório: {config["train_path"][:config["train_path"].rfind("/") + 1]}\n'
                    f'classificador: {config["classifier"]}\n'
                    f'Tempo de treino: {metrics_values["tempo_treino"]:.3f}s\n'
                    f'Tempo de inferência por amostra: {metrics_values["tempo_inferencia"]:.3f}s\n'
                    f'Precisão: {metrics_values["accuracy"]:.2f}')
