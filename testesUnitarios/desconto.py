def calcula_desconto(valor_total: float, percentual_desconto: float) -> float:
    """
    Calcula o valor final após aplicar um desconto.

    Args:
        valor_total: O valor total original.
        percentual_desconto: O percentual de desconto (de 0 a 100).

    Returns:
        O valor com o desconto aplicado.

    Raises:
        ValueError: Se o percentual de desconto for negativo ou maior que 100.
    """
    if not 0 <= percentual_desconto <= 100:
        raise ValueError("O percentual de desconto deve estar entre 0 e 100.")

    desconto = valor_total * (percentual_desconto / 100)
    return valor_total - desconto