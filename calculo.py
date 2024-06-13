
import pandas as pd

def eliminar_dados_nulos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Elimina linhas com dados nulos de um DataFrame do Pandas.

    Args:
    - df (pd.DataFrame): DataFrame original.

    Returns:
    - pd.DataFrame: DataFrame sem linhas com dados nulos.
    """
    return df.dropna()

def multiplica_por_2d_dados(df: pd.DataFrame) -> pd.DataFrame:
    return df*2
# Se desejar adicionar outras funções ou utilitários relacionados à limpeza de dados, 
# você pode continuar a expandir este módulo.