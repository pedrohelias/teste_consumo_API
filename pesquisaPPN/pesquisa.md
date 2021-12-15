<h1>Cloud Computing</h1>
<h2>A nuvem</h2>
A Nuvem é descrita por uma rede global de servidores remotos conectados ao redor do mundo, operando como um ecossistema, cada um com funções específicas e únicas. Esse serviço é bastante caracterizado por ser possível acessar esses servidores a partir de qualquer dispositivo com acesso a internet, a qualquer hora e de qualquer local. Os servidores que compõe a nuvem são responsáveis por armazenar e gerenciar dados, executar aplicações, fornecer serviços online ou conteúdos. Como forte característica, tem-se a Transparência, que há a ocultação para desenvolvedores e usuários finais da complexidade da infraestrutura por trás, disponibilizando apenas a interface ao usuário. Tem como princípios: Flexibilidade, Escalabilidade, Elasticidade e Confiabilidade.

Como vantagens de se utilizar Nuvem, tem-se:

- O acesso aos recursos independe do sistema operacional do usuário;
- Há centralização dos Recursos; É acessível de qualquer lugar;
- Há o controle de gastos;
- Inexistência da necessidade de manutenção de infra-estrutura física. Como desvantagem, encontra-se apenas a dependência de conexão à internet.

<h2>Métodos de implementação</h2>

Há 4 métodos diferentes para implementação de recursos em nuvem. Há a nuvem publica que compartilha recursos e fornece serviços acessíveis ao publico em geral. Núvens privadas, não compartilhadas e servem a redes internas privadas. Existe a nuvem híbrida, que compartilha serviços entre nuvem pública e privada, relacionada a seu proposito. Por fim, tem-se a nuvem de comunidade, que compartilha recursos apenas entre organizações.

Como os 5 pilares essenciais, temos:

<ol>
    <li><b>"On Demand self-service"</b>: os serviços são selecionados a partir das demandas e dores do cliente, isso tudo a partir de interfaces 	automatizadas que garantem recursos de armazenamento, rede e processamento, o que exclue a necessidade de intervenção humana para 	garantir esses recursos. É garantida a escalabilidade, utilizando recursos sob demanda.
</li>
    <li><b>"Broad Network Access"</b>: Os serviços de uma nuvem são acessíveis de qualquer lugar (a partir de conexões de internet)
</li>
    <li><b>"Resource Pooling"</b>: Uma grande agrupamento de recursos e serviços,que não são seus, mas são compartilhados entre usuários. Clientes não precisam se preocupar sobre a alocação física desses recursos.
</li>
    <li><b>"Rapid Elasticity"</b>: Aumento e extensão de serviços, é possível aumentar e reduzir a capacidade de serviços como quiser. Os recursos são elásticos. Clientes que precisam de recursos mais rapidamente podem obter os mesmos.
</li>
    <li><b>    "Measured Service"</b>: Cobra-se o que é consumido ou reservado. Especificamente, as ofertas Google possuem diversas possibilidades de 	oferta desse serviço.
</li>

</ol>
<h2>Modelos de Serviços</h2>
Há 3 modelos de serviços descritos em computação em Nuvem:

- <b>"SaaS"</b>: Software as a Service - Software como Serviço, oferece aplicações que são acessadas por toda WEB, mas são gerenciadas pelo provedor do Software. É uma forma de disponibilizar softwares e soluções de tecnologia por meio da internet como um serviço. Como a gerência fica a cargo do provedor do software, a empresa não precisa instalar, manter e atualizar hadwares e softwares. A simplicidade é tamanha, que é necessário apenas conexão com a internet para acessar esse tipo de serviço. Como exemplo, temos: Gmail, Google Docs, Heroku, Salesforce.
- <b>"IaaS"</b>: Infrastructure as a Service - Intraestrutura como serviço, oferece recursos fundamentais de computação, armazenamento e rede sob demanda e pagos conforme o uso, o que a caracteriza como escalavel e flexivel. O serviço IaaS envolve toda a mudança de uma infraestrutura física para os servidores do serviço contratado. O IaaS é o serviço mais simples entre Iaas, PaaS e SaaS. Como exemplo, temos o Google Compute Engine.

- <b>"PaaS"</b>: Plataform as a Service - Plataforma como Serviço, é uma mistura entre SaaS e IaaS, oferece funcionamento semelhante a um ambiente digital, onde usuários tem liberdade para desenvolver e implantar programas. Por meio da internet, é possível criar, hospedar e gerir um software. O PaaS então funciona como um ambiente para o desenvolvimento. Como vantagens, tem gerenciamento e acesso a grandes volumes de dados. Como exemplo, temos o Google App Engine.

<h2>Bilhetagem</h2>

Há diversas opções de consumo relacionadas a bilhetagem na Google.
A Google foi pioneira em um sistema de bilhetagem amigável ao usuário(especificamente, per-second billing). Esse sistema é oferecido para usuário de Compute Engine, Kubernetes Engine, Cloud Dataproc e App Engine. Possui as as seguintes características:

- <b>Billing in sub-hour increments</b>: Específica para processamento de dados e outros serviços.

- <b>Discounts for Sustained use ( uso prolongado )</b>: Aplicado ao uso incremental quando determinados limites são atingidos. É pago apenas pelo número de minutos usados para uma instância, e o Compute Engine oferece automaticamente o melhor preço. Um exemplo, se a máquina é utilizada em 75% do mês, há um desconto de 20%. Para o mês inteiro, há um desconto de 30%.

- <b>Discounts for commited use ( uso contínuo )</b>: Pague menos por cargas de trabalho estáveis e de longo prazo. Esse desconto é ideal para cargas de trabalho com necessidades previsíveis de recursos. Ao optar por essa forma de bilhetagem, o cliente compra recursos do Compute Engine, como Memória, GPU, vCPU's, SSD locais, a um preço com desconto em troca do compromisso de pagamento desses recursos por um ou três anos. Para a maioria das máquinas o desconto vai até 57%. Para máquinas com otimização de memória o desconto vai até 70%.

- <b>Discounts for preemptible use</b>: Pague menos por cargas de trabalho interruptas. As instâncias preemptiveis são disponibilizadas por um preço muito mais baixo em comparação a máquinas normais, e isso se da ao fato de suas limitações em relação a outros serviços de bilhetagem. Essas instâncias são utilizadas como capacidade extra do compute engine, por isso sua disponibilidade varia com o uso.Esse tipo de sistema garante uma máquina ligada por até 24h. Após isso, o Compute Engine interrompe essas máquinas. Outra limitação é que instâncias preemptiveis são recursos finitos, ou seja, pode ser que nem sempre estejam disponíveis.

- <b>Custom VM instance Types</b>: Pague apenas por recursos demandados pela aplicação.

É importante ressaltar que os descontos não podem ser combinados. A Google possui um sistema de simulação de precificação, onde é possível verificar previamente o quanto será cobrado pelo consumo especificado da máquina.
