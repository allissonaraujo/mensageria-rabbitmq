![](https://www.rabbitmq.com/img/rabbitmq-logo-with-name.svg)

Repositório sobre ume estudo básico realizado sobre mensageria utilizando o RabbitMQ como base.

## O que é um serviço de mensageria?
Mensageria é o conjunto de tecnologias e práticas usadas para enviar, receber e processar mensagens entre sistemas ou componentes de software, de maneira assíncrona. 

Em vez de depender de chamadas diretas e síncronas, onde um sistema precisa esperar a resposta do outro, a mensageria permite que os sistemas se comuniquem de forma desacoplada, enviando mensagens que podem ser processadas quando o receptor estiver disponível.

## O que eu utilizei como base para este estudo?

Utilizei Python como linguagem e o RabbitMQ rodando em Docker, que pode ser executado na sua máquina com o comando abaixo:

```bash
docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
```

Após a execução do Docker, você pode acessar sua área administrativa através da url: 
[Acessar Área Administrava do RabbitMQ](http://localhost:15672)

>As credenciais são guest/guest

## Um pouco sobre os dois arquivos do repositório

<table>
<thead>
	<tr>
		<th>produtor.py</th>
		<th>consumidor.py</th>
	</tr>
</thead>
<tbody>
	<tr>
		<td>Este arquivo é resposável pelo envio das mensagens para o RabbitMQ</td>
		<td>Este arquivo é responsável pelo recebimento das mensagens que chegam no RabbitMQ</td>
	</tr>
</tbody>
</table>

## Como é fluxo de mensageria funcionando?
![Mensageria com RabbitMQ](https://github.com/user-attachments/assets/8eb41eea-986d-4414-beed-e6f7245feebe)


