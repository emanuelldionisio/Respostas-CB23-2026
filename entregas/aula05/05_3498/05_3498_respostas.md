# 1. Identifique relações de herança entre as classes.
_Explique como as classes poderiam ser organizadas em uma hierarquia de herança, indicando quais classes seriam classes base e quais seriam subclasses, e descreva o que seria herdado em cada caso. 

A classe funcionário herda de pessoa, pois um funcionário é uma pessoa com atributos adicionais: carga_horaria e salário, assim, os funcionários herdam os atributos de nome e idade.

Funcionário é uma classe base para as classes Chefe de cozinha, Gerente e Garçom, pois essas classes são tipos de funcionários, com nome, idade, salário e carga horária, com métodos adicionais.

Restaurante é uma classe base para a classe Pizzaria, pois uma pizzaria é um tipo de restaurante, por isso precisa de nome, endereço e telefone, mas com a opção de oferecer rodízio. 

Iguaria é uma classe base para Bolo e Pizza, pois uma iguaria é um tipo de comida, com nome e preço. Bolo é uma iguaria com formato e pizza é uma iguaria com a opção de borda recheada.

# 2. Como você modelaria a relação entre a classe Restaurante e a classe Iguaria? 
_Explique como essa relação seria implementada. Se necessário, sugira a criação de novos atributos ou até mesmo de novas classes para representar essa relação de forma eficiente._

A classe Restaurante e a classe Iguaria não possuem relação de herança, mas sim uma relação de composição, pois um restaurante possui iguarias, mas uma iguaria não é um restaurante (semelhante a Restaurante que contém funcionários, mas um funcionário não é um restaurante). Assim, a classe Restaurante poderia ter um atributo cardápio, que seria uma lista de iguarias.

# 3.  Indique os tipos que você atribuiria para os argumentos: argumento1, argumento2, argumento3
_Explique quais seriam os tipos apropriados para cada argumento com base no seu uso e na função em que são empregados. Considere se eles seriam, por exemplo, tipos primitivos, instâncias de classes, ou listas, e justifique sua escolha._

- argumento1: list[ Iguaria ] - O argumento1 é uma lista de iguarias, pois o garçom, ao anotar um pedido, precisa receber uma lista de iguarias que o cliente deseja pedir.

- argumento2: Iguaria - O argumento2 é uma iguaria, pois o chefe de cozinha, ao preparar uma iguaria, precisa receber a iguaria que ele vai preparar.

- argumento3: Funcionário - O argumento3 é um funcionário, pois o gerente, ao demitir um funcionário, precisa receber o funcionário que será demitido.
