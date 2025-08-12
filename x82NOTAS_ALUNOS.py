def notas(*n, sit=False):
    """
    -> funcão para analizar notas e situações dos alunos.
    :param n: notas dos alunos
    :param sit: situação da nota do aluno: igual ou acima de 7 = aprovado
    :return: dicionario com varias informações sobre a turma
    """
    r = dict()
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["soma"] = round(sum(n), 1)
    r["media"] = round(sum(n) / len(n), 1)
    if sit:
        if r["media"] >= 7:
            r["situação"] = 'BOA'

        elif r["media"] >= 5:
            r["situação"] = 'RAZOAVEL'

        else:
            r["situação"] = 'RUIM'
    return r


resp = notas(2, 4, 6.7, 8, sit=True)
print(resp)
help(notas)
