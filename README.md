# Sistema de Acompanhamento de TCC

## Descrição do Projeto

Este projeto tem como objetivo auxiliar a coordenação de um curso no acompanhamento das entregas e avaliações dos TCC's dos alunos. 

O Projeto foi realizado como um trabalho para a universidade Unimar, na matéria de Estrutura de Dados, buscando demonstrar os conhecimentos em listas, dicionários e tuplas.

O sistema permite o cadastro de orientadores e alunos, o registro de versões do TCC, atribuição de notas e a geração de relatórios com pendências e médias.

## Funcionalidades

- É possível cadastrar orientadores
- Cadastro de alunos, vinculados a orientadores
- Registrar as versões do TCC
- Orientadores podem atribuir notas às versões entregues
- Possui relatório de pendências (entregas sem avaliação)
- Possui Relatório com médias por aluno e da média geral

## Regras de Negócio

- Um aluno só pode registrar uma nova entrega se não houver versões pendentes de avaliação.
- Só é possível cadastrar um aluno com um orientador previamente registrado.
- A média geral considera apenas a última versão avaliada de cada aluno.
- A nota de uma entrega é opcional e pode ser atribuída posteriormente.

<p align="center"> Desenvolvido por Thierry, Vinicius e Artur para um projeto da Unimar