# PlacaFipy

PlacaFipy é uma biblioteca Python que permite realizar consultas FIPE pela placa do veículo.

## Funcionalidades

- `obter_estado(sigla)`: Retorna o estado a partir da sigla.
- `verificar_placa_mercosul(placa)`: Verifica se uma placa é do modelo Mercosul.
- `converter_placa(placa)`: Converte a placa informada para o padrão Mercosul ou vice-versa.
- `consulta(placa)`: Consulta informações de um veículo pela placa.

## Obtenha um API Token em ScrapingAnt

Para usar o PlacaFipy, é necessário um token de API do ScrapingAnt para contornar verificações anti-webscraping.

O ScrapingAnt fornece 1.000 consultas gratuitas por mês.

Você pode criar uma conta em [ScrapingAnt][scrapingant] e obter seu token API lá.

## Instalação

Você pode instalar este pacote via pip:

```bash
pip install placafipy
```

## Como utilizar

```python
from placafipy import PlacaFipy

# Crie uma instância do PlacaFipy passando uma lista com os tokens do ScrapingAnt como parâmetros. Você pode adicionar quantos tokens forem necessários.
tokens = ["SEU_TOKEN_1", "SEU_TOKEN_2", "SEU_TOKEN_3"]
placafipy = PlacaFipy(tokens)

# Obter o estado a partir da sigla
estado = placafipy.obter_estado('PE')
print(estado)  # Saída: PERNAMBUCO

# Verificar se uma placa é do modelo Mercosul
placa_mercosul = placafipy.verificar_placa_mercosul('ABC1C34')
print(placa_mercosul)  # Saída: True

# Conversão de placas
placa_convertida = placafipy.converter_placa('ABC1234')
print(placa_convertida)  # Saída: ABC1C34

placa_convertida = placafipy.converter_placa('ABC1C34')
print(placa_convertida)  # Saída: ABC1234

# Consultar informações de um veículo pela placa
placa = "ABC1234"
informacoes_veiculo = placafipy.consulta(placa)

if informacoes_veiculo:
    print(informacoes_veiculo)
else:
    print("Não foi possível obter informações para a placa especificada.")
```

## Exemplo de Saída

```json
{
    "tabela_fipe": {
        "valores": {...},
        "valores_ipva": {...}
    },
    "detalhes": {...},
    "imagem_logo_url": "https://example.com/logo.png",
    "imagem_placa_url": "https://example.com/placa.png",
    "orgao_emissor": "DETRAN",
    "veiculos_registrados": 10000,
    "tipo_veiculo": "carro",
    ...
}
```

**Nota:** A saída é obtida de forma dinâmica, portanto, alguns resultados podem conter diferentes chaves dependendo dos dados disponíveis no momento da consulta.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Autor
- [Antônio Roberto Júnior][krz]

## Licença

Este pacote está sob a licença [MIT](LICENSE).

[krz]: https://github.com/juniorkrz
[scrapingant]: https://scrapingant.com/