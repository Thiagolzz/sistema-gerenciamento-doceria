# 🍬 Sistema de Gerenciamento de Pedidos da Doceria

Sistema desenvolvido em **Python** para gerenciamento de pedidos de uma doceria.

Este projeto está sendo desenvolvido como forma de **prática e evolução na programação**, aplicando conceitos de Python, Programação Orientada a Objetos (POO), estruturas de dados e organização de código.

## 📌 Status do projeto

🚧 **Em desenvolvimento — V1**

### Funcionalidades atuais

* [x] Cadastrar pedido
* [x] Armazenar pedidos em uma lista
* [x] Criar pedidos utilizando classes e instâncias
* [x] Listar pedidos cadastrados

### Próximas funcionalidades

* [ ] Buscar pedido
* [ ] Alterar/atualizar status
* [ ] Excluir pedido
* [ ] Melhorar a experiência do usuário
* [ ] Persistência dos dados
* [ ] Banco de dados

## 🛠️ Tecnologias utilizadas

* **Python**
* Programação Orientada a Objetos (POO)
* Listas
* Funções
* `match-case`
* `enumerate()`

## 🧠 Conceitos praticados

O projeto utiliza conceitos como:

* Classes
* Instâncias
* Atributos
* Métodos
* Funções
* Listas
* Estruturas condicionais
* Laços de repetição
* Entrada de dados com `input()`
* Organização e reutilização de código

## 📋 Estrutura atual

Cada pedido é representado por uma instância da classe `Pedidos`, contendo:

* Nome
* Quantidade
* Sabor

Os pedidos são armazenados em uma lista:

```python
lista_de_pedidos = []
```

Ao cadastrar um pedido, uma nova instância é criada e adicionada à lista:

```python
pedido = Pedidos(nome, quantidade, sabor)
lista_de_pedidos.append(pedido)
```

## 🎯 Objetivo

O objetivo principal é desenvolver um sistema simples de gerenciamento de pedidos enquanto pratico e consolido conhecimentos em Python e POO.

O projeto será evoluído gradualmente, adicionando novas funcionalidades e posteriormente novos recursos, como persistência de dados e banco de dados.

## 📈 Evolução do projeto

### V1 — Início do projeto

* Estrutura inicial do sistema
* Menu de opções
* Classe `Pedidos`
* Cadastro de pedidos
* Armazenamento das instâncias
* Listagem dos pedidos

> Projeto em constante evolução.
