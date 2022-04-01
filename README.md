# DESAFIO TECH -  FREXCO

Este repositório faz parte do desafio tech proposto pela FREXCO em seu processo de seleção.

O servidor API foi desenvolvido com FLASK.

Para inicializá-lo atente-se ao documento .env.example e preencha todas as informações pertinentes.

O banco de dados utilizado foi o POSTGRESQL.

!Importante. As tabelas serão geradas automaticamente, mas o banco de dados não. Certifique de criar a DB com o exato nome que incluir no .env.

Faça a instalação das dependências:

```bash
    python -m venv venv

    pip install -r requirements.txt
```

# Endpoints

Nessa implementaçãonão todas as rotas são públicas, sem autenticação.

O url base da API é http://localhosto:5000/api

## **REGION**

A tabelas **fruit** depende da existencia de informações da tabela **region**.

Um campo é obrigatório: *name*.

### **Para criar uma região**
O nome da região deverá ser único.

`POST /region - FORMATO DA REQUISIÇÃO`
```json
{
    "name": "norte"
}
```
Caso dê tudo certo a resposta será:

`FORMATO DA RESPOSTA - STATUS 201`
```json
{
    "id_region": 1,
    "name": "norte"
}
```

### **Recuperar as regiões cadastradas**

`GET /region - FORMATO DA RESPOSTA - STATUS 200`
```json
[
    {
        "id_region": 1,
        "name": "norte"
    },
    {
        "id_region": 2,
        "name": "nordeste"
    }
]
```
### **Recuperar uma região**

`GET /region/:id - FORMATO DA RESPOSTA - STATUS 200`
```json
[
    {
        "id_region": 3,
        "name": "centro oeste"
    }
]
```

### **Atualizar uma região**

Caso precise modificar o nome de uma região.

`PUT /region/:id - FORMATO DA REQUISIÇÃO`
```json
{
    "name": "centro-oeste"
}
```

Caso dê tudo certo a resposta será:

`FORMATO DA RESPOSTA - STATUS 200`
```json
{
    "id_region": 3,
    "name": "centro-oeste"
}
```

### **Apagar uma região**
De forma prática, não é possível apagar um registro da tabela **região** por sua associação a tabela **fruit**. Forçar essa ação implicaria em perder todos os registros de **fruit** associados a região que deseja excluir.
Por isso, o que esta rota faz é inativar o registro.

`DELETE /region/:id - FORMATO DA REQUISIÇÃO`

Caso dê tudo certo a resposta será:

`FORMATO DA RESPOSTA - STATUS 200`
```json
{
    "id_region": 2,
    "name": "sul"
}
```

## **FRUIT**

A tabelas **fruit** depende da existencia de informações da tabela **region**.

Dois campos são obrigatórios: *name* e *region*.

### **Para criar uma fruta**
O nome da fruta deverá ser único.

`POST /fruit - FORMATO DA REQUISIÇÃO`
```json
{
	"name": "morango",
	"region": "nordeste"
}
```
Caso dê tudo certo a resposta será:

`FORMATO DA REQUISIÇÃO - STATUS 201`
```json
{
    "id_fruit": 7,
    "name": "morango",
    "region": 4
}
```

### **Recuperar as frutas cadastradas**

`GET /fruit - FORMATO DA RESPOSTA - STATUS 200`
```json
[
    {
        "id_fruit": 1,
        "name": "amora",
        "region": "norte"
    },
    {
        "id_fruit": 2,
        "name": "laranja",
        "region": "sul"
    },
    {
        "id_fruit": 5,
        "name": "goiaba",
        "region": "sul"
    },
    {
        "id_fruit": 7,
        "name": "morango",
        "region": "nordeste"
    }
]
```
### **Recuperar uma fruta**

`GET /fruit/:id - FORMATO DA RESPOSTA - STATUS 200`
```json
[
    {
        "id_fruit": 7,
        "name": "morango",
        "region": "nordeste"
    }
]
```

### **Atualizar uma fruta**
Caso precise modificar o nome de uma fruta.

`PUT /fruit/:id - FORMATO DA REQUISIÇÃO`
```json
{
	"name": "Limão",
	"region": "nordeste"
}
```

Caso dê tudo certo a resposta será:

`FORMATO DA REQUISIÇÃO - STATUS 200`
```json
{
    "id_fruit": 6,
    "name": "limão",
    "region": 1
}
```

### **Apagar uma fruta**

Caso precise apagar uma fruta.

`DELETE /fruit/:id - FORMATO DA REQUISIÇÃO`

Caso dê tudo certo a resposta será:

`FORMATO DA RESPOSTA - STATUS 200`
```json
{
    "id_fruit": 1,
    "name": "amora",
    "region": 1
}
```
