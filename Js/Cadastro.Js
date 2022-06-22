const nome = document.querySelector('#jogo');
const idade = document.querySelector('#idade');
const tipo = document.querySelector('#tipo');
const valor = document.querySelector('#valor');
const formulario = document.querySelector('.formulario');

formulario.addEventListener('submit', function(event) {
  event.preventDefault();
  const game = {
    primeiroNome: jogo.value,
    primeiraIdade: idade.value,
    primeiroTipo: tipo.value,
    primeirValor: valor.value,
  }

  cadastrarJogos(game)
})

function cadastrarJogos(game) {
  const headers = new Headers()
  headers.append('Content-Type', 'application/json');

  fetch('http://127.0.0.1:5000', {
    method: 'POST',
    headers: headers,
    body: JSON.stringify(game)
  }).then(function(dados) {
    return dados.json()
  }).then(function(resposta) {
    if (resposta.message) {
      alert(resposta.message[0]);
    } else {
      nome.value = ''
      idade.value = '';
      tipo.value = '';
      valor.value = '';
      alert('Informações sobre o jogo');
    }
  })
}